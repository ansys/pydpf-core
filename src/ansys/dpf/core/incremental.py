# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Incremental."""

from typing import Any, Dict

from ansys.dpf import core


class IncrementalHelper:
    """Provides an API to transform an existing workflow into an incrementally evaluating one.

    It works by plugging operators into an incomplete workflow.

    Example
    -------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> path = examples.find_msup_transient()
    >>> ds = dpf.DataSources(path)
    >>> scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)
    >>>
    >>> result_op = dpf.operators.result.displacement(data_sources=ds, time_scoping=scoping)
    >>> minmax_op = dpf.operators.min_max.min_max_fc_inc(result_op)
    >>>
    >>> new_op = dpf.split_workflow_in_chunks(result_op, minmax_op, scoping, chunk_size=5)
    >>> min_field = new_op.get_output(0, dpf.types.field)
    >>> max_field = new_op.get_output(1, dpf.types.field)
    """

    def __init__(
        self,
        start_op: core.Operator,
        end_op: core.Operator,
        scoping: core.Scoping,
        scoping_pin: int = None,
    ):
        """Construct an IncrementalHelper object.

        Given the first and the last operator of a workflow, as well as the scoping.

        This class can be used to simplify the use of incremental operators, and automatically
        be enabled to incrementally evaluate a workflow.

        Under the constraint that the end_op supports incremental evaluation.

        Parameters
        ----------
        start_op : Operator
            First operator in the workflow to convert
        end_op : Operator
            Last operator in the workflow to convert (Operator providing the meaningful output)
        scoping : Scoping
            Scoping used to chunk the data
        scoping_pin : int, optional
            Pin number of the scoping on the first operator, otherwise it is deduced with types
        """
        # Input operator should accept a scoping
        # Last operator should support incremental evaluation
        # but as we don't have a consistent method to check,
        # it should be permissive in the case the specification isn't up to date
        self._start_op = start_op
        self._end_op = self._map_to_incremental(end_op)

        self._scoping = scoping
        self._scoping_pin = self._find_scoping_pin(scoping_pin)

    def estimate_size(self, max_bytes: int, _dict_inputs: Dict[int, Any] = {}) -> int:
        """Estimates the chunk size from the estimated number of bytes outputted in one iteration.

        Estimation is based on the size of the output for one ID of the given time_scoping,
        so it will run the operator for only one iteration.

        It only supports Field and FieldContainer.
        For other types, you should specify chunk_size argument in the split() method.

        Parameters
        ----------
            max_bytes : int
                Max allowed size of an output from the first operator, for one iteration (in bytes).
            _dict_inputs: dict[int,any]
                Dictionary associating pin number to inputs, for evaluating output of one iteration.
        """
        # Evaluate for the first element to try to guess memory consumption
        # It is best to use with a lot of elements
        first_id = self._scoping.ids[0]
        srv = self._scoping._server
        loc = self._scoping.location
        _dict_inputs[self._scoping_pin] = core.Scoping(server=srv, ids=[first_id], location=loc)

        outputs = self._prerun(_dict_inputs)

        _outputs = outputs._outputs
        data = map(lambda o: o.get_data(), _outputs)
        # Output sizes of all inputs for one iteration
        sizes = map(lambda obj: self._compute_size(obj), data)

        # Total size for one ID in the scoping
        size_for_one = sum(sizes)
        # total_size = size_for_one * self._scoping.size

        num_iter = int(max_bytes / size_for_one)
        num_iter = min(max(num_iter, 1), self._scoping.size)  # clamp(num_iter, 1, scoping size)
        return num_iter  # math.gcd(num_iter, self._scoping.size)

    def _compute_size(self, obj):
        if isinstance(obj, core.FieldsContainer):
            fc = obj
            return self._compute_size(fc[0])
        elif isinstance(obj, core.Field):
            field = obj
            # Double = 8 bytes assumption
            return field.size * 8

        raise NotImplementedError()

    def _prerun(self, _dict_inputs: Dict[int, Any]):
        for pin_idx, val in _dict_inputs.items():
            self._start_op.connect(pin_idx, val)
        self._start_op.run()
        return self._start_op.outputs

    # Transforms a user workflow:
    #
    #           +----------+    +---------------+    +---------+
    # scoping ->| start_op | -> | middle ops... | -> | end_op  | ->
    #           +----------+    +---------------+    +---------+
    #
    # Into a new workflow like this:
    #
    #           +----------+    +---------------+    +---------+
    # scoping ->| start_op | -> | middle ops... | -> | end_op  |
    #   \       +----------+    +---------------+    +---------+
    #    \           \                                  |
    #     \           \   +------------------+          |                    (pins remaps)
    #      \           \> |                  |          |   +----------+    +-----------+
    #       \ scop_pin -> | chunk_in         |          +-> |          | -> | forward   | -> final
    #        +----------> |   for_each_range |  iterables   |          |    | (new end) |    outputs
    #       chunk_size -> |                  | -----------> | for_each |    +-----------+
    #                     +------------------+              |          |
    #                                     end_input_pin-->  |          |
    #                                                       +----------+
    def split(
        self, chunk_size: int, end_input_pin: int = 0, rescope: bool = False
    ) -> core.Operator:
        """Integrate given operators into a new workflow enabling incremental evaluation.

        Given a chunk size (multiple of given scoping), it will provide a new operator to retrieve
        outputs from, and enable incremental evaluation, notably reducing peak memory usage.

        Parameters
        ----------
            chunk_size : int
                Number of iterations per run
            end_input_pin : int, optional
                Pin number of the output to use from the first operator (default = 0)
            rescope : bool, optional
                Rescope all the outputs based on the given scoping (default = False)
        """
        # Enables incremental evaluation:
        # Using for_each, chunk_in_for_each_range and incremental version of the last operator
        # by returning two operators with remapped inputs and outputs to other operators

        _server = self._start_op._server

        for_each = core.Operator("for_each", server=_server)
        split_in_range = core.Operator("chunk_in_for_each_range", server=_server)
        forward = core.Operator("forward", server=_server)

        split_in_range.connect_operator_as_input(1, self._start_op)
        split_in_range.connect(2, self._scoping_pin)
        split_in_range.connect(3, self._scoping)
        split_in_range.connect(4, chunk_size)

        for_each.connect(0, split_in_range, 0)
        for_each.connect(2, end_input_pin)

        # connect inputs
        dict_outputs = core.Operator.operator_specification(
            op_name=self._end_op.name, server=_server
        ).outputs
        if not dict_outputs:
            # temporary patch for incremental:: operators
            dict_outputs = {0: None}

        fe_pin_idx = 3  # see doc of for_each
        for pin_idx in dict_outputs.keys():
            # connect end_op to for_each
            for_each.connect(fe_pin_idx, self._end_op, pin_idx)
            # remap
            forward.connect(pin_idx, for_each, fe_pin_idx)
            fe_pin_idx += 1

        output = forward

        if rescope:
            new_forward = core.Operator("forward")
            for pin_idx in dict_outputs.keys():
                rescope = core.Operator("Rescope")
                rescope.connect(0, forward, pin_idx)
                rescope.connect(1, self._scoping)
                new_forward.connect(pin_idx, rescope, 0)

            output = new_forward
        return output

    def _map_to_incremental(self, end_op: core.Operator):
        # The goal of this function is to validate that a given operator is indeed incremental.
        # If an operator is found to not support incremental evaluation, it must not be strict
        # it should only output warnings
        # because this function -by design- may be outdated.
        inc_operators = [
            "accumulate_level_over_label_fc",
            "accumulate_min_over_label_fc",
            "accumulate_over_label_fc",
            "average_over_label_fc",
            "min_max_inc",
            "min_max_fc_inc",
            "max_over_time_by_entity",
            "min_max_over_time_by_entity",
            "min_max_by_time",
            "min_over_time_by_entity",
            "time_of_max_by_entity",
            "time_of_min_by_entity",
            "incremental::merge::property_field",
            "incremental::merge::mesh",
            "incremental::merge::field",
            "incremental::merge::fields_container",
        ]

        map_to_inc = {"min_max": "min_max_inc", "min_max_fc": "min_max_fc_inc"}

        if end_op.name not in inc_operators:
            print(f"WARNING: Operator named {end_op.name} may not support incremental evaluation")
            if end_op.name in map_to_inc.keys():
                print(
                    f"An operator named {map_to_inc[end_op.name]} supports incremental evaluation"
                )

        if "incremental" in end_op.config.available_config_options:
            end_op.config.set_config_option("incremental", True)

        return end_op

    def _find_scoping_pin(self, pin_idx):
        dict_inputs = self._start_op.inputs._dict_inputs
        # validate given pin_idx
        if pin_idx != None and pin_idx in dict_inputs:
            pin_spec = dict_inputs[pin_idx]
            if "scoping" in pin_spec.type_names:
                return pin_idx

        # look for scoping pin
        for pin_idx, spec in dict_inputs.items():
            if "scoping" in spec.type_names:
                return pin_idx

        raise Exception(
            f"Scoping pin could not be found in start_op with name '{self._start_op.name}'"
        )


def split_workflow_in_chunks(
    start_op: core.Operator,
    end_op: core.Operator,
    scoping: core.Scoping,
    rescope: bool = False,
    max_bytes: int = 1024**3,
    dict_inputs: Dict[int, Any] = {},
    chunk_size: int = None,
    scoping_pin: int = None,
    end_input_pin: int = 0,
):
    """Transform a workflow into an incrementally evaluating one.

    It wraps in one method the functionality of the IncrementalHelper class as well
    as the estimation of the chunk size.

    If no chunk_size is specified, the function will attempt to estimate the value
    by calling IncrementalHelper.estimate_size(max_bytes, dict_inputs).

    If no scoping_pin is specified, the function will attempt to deduce the correct pin,
    which would be the first input pin matching a scoping type.

    Parameters
    ----------
        start_op : Operator
            Initial operator of the workflow to convert
        end_op : Operator
            Last operator of the workflow to convert
        scoping : Scoping
            Scoping to split across multiple evaluation
        rescope : bool, optional
            If enabled, will rescope final outputs with the given scoping (default = False)
        max_bytes : int, optional
            Max allowed size for the output from the first operator (default = 1024**3)
        dict_inputs : dict[int, any], optional
            Inputs to pass to the first operator, used only for the estimation run (default = {})
        chunk_size = int, optional
            Maximum number of scoping elements to process in an iteration (default = None)
        scoping_pin : int, optional
            The pin number on the first operator to bind the scoping (default = None)
        end_input_pin : int, optional
            Pin number of the output to use from the first operator(default = 0)
    """
    splitter = IncrementalHelper(start_op, end_op, scoping, scoping_pin)

    if chunk_size == None:
        print(f"Estimating chunk_size with max_bytes: {max_bytes}")
        chunk_size = splitter.estimate_size(max_bytes, dict_inputs)
        print(f"Done. chunk_size set to {chunk_size} (scoping size: {scoping.size})")

    return splitter.split(chunk_size, end_input_pin, rescope)
