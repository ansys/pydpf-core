# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""
FieldsContainer.

Contains classes associated with the DPF FieldsContainer.
"""

from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING, Sequence, Union

from ansys import dpf
from ansys.dpf.core import errors as dpf_errors, field
from ansys.dpf.core.check_version import server_meet_version
from ansys.dpf.core.collection_base import CollectionBase
from ansys.dpf.core.common import shell_layers

if TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.core import Operator, Result


class FieldsContainer(CollectionBase["field.Field"]):
    """Represents a fields container, which contains fields belonging to a common result.

    A fields container is a set of fields ordered by labels and IDs. Each field
    of the fields container has an ID for each label defining the given fields
    container. These IDs allow splitting the fields on any criteria.

    The most common fields container has the label ``"time"`` with IDs
    corresponding to time sets. The label ``"complex"``, which is
    used in a harmonic analysis for example, allows real parts (``id=0``)
    to be separated from imaginary parts (``id=1``).

    For more information, see the `Fields container and fields
    <https://dpf.docs.pyansys.com/version/stable/user_guide/fields_container.html>`_
    documentation section.

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_message_pb2.Collection, ctypes.c_void_p,
    FieldsContainer, optional
        Fields container created from either a collection message or by copying an existing
        fields container. The default is "None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Extract a displacement fields container from a transient result file.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> disp.inputs.time_scoping.connect([1,5])
    >>> fields_container = disp.outputs.fields_container()
    >>> field_set_5 =fields_container.get_fields_by_time_complex_ids(5)
    >>> #print(fields_container)


    Create a fields container from scratch.

    >>> from ansys.dpf import core as dpf
    >>> fc= dpf.FieldsContainer()
    >>> fc.labels =['time','complex']
    >>> for i in range(0,20): #real fields
    ...     mscop = {"time":i+1,"complex":0}
    ...     fc.add_field(mscop,dpf.Field(nentities=i+10))
    >>> for i in range(0,20): #imaginary fields
    ...     mscop = {"time":i+1,"complex":1}
    ...     fc.add_field(mscop,dpf.Field(nentities=i+10))

    """

    def __init__(self, fields_container=None, server=None):
        super().__init__(collection=fields_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_field_new_on_client(
                    self._server.client
                )
            else:
                self._internal_obj = self._api.collection_of_field_new()

        self._component_index = None  # component index
        self._component_info = None  # for norm/max/min

    def create_subtype(self, obj_by_copy):
        """Create a field subtype."""
        return field.Field(field=obj_by_copy, server=self._server)

    def get_fields_by_time_complex_ids(self, timeid=None, complexid=None):
        """Retrieve fields at a requested time ID or complex ID.

        Parameters
        ----------
        timeid : int, optional
            Time ID or frequency ID, which is the one-based index of the
            result set.
        complexid : int, optional
            Complex ID, where ``1`` is for imaginary and ``0`` is for real.

        Returns
        -------
        fields : list[Field]
            Fields corresponding to the request.

        Examples
        --------
        Extract the fifth time set of a transient analysis.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> len(model.metadata.time_freq_support.time_frequencies)
        35
        >>> disp = model.results.displacement()
        >>> disp.inputs.time_scoping.connect([1,5])
        >>> fields_container = disp.outputs.fields_container()
        >>> field_set_5 =fields_container.get_fields_by_time_complex_ids(5)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        return super()._get_entries(label_space)

    def get_field_by_time_complex_ids(self, timeid=None, complexid=None):
        """Retrieve a field at a requested time ID or complex ID.

        An exception is raised if the number of fields matching the request is
        greater than one.

        Parameters
        ----------
        timeid : int, optional
            Time ID or frequency ID, which is the one-based index of the
            result set.
        complexid : int, optional
            Complex ID, where ``1`` is for imaginary and ``0`` is for real.

        Returns
        -------
        fields : Field
            Field corresponding to the request

        Examples
        --------
        Extract the fifth time set of a transient analysis.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> len(model.metadata.time_freq_support.time_frequencies)
        35
        >>> disp = model.results.displacement()
        >>> disp.inputs.time_scoping.connect([1,5])
        >>> fields_container = disp.outputs.fields_container()
        >>> field_set_5 =fields_container.get_fields_by_time_complex_ids(5)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        return super()._get_entry(label_space)

    def __time_complex_label_space__(self, timeid=None, complexid=None):
        """Return a label space dictionary mapping scoping to given id.

        Parameters
        ----------
        timeid : int, optional
            time based id, by default None
        complexid : int, optional
            complex id, by default None

        Returns
        -------
        dict[str,int]
            mapping of space type to given id.
        """
        label_space = {}
        if timeid is not None:
            label_space["time"] = timeid
        if complexid is not None:
            label_space["complex"] = complexid
        return label_space

    def get_fields(self, label_space):
        """Retrieve the fields at a requested index or label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Scoping of the requested fields. For example,
            ``{"time": 1, "complex": 0}``.

        Returns
        -------
        fields : list[Field]
            Fields corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> fc= dpf.FieldsContainer()
        >>> fc.labels =['time','complex']
        >>> #real fields
        >>> for i in range(0,20):
        ...     mscop = {"time":i+1,"complex":0}
        ...     fc.add_field(mscop,dpf.Field(nentities=i+10))
        >>> #imaginary fields
        >>> for i in range(0,20):
        ...     mscop = {"time":i+1,"complex":1}
        ...     fc.add_field(mscop,dpf.Field(nentities=i+10))

        >>> fields = fc.get_fields({"time":2})
        >>> # imaginary and real fields of time 2
        >>> len(fields)
        2

        """
        return super()._get_entries(label_space)

    def get_field(self, label_space_or_index):
        """Retrieve the field at a requested index or label space.

        An exception is raised if the number of fields matching the request is
        greater than one.

        Parameters
        ----------
        label_space_or_index : dict[str,int], int
            Scoping of the requested fields. For example,
            ``{"time": 1, "complex": 0}`` or the index of the field.

        Returns
        -------
        field : Field
            Field corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> fc = dpf.fields_container_factory.over_time_freq_fields_container(
        ...     [dpf.Field(nentities=10)]
        ... )
        >>> field = fc.get_field({"time":1})

        """
        return super()._get_entry(label_space_or_index)

    def get_field_by_time_id(self, timeid=None):
        """Retrieve the complex field at a requested time.

        Parameters
        ----------
        timeid: int, optional
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        fields : Field
            Fields corresponding to the request.
        """
        if not self.has_label("time"):
            raise dpf_errors.DpfValueError("The fields container is not based on time scoping.")

        if self.has_label("complex"):
            label_space = self.__time_complex_label_space__(timeid, 0)
        else:
            label_space = self.__time_complex_label_space__(timeid)

        return super()._get_entry(label_space)

    def get_imaginary_fields(self, timeid=None):
        """Retrieve the complex fields at a requested time.

        Parameters
        ----------
        timeid: int, optional
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        fields : list[Field]
            Fields corresponding to the request.
        """
        if not self.has_label("complex") or not self.has_label("time"):
            raise dpf_errors.DpfValueError(
                "The fields container is not based on time and complex scoping."
            )

        label_space = self.__time_complex_label_space__(timeid, 1)

        return super()._get_entries(label_space)

    def get_imaginary_field(self, timeid=None):
        """Retrieve the complex field at a requested time.

        Parameters
        ----------
        timeid: int, optional
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        fields : Field
            Field corresponding to the request.
        """
        if not self.has_label("complex") or not self.has_label("time"):
            raise dpf_errors.DpfValueError(
                "The fields container is not based on time and complex scoping."
            )

        label_space = self.__time_complex_label_space__(timeid, 1)

        return super()._get_entry(label_space)

    def __getitem__(self, key) -> "field.Field":
        """Retrieve the field at a requested index.

        Parameters
        ----------
        key : int
            Index.

        Returns
        -------
        field : Field
            Field corresponding to the request.
        """
        return super().__getitem__(key)

    def add_field(self, label_space, field):
        """Add or update a field at a requested label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Label space of the requested field. For example,
            {"time":1, "complex":0}.
        field : Field
            DPF field to add or update.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> fc= dpf.FieldsContainer()
        >>> fc.labels =['time','complex']
        >>> for i in range(0,20): #real fields
        ...     mscop = {"time":i+1,"complex":0}
        ...     fc.add_field(mscop,dpf.Field(nentities=i+10))
        >>> for i in range(0,20): #imaginary fields
        ...     mscop = {"time":i+1,"complex":1}
        ...     fc.add_field(mscop,dpf.Field(nentities=i+10))

        """
        super()._add_entry(label_space, field)

    def add_field_by_time_id(self, field, timeid=1):
        """Add or update a field at a requested time ID.

        Parameters
        ----------
        field : Field
            DPF field to add or update.
        timeid: int, optional
            Time ID for the requested time set. The default is ``1``.

        """
        labels = self.labels
        if not self.has_label("time") and (
            len(self.labels) == 0 or (len(self.labels) == 1 and self.has_label("complex"))
        ):
            self.add_label("time")
        if len(self.labels) == 1:
            super()._add_entry({"time": timeid}, field)
        elif self.has_label("time") and self.has_label("complex") and len(labels) == 2:
            super()._add_entry({"time": timeid, "complex": 0}, field)
        else:
            raise dpf_errors.DpfValueError(
                "The fields container is not only based on time scoping."
            )

    def add_imaginary_field(self, field, timeid=1):
        """Add or update an imaginary field at a requested time ID.

        Parameters
        ----------
        field : Field
            DPF field to add or update.
        timeid: int, optional
            Time ID for the requested time set. The default is ``1``.
        """
        if not self.has_label("time") and (
            len(self.labels) == 0 or (len(self.labels) == 1 and self.has_label("complex"))
        ):
            self.add_label("time")
        if not self.has_label("complex") and len(self.labels) == 1 and self.has_label("time"):
            self.add_label("complex")
        if self.has_label("time") and self.has_label("complex") and len(self.labels) == 2:
            super()._add_entry({"time": timeid, "complex": 1}, field)
        else:
            raise dpf_errors.DpfValueError(
                "The fields container is not only based on time scoping."
            )

    def select_component(self, index):
        """Select fields containing only the component index.

        Fields can be selected only by component index as multiple fields may
        contain a different number of components.

        Parameters
        ----------
        index : int
            Index of the component.

        Returns
        -------
        fields : FieldsContainer
            Fields container with one component selected in each field.

        Examples
        --------
        Select using a component index.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> disp.inputs.time_scoping.connect([1,5])
        >>> fields_container = disp.outputs.fields_container()
        >>> disp_x_fields = fields_container.select_component(0)
        >>> my_field = disp_x_fields[0]

        """
        comp_select = dpf.core.Operator("component_selector_fc")
        comp_select.connect(0, self)
        comp_select.connect(1, index)
        return comp_select.outputs.fields_container.get_data()

    @property
    def time_freq_support(self):
        """Time frequency support."""
        return self._get_time_freq_support()

    @time_freq_support.setter
    def time_freq_support(self, value):
        return super()._set_time_freq_support(value)

    def deep_copy(self, server=None):
        """Create a deep copy of the fields container's data (and its fields) on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        fields_container_copy : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> disp.inputs.time_scoping.connect([1,5])
        >>> fields_container = disp.outputs.fields_container()
        >>> other_server = dpf.start_local_server(as_global=False)
        >>> deep_copy = fields_container.deep_copy(server=other_server)

        """
        fc = FieldsContainer(server=server)
        fc.labels = self.labels
        for i, f in enumerate(self):
            fc.add_field(self.get_label_space(i), f.deep_copy(server))
        with suppress(Exception):
            if server_meet_version("12.0", self._server):
                self.deep_copy_supports(fc)
            else:
                fc.time_freq_support = self.time_freq_support.deep_copy(server)
        return fc

    def get_time_scoping(self):
        """Retrieve the time scoping containing the time sets.

        Returns
        -------
        scoping: Scoping
            Scoping containing the time set IDs available in the fields container.
        """
        return self.get_label_scoping("time")

    def plot(self, label_space: dict = None, **kwargs):
        """Plot the fields in the FieldsContainer for the given LabelSpace.

        Check the labels available for the FieldsContainer with
        :func:`~fields_container.FieldsContainer.labels`.

        Parameters
        ----------
        label_space:
            A dictionary (LabelSpace) of labels of the :class:`FieldsContainer` with associated
            values to select for plotting.
            This is used to filter the data to plot, for example:
            - if ``label_space={'time': 10}``: a single time step (mandatory for transient)
            - if ``label_space={'complex': 0, 'part': 12}``: real part of complex data for a part
            See :func:`~fields_container.FieldsContainer.get_fields`.
            If None is given, it renders all fields available, which may not make sense.
        **kwargs:
            For more information on accepted keyword arguments, see :func:`~field.Field.plot` and
            :class:`~plotter.DpfPlotter`.
        """
        from ansys.dpf.core import plotter

        plt = plotter.DpfPlotter(**kwargs)
        if label_space is None:
            label_space = {}
        fields = self.get_fields(label_space=label_space)
        # Fields with same support will override each other so we first merge them
        merge_op = dpf.core.operators.utility.merge_fields()
        for i, f in enumerate(fields):
            merge_op.connect(i, f)
        merged_field = merge_op.eval()
        plt.add_field(field=merged_field, **kwargs)
        return plt.show_figure(**kwargs)

    def animate(
        self,
        save_as: str = None,
        deform_by: Union[FieldsContainer, Result, Operator] = None,
        scale_factor: Union[float, Sequence[float]] = 1.0,
        shell_layer: shell_layers = shell_layers.top,
        label: str = "time",
        **kwargs,
    ):
        """Create an animation based on the Fields contained in the FieldsContainer.

        Iterates over the entries indexed by *label*, rendering each
        :class:`~ansys.dpf.core.Field` as a separate frame.
        For kwargs see pyvista.Plotter.open_movie/add_text/show.

        Parameters
        ----------
        save_as:
            Path of file to save the animation to. Defaults to None. Can be of any format
            supported by pyvista.Plotter.write_frame (.gif, .mp4, ...).
        deform_by:
            Used to deform the plotted mesh. Must return a FieldsContainer of the same length as
            self, containing 3D vector Fields of distances.
            Defaults to None, which takes self if possible. Set as False to force static animation.
        scale_factor : float, list, optional
            Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
            scaling frequency-dependent.
        shell_layer:
            Enum used to set the shell layer if the field to plot
            contains shell elements. Defaults to top layer.
        label : str, optional
            Name of the label to animate over.  Defaults to ``"time"``.  The label
            must exist in this :class:`FieldsContainer`.
        **kwargs:
            Additional keyword arguments for the animator.
            Used by :func:`pyvista.Plotter` (off_screen, cpos, ...),
            or by :func:`pyvista.Plotter.open_movie`
            (framerate, quality, ...)
        """
        from ansys.dpf.core.animator import Animator

        # ── validate label ───────────────────────────────────────────────
        available_labels = self.labels
        if label not in available_labels:
            raise ValueError(
                f"Label '{label}' not found in this FieldsContainer. "
                f"Available labels: {available_labels}"
            )

        # ── build the server-side workflow ────────────────────────────────────
        # Multiple operator inputs can share the same workflow input name, so a
        # single workflow.connect("label_space", dict) fans out to every extract
        # operator registered under that name.
        wf = dpf.core.Workflow()

        # Field extraction: extract_sub_fc filters by the label_space dict and,
        # with collapse_labels=True, removes the animated label from the output
        # FC's label set. merge_fields merges all remaining fields into one Field.
        extract_fc_op = dpf.core.operators.utility.extract_sub_fc(
            fields_container=self, collapse_labels=True
        )
        wf.set_input_name("label_space", extract_fc_op.inputs.label_space)
        merge_field_op = dpf.core.operators.utility.merge_fields(
            fields1=extract_fc_op.outputs.fields_container
        )
        to_render_field = merge_field_op.outputs.merged_field

        # Extract the mesh support from the merged field — this makes the
        # workflow expose a "to_render" MeshedRegion, the same convention used
        # by MeshesContainer.animate, so animate_workflow always uses add_mesh /
        # add_field regardless of whether the source is a FC or MC.
        from_field_op = dpf.core.operators.mesh.from_field(
            field=merge_field_op.outputs.merged_field
        )
        wf.add_operators([extract_fc_op, merge_field_op, from_field_op])
        wf.set_output_name("to_render", from_field_op.outputs.mesh)

        # The field (scalar norm for multi-component) becomes "to_render_field"
        # for coloring, matching the MeshesContainer.animate convention.
        n_components = self[0].component_count
        if n_components > 1:
            norm_op = dpf.core.operators.math.norm(merge_field_op.outputs.merged_field)
            wf.add_operator(norm_op)
            to_render_field = norm_op.outputs.field
        wf.set_output_name("to_render_field", to_render_field)

        # Get label IDs and build the loop_over values
        label_scoping = self.get_label_scoping(label)

        deform = True
        # Define whether to deform and what with
        if deform_by is not False:
            if deform_by is None or isinstance(deform_by, bool):
                # By default, set deform_by as self if nodal 3D vector field
                if self[0].location == dpf.core.common.locations.nodal and n_components == 3:
                    deform_by = self
                else:
                    deform = False
            if deform_by and not isinstance(deform_by, dpf.core.FieldsContainer):
                deform_by = deform_by.eval()
                if len(deform_by) != len(self):
                    raise ValueError(
                        "'deform_by' argument must result in a FieldsContainer "
                        "of same length as the animated one "
                        f"(len(deform_by.eval())={len(deform_by)} "
                        f"!= len(self)={len(self)})."
                    )
        else:
            deform = False

        if deform:
            # Deformation path: register under the same "label_space" name so
            # the single workflow.connect call fans out here too.
            extract_deform_fc_op = dpf.core.operators.utility.extract_sub_fc(
                fields_container=deform_by, collapse_labels=True
            )
            wf.set_input_name("label_space", extract_deform_fc_op.inputs.label_space)
            merge_deform_op = dpf.core.operators.utility.merge_fields(
                fields1=extract_deform_fc_op.outputs.fields_container
            )
            wf.set_output_name("deform_by", merge_deform_op.outputs.merged_field)
            wf.add_operators([extract_deform_fc_op, merge_deform_op])

        wf.progress_bar = False

        # Build loop_over field: use real time/freq values when animating over
        # "time", otherwise fall back to the raw label IDs.
        if label == "time" and self.time_freq_support is not None:
            frequencies = self.time_freq_support.time_frequencies
            if frequencies is None:
                raise ValueError("The fields_container has no time_frequencies.")
            values = frequencies.data[label_scoping.ids - 1]
            unit = frequencies.unit
            freq_fmt = ".3e"
        else:
            import numpy as _np

            values = _np.array(label_scoping.ids, dtype=float)
            unit = ""
            freq_fmt = "g"

        loop_over_field = dpf.core.fields_factory.field_from_array(values)
        loop_over_field.scoping.ids = label_scoping.ids
        loop_over_field.unit = unit

        # Initiate the Animator
        anim = Animator(workflow=wf, **kwargs)

        kwargs.setdefault("freq_kwargs", {"font_size": 12, "fmt": freq_fmt})

        return anim.animate(
            loop_over=loop_over_field,
            save_as=save_as,
            scale_factor=scale_factor,
            shell_layer=shell_layer,
            input_name="label_space",
            label=label,
            output_type=dpf.core.types.meshed_region,
            **kwargs,
        )

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
        """Compute element-wise field[i]^2."""
        if value != 2:
            raise ValueError('DPF only the value is "2" supported')
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
