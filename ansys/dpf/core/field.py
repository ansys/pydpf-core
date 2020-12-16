from functools import wraps

import numpy as np

from ansys import dpf
from ansys.grpc.dpf import field_pb2, field_pb2_grpc, base_pb2, field_definition_pb2, field_definition_pb2_grpc
from ansys.dpf.core.common import natures, types, locations, ShellLayers
from ansys.dpf.core import operators_helper, plotting, scoping, meshed_region, time_freq_support
from ansys.dpf.core.plotter import Plotter

class Field:
    """Class representing evaluated data from a ``ansys.dpf.core.Operator``.

    Parameters
    ----------
    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to the global channel.
     
    
    nentities : int
        Number of entities

    nature : ansys.dpf.core.natures, optional
        Nature of the field.

    location : str optional
        Location of the field ("Nodal", "Elemental", "ElementalNodal"...)

    field : ansys.grpc.dpf.field_pb2.Field, optional
        Field message generated from a grpc stub.

    Attributes
    ----------
    data : data of the field

    scoping : ids used to link the field to its support (often a meshedregion)
    """

    def __init__(self, nentities=0,
                 nature=natures.vector,
                 location=locations.nodal, field=None, channel=None):
        """Intialize the field with either optional field message, or
        by connecting to a stub.
        """
        if channel is None:
            channel = dpf.core._global_channel()       
            
        self._channel=channel
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
            self._message = self._stub.Create(request)
        else:
            if isinstance(field, dpf.core.Field):
                self._message = field._message
            elif isinstance(field, field_pb2.Field):
                self._message = field
            else:
                raise TypeError(f'Cannot create a field from a "{type(field)}" object')

        self._field_definition = self._load_field_definition()
        
        # add dynamic methods
        self._update_dynamic_methods()
        

    @property
    def size(self):
        """Number of elements times the number of components"""
        return self.elementary_data_count*self.component_count

    @property
    def shape(self):
        """Numpy-like shape of the field"""
        if self.component_count!=1:
            return (self.elementary_data_count, self.component_count)
        else :
            return self.elementary_data_count
        
    @property
    def elementary_data_shape(self):
        """Numpy-like shape of the field"""
        if self.component_count!=1:
            return (1, self.component_count)
        else :
            return self.component_count
        
    def _update_dynamic_methods(self):
        """Add or remove dynamic methods to this instance based on the
        field type"""
        if self.location in [locations.elemental_nodal, locations.elemental]:
            self.to_nodal = self.__to_nodal

    @property
    def location(self):
        """Return the field location.

        Returns
        -------
        location : str
        """
        if self._field_definition:
            return self._field_definition.location
        
    @property
    def shell_layers(self):
        """Return the field shell layers.
        
        Returns
        -------
        Enum 
            dpf.core.common.ShellLayers enum value
        """
        if self._field_definition:
            return self._field_definition.shell_layers
        
    def __to_nodal(self):
        """create a to_nodal operator and evaluates it"""
        op = dpf.core.Operator("to_nodal")
        op.inputs.connect(self)
        return op.outputs.field()
    
    def plot(self, notebook = None):
        """Plot the field/fields container on mesh support if exists.
        
        Parameters
        ----------         
        notebook (default: True)
            bool, that specifies if the plotting is in the notebook (2D) or not (3D)
        """
        pl = Plotter(self.meshed_region)
        pl.plot_contour(self, notebook)
    
    def resize(self, nentities, datasize):
        """allocate memory

        Parameters
        ----------
        nentities : int
            num ids in the scoping
        datasize : int
            data vector size
        """
        request=field_pb2.UpdateSizeRequest()
        request.field.CopyFrom(self._message)
        request.size.scoping_size = nentities
        request.size.data_size = datasize
        self._stub.UpdateSize(request)
        

    def _load_field_definition(self):
        """Attempt to load the field definition for this field"""
        try:
            request=field_pb2.GetRequest()
            request.field.CopyFrom(self._message)
            out = self._stub.GetFieldDefinition(request)
            return FieldDefinition(out.field_definition)
        except:
            return
    @property
    def unit(self):
        """Units of the field"""
        if self._field_definition:
            return self._field_definition.unit

    @property
    def name(self):
        request=field_pb2.GetRequest()
        request.field.CopyFrom(self._message)
        out = self._stub.GetFieldDefinition(request)
        return out.name

    def _set_data(self, data):
        """
        Parameters
        ----------
        data : list of double or array
        """
        if isinstance(data,  (np.ndarray, np.generic)):
            if data.shape !=  self.shape and data.size != self.size:
                raise ValueError(f'an array of shape {self.shape} is expected and shape {data.shape} is in input')
            else:
                data = data.reshape(data.size).tolist()
        request = field_pb2.UpdateDataRequest()
        request.data_containers.data.datadouble.rep_double.extend(data)
        request.field.CopyFrom(self._message)
        self._stub.UpdateData(request)

    def get_entity_data(self, index):
        """
        Returns the data of the scoping's index in parameter of the field
        
        Returns
        -------
        data : numpy.array
        """
        request = field_pb2.GetElementaryDataRequest()
        request.field.CopyFrom(self._message)
        request.index = index
        list_message = self._stub.GetElementaryData(request, metadata=[(b'float_or_double', b'double')])
        list = []
        if list_message.elemdata_containers.data.HasField("datadouble"):
            list= list_message.elemdata_containers.data.datadouble.rep_double
        elif list_message.elemdata_containers.data.HasField("dataint"):
            list = list_message.elemdata_containers.data.dataint.rep_int
        
        array = np.array(list)
        if self.component_count !=1 :
            array = array.reshape((len(list)//self.component_count,self.component_count))
        
        return array

    def get_entity_data_by_id(self, id):
        """
        Returns the data of the scoping's id in parameter of the field
        
        Returns
        -------
        data : numpy.array
        """
        index = self.scoping.index(id)
        if index<0:
            raise ValueError(f'the id {id} doesn\'t belong to this field')
        else:
            return self.get_entity_data(index)
        
    def set_entity_data(self, data, index, scopingid):
        """
        Parameters
        ----------
        data : list of double or array

        index : int
            index of the scoping

        scopingid : int
            id of the scoping
        """
        if isinstance(data,  (np.ndarray, np.generic)):
            data = data.reshape(data.size).tolist()
        request = field_pb2.UpdateDataRequest()
        request.elemdata_containers.data.datadouble.rep_double.extend(data)
        request.elemdata_containers.scoping_index = index
        if scopingid is None:
            scopingid=self.scoping.id(index)
            
        request.elemdata_containers.scoping_id = scopingid
            
        request.field.CopyFrom(self._message)
        self._stub.UpdateData(request)

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

    def _get_data(self):
        """
        Returns all the data of the field
        
        Returns
        -------
        data : numpy.array
        """
        request = field_pb2.ListRequest()
        request.field.CopyFrom(self._message)
        if self._message.datatype == u"int":
            data_type = u"int"
            dtype = np.int32
        else :
            data_type = u"double"
            dtype = np.float
        service = self._stub.List(request, metadata=[(u"float_or_double", data_type)])
        tupleMetaData = service.initial_metadata()
        for iMeta in range(len(tupleMetaData)):
            if tupleMetaData[iMeta].key == u"size_tot":
                size = int(tupleMetaData[iMeta].value)
    
        ncomp=self.component_count
        itemsize = np.dtype(dtype).itemsize
        arr = np.empty(size//itemsize,dtype)
        i = 0
        for chunk in service:
            curr_size=len(chunk.array)//itemsize
            arr[i:i + curr_size] = np.frombuffer(chunk.array, dtype)
            i += curr_size
            
        if ncomp!=1:
            arr =arr.reshape(self.shape)

        return arr

    @property
    def elementary_data_count(self):
        """
        Returns
        ------- 
        ndata : int
            number of elementary data in the field
        """
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.field.CopyFrom(self._message)
        return self._stub.Count(request).count

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
    
    def _get_meshed_region(self):
        """
        Returns
        -------
        meshed_region : MeshedRegion
        """
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("MESHED_REGION")
        try:
            message = self._stub.GetSupport(request)
            return meshed_region.MeshedRegion(mesh=message)
        except:
            print("the field's support is not a mesh (try a time_freq_support)")
    
    def _get_time_freq_support(self):
        """
        Returns
        -------
        time_freq_support : TimeFreqSupport
        """
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        try:
            message = self._stub.GetSupport(request)
            return time_freq_support.TimeFreqSupport(time_freq_support=message)
        except:
            print("the field's support is not a timefreqsupport (try a mesh)")
    

    @property
    def time_freq_support(self):
        return self._get_time_freq_support()
    
    @property
    def meshed_region(self):
        return self._get_meshed_region()
    
    # TODO: Consider making this private or just using the ndim property
    @property
    def component_count(self):
        """
        Returns
        -------
        ncomp : int
            Number of component of the each elementary data
        """
        request = field_pb2.CountRequest()
        request.entity = base_pb2.NUM_COMPONENT
        request.field.CopyFrom(self._message)
        return self._stub.Count(request).count
    
    def __add__(self, field_b):
        """Adds two fields together"""
        return dpf.core.operators_helper.add(self, field_b)

    def __pow__(self, value):
        if value != 2:
            raise ValueError('DPF only the value is "2" suppported')
        return dpf.core.operators_helper.sqr(self)

    def _del_data(self):
        pass

    def _del_scoping(self, scoping):
        scoping.__del__()

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def _connect(self):
        """Connect to the grpc service"""
        return field_pb2_grpc.FieldServiceStub(self._channel)

    # TOOD: Consider writing out setters and getters
    data = property(_get_data, _set_data, _del_data, "data")
    scoping = property(_get_scoping, _set_scoping, _del_scoping, "scoping")

    @property
    def ndim(self):
        return self.component_count

    def __str__(self):
        txt = 'DPF %s Field\n' % self.name
        txt += '\tLocation: %s\n' % self.location
        txt += '\tUnit: %s\n' % self.unit
        txt += '\t%d id(s)\n' % self.scoping.size
        txt += '\tdata size: %s\n' % self.size
        txt += f'\tshape: {self.shape}\n'
        try:
            if self.size == 1:
                txt += f'\tValue: {self.data[0]}\n'
        except:
            pass

        return txt
    
    def __len__(self):
        return self.size


    @wraps(operators_helper.min_max)
    def _min_max(self):
        return operators_helper.min_max(self)

    def min(self):
        """Component-wise minimum over this field

        Returns
        -------
        min : ansys.dpf.core.Field
            Component-wise minimum field.
        """
        
        return self._min_max().get_output(0, types.field)

    def max(self):
        """Component-wise maximum over this field

        Returns
        -------
        max : ansys.dpf.core.Field
            Component-wise maximum field.
        """
        return self._min_max().get_output(1, types.field)

  

class FieldDefinition:
    """Represent a Field definition"""

    def __init__(self, field_definition=None, channel=None):
        if channel is None:
            channel = dpf.core._global_channel()  
            
        self._messageDefinition = field_definition
        self._stub = self._connect(channel)

    @property
    def location(self):
        out = self._stub.List(self._messageDefinition)
        return out.location.location
    
    @property
    def unit(self):
        return self._stub.List(self._messageDefinition).unit.symbol
    
    @property
    def shell_layers(self):
        enum_val = self._stub.List(self._messageDefinition).shell_layers
        return ShellLayers(enum_val)

    def __del__(self):
        try:
            self._stub.Delete(self._messageDefinition)
        except:
            pass

    def _connect(self, channel):
        """Connect to the grpc service"""
        return field_definition_pb2_grpc.FieldDefinitionServiceStub(channel)
