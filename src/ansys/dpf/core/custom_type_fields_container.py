"""
.. _ref_custom_type_fields_container:

CustomTypeFieldsContainer
===============
Contains classes associated with the DPF CustomTypeFieldsContainer.
"""
from __future__ import annotations
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import CustomTypeField, FieldsContainer, Operator
from ansys.dpf.core import TimeFreqSupport, Scoping
from ansys.dpf.core.results import Result
from typing import Union
import numpy as np


class CustomTypeFieldsContainer(Collection):
    """Represents a custom type fields container, containing custom type fields for a common result.

    A custom type fields container is a set of custom type fields ordered by labels and IDs.
    Each custom type field of the custom type fields container has an ID for each label
    defining the given custom type fields container.
    These IDs allow splitting the custom type fields on any criteria.

    The most common custom type fields container has the label ``"time"`` with IDs
    corresponding to time sets. The label ``"complex"``, which is
    used in a harmonic analysis for example, allows real parts (``id=0``)
    to be separated from imaginary parts (``id=1``).

    For more information, see the `Fields container and fields
    <https://dpf.docs.pyansys.com/user_guide/fields_container.html#ref-user-guide-fields-container>
    `_ documentation section.

    Parameters
    ----------
    unitary_type:
        Type of data in the custom type fields.
    custom_type_fields_container : ansys.grpc.dpf.collection_pb2.Collection, ctypes.c_void_p,
    CustomTypeFieldsContainer, optional
        Custom type fields container created from either a collection message or by copying an
        existing custom type fields container. The default is "None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    """

    def __init__(
        self,
        unitary_type: Union[np.dtype, None] = None,
        custom_type_fields_container=None,
        server=None,
    ):
        super().__init__(collection=custom_type_fields_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = (
                    self._api.collection_of_custom_type_field_new_on_client(  # TODO
                        self._server.client
                    )
                )
            else:
                self._internal_obj = self._api.collection_of_custom_type_field_new()
        self._type = unitary_type
        self._component_index = None  # component index
        self._component_info = None  # for norm/max/min

    def create_subtype(self, obj_by_copy) -> CustomTypeField:
        return CustomTypeField(unitary_type=self._type, field=obj_by_copy, server=self._server)

    def get_fields_by_time_complex_ids(
        self, timeid: Union[int, None] = None, complexid: Union[int, None] = None
    ) -> list[CustomTypeField]:
        """Retrieve custom type fields at a requested time ID or complex ID.

        Parameters
        ----------
        timeid:
            Time ID or frequency ID, which is the one-based index of the
            result set.
        complexid:
            Complex ID, where ``1`` is for imaginary and ``0`` is for real.

        Returns
        -------
        fields :
            Custom type fields corresponding to the request.

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        return super()._get_entries(label_space)

    def get_field_by_time_complex_ids(
        self, timeid: Union[int, None] = None, complexid: Union[int, None] = None
    ) -> CustomTypeField:
        """Retrieve a custom type field at a requested time ID or complex ID.

        An exception is raised if the number of fields matching the request is
        greater than one.

        Parameters
        ----------
        timeid:
            Time ID or frequency ID, which is the one-based index of the
            result set.
        complexid:
            Complex ID, where ``1`` is for imaginary and ``0`` is for real.

        Returns
        -------
        fields:
            Custom type field corresponding to the request

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        return super()._get_entry(label_space)

    def __time_complex_label_space__(self, timeid: int = None, complexid: int = None) -> dict:
        label_space = {}
        if timeid is not None:
            label_space["time"] = timeid
        if complexid is not None:
            label_space["complex"] = complexid
        return label_space

    def get_fields(self, label_space: dict[str, int]) -> list[CustomTypeField]:
        """Retrieve the custom type fields at a requested index or label space.

        Parameters
        ----------
        label_space:
            Scoping of the requested fields. For example,
            ``{"time": 1, "complex": 0}``.

        Returns
        -------
        fields:
            Custom type fields corresponding to the request.

        """
        return super()._get_entries(label_space)

    def get_field(self, label_space_or_index: Union[dict[str, int], int]) -> CustomTypeField:
        """Retrieves the custom type field at a requested index or label space.

        An exception is raised if the number of fields matching the request is
        greater than one.

        Parameters
        ----------
        label_space_or_index:
            Scoping of the requested fields. For example,
            ``{"time": 1, "complex": 0}`` or the index of the field.

        Returns
        -------
        field:
            CustomTypeField corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> fc = dpf.fields_container_factory.over_time_freq_fields_container(
        ...     [dpf.Field(nentities=10)]
        ... )
        >>> field = fc.get_field({"time":1})

        """
        return super()._get_entry(label_space_or_index)

    def get_field_by_time_id(self, timeid: Union[int, None] = None) -> CustomTypeField:
        """Retrieves the complex field at a requested time.

        Parameters
        ----------
        timeid:
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        field
            CustomTypeField corresponding to the request.
        """
        if not self.has_label("time"):
            raise dpf_errors.DpfValueError("The fields container is not based on time scoping.")

        if self.has_label("complex"):
            label_space = self.__time_complex_label_space__(timeid, 0)
        else:
            label_space = self.__time_complex_label_space__(timeid)

        return super()._get_entry(label_space)

    def get_imaginary_fields(self, timeid: Union[int, None] = None) -> list[CustomTypeField]:
        """Retrieve the complex fields at a requested time.

        Parameters
        ----------
        timeid:
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        fields:
            CustomTypeFields corresponding to the request.
        """
        if not self.has_label("complex") or not self.has_label("time"):
            raise dpf_errors.DpfValueError(
                "The fields container is not based on time and complex scoping."
            )

        label_space = self.__time_complex_label_space__(timeid, 1)

        return super()._get_entries(label_space)

    def get_imaginary_field(self, timeid: Union[int, None] = None) -> CustomTypeField:
        """Retrieve the complex custom type field at a requested time.

        Parameters
        ----------
        timeid:
            Time ID, which is the one-based index of the result set.

        Returns
        -------
        field:
            CustomTypeField corresponding to the request.
        """
        if not self.has_label("complex") or not self.has_label("time"):
            raise dpf_errors.DpfValueError(
                "The fields container is not based on time and complex scoping."
            )

        label_space = self.__time_complex_label_space__(timeid, 1)

        return super()._get_entry(label_space)

    def __getitem__(self, key: int) -> CustomTypeField:
        """Retrieve the custom type field at a requested index.

        Parameters
        ----------
        key:
            Index.

        Returns
        -------
        field:
            CustomTypeField corresponding to the request.
        """
        return super().__getitem__(key)

    def add_field(self, label_space: dict[str, int], field: CustomTypeField):
        """Add or update a field at a requested label space.

        Parameters
        ----------
        label_space:
            Label space of the requested field. For example,
            {"time":1, "complex":0}.
        field:
            CustomTypeField to add or update.

        """
        super()._add_entry(label_space, field)

    def add_field_by_time_id(self, field: CustomTypeField, timeid: int = 1):
        """Add or update a custom type field at a requested time ID.

        Parameters
        ----------
        field:
            DPF field to add or update.
        timeid:
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
                "The custom type fields container is not only based on time scoping."
            )

    def add_imaginary_field(self, field: CustomTypeField, timeid: int = 1):
        """Add or update an imaginary custom type field at a requested time ID.

        Parameters
        ----------
        field:
            CustomTypeField to add or update.
        timeid:
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
                "The custom type fields container is not only based on time scoping."
            )

    def select_component(self, index: int) -> CustomTypeFieldsContainer:
        """Select fields containing only the component index.

        Fields can be selected only by component index as multiple fields may
        contain a different number of components.

        Parameters
        ----------
        index:
            Index of the component.

        Returns
        -------
        fields:
            Fields container with one component selected in each field.

        """
        comp_select = dpf.core.operators.logic.component_selector_fc(
            fields_container=self,
            component_number=index,
            server=self._server,
        )
        return comp_select.outputs.fields_container.get_data()

    @property
    def time_freq_support(self) -> TimeFreqSupport:
        """Time frequency support."""
        return self._get_time_freq_support()

    @time_freq_support.setter
    def time_freq_support(self, value: TimeFreqSupport):
        super()._set_time_freq_support(value)

    def deep_copy(self, server=None) -> CustomTypeFieldsContainer:
        """Create a deep copy of the custom type fields container's data on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        fields_container_copy:
            Copy on the given server of the CustomTypeFieldsContainer.

        """
        fc = CustomTypeFieldsContainer(unitary_type=self._type, server=server)
        fc.labels = self.labels
        for i, f in enumerate(self):
            fc.add_field(self.get_label_space(i), f.deep_copy(server))
        try:
            fc.time_freq_support = self.time_freq_support.deep_copy(server)
        except:
            pass
        return fc

    def get_time_scoping(self) -> Scoping:
        """Retrieves the time scoping containing the time sets.

        Returns
        -------
        scoping:
            Scoping containing the time set IDs available in the custom type fields container.
        """
        return self.get_label_scoping("time")

    def animate(
        self,
        save_as: Union[str, None] = None,
        deform_by: Union[CustomTypeFieldsContainer, FieldsContainer, Result, Operator, None] = None,
        scale_factor: Union[float, list[float]] = 1.0,
        **kwargs,
    ):
        """Creates an animation based on the data contained in the CustomTypeFieldsContainer.

        This method creates a movie or a gif based on the time ids of a CustomTypeFieldsContainer.
        For kwargs see pyvista.Plotter.open_movie/add_text/show.

        Parameters
        ----------
        save_as :
            Path of file to save the animation to. Defaults to None. Can be of any format
            supported by pyvista.Plotter.write_frame (.gif, .mp4, ...).
        deform_by:
            Used to deform the plotted mesh. Must return a FieldsContainer of the same length as
            self, containing 3D vector Fields of distances.
            Defaults to None, which takes self if possible. Set as False to force static animation.
        scale_factor:
            Scale factor to apply when warping the mesh. Defaults to 1.0. Can be a list to make
            scaling frequency-dependent.
        """
        from ansys.dpf.core.animator import Animator

        # Create a workflow defining the result to render at each step of the animation
        wf = dpf.core.Workflow()
        # First define the workflow index input
        forward_index = dpf.core.operators.utility.forward()
        wf.set_input_name("loop_over", forward_index.inputs.any)
        # Define the field extraction using the fields_container and indices
        extract_field_op = dpf.core.operators.utility.extract_field(self)
        to_render = extract_field_op.outputs.field
        n_components = self[0].component_count
        if n_components > 1:
            norm_op = dpf.core.operators.math.norm(extract_field_op.outputs.field)
            to_render = norm_op.outputs.field

        loop_over = self.get_time_scoping()
        frequencies = self.time_freq_support.time_frequencies
        if frequencies is None:
            raise ValueError("The fields_container has no time_frequencies.")

        # TODO /!\ We should be using a mechanical::time_selector, however it is not wrapped.

        wf.set_input_name("indices", extract_field_op.inputs.indices)  # Have to do it this way
        wf.connect("indices", forward_index)  # Otherwise not accepted
        # Add the operators to the workflow
        wf.add_operators([extract_field_op, forward_index])

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
            scale_factor_fc = dpf.core.animator.scale_factor_to_fc(scale_factor, deform_by)
            scale_factor_invert = dpf.core.operators.math.invert_fc(scale_factor_fc)
            # Extraction of the field of interest based on index
            # time_selector = dpf.core.Operator("mechanical::time_selector")
            extract_field_op_2 = dpf.core.operators.utility.extract_field(deform_by)
            wf.set_input_name("indices", extract_field_op_2.inputs.indices)
            wf.connect("indices", forward_index)  # Otherwise not accepted
            # Scaling of the field based on scale_factor and index
            extract_scale_factor_op = dpf.core.operators.utility.extract_field(scale_factor_invert)
            wf.set_input_name("indices", extract_scale_factor_op.inputs.indices)
            wf.connect("indices", forward_index)  # Otherwise not accepted

            divide_op = dpf.core.operators.math.component_wise_divide(
                extract_field_op_2.outputs.field, extract_scale_factor_op.outputs.field
            )
            wf.set_output_name("deform_by", divide_op.outputs.field)
        else:
            scale_factor = None
        wf.set_output_name("to_render", to_render)
        wf.progress_bar = False

        loop_over_field = dpf.core.fields_factory.field_from_array(
            frequencies.data[loop_over.ids - 1]
        )
        loop_over_field.scoping.ids = loop_over.ids
        loop_over_field.unit = frequencies.unit

        # Initiate the Animator
        anim = Animator(workflow=wf, **kwargs)

        kwargs.setdefault("freq_kwargs", {"font_size": 12, "fmt": ".3e"})

        return anim.animate(
            loop_over=loop_over_field,
            save_as=save_as,
            scale_factor=scale_factor,
            **kwargs,
        )

    def __add__(self, fields_b: CustomTypeFieldsContainer) -> dpf.core.operators.math.add_fc:
        """Add two custom type fields containers.

        Returns
        -------
        add:
            Addition operator
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators

        if hasattr(operators, "math") and hasattr(operators.math, "add_fc"):
            op = operators.math.add_fc(self, fields_b, server=self._server)
        else:
            op = dpf_operator.Operator("add_fc", server=self._server)
            op.connect(0, self)
            op.connect(1, fields_b)
        return op

    def __sub__(self, fields_b: CustomTypeFieldsContainer) -> dpf.core.operators.math.minus_fc:
        """Subtract two fields or two fields containers.

        Returns
        -------
        minus:
            Subtraction operator
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators

        if hasattr(operators, "math") and hasattr(operators.math, "minus_fc"):
            op = operators.math.minus_fc(server=self._server)
        else:
            op = dpf_operator.Operator("minus_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, fields_b)
        return op

    def __pow__(self, value: int) -> dpf.core.operators.math.sqr_fc:
        if value != 2:
            raise ValueError('DPF only the value is "2" supported')
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators

        if hasattr(operators, "math") and hasattr(operators.math, "sqr_fc"):
            op = operators.math.sqr_fc(server=self._server)
        else:
            op = dpf_operator.Operator("sqr_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    def __mul__(
        self, value: Union[int, float]
    ) -> dpf.core.operators.math.generalized_inner_product_fc:
        """Multiply two custom type fields containers.

        Returns
        -------
        mul:
            Generalized inner product operator
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators

        if hasattr(operators, "math") and hasattr(operators.math, "generalized_inner_product_fc"):
            op = operators.math.generalized_inner_product_fc(server=self._server)
        else:
            op = dpf_operator.Operator("generalized_inner_product_fc", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    @property
    def type(self) -> np.dtype:
        """Type of unitary data in the CustomFieldsContainer."""
        return self._type

    def is_of_type(self, type_to_compare: np.dtype) -> bool:
        """Checks whether the CustomTypeFieldsContainer unitary type is the same as the input type.

        Parameters
        ----------
        type_to_compare: numpy.dtype

        Returns
        -------
        bool

        """
        return self.type == type_to_compare
