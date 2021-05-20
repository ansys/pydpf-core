
from ansys.grpc.dpf import field_pb2, base_pb2, field_pb2_grpc
from ansys.dpf.core import scoping
from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import errors 
from ansys.dpf.core import server as serverlib

import numpy as np
import array

class _FieldBase:
    """Base APIs for all implementations that follow Dpf's
    field concept."""
    
    
    def __init__(self, nentities=0, nature=natures.vector,
                 location=locations.nodal, is_property_field = False, 
                 field=None, server=None):
        """Initialize the field with either optional field message, or
        by connecting to a stub.
        """
        if server is None:
            server = serverlib._global_server()

        self._server = server
        self._stub = self._connect()

        if field is None:
            request = field_pb2.FieldRequest()
            if hasattr(nature, 'name'):
                snature = nature.name
            else:
                snature = nature
            request.nature = base_pb2.Nature.Value(snature.upper())
            request.location.location = location
            request.size.scoping_size = nentities
            if snature==natures.vector.name:
                elem_data_size =3
            elif snature==natures.symmatrix.name:
                elem_data_size =6
            else:
                elem_data_size=1
            request.size.data_size = nentities*elem_data_size
            if is_property_field:
                request.datatype = u"int"
            self._message = self._stub.Create(request)
        else:
            from ansys.dpf.core import field as field_module
            from ansys.dpf.core import property_field
            if isinstance(field, field_module.Field):
                self._message = field._message
            elif isinstance(field, property_field.PropertyField):
                self._message = field._message
            elif isinstance(field, field_pb2.Field):
                self._message = field
            else:
                raise TypeError(f'Cannot create a field from a "{type(field)}" object')
    @property
    def shape(self):
        """Numpy-like shape of the field
        
        Examples
        --------
        Shape of a stress field
        
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_transient_result())
        >>> s_op =model.results.stress()
        >>> s_fc = s_op.outputs.fields_container()
        >>> field = s_fc[0]
        >>> field.shape
        (5720, 6)
        
        """
        if self.component_count != 1:
            return (self.elementary_data_count, self.component_count)
        return self.elementary_data_count       
                
    @property
    def component_count(self):
        """Number of components in an elementary data of the Field
        
        Returns
        -------
        ncomp : int
            Number of component of the each elementary data
        """
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_COMPONENT
        request.field.CopyFrom(self._message)
        return self._stub.Count(request).count
    
    @property
    def elementary_data_count(self):
        """Number of elementary data in the field"""
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.field.CopyFrom(self._message)
        return self._stub.Count(request).count
    
    @property
    def size(self):
        """The length of the data vector.
        Also equals to the number of elementary data times the number of components.
        
        Returns
        -------
        size : int
        """
        return self.elementary_data_count*self.component_count
    
    @property
    def elementary_data_shape(self):
        """Numpy-like shape of the field"""
        if self.component_count != 1:
            return (1, self.component_count)
        else:
            return self.component_count
        
    @property
    def ndim(self):
        return self.component_count

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """        
        from ansys.dpf.core.core import _description
        return _description(self._message, self._server)

    def __len__(self):
        return self.size
    
    def _del_scoping(self, scope):
        scope.__del__()

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def _connect(self):
        """Connect to the grpc service"""
        return field_pb2_grpc.FieldServiceStub(self._server.channel)
    
    def _set_scoping(self, scoping):
        """
        Parameters
        ----------
        scoping : Scoping
        """
        request = field_pb2.UpdateScopingRequest()
        request.scoping.CopyFrom(scoping._message)
        request.field.CopyFrom(self._message)
        self._stub.UpdateScoping(request)
        
    def _get_scoping(self):
        """
        Returns
        -------
        scoping : Scoping
        """
        request = field_pb2.GetRequest()
        request.field.CopyFrom(self._message)
        message = self._stub.GetScoping(request)
        return scoping.Scoping(scoping=message.scoping)

    @property
    def scoping(self):
        """ The scoping allows to know where is the data.
        Each entity data is on a given scoping id.
        
        Returns
        -------
        scoping : Scoping
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> scoping = fields_container[0].scoping
        >>> scoping.location
        'Elemental'
        >>> scoping.id(3)
        586
        >>> #The fourth elementary data of the field corresponds to 
        >>> #the element id number 586 in the mesh
        """
        return self._get_scoping()
    
    @scoping.setter
    def scoping(self, scoping):
        """
        Parameters
        ----------
        scoping : Scoping
        """
        return self._set_scoping(scoping)
               
        
    def get_entity_data(self, index):
        """Returns the elementary data of the scoping's index in parameter
        
        Returns
        --------
        data : numpy.array
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> fields_container[0].get_entity_data(0)
        array([[-3.27795062e+05,  1.36012200e+06,  1.49090608e+08,
                -4.88688900e+06,  1.43038560e+07,  1.65455040e+07],
               [-4.63817550e+06,  1.29312225e+06,  1.20411832e+08,
                -6.06617800e+06,  2.34829700e+07,  1.77231120e+07],
               [-2.35684860e+07, -3.53474400e+07,  2.01501168e+08,
                -5.23361700e+06, -2.88789280e+07, -6.16478200e+06],
               [-3.92756960e+07, -2.72369280e+07,  1.81454016e+08,
                -3.75441450e+06, -3.62480300e+06, -3.26075620e+07],
               [ 1.63554530e+07,  2.83190520e+07,  1.05084256e+08,
                -1.30219020e+07,  5.19906719e+05,  8.82430200e+06],
               [ 1.80755620e+07,  5.25578750e+06,  7.76211600e+07,
                -7.53063750e+06,  2.44717000e+06,  2.92675125e+06],
               [ 9.25567760e+07,  8.15244320e+07,  2.77157632e+08,
                -1.48489875e+06,  5.89250600e+07,  2.05608920e+07],
               [ 6.70443680e+07,  8.70343440e+07,  2.73050464e+08,
                -2.48670150e+06,  1.52268930e+07,  6.09583280e+07]])
        
        """
        request = field_pb2.GetElementaryDataRequest()
        request.field.CopyFrom(self._message)
        request.index = index
        list_message = self._stub.GetElementaryData(request, metadata=[(b'float_or_double', b'double')])
        data = []
        if list_message.elemdata_containers.data.HasField("datadouble"):
            data = list_message.elemdata_containers.data.datadouble.rep_double
        elif list_message.elemdata_containers.data.HasField("dataint"):
            data = list_message.elemdata_containers.data.dataint.rep_int

        array = np.array(data)
        if self.component_count !=1:
            n_comp = self.component_count
            array = array.reshape((len(data)//n_comp, n_comp))

        return array

    def get_entity_data_by_id(self, id):
        """Return the data of the scoping's id in parameter of the field.

        Returns
        -------
        data : numpy.array
            Data based on the scoping id.            
                  
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> fields_container[0].get_entity_data_by_id(391)
        array([[-3.27795062e+05,  1.36012200e+06,  1.49090608e+08,
                -4.88688900e+06,  1.43038560e+07,  1.65455040e+07],
               [-4.63817550e+06,  1.29312225e+06,  1.20411832e+08,
                -6.06617800e+06,  2.34829700e+07,  1.77231120e+07],
               [-2.35684860e+07, -3.53474400e+07,  2.01501168e+08,
                -5.23361700e+06, -2.88789280e+07, -6.16478200e+06],
               [-3.92756960e+07, -2.72369280e+07,  1.81454016e+08,
                -3.75441450e+06, -3.62480300e+06, -3.26075620e+07],
               [ 1.63554530e+07,  2.83190520e+07,  1.05084256e+08,
                -1.30219020e+07,  5.19906719e+05,  8.82430200e+06],
               [ 1.80755620e+07,  5.25578750e+06,  7.76211600e+07,
                -7.53063750e+06,  2.44717000e+06,  2.92675125e+06],
               [ 9.25567760e+07,  8.15244320e+07,  2.77157632e+08,
                -1.48489875e+06,  5.89250600e+07,  2.05608920e+07],
               [ 6.70443680e+07,  8.70343440e+07,  2.73050464e+08,
                -2.48670150e+06,  1.52268930e+07,  6.09583280e+07]])
        
        """
        index = self.scoping.index(id)
        if index < 0:
            raise ValueError(f'The id {id} must be greater than 0')
        return self.get_entity_data(index)

    def append(self, data, scopingid):
        """add an entity data to the existing data

        Parameters
        ----------
        data : list of int, double or array

        scopingid : int
            id of the scoping
                
        Examples
        --------
        >>> from ansys.dpf.core import fields_factory
        >>> field = fields_factory.create_3d_vector_field(2)
        >>> field.append([1.,2.,3.],1)        
        >>> field.append([1.,2.,3.],2)
        >>> field.data
        array([[1., 2., 3.],
               [1., 2., 3.]])
        >>> field.scoping.ids
        [1, 2]
        
        """
        if isinstance(data, (np.ndarray, np.generic)):
            data = data.reshape(data.size).tolist()
        elif len(data)>0 and isinstance(data[0], list):
            data = np.array(data)
            data = data.reshape(data.size).tolist()
        request = field_pb2.AddDataRequest()
        if self._message.datatype == u"int":
            request.elemdata_containers.data.dataint.rep_int.extend(data)
        else:
            request.elemdata_containers.data.datadouble.rep_double.extend(data)
        request.elemdata_containers.scoping_id = scopingid

        request.field.CopyFrom(self._message)
        self._stub.AddData(request)
           
    @property
    def _data_pointer(self):
        """Gives the first index of each entity data

        Returns
        -------
        data : numpy.ndarray
            Data of this field.
        """
        request = field_pb2.ListRequest()
        request.field.CopyFrom(self._message)
        service = self._stub.ListDataPointer(request)
        dtype = np.int32
        return self.__data_get_chunk__(dtype, service)
    
    @property
    def _data_pointer_as_list(self):
        """Gives the first index of each entity data

        Returns
        -------
        data : list of int
            Data of this field.
        """
        request = field_pb2.ListRequest()
        request.field.CopyFrom(self._message)
        service = self._stub.ListDataPointer(request)
        dtype = np.int32
        return self.__data_get_chunk__(dtype, service, False)
    
    @_data_pointer.setter
    def _data_pointer(self, data):
        """Set the data pointer of the field.

        Parameters
        ----------
        data : list of int or array
        """
        self._set_data_pointer(data)
        
           
    def _set_data_pointer(self,data):
        if isinstance(data,  (np.ndarray, np.generic)):
            data = np.array(data.reshape(data.size), dtype=int)
        else:
            data = np.array(data, dtype=int)
        if data.size ==0:
            return
        metadata=[(u"size_int", f"{len(data)}")]
        request = field_pb2.UpdateDataRequest()
        request.field.CopyFrom(self._message)
        self._stub.UpdateDataPointer(scoping._data_chunk_yielder(request, data), metadata=metadata)
        
        
    @property
    def data(self):
        """Access the data of this field.
        
        Returns
        -------
        data : numpy.ndarray
            Data of this field.
        """
        return self._get_data()
    
    @property
    def data_as_list(self):
        """The data of this field in a python list

        Returns
        -------
        data : list
            Data of this field.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> # field.data_as_list
         
         """
        return self._get_data(np_array=False)
    
    def _get_data(self, np_array=True):
        request = field_pb2.ListRequest()
        request.field.CopyFrom(self._message)
        if self._message.datatype == u"int":
            data_type = u"int"
            dtype = np.int32
        else:
            data_type = u"double"
            dtype = np.float
        service = self._stub.List(request, metadata=[(u"float_or_double", data_type)])
        array= self.__data_get_chunk__(dtype, service, np_array)
        
        ncomp = self.component_count
        if ncomp != 1 and np_array:
            array = array.reshape(self.shape)
        
        return array
    
    def __data_get_chunk__(self,dtype, service, np_array=True):
        tupleMetaData = service.initial_metadata()
        for iMeta in range(len(tupleMetaData)):
            if tupleMetaData[iMeta].key == u"size_tot":
                size = int(tupleMetaData[iMeta].value)
        
        if np_array:
            itemsize = np.dtype(dtype).itemsize
            arr = np.empty(size//itemsize, dtype)
            i = 0
            for chunk in service:
                curr_size = len(chunk.array)//itemsize
                arr[i:i + curr_size] = np.frombuffer(chunk.array, dtype)
                i += curr_size
        
        else:
            arr=[]
            if dtype==np.float:
                dtype = 'd'
            else:
                dtype='i'
            for chunk in service:
                arr.extend(array.array(dtype,chunk.array))

        return arr
        
        
    @data.setter
    def data(self, data):
        """Set the data of the field.

        Parameters
        ----------
        data : list of int (property field only), double or array
        """
        self._set_data(data)
    
    def _set_data(self,data):
        if self._message.datatype == u"int":
            if not isinstance(data[0], int)and not isinstance(data[0], np.int32):
                raise errors.InvalidTypeError("data", "list of int")
            data = np.array(data, dtype=int)
            metadata=[(u"size_int", f"{len(data)}")]
        else:
            if isinstance(data,  (np.ndarray, np.generic)):
                if data.shape !=  self.shape and 0 != self.size:
                    raise ValueError(f'An array of shape {self.shape} is expected and shape {data.shape} is in input')
                else:
                    data = np.array(data.reshape(data.size), dtype=float)
            else:
                data = np.array(data, dtype=float)
            metadata=[(u"float_or_double", u"double"), (u"size_double", f"{len(data)}")]
        request = field_pb2.UpdateDataRequest()
        request.field.CopyFrom(self._message)
        self._stub.UpdateData(scoping._data_chunk_yielder(request, data), metadata=metadata)
        
    
    

class _LocalFieldBase(_FieldBase):
    """Class only created by a field to cache the internal data of the field,
    modify it locallly, and send a single update request to the server 
    when the local field is deleted
    
    Parameters
    ----------
    field : _FieldBase
        field to copy
    """
    def __init__(self, field):
        self._message = field._message
        self._server =field._server
        self._stub = field._stub
        self._is_property_field = field._message.datatype == u"int"
        self._owner_field = field
        self.__cache_data__()
        
    def __cache_data__(self):
        self._ncomp = super().component_count
        self._data_copy = super().data_as_list
        self._num_entities_reserved = len(self._data_copy)
        self._data_pointer_copy = super()._data_pointer_as_list
        self._scoping_ids_copy = super().scoping.ids
        self._num_entities = len(self._scoping_ids_copy)
        self._has_data_pointer = len(self._data_pointer_copy)>0
    
    @property
    def size(self):
        """The length of the data vector.
        Also equals to the number of elementary data times the number of components.
        
        Returns
        -------
        size : int
        """
        return len(self._data_copy)
    
    def get_entity_data(self, index):
        """Returns the elementary data of the scoping's index in parameter

        Returns
        -------
        data : numpy.array
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     print(f.get_entity_data(0))
        [[-3.27795062e+05  1.36012200e+06  1.49090608e+08 -4.88688900e+06
           1.43038560e+07  1.65455040e+07]
         [-4.63817550e+06  1.29312225e+06  1.20411832e+08 -6.06617800e+06
           2.34829700e+07  1.77231120e+07]
         [-2.35684860e+07 -3.53474400e+07  2.01501168e+08 -5.23361700e+06
          -2.88789280e+07 -6.16478200e+06]
         [-3.92756960e+07 -2.72369280e+07  1.81454016e+08 -3.75441450e+06
          -3.62480300e+06 -3.26075620e+07]
         [ 1.63554530e+07  2.83190520e+07  1.05084256e+08 -1.30219020e+07
           5.19906719e+05  8.82430200e+06]
         [ 1.80755620e+07  5.25578750e+06  7.76211600e+07 -7.53063750e+06
           2.44717000e+06  2.92675125e+06]
         [ 9.25567760e+07  8.15244320e+07  2.77157632e+08 -1.48489875e+06
           5.89250600e+07  2.05608920e+07]
         [ 6.70443680e+07  8.70343440e+07  2.73050464e+08 -2.48670150e+06
           1.52268930e+07  6.09583280e+07]]
        
        """
        if index > self._num_entities:
            raise ValueError(f"asked scoping {index} is greater than the number of available indices {len(self._scoping_ids_copy)}")
        if self._has_data_pointer:
            first_index = self._data_pointer_copy[index]
            if index < len(self._data_pointer_copy) -1:
                last_index =  self._data_pointer_copy[index+1]-1
            else:
                last_index = len(self._data_copy)-1
        else:
            first_index = self._ncomp * index
            last_index = self._ncomp * (index+1)-1
        array = np.array([self._data_copy[first_index:last_index+1]])
        if self._ncomp>1:
            return array.reshape((array.size//self._ncomp,self._ncomp))
        else:
            return array
    
    def get_entity_data_by_id(self, id):
        """Return the data of the scoping's id in parameter of the field.

        Returns
        -------
        data : numpy.array
            Data based on the scoping id.
            
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> with fields_container[0].as_local_field() as f:
        ...     for id in f.scoping_ids:
        ...         if id < 2:
        ...             print(f.get_entity_data_by_id(id))
        [[-5.83890625e+03 -1.04498969e+05 -5.83890625e+03  2.10637354e+03
          -2.10637354e+03 -1.45397385e+02]
         [ 3.53322632e+03 -1.00388367e+05  3.53322632e+03 -1.66410352e+03
           1.66410352e+03  5.36620178e+01]
         [-1.05799683e+03 -1.00437922e+05  2.14961670e+03  5.90637268e+02
           1.37861340e+03 -1.68223175e+02]
         [ 2.62742480e+03 -9.89340078e+04 -2.02909998e+03 -2.40310791e+03
          -1.84942798e+03  7.16406616e+02]
         [-2.02909998e+03 -9.89340078e+04  2.62742480e+03  1.84942798e+03
           2.40310791e+03  7.16406616e+02]
         [ 2.14961670e+03 -1.00437922e+05 -1.05799683e+03 -1.37861340e+03
          -5.90637268e+02 -1.68223175e+02]
         [-4.94986755e+02 -9.87357891e+04 -4.94986755e+02 -6.93923187e+01
           6.93923187e+01 -1.59779755e+02]
         [ 1.36953296e+03 -9.76330156e+04  1.36953296e+03 -7.69014221e+02
           7.69014221e+02  4.90502930e+02]]

        """
        index = self._scoping_ids_copy.index(id)
        if index < 0:
            raise ValueError(f"The id {id} doesn't exist in the scoping")
        return self.get_entity_data(index)
    
    def append(self, data, scopingid):
        """Add an entity data to the existing data

        Parameters
        ----------
        data : list of int, double or array

        scopingid : int
            id of the scoping
            
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities=100
        >>> field_to_local = dpf.fields_factory.create_3d_vector_field(num_entities, location=dpf.locations.elemental_nodal)
        >>> with field_to_local.as_local_field() as f:    
        ...     for i in range(1,num_entities+1):
        ...         f.append([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]],i)
                    
        """
        if self._is_property_field:
            if not isinstance(data[0], int) and not isinstance(data[0], np.int32):
                raise errors.InvalidTypeError("data", "list of int")
        if (len(data)>0 and isinstance(data, list)) or isinstance(data,  (np.ndarray, np.generic)):
                data=np.array(data).flatten().tolist()
            
        data_size =len(self._data_copy)      
        self._scoping_ids_copy.append(scopingid)
        if len(self._data_pointer_copy)>0:
            self._data_pointer_copy.append(data_size)

        self._data_copy.extend(data)
        self._num_entities+=1
        if self._has_data_pointer==False:
            if isinstance(data,  (np.ndarray, np.generic)):
                data_size = data.size
            else:
                data_size=len(data)
            if data_size>self._ncomp:
                self._data_pointer_copy=[i*self._ncomp for i in range(0,self._num_entities) ]
                self._has_data_pointer=True   
                
    def data_as_list(self):
        """The data of this field in a python list

        Returns
        -------
        data : list
            Data of this field.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     my_data_list = f.data_as_list
         
        """
        return self._data_copy   
    
     
    @property
    def data(self):
        """The data of this field.

        Returns
        -------
        data : numpy.ndarray
            Data of this field.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     print(f.data)
        [[ 6.25586668e-03 -1.39243136e-02  2.42697211e-05]
         [ 1.79675948e-02 -2.74812825e-02  1.83822050e-05]
         [-6.72664571e-03 -3.21373459e-02  1.67159110e-04]
         ...
         [-6.07730368e-03  3.22569017e-02  3.10184480e-04]
         [-3.51074714e-06  2.16872928e-08  6.40738989e-05]
         [ 1.03542516e-02 -3.53018374e-03 -3.98914380e-05]]
        
        """
        if self._ncomp>1:
            return np.array(self._data_copy).reshape(len(self._data_copy)//self._ncomp,self._ncomp)
        else:
            return np.array(self._data_copy)
        
    
    @data.setter
    def data(self, data):
        if self._is_property_field:
            if not isinstance(data[0], int)and not isinstance(data[0], np.int32):
                raise errors.InvalidTypeError("data", "list of int")
        else:
            if isinstance(data,  (np.ndarray, np.generic)):
                if data.shape !=  self.shape and 0 != self.size:
                    raise ValueError(f'An array of shape {self.shape} is expected and shape {data.shape} is in input')
        if isinstance(data,  (np.ndarray, np.generic)):
            self._data_copy = data.flatten().tolist()
        elif len(data)>0 and isinstance(data, list):
            self._data_copy=np.array(data).flatten().tolist()
        else:
            self._data_copy = data
        
        
    @property
    def elementary_data_count(self):
        """Number of elementary data in the field"""
        if (hasattr(self, "_data_copy")):
            return len(self._data_copy) / self._ncomp
        else:
            return super().elementary_data_count
    
    
    @property
    def component_count(self):
        """
        Returns
        -------
        ncomp : int
            Number of component of the each elementary data
        """
        return self._ncomp
    
        
    @property
    def _data_pointer(self):
        """Gives the first index of each entity data

        Returns
        -------
        data : numpy.ndarray
            Data of this field.
        """
        return np.array(self._data_pointer_copy)
    
    @property
    def _data_pointer_as_list(self):
        """Gives the first index of each entity data

        Returns
        -------
        data : list of int
            Data of this field.
        """
        return self._data_pointer_copy
    
    
    @_data_pointer.setter
    def _data_pointer(self, data):
        """Set the data pointer of the field.

        Parameters
        ----------
        data : list of int or array
        """
        if isinstance(data,  (np.ndarray, np.generic)):
            self._data_pointer_copy = data.tolist()
        else:
            self._data_pointer_copy = data
        if self._has_data_pointer == False and len(data)>0:
            self._has_data_pointer=True
    
    @property
    def scoping_ids(self):
        """List of int representing the scoping ids of the field.
        """
        return self._scoping_ids_copy
    
    @scoping_ids.setter
    def scoping_ids(self, data):
        self._scoping_ids_copy =data
        self._num_entities =len(data)
    
        
    def release_data(self):
        super()._set_data(self._data_copy)
        super()._set_data_pointer(self._data_pointer_copy)
        super().scoping.ids = self._scoping_ids_copy
        
    def __enter__(self):
        return self
    
    def __exit__(self,type, value, tb):
        if tb is None:
            self.release_data()
        else :
            print(tb)
            
    def __del__(self):
        pass
     

            
        