"""Contains classes associated to the DPF FieldsContainer"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types
from ansys.dpf.core import errors as dpf_errors


class FieldsContainer(Collection):
    """A class used to represent a FieldsContainer which contains
    fields belonging to an analysis.

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or ansys.dpf.core.FieldsContainer, optional
        Create a fields container from a Collection message or create a copy from an existing fields container

    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
        
    Examples
    --------
    Create a fields container based on time labels from scratch
    
    >>> from ansys.dpf import core
    >>> field1 = core.Field()
    >>> field2 = core.Field()
    >>> # 1. using the classic API
    >>> my_fc = core.FieldsContainer()
    >>> my_fc.labels = ["time"]
    >>> my_fc.add_field({"time" : 1}, field1)
    >>> my_fc.add_field({"time" : 2}, field2)
    >>> # 2. using the fields_container_factory
    >>> from ansys.dpf.core import fields_container_factory
    >>> fields_container_factory.over_time_freq_fields_container([ field1, field2 ])
    """

    def __init__(self, fields_container=None, server=None):
        """Initialize the scoping with either optional scoping message,
        or by connecting to a stub.
        """
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()

        self._component_index = None  # component index
        self._component_info = None  # for norm/max/min

        Collection.__init__(self, types.field,
                            collection=fields_container, server=self._server)

    def get_fields_by_time_complex_ids(self, timeid=None, complexid=None):
        """Returns the fields at a requested time/freq id and real or imaginary depending on 
        complexid (complexid=1:imaginary, complexid=0:real)

        Parameters
        ----------
        timeid : int, optional
            The time id. One based index of the result set.

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
        """Returns the fields at a requested index or label space

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
    
    def get_field_by_time_id(self, timeid=None):
        """Returns the complex field at a requested time

        Parameters
        ----------
        timeid: int, optional
            The time id. Index of the result set.

        Returns
        -------
        fields : list of fields or field (if only one)
            fields corresponding to the request
        """
        if (not self.has_label('time')):
            raise dpf_errors.DpfValueError("The fields container is not based on time scoping.")
        
        label_space ={}
        if (self.has_label('complex')):
            label_space = { 'time' : timeid, 'complex' : 0 }
        else:
            label_space = { 'time' : timeid }
        
        return super()._get_entries(label_space)
    
    def get_imaginary_fields(self, timeid=None):
        """Returns the complex field at a requested time

        Parameters
        ----------
        timeid: int, optional
            The time id. Index of the result set.

        Returns
        -------
        fields : list of fields or field (if only one)
            fields corresponding to the request
        """
        if (not self.has_label('complex') or not self.has_label('time')):
            raise dpf_errors.DpfValueError("The fields container is not based on time and complex scoping.")
        
        label_space ={}
        if timeid is not None:
            label_space["time"] = timeid
        label_space["complex"] = 1
        
        return super()._get_entries(label_space)

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
        """Update or add the field at a requested label space.

        Parameters
        ----------
        label_space : dict(string:int)
            label_space of the requested fields, ex : {"time":1, "complex":0}

        field : dpf.core.Field
            DPF field to add.
        """
        super()._add_entry(label_space, field)

    def add_field_by_time_id(self, field, timeid = 1):
        """Update or add the field at a requested time id.

        Parameters
        ----------        
        field : dpf.core.Field
            DPF field to add.
            
        timeid: int, optional
            time id corresponding to the requested time set. Default: 1
        """
        labels = self.labels
        if (not self.has_label('time') 
            and (len(self.labels) == 0 
            or (len(self.labels) == 1 and self.has_label("complex")))):
            self.add_label('time')
        if (len(self.labels) == 1):
            super()._add_entry({'time': timeid}, field)
        elif (self.has_label('time') and self.has_label('complex') and len(labels) == 2):
            super()._add_entry({'time': timeid, 'complex': 0}, field)
        else:
            raise dpf_errors.DpfValueError('The fields container is not only based on time scoping.')
            
    def add_imaginary_field(self, field, timeid = 1):
        """Update or add the imaginary field at a requested time id.

        Parameters
        ----------        
        field : dpf.core.Field
            DPF field to add.
            
        timeid: int, optional
            time id corresponding to the requested time set. Default: 1
        """
        if (not self.has_label('time') 
            and (len(self.labels) == 0 
            or (len(self.labels) == 1 and self.has_label("complex")))):
            self.add_label('time')
        if (not self.has_label('complex') and len(self.labels) == 1 and self.has_label('time')):
            self.add_label('complex')
        if (self.has_label('time') and self.has_label('complex') and len(self.labels) == 2):
            super()._add_entry({'time': timeid, 'complex': 1}, field)
        else:
            raise dpf_errors.DpfValueError('The fields container is not only based on time scoping.')

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
    
    @time_freq_support.setter
    def time_freq_support(self, value):
        return super()._set_time_freq_support(value)
    
