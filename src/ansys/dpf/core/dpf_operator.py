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

"""Operator."""

from enum import Enum
import logging
import os
import traceback
import warnings

import numpy

from ansys.dpf.core import server as server_module
from ansys.dpf.core.check_version import (
    server_meet_version,
    server_meet_version_and_raise,
    version_requires,
)
from ansys.dpf.core.common import types, types_enum_to_types
from ansys.dpf.core.config import Config
from ansys.dpf.core.errors import DpfVersionNotSupported
from ansys.dpf.core.inputs import Inputs
from ansys.dpf.core.operator_specification import Specification
from ansys.dpf.core.outputs import Output, Outputs, _Outputs
from ansys.dpf.core.unit_system import UnitSystem
from ansys.dpf.gate import (
    collection_capi,
    collection_grpcapi,
    data_processing_capi,
    data_processing_grpcapi,
    dpf_vector,
    integral_types,
    object_handler,
    operator_abstract_api,
    operator_capi,
    operator_grpcapi,
)

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")


class _SubOperator:
    def __init__(self, op_name, op_to_connect):
        self.op_name = op_name
        self.op = Operator(self.op_name, server=op_to_connect._server)
        if op_to_connect.inputs is not None:
            for key in op_to_connect.inputs._connected_inputs:
                inpt = op_to_connect.inputs._connected_inputs[key]
                if type(inpt).__name__ == "dict":
                    for keyout in inpt:
                        if inpt[keyout]() is not None:
                            self.op.connect(key, inpt[keyout](), keyout)
                else:
                    self.op.connect(key, inpt())

    def __call__(self):
        return self.op


class Operator:
    """Represents an operator, which is an elementary operation.

    The operator is the only object used to create and transform
    data. When the operator is evaluated, it processes the
    input information to compute its output with respect to its
    description.

    Parameters
    ----------
    name : str
        Name of the operator. For example, ``"U"``. You can use the
        ``"html_doc"`` operator to retrieve a list of existing operators.

    config : Config, optional
        The Configuration allows to customize how the operation
        will be processed by the operator. The default is ``None``.

    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create an operator from the library of operators.

    >>> from ansys.dpf import core as dpf
    >>> disp_oper = dpf.operators.result.displacement()

    Create an operator from a model.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> model = Model(examples.find_static_rst())
    >>> disp_oper = model.results.displacement()

    """

    def __init__(self, name=None, config=None, server=None, operator=None):
        """Initialize the operator with its name by connecting to a stub."""
        self.name = name
        self._internal_obj = None
        self._description = None
        self._inputs = None
        self._id = None

        # step 1: get server
        self._server = server_module.get_or_create_server(
            config._server if isinstance(config, Config) else server
        )

        # step 2: get api
        self._api_instance = None  # see _api property

        # step 3: init environment
        self._api.init_operator_environment(self)  # creates stub when gRPC

        # step 4: if object exists, take the instance, else create it
        if operator is not None:
            if isinstance(operator, Operator):
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(operator)
                self.name = operator.name
            else:
                self._internal_obj = operator
                self.name = self._api.operator_name(self)
        else:
            if self._server.has_client():
                self._internal_obj = self._api.operator_new_on_client(
                    self.name, self._server.client
                )
            else:
                self._internal_obj = self._api.operator_new(self.name)

        if self._internal_obj is None:
            raise KeyError(
                f"The operator {self.name} doesn't exist in the registry. "
                f"Check its spelling in the documentation or verify its availability "
                f"in your loaded plugins. The current available operator names can be "
                f"accessed using 'available_operator_names' method."
            )

        self._spec = Specification(operator_name=self.name, server=self._server)
        # add dynamic inputs
        if len(self._spec.inputs) > 0 and self._inputs is None:
            self._inputs = Inputs(self._spec.inputs, self)

        # step4: if object exists: take instance (config)
        if config:
            self.config = config

        self._description = self._spec.description
        self._progress_bar = False

    @property
    def _api(self) -> operator_abstract_api.OperatorAbstractAPI:
        if self._api_instance is None:
            self._api_instance = self._server.get_api_for_type(
                capi=operator_capi.OperatorCAPI,
                grpcapi=operator_grpcapi.OperatorGRPCAPI,
            )
        return self._api_instance

    def _add_sub_res_operators(self, sub_results):
        """Dynamically add operators for instantiating subresults.

        Subresults for new operators are connected to the parent
        operator's inputs when created but are then completely
        independent of them.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> model = Model(examples.find_static_rst())
        >>> disp_oper = model.results.displacement()
        >>> disp_oper = model.results.displacement()
        >>> disp_x = model.results.displacement().X()
        >>> disp_y = model.results.displacement().Y()
        >>> disp_z = model.results.displacement().Z()

        """
        for result_type in sub_results:
            try:
                setattr(
                    self,
                    result_type["name"],
                    _SubOperator(result_type["operator name"], self),
                )
            except KeyError:
                pass

    @property
    def _outputs(self):
        if self._spec and len(self._spec.outputs) != 0:
            return Outputs(self._spec.outputs, self)

    @_outputs.setter
    def _outputs(self, value):
        # the Operator should not hold a reference on its outputs because outputs hold a reference
        # on the Operator
        pass

    @property
    @version_requires("3.0")
    def progress_bar(self) -> bool:
        """Enable or disable progress bar display when requesting the operator's output.

        With this property, the user can choose to print a progress bar when
        the operator's output is requested, default is False
        """
        return self._progress_bar

    @progress_bar.setter
    def progress_bar(self, value: bool) -> None:
        self._progress_bar = value

    def connect(self, pin, inpt, pin_out=0):
        """Connect an input on the operator using a pin number.

        Parameters
        ----------
        pin : int
            Number of the input pin.

        inpt : str, int, double, bool, list[int], list[float], Field, FieldsContainer, Scoping,
        ScopingsContainer, MeshedRegion, MeshesContainer, DataSources, CyclicSupport, dict, Outputs
            Operator, os.PathLike Object to connect to.

        pin_out : int, optional
            If the input is an operator, the output pin of the input operator. The default is ``0``.

        Examples
        --------
        Compute the minimum of displacement by chaining the ``"U"`` and ``"min_max_fc"`` operators.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.find_multishells_rst())
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> max_fc_op = dpf.operators.min_max.min_max_fc()
        >>> max_fc_op.inputs.connect(disp_op.outputs)
        >>> max_field = max_fc_op.outputs.field_max()
        >>> max_field.data
        DPFArray([[0.59428386, 0.00201751, 0.0006032 ]]...

        """
        if inpt is self:
            raise ValueError("Cannot connect to itself.")
        elif isinstance(inpt, Operator):
            self._api.operator_connect_operator_output(self, pin, inpt, pin_out)
        elif isinstance(inpt, Output):
            self._api.operator_connect_operator_output(self, pin, inpt._operator, inpt._pin)
        elif isinstance(inpt, (list, numpy.ndarray)):
            from ansys.dpf.core import collection

            inpt = collection.CollectionBase.integral_collection(inpt, self._server)
            self._api.operator_connect_collection_as_vector(self, pin, inpt)
        elif isinstance(inpt, dict):
            from ansys.dpf.core import label_space

            label_space_to_con = label_space.LabelSpace(
                label_space=inpt, obj=self, server=self._server
            )
            self._api.operator_connect_label_space(self, pin, label_space_to_con)
        elif isinstance(inpt, UnitSystem):
            if inpt.ID != -2:  # Ansys UnitSystem
                self.connect(pin, inpt.ID)
            else:  # Custom UnitSystem
                self.connect(pin, inpt.unit_names)
        else:
            if isinstance(inpt, os.PathLike):
                inpt = str(inpt)
            for type_tuple in self._type_to_input_method:
                if isinstance(inpt, type_tuple[0]):
                    if len(type_tuple) == 3:
                        inpt = type_tuple[2](inpt)
                    return type_tuple[1](self, pin, inpt)
            errormsg = f"input type {inpt.__class__} cannot be connected"
            raise TypeError(errormsg)

    @version_requires("6.2")
    def connect_operator_as_input(self, pin, op):
        """Connect an operator as an input on a pin.

        Parameters
        ----------
        pin : int
            Number of the output pin. The default is ``0``.
        op : :class:`ansys.dpf.core.dpf_operator.Operator`
            Requested type of the output. The default is ``None``.
        """
        self._api.operator_connect_operator_as_input(self, pin, op)

    @staticmethod
    def _getoutput_string(self, pin):
        out = Operator._getoutput_string_as_bytes(self, pin)
        if out is not None and not isinstance(out, str):
            return out.decode("utf-8")
        return out

    @staticmethod
    def _connect_string(self, pin, str):
        return Operator._connect_string_as_bytes(self, pin, str.encode("utf-8"))

    @staticmethod
    def _getoutput_string_as_bytes(self, pin):
        if server_meet_version("8.0", self._server):
            size = integral_types.MutableUInt64(0)
            return self._api.operator_getoutput_string_with_size(self, pin, size)
        else:
            return self._api.operator_getoutput_string(self, pin)

    @staticmethod
    def _getoutput_bytes(self, pin):
        server_meet_version_and_raise(
            "8.0",
            self._server,
            "output of type bytes available with server's version starting at 8.0 (Ansys 2024R2).",
        )
        return Operator._getoutput_string_as_bytes(self, pin)

    @staticmethod
    def _connect_string_as_bytes(self, pin, str):
        if server_meet_version("8.0", self._server):
            size = integral_types.MutableUInt64(len(str))
            return self._api.operator_connect_string_with_size(self, pin, str, size)
        else:
            return self._api.operator_connect_string(self, pin, str)

    @property
    def _type_to_output_method(self):
        from ansys.dpf.core import (
            any,
            collection,
            collection_base,
            custom_container_base,
            custom_type_field,
            cyclic_support,
            data_sources,
            data_tree,
            field,
            fields_container,
            generic_data_container,
            mesh_info,
            meshed_region,
            meshes_container,
            property_field,
            result_info,
            scoping,
            scopings_container,
            streams_container,
            string_field,
            time_freq_support,
            workflow,
        )

        out = [
            (any.Any, self._api.operator_getoutput_as_any),
            (bool, self._api.operator_getoutput_bool),
            (int, self._api.operator_getoutput_int),
            (str, self._getoutput_string),
            (bytes, self._getoutput_bytes),
            (float, self._api.operator_getoutput_double),
            (field.Field, self._api.operator_getoutput_field, "field"),
            (
                property_field.PropertyField,
                self._api.operator_getoutput_property_field,
                "property_field",
            ),
            (
                string_field.StringField,
                self._api.operator_getoutput_string_field,
                "string_field",
            ),
            (
                custom_type_field.CustomTypeField,
                self._api.operator_getoutput_custom_type_field,
                "field",
            ),
            (scoping.Scoping, self._api.operator_getoutput_scoping, "scoping"),
            (
                fields_container.FieldsContainer,
                self._api.operator_getoutput_fields_container,
                "fields_container",
            ),
            (
                scopings_container.ScopingsContainer,
                self._api.operator_getoutput_scopings_container,
                "scopings_container",
            ),
            (
                meshes_container.MeshesContainer,
                self._api.operator_getoutput_meshes_container,
                "meshes_container",
            ),
            (
                streams_container.StreamsContainer,
                self._api.operator_getoutput_streams,
                "streams_container",
            ),
            (
                data_sources.DataSources,
                self._api.operator_getoutput_data_sources,
                "data_sources",
            ),
            (
                cyclic_support.CyclicSupport,
                self._api.operator_getoutput_cyclic_support,
                "cyclic_support",
            ),
            (
                meshed_region.MeshedRegion,
                self._api.operator_getoutput_meshed_region,
                "mesh",
            ),
            (
                result_info.ResultInfo,
                self._api.operator_getoutput_result_info,
                "result_info",
            ),
            (
                time_freq_support.TimeFreqSupport,
                self._api.operator_getoutput_time_freq_support,
                "time_freq_support",
            ),
            (
                mesh_info.MeshInfo,
                "mesh_info",
            ),
            (workflow.Workflow, self._api.operator_getoutput_workflow, "workflow"),
            (data_tree.DataTree, self._api.operator_getoutput_data_tree, "data_tree"),
            (Operator, self._api.operator_getoutput_operator, "operator"),
            (
                dpf_vector.DPFVectorInt,
                self._api.operator_getoutput_int_collection,
                lambda obj, type: collection_base.IntCollection(
                    server=self._server, collection=obj
                ).get_integral_entries(),
            ),
            (
                dpf_vector.DPFVectorDouble,
                self._api.operator_getoutput_double_collection,
                lambda obj, type: collection_base.FloatCollection(
                    server=self._server, collection=obj
                ).get_integral_entries(),
            ),
            (
                collection.Collection,
                self._api.operator_getoutput_as_any,
                lambda obj, type: any.Any(server=self._server, any_dpf=obj).cast(type),
            ),
            (
                custom_container_base.CustomContainerBase,
                self._api.operator_getoutput_generic_data_container,
                lambda obj, type: type(
                    container=generic_data_container.GenericDataContainer(
                        generic_data_container=obj, server=self._server
                    )
                ),
            ),
        ]
        if hasattr(self._api, "operator_getoutput_generic_data_container"):
            out.append(
                (
                    generic_data_container.GenericDataContainer,
                    self._api.operator_getoutput_generic_data_container,
                    "generic_data_container",
                )
            )
        return out

    @property
    def _type_to_input_method(self):
        from ansys.dpf.core import (
            any,
            collection_base,
            custom_type_field,
            cyclic_support,
            data_sources,
            data_tree,
            field,
            generic_data_container,
            meshed_region,
            model,
            property_field,
            scoping,
            streams_container,
            string_field,
            time_freq_support,
            workflow,
        )

        out = [
            (streams_container.StreamsContainer, self._api.operator_connect_streams),
            (any.Any, self._api.operator_connect_any),
            (bool, self._api.operator_connect_bool),
            ((int, Enum), self._api.operator_connect_int),
            (str, self._connect_string),
            (bytes, self._connect_string_as_bytes),
            (float, self._api.operator_connect_double),
            (field.Field, self._api.operator_connect_field),
            (property_field.PropertyField, self._api.operator_connect_property_field),
            (string_field.StringField, self._api.operator_connect_string_field),
            (
                custom_type_field.CustomTypeField,
                self._api.operator_connect_custom_type_field,
            ),
            (scoping.Scoping, self._api.operator_connect_scoping),
            (collection_base.CollectionBase, self._api.operator_connect_collection),
            (data_sources.DataSources, self._api.operator_connect_data_sources),
            (
                model.Model,
                self._api.operator_connect_data_sources,
                lambda obj: obj.metadata.data_sources,
            ),
            (cyclic_support.CyclicSupport, self._api.operator_connect_cyclic_support),
            (meshed_region.MeshedRegion, self._api.operator_connect_meshed_region),
            # TO DO: (result_info.ResultInfo, self._api.operator_connect_result_info),
            (
                time_freq_support.TimeFreqSupport,
                self._api.operator_connect_time_freq_support,
            ),
            (workflow.Workflow, self._api.operator_connect_workflow),
            (data_tree.DataTree, self._api.operator_connect_data_tree),
            (Operator, self._api.operator_connect_operator_as_input),
        ]
        if hasattr(self._api, "operator_connect_generic_data_container"):
            out.append(
                (
                    generic_data_container.GenericDataContainer,
                    self._api.operator_connect_generic_data_container,
                )
            )
        return out

    def get_output(self, pin=0, output_type=None):
        """Retrieve the output of the operator on the pin number.

        To activate the progress bar for server version higher or equal to 3.0,
        use ``my_op.progress_bar=True``

        Parameters
        ----------
        pin : int, optional
            Number of the output pin. The default is ``0``.
        output_type : :class:`ansys.dpf.core.common.types`, type,  optional
            Requested type of the output. The default is ``None``.

        Returns
        -------
        type
            Output of the operator.
        """
        output_type = _write_output_type_to_type(output_type)
        if self._server.meet_version("3.0") and self.progress_bar:
            self._server.session.add_operator(self, pin, "operator")
            self._progress_thread = self._server.session.listen_to_progress()
        if output_type is None:
            return self._api.operator_run(self)
        out = None
        for type_tuple in self._type_to_output_method:
            if issubclass(output_type, type_tuple[0]):
                if len(type_tuple) >= 3:
                    internal_obj = type_tuple[1](self, pin)
                    if internal_obj is None:
                        self._progress_thread = None
                        return
                    if isinstance(type_tuple[2], str):
                        parameters = {type_tuple[2]: internal_obj}
                        out = output_type(**parameters, server=self._server)
                    else:
                        out = type_tuple[2](internal_obj, output_type)
                if out is None:
                    internal_obj = type_tuple[1](self, pin)
                    if internal_obj is None:
                        self._progress_thread = None
                        return
                    try:
                        return output_type(internal_obj, server=self._server)
                    except TypeError:
                        self._progress_thread = None
                        return output_type(internal_obj)

        if out is not None:
            self._progress_thread = None
            return out
        raise TypeError(f"{output_type} is not an implemented Operator's output")

    @property
    def config(self):
        """Copy of the operator's current configuration.

        You can modify the copy of the configuration and then use ``operator.config = new_config``
        or instantiate an operator with the new configuration as a parameter.

        For information on an operator's options, see the documentation for that operator.

        Returns
        -------
        :class:`ansys.dpf.core.config.Config`
            Copy of the operator's current configuration.

        Examples
        --------
        Modify the copy of an operator's configuration and set it as current config
        of the operator.

        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.add()
        >>> config_add = op.config
        >>> config_add.set_work_by_index_option(True)
        >>> op.config = config_add

        """
        config = self._api.operator_get_config(self)
        return Config(config=config, server=self._server, spec=self._spec)

    @config.setter
    def config(self, value):
        """Change the configuration of the operator.

        If the operator is up to date, changing the configuration
        doesn't make it not up to date.

        Parameters
        ----------
        value : Config
        """
        self._api.operator_set_config(self, value)

    @property
    @version_requires("10.0")
    def id(self) -> int:
        """Retrieve the unique identifier of the operator.

        This property returns the unique ID associated with the operator.
        This property is lazily initialized.

        Returns
        -------
        int
            The unique identifier of the operator.

        Notes
        -----
        Property available with server's version starting at 10.0.
        """
        if self._id is None:
            operator_id_op = Operator("operator_id", server=self._server)
            operator_id_op.connect_operator_as_input(0, self)
            self._id = operator_id_op.outputs.id()

        return self._id

    @property
    def inputs(self) -> Inputs:
        """Inputs connected to the operator.

        Returns
        -------
        :class:`ansys.dpf.core.inputs`
            Inputs connected to the operator.

        Examples
        --------
        Use the displacement operator.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.find_multishells_rst())
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)

        """
        return self._inputs

    @property
    def outputs(self) -> Outputs:
        """Outputs from the operator's evaluation.

        Returns
        -------
        :class:`ansys.dpf.core.outputs`
            Outputs from the operator's evaluation.

        Examples
        --------
        Use the displacement operator.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.find_multishells_rst())
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> disp_fc = disp_op.outputs.fields_container()

        """
        return self._outputs

    @staticmethod
    def default_config(name, server=None):
        """Retrieve the default configuration for an operator.

        You can change the copy of the default configuration to meet your needs
        before instantiating the operator.
        The Configuration allows to customize how the operation
        will be processed by the operator.

        Parameters
        ----------
        name : str
            Name of the operator.  For example ``"U"``. You can use the
            ``"html_doc"`` operator to retrieve a list of existing operators.
        server : server.DPFServer, optional
            Server with the channel connected to the remote or local instance. The
            default is ``None``, in which case an attempt is made to use the global
            server.

        Returns
        -------
        :class"`ansys.dpf.core.config.Config`
            Default configuration for the operator.

        """
        return Config(operator_name=name, server=server)

    def __del__(self):
        """Delete this instance."""
        try:
            if hasattr(self, "_deleter_func"):
                obj = self._deleter_func[1](self)
                if obj is not None:
                    self._deleter_func[0](obj)
        except:
            warnings.warn(traceback.format_exc())

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def run(self):
        """Evaluate this operator."""
        self.get_output()

    def eval(self, pin=None):
        """Evaluate this operator.

        Parameters
        ----------
        pin : int
            Number of the output pin. The default is ``None``.

        Returns
        -------
        output : FieldsContainer, Field, MeshedRegion, Scoping
            Returns the first output of the operator by default and the output of a
            given pin when specified. Or, it only evaluates the operator without output.

        Examples
        --------
        Use the ``eval`` method.

        >>> from ansys.dpf import core as dpf
        >>> import ansys.dpf.core.operators.math as math
        >>> from ansys.dpf.core import examples
        >>> data_src = dpf.DataSources(examples.find_multishells_rst())
        >>> disp_op = dpf.operators.result.displacement()
        >>> disp_op.inputs.data_sources(data_src)
        >>> normfc = math.norm_fc(disp_op).eval()

        """
        if not pin:
            if self.outputs != None and len(self.outputs._outputs) > 0:
                return self.outputs._outputs[0]()
            else:
                self.run()
        else:
            for output in self.outputs._outputs:
                if output._pin == pin:
                    return output()

    def _find_outputs_corresponding_pins(self, type_names, inpt, pin, corresponding_pins):
        from ansys.dpf.core.results import Result

        for python_name in type_names:
            # appears to be an issue on Linux.  This check is here
            # because cpp mappings are a single type mapping and
            # sometimes the spec contains 'B' instead of 'bool'
            if python_name == "B":
                python_name = "bool"

            # Type match
            if type(inpt).__name__ == python_name:
                corresponding_pins.append(pin)
            # if the inpt has multiple potential outputs, find which ones can match
            elif isinstance(inpt, (_Outputs, Operator, Result)):
                if isinstance(inpt, Operator):
                    output_pin_available = inpt.outputs._get_given_output([python_name])
                elif isinstance(inpt, Result):
                    output_pin_available = inpt().outputs._get_given_output([python_name])
                else:
                    output_pin_available = inpt._get_given_output([python_name])
                for outputpin in output_pin_available:
                    corresponding_pins.append((pin, outputpin))
            # If any output type matches python_name
            elif isinstance(inpt, Output):
                if python_name == "Any":
                    corresponding_pins.append(pin)
                else:
                    for inpttype in inpt._python_expected_types:
                        if inpttype == python_name:
                            corresponding_pins.append(pin)
            elif python_name == "Any":
                corresponding_pins.append(pin)

    def __add__(self, fields_b):
        """Add two fields or two fields containers.

        Returns
        -------
        add : operators.math.add_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "add_fc"):
            op = operators.math.add_fc(self, fields_b, server=self._server)
        else:
            op = dpf_operator.Operator("add_fc", server=self._server)
            op.connect(0, self)
            op.connect(1, fields_b)
        return op

    def __sub__(self, fields_b):
        """Subtract two fields or two fields containers.

        Returns
        -------
        minus : operators.math.minus_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "minus_fc"):
            op = operators.math.minus_fc(server=self._server)
        else:
            op = dpf_operator.Operator("minus_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, fields_b)
        return op

    def __pow__(self, value):
        """Raise each element of a field or a fields container to power 2."""
        if value != 2:
            raise ValueError('Only the value "2" is supported.')
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "sqr_fc"):
            op = operators.math.sqr_fc(server=self._server)
        else:
            op = dpf_operator.Operator("sqr_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    def __mul__(self, value):
        """Multiply two fields or two fields containers.

        Returns
        -------
        mul : operators.math.generalized_inner_product_fc
        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "generalized_inner_product_fc"):
            op = operators.math.generalized_inner_product_fc(server=self._server)
        else:
            op = dpf_operator.Operator("generalized_inner_product_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    @staticmethod
    def operator_specification(op_name, server=None):
        """Documents an Operator with its description (what the Operator does),its inputs and outputs and some properties."""
        return Specification(operator_name=op_name, server=server)

    @property
    def specification(self):
        """Returns the Specification (or documentation) of this Operator.

        Returns
        -------
        Specification
        """
        if isinstance(self._spec, Specification):
            return self._spec
        else:
            return Specification(operator_name=self.name, server=self._server)

    def __truediv__(self, inpt):
        """
        Perform division with another operator or a scalar.

        This method allows the use of the division operator (`/`) between an
        `Operator` instance and either another `Operator` or a scalar value (float).
        """
        if isinstance(inpt, Operator):
            op = Operator("div")
            op.connect(0, self, 0)
            op.connect(1, inpt, 0)
        elif isinstance(inpt, float):
            op = Operator("scale")
            op.connect(0, self, 0)
            op.connect(1, 1.0 / inpt)
        return op


def available_operator_names(server=None):
    """Return the list of operator names available in the server.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
    list

    Notes
    -----
    Function available with server's version starting at 3.0. Not available for server
    of type GrpcServer.

    """
    if server is None:
        server = server_module._global_server()

    if not server.meet_version("3.0"):
        raise DpfVersionNotSupported("3.0")

    api = server.get_api_for_type(
        capi=data_processing_capi.DataProcessingCAPI,
        grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
    )
    api.init_data_processing_environment(server)  # creates stub when gRPC
    coll_api = server.get_api_for_type(
        capi=collection_capi.CollectionCAPI,
        grpcapi=collection_grpcapi.CollectionGRPCAPI,
    )
    coll_api.init_collection_environment(server)

    if server.has_client():
        coll_obj = object_handler.ObjHandler(
            data_processing_api=api,
            internal_obj=api.data_processing_list_operators_as_collection_on_client(server.client),
        )
    else:
        coll_obj = object_handler.ObjHandler(
            data_processing_api=api,
            internal_obj=api.data_processing_list_operators_as_collection(),
        )
    num = coll_api.collection_get_size(coll_obj)
    out = []
    for i in range(num):
        out.append(coll_api.collection_get_string_entry(coll_obj, i))
    return out


def _write_output_type_to_type(output_type):
    if isinstance(output_type, str):
        output_type = types[output_type]

    if isinstance(output_type, types):
        try:
            return types_enum_to_types()[output_type]
        except KeyError as e:
            raise TypeError(f"{output_type} is not an implemented Operator's output")
    return output_type
