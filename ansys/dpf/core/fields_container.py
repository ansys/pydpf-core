"""
.. _ref_fields_container:
    
FieldsContainer
===============
Contains classes associated to the DPF FieldsContainer
"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types
from ansys.dpf.core import errors as dpf_errors


class FieldsContainer(Collection):
    """A class used to represent a FieldsContainer which contains
    fields belonging to a common results.
    The fields container is designed as a set of fields ordered by labels 
    and ids. Each field of the Fields Container has an id for each label 
    defining the given Fields Container. This allows to split the fields 
    on any criteria.
    The most common fields container have the label "time" with ids 
    corresponding to each time sets, the label "complex" will allow 
    to separate real parts (id=0) from imaginary parts (id=1) 
    in a harmonic analysis for example. 

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or FieldsContainer, optional
        Create a fields container from a Collection message or create a copy from an existing fields container

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    
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

    
    Create a fields container from scratch
    
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

        complexid : int, optional
            The complex id.

        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
            
        Examples
        --------
        Extract a the 5th time set of a transient analysis.
    
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
        label_space = self.__time_complex_label_space__(timeid,complexid)
        return super()._get_entries(label_space)
    
    def get_field_by_time_complex_ids(self, timeid=None, complexid=None):
        """Returns the field at a requested time/freq id and real or imaginary depending on 
        complexid (complexid=1:imaginary, complexid=0:real).
        It throws if the number of fields matching the request is 
        higher than 1.

        Parameters
        ----------
        timeid : int, optional
            The time id. One based index of the result set.

        complexid : int, optional
            The complex id.

        Returns
        -------
        fields : Field
            field corresponding to the request
            
        Examples
        --------
        Extract a the 5th time set of a transient analysis.
    
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
        label_space = self.__time_complex_label_space__(timeid,complexid)
        return super()._get_entry(label_space)
    
    def __time_complex_label_space__(self, timeid=None, complexid=None):
        label_space ={}
        if timeid is not None:
            label_space["time"] = timeid
        if complexid is not None:
            label_space["complex"] = complexid
        return label_space

    def get_fields(self, label_space):
        """Returns the fields at a requested index or label space

        Parameters
        ----------
        label_space : dict[str,int] 
            Scoping of the requested fields, for example:
            ``{"time": 1, "complex": 0}``

        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
          
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
        """Returns the field at a requested index or label space.
        Throws if the request returns several fields

        Parameters
        ----------
        label_space_or_index : dict[str,int] , int 
            Scoping of the requested fields, for example:
            ``{"time": 1, "complex": 0}``
            or Index of the field.

        Returns
        -------
        field : Field
            field corresponding to the request
          
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> fc= dpf.fields_container_factory.over_time_freq_fields_container([dpf.Field(nentities=10)])
        >>> field = fc.get_field({"time":1})

        """        
        return super()._get_entry(label_space_or_index)
    
    
    def get_field_by_time_id(self, timeid=None):
        """Returns the complex field at a requested time

        Parameters
        ----------
        timeid: int, optional
            The time id. Index of the result set.

        Returns
        -------
        fields : Field 
            fields corresponding to the request
        """
        if (not self.has_label('time')):
            raise dpf_errors.DpfValueError("The fields container is not based on time scoping.")
        
        if self.has_label('complex'):
             label_space = self.__time_complex_label_space__(timeid,0)
        else:
            label_space = self.__time_complex_label_space__(timeid)
        
        return super()._get_entry(label_space)
    
    def get_imaginary_fields(self, timeid=None):
        """Returns the complex fields at a requested time

        Parameters
        ----------
        timeid: int, optional
            The time id. Index of the result set.

        Returns
        -------
        fields : list[Field] 
            fields corresponding to the request
        """
        if (not self.has_label('complex') or not self.has_label('time')):
            raise dpf_errors.DpfValueError("The fields container is not based on time and complex scoping.")
        
        label_space = self.__time_complex_label_space__(timeid,1)
        
        return super()._get_entries(label_space)
    
    def get_imaginary_field(self, timeid=None):
        """Returns the complex field at a requested time

        Parameters
        ----------
        timeid: int, optional
            The time id. Index of the result set.

        Returns
        -------
        fields : Field 
            field corresponding to the request
        """
        if (not self.has_label('complex') or not self.has_label('time')):
            raise dpf_errors.DpfValueError("The fields container is not based on time and complex scoping.")
        
        label_space = self.__time_complex_label_space__(timeid,1)
        
        return super()._get_entry(label_space)

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
        label_space : dict[str,int]
            label_space of the requested fields, ex : {"time":1, "complex":0}

        field : Field
            DPF field to add.
            
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

    def add_field_by_time_id(self, field, timeid = 1):
        """Update or add the field at a requested time id.

        Parameters
        ----------        
        field : Field
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
        field : Field
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
        fields : FieldsContainer
            Fields container with one component selected in each field.

        Examples
        --------
        Select using a component index
    
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
        comp_select.connect(0,self)
        comp_select.connect(1,index)
        return comp_select.outputs.fields_container.get_data()

    @property
    def time_freq_support(self):
        return self._get_time_freq_support()
    
    @time_freq_support.setter
    def time_freq_support(self, value):
        return super()._set_time_freq_support(value)
    
    
    def deep_copy(self,server=None):
        """Creates a deep copy of the fields container's data (and its fields) on a given server.
        This can be useful to pass data from one server instance to another.
        
        Parameters
        ----------
        server : DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the the global server.
        
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
        fc.labels= self.labels
        for i,f in enumerate(self):
            fc.add_field(self.get_label_space(i),f.deep_copy(server))        
        try:
            fc.time_freq_support = self.time_freq_support.deep_copy(server)
        except:
            pass
        return fc
    
    def get_time_scoping(self):
        """Returns the time scoping containing the time sets
        
        Returns
        -------
        scoping: Scoping
            scoping containing the time set ids available in the fields container
        """
        return self.get_label_scoping("time")
    
    def __add__(self, fields_b):
        """Adds two fields or fields containers together
                
        Returns
        -------
        add : operators.math.add_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "add_fc") :
            op= operators.math.add_fc(self, fields_b, server=self._server)
        else :
            op= dpf_operator.Operator("add_fc", server=self._server)
            op.connect(0,self)        
            op.connect(1, fields_b)
        return op
    
    def __sub__(self, fields_b):
        """Subtract two fields or fields containers together
                
        Returns
        -------
        minus : operators.math.minus_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "minus_fc") :
            op= operators.math.minus_fc(server=self._server)
        else :
            op= dpf_operator.Operator("minus_fc", server=self._server)
        op.connect(0,self)        
        op.connect(1, fields_b)
        return op

    def __pow__(self, value):
        if value != 2:
            raise ValueError('DPF only the value is "2" suppported')
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "sqr_fc") :
            op= operators.math.sqr_fc(server=self._server)
        else :
            op= dpf_operator.Operator("sqr_fc",server=self._server)
        op.connect(0,self)        
        op.connect(1, value)
        return op
    
    def __mul__(self, value):
        """Multiplies two fields or fields containers together
        
        Returns
        -------
        mul : operators.math.generalized_inner_product_fc
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "generalized_inner_product_fc") :
            op= operators.math.generalized_inner_product_fc(server=self._server)
        else :
            op= dpf_operator.Operator("generalized_inner_product_fc",server=self._server)
        op.connect(0,self)        
        op.connect(1, value)
        return op
    
    
