"""
.. _ref_fields_container:

FieldsContainer
===============
Contains classes associated with the DPF FieldsContainer.
"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import field

class FieldsContainer(Collection):
    """Represents a fields container, which contains fields belonging to a common result.

    A fields container is a set of fields ordered by labels and IDs. Each field
    of the fields container has an ID for each label defining the given fields
    container. These IDs allow splitting the fields on any criteria.

    The most common fields container has the label ``"time"`` with IDs
    corresponding to time sets. The label ``"complex"``, which is
    used in a harmonic analysis for example, allows real parts (``id=0``)
    to be separated from imaginary parts (``id=1``).

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection, ctypes.c_void_p,
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
        super().__init__(
            collection=fields_container, server=server
        )
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
        """Retrieves the field at a requested index or label space.

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
        """Retrieves the complex field at a requested time.

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
            raise dpf_errors.DpfValueError(
                "The fields container is not based on time scoping."
            )

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

    def __getitem__(self, key):
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
            len(self.labels) == 0
            or (len(self.labels) == 1 and self.has_label("complex"))
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
            len(self.labels) == 0
            or (len(self.labels) == 1 and self.has_label("complex"))
        ):
            self.add_label("time")
        if (
            not self.has_label("complex")
            and len(self.labels) == 1
            and self.has_label("time")
        ):
            self.add_label("complex")
        if (
            self.has_label("time")
            and self.has_label("complex")
            and len(self.labels) == 2
        ):
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
        try:
            fc.time_freq_support = self.time_freq_support.deep_copy(server)
        except:
            pass
        return fc

    def get_time_scoping(self):
        """Retrieves the time scoping containing the time sets.

        Returns
        -------
        scoping: Scoping
            Scoping containing the time set IDs available in the fields container.
        """
        return self.get_label_scoping("time")

    def __add__(self, fields_b):
        """Add two fields or two fields containers.

        Returns
        -------
        add : operators.math.add_fc
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

    def __sub__(self, fields_b):
        """Subtract two fields or two fields containers.

        Returns
        -------
        minus : operators.math.minus_fc
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

    def __pow__(self, value):
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

    def __mul__(self, value):
        """Multiply two fields or two fields containers.

        Returns
        -------
        mul : operators.math.generalized_inner_product_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators

        if hasattr(operators, "math") and hasattr(
            operators.math, "generalized_inner_product_fc"
        ):
            op = operators.math.generalized_inner_product_fc(server=self._server)
        else:
            op = dpf_operator.Operator(
                "generalized_inner_product_fc", server=self._server
            )
        op.connect(0, self)
        op.connect(1, value)
        return op
