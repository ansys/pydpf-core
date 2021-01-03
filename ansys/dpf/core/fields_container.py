"""Contains classes associated to the DPF FieldsContainer"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types


class FieldsContainer(Collection):
    """A class used to represent a FieldsContainer which contains
    fields belonging to an analysis.

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.fields_container_pb2.FieldsContainer, optional
        Create a fields container from a FieldsContainer message.

    channel : channel, optional
        Channel connected to the remote or local instance. When
        ``None``, attempts to use the the global channel.
    """

    def __init__(self, fields_container=None, channel=None):
        """Initialize the scoping with either optional scoping message,
        or by connecting to a stub.
        """
        if channel is None:
            channel = dpf.core._global_channel()
        self._channel = channel
        self._stub = self._connect()

        self._component_index = None  # component index
        self._component_info = None  # for norm/max/min

        Collection.__init__(self, types.field,
                            collection=fields_container, channel=channel)

    def get_fields_by_time_complex_ids(self, timeid=None, complexid=None):
        """Returns the fields at a requested index or scoping

        Parameters
        ----------
        timeid : int, optional
            The time id.  Index of the result set.

        complexid (optional) : int, optional
            The complex id.

        Returns
        -------
        fields : list of fields
            fields corresponding to the request
        """
        label_space ={}
        if timeid is not None:
            label_space["time"] = timeid
        if complexid is not None:
            label_space["complex"] = complexid

        return super()._get_entries(label_space)

    def get_fields(self, label_space_or_index):
        """Returns the fields at a requested index or scoping

        Parameters
        ----------
        label_space_or_index (optional) : dict(string:int) or int
            Scoping of the requested fields, for example:
            ``{"time": 1, "complex": 0}``
            or Index of the field.

        Returns
        -------
        fields : list of fields or field (if only one)
            fields corresponding to the request
        """
        return super()._get_entries(label_space_or_index)

    def __getitem__(self, key):
        """Returns the field at a requested index

        Parameters
        ----------
        key : int
            the index

        Returns
        -------
        field : Field
            field corresponding to the request
        """
        return super().__getitem__(key)

    def add_field(self, label_space, field):
        """Update or add the field at a requested scoping.

        Parameters
        ----------
        label_space : dict(string:int)
            label_space of the requested fields, ex : {"time":1, "complex":0}

        field : dpf.core.Field
            DPF field to add.
        """
        return super()._add_entry(label_space, field)

    def __str__(self):
        txt = 'DPF Field Container with\n'
        txt += "\t%d field(s)\n" % len(self)
        txt += f"\tdefined on labels {self.labels} \n\n"
        return txt

    def select_component(self, index):
        """Returns fields containing only the component index.

        Can only select by component index as multiple fields may
        contain different number of components.

        Parameters
        ----------
        index : int
            Component index.

        Returns
        -------
        fields : ansys.dpf.core.FieldsContainer
            Fields container with one component selected in each field.

        Examples
        --------
        Select using a component index

        >>> disp_x_fields = disp_fields.select_component(0)

        """
        comp_select = dpf.core.Operator("component_selector_fc")
        comp_select.connect(0,self)
        comp_select.connect(1,index)
        return comp_select.outputs.fields_container.get_data()

    @property
    def time_freq_support(self):
        return self._get_time_freq_support()
