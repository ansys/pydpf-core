"""
Field
=====
"""
from functools import wraps

import numpy as np

from ansys import dpf
from ansys.grpc.dpf import (field_pb2, field_pb2_grpc, base_pb2,
                            field_definition_pb2, field_definition_pb2_grpc)
from ansys.dpf.core.core import BaseService
from ansys.dpf.core.common import natures, types, locations, shell_layers
from ansys.dpf.core import operators_helper, scoping, meshed_region, time_freq_support
from ansys.dpf.core.plotter import Plotter
from ansys.dpf.core import errors

class Field:
    """Class representing evaluated data from a ``ansys.dpf.core.Operator``.

    Parameters
    ----------
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    nentities : int
        Number of entities reserved

    nature : ansys.dpf.core.natures, optional
        Nature of the field.

    location : str, optional
        Location of the field.  For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ``"ElementalNodal"``

    field : ansys.grpc.dpf.field_pb2.Field, optional
        Field message generated from a grpc stub.

    Examples
    --------
    >>> # 1. Create a field from scratch
    >>> from ansys.dpf.core import fields_factory
    >>> from ansys.dpf.core import locations
    >>> from ansys.dpf import core
    >>> field_with_classic_api = core.Field()
    >>> field_with_classic_api.location = locations.scalar
    >>> field_with_factory = fields_factory.create_scalar_field(10)
    
    >>> # 2. Extract a displacement field from a transient result file.
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> fields_container = disp.outputs.fields_container()
    >>> field = fields_container[0]
    >>> print(field)
    DPF displacement_0.676628s Field
        Location: Nodal
        Unit: m
        3820 entities 
        Data:3 components and 3820 elementary data 
        
    Create a displacement field
    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
    >>> my_field.data = np.zeros(30)
    >>> my_field.scoping.ids = range(1,11)
    """

    def __init__(self, nentities=0, nature=natures.vector,
                 location=locations.nodal, field=None, server=None):
        """Initialize the field with either optional field message, or
        by connecting to a stub.
        """
        if server is None:
            server = dpf.core._global_server()

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
            self._message = self._stub.Create(request)
        else:
            if isinstance(field, dpf.core.Field):
                self._message = field._message
            elif isinstance(field, field_pb2.Field):
                self._message = field
            else:
                raise TypeError(f'Cannot create a field from a "{type(field)}" object')

        self._field_definition = self._load_field_definition()

    @property
    def size(self):
        """Number of elements times the number of components"""
        return self.elementary_data_count*self.component_count

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
    def elementary_data_shape(self):
        """Numpy-like shape of the field"""
        if self.component_count != 1:
            return (1, self.component_count)
        else:
            return self.component_count

    @property
    def location(self):
        """Return the field location.

        Returns
        -------
        location : str
            Location string.  Either ``'Nodal'``, ``'Elemental'``, or
            ``'ElementalNodal'``.

        Examples
        --------
        Location for a stress field evaluated at nodes

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_transient_result())
        >>> s_op =model.results.stress()
        >>> s_fc = s_op.outputs.fields_container()
        >>> field = s_fc[0]
        >>> field.location
        'ElementalNodal'
        """
        if self.field_definition:
            return self.field_definition.location
        
    @location.setter
    def location(self, value):
        """Change the field location.

        Parameters
        -------
        location : stror dpf.core.locations
            Location string.  Either ``'Nodal'``, ``'Elemental'``, 
            ``'ElementalNodal'``...

        Examples
        --------
        Location for a field evaluated at nodes

        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.data = np.zeros(30)
        >>> my_field.scoping.ids = range(1,11)
        >>> my_field.location
        'Nodal'
        >>> my_field.location = dpf.locations.elemental_nodal
        >>> my_field.location
        'ElementalNodal'
        """
        fielddef = self.field_definition
        fielddef.location = value
        self.field_definition = fielddef

    @property
    def shell_layers(self):
        """Return the field's shell layers.

        Returns
        -------
        Enum
            dpf.core.common.shell_layers enum value
        """
        if self.field_definition:
            return self.field_definition.shell_layers
        
    @shell_layers.setter
    def shell_layers(self, value):
        """Change the field's shell layers.

        Parameters
        -------
        Enum
            dpf.core.common.shell_layers enum value
        """
        fielddef = self.field_definition
        fielddef.shell_layers = value
        self.field_definition = fielddef

    def to_nodal(self):
        """Convert this field to one with a Nodal location.

        Only valid when this field's location is ElementalNodal or
        Elemental.

        Returns
        -------
        Field
            Field with ``location=='Nodal'``.
        """
        if self.location == 'Nodal':
            raise errors.LocationError('Location is already "Nodal"')

        op = dpf.core.Operator("to_nodal")
        op.inputs.connect(self)
        return op.outputs.field()

    def plot(self, notebook=None, shell_layers=None):
        """Plot the field/fields container on mesh support if exists.

        Warning
        -------
        This is primarily added out of convenience as plotting
        directly from the field can be slower than extracting the
        meshed region and plotting the field on top of that.  It is
        more efficient to plot with:

        >>> mesh = model.metadata.meshed_region
        >>> mesh.plot(field)

        Parameters
        ----------
        notebook : bool, optional
            Bool, that specifies if the plotting is in the notebook as
            a static image or or as a dynamic plot outside of the
            notebook.

        shell_layers : core.shell_layers, optional
            Enum used to set the shell layers if the model to plot
            contains shell elements.
        """
        pl = Plotter(self.meshed_region)
        pl.plot_contour(self, notebook, shell_layers)

    def resize(self, nentities, datasize):
        """Allocate memory.

        Parameters
        ----------
        nentities : int
            num ids in the scoping

        datasize : int
            data vector size
        """
        request = field_pb2.UpdateSizeRequest()
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
        """Units of the field

        Returns
        ----------
        unit : str
        
        Examples
        --------
        Units of a displacement field

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'
        """
        if self.field_definition:
            return self.field_definition.unit
        
    @unit.setter
    def unit(self, value):
        """Change the unit of the field
        
        Parameters
        ----------
        unit : str

        Examples
        --------
        Units of a displacement field

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'
        """
        fielddef = self.field_definition
        fielddef.unit = value
        self.field_definition = fielddef
        
    @property
    def dimensionnality(self):
        """
        Returns
        -------
        dimensionnality : dpf.core.Dimensionnality
            nature and size of the elementary data
        """
        if self.field_definition:
            return self.field_definition.dimensionnality
        
    @dimensionnality.setter
    def dimensionnality(self, value):
        """
        Parameters
        ----------
        dimensionnality : dpf.core.Dimensionnality
            nature and size of the elementary data
        """
        fielddef = self.field_definition
        fielddef.dimensionnality = value
        self.field_definition = fielddef
        
    @property
    def name(self):
        request = field_pb2.GetRequest()
        request.field.CopyFrom(self._message)
        out = self._stub.GetFieldDefinition(request)
        return out.name

    def get_entity_data(self, index):
        """Returns the data of the scoping's index in parameter of the
        field.

        Returns
        -------
        data : numpy.array
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
        """
        index = self.scoping.index(id)
        if index < 0:
            raise ValueError(f'The id {id} must be greater than 0')
        return self.get_entity_data(index)

    def append(self, data, scopingid):
        """add an entity data to the existing data

        Parameters
        ----------
        data : list of double or array

        scopingid : int
            id of the scoping
        """
        if isinstance(data, (np.ndarray, np.generic)):
            data = data.reshape(data.size).tolist()
        request = field_pb2.AddDataRequest()
        request.elemdata_containers.data.datadouble.rep_double.extend(data)
        request.elemdata_containers.scoping_id = scopingid

        request.field.CopyFrom(self._message)
        self._stub.AddData(request)

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
        
    def _set_field_definition(self, field_definition):
        """
        Parameters
        ----------
        field_definition : FieldDefinition
        """
        request = field_pb2.UpdateFieldDefinitionRequest()
        request.field_def.CopyFrom(field_definition._messageDefinition)
        request.field.CopyFrom(self._message)
        self._stub.UpdateFieldDefinition(request)

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
        >>> field.data
        array([[ 6.25586668e-03, -1.39243136e-02,  2.42697211e-05],
           [ 1.79675948e-02, -2.74812825e-02,  1.83822050e-05],
           [-6.72664571e-03, -3.21373459e-02,  1.67159110e-04],
           ...,
           [-6.07730368e-03,  3.22569017e-02,  3.10184480e-04],
           [-3.51074714e-06,  2.16872928e-08,  6.40738989e-05],
           [ 1.03542516e-02, -3.53018374e-03, -3.98914380e-05]])
        """
        request = field_pb2.ListRequest()
        request.field.CopyFrom(self._message)
        if self._message.datatype == u"int":
            data_type = u"int"
            dtype = np.int32
        else:
            data_type = u"double"
            dtype = np.float
        service = self._stub.List(request, metadata=[(u"float_or_double", data_type)])
        tupleMetaData = service.initial_metadata()
        for iMeta in range(len(tupleMetaData)):
            if tupleMetaData[iMeta].key == u"size_tot":
                size = int(tupleMetaData[iMeta].value)

        ncomp = self.component_count
        itemsize = np.dtype(dtype).itemsize
        arr = np.empty(size//itemsize, dtype)
        i = 0
        for chunk in service:
            curr_size = len(chunk.array)//itemsize
            arr[i:i + curr_size] = np.frombuffer(chunk.array, dtype)
            i += curr_size

        if ncomp != 1:
            arr = arr.reshape(self.shape)

        return arr

    @data.setter
    def data(self, data):
        """Set the data of the field.

        Parameters
        ----------
        data : list of double or array
        """
        if isinstance(data,  (np.ndarray, np.generic)):
            if data.shape !=  self.shape and 0 != self.size:
                raise ValueError(f'An array of shape {self.shape} is expected and shape {data.shape} is in input')
            else:
                data = np.array(data.reshape(data.size), dtype=float)
        else:
            data = np.array(data, dtype=float)
        if len(data)==0:
            return
        
        metadata=[(u"float_or_double", u"double"), (u"size_double", f"{len(data)}")]
        request = field_pb2.UpdateDataRequest()
        request.field.CopyFrom(self._message)
        self._stub.UpdateData(scoping._data_chunk_yielder(request, data), metadata=metadata)
           
   
    @property
    def field_definition(self):
        """The field definition defines what is the field: its location, unit, dimensionnality, shell layers...
        """
        return self._field_definition
    
    @field_definition.setter
    def field_definition(self, value):
        """The field definition defines what is the field: its location, unit, dimensionnality, shell layers...

        Parameters
        ----------
        field_definition : FieldDefinition
        """
        return self._set_field_definition(value)

    @property
    def elementary_data_count(self):
        """Number of elementary data in the field"""
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
            raise RuntimeError("The field's support is not a mesh.  Try a time_freq_support.")

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
            raise RuntimeError("The field's support is not a timefreqsupport.  Try a mesh.")

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

    # TODO: Consider writing out setters and getters
    scoping = property(_get_scoping, _set_scoping, _del_scoping, "scoping")

    @property
    def ndim(self):
        return self.component_count

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        return BaseService(self._server)._description(self._message)

    def __len__(self):
        return self.size


    def _min_max(self):
        from ansys.dpf.core import dpf_operator
        op = dpf_operator.Operator("min_max")
        op.connect(0, self)
        return op

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

class Dimensionnality:
    """Class representing the dimensionnality of the field
        Read list of dim (1D vector for scalar and vector and 2D vector for matrix)
        and create a field_definition_pb2.Dimensionality message
        
    Parameters
    ----------
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    dim_vec : list of int
        [1]: scalar
        [3]: 3d vector
        [3,3]: matrix 3 3
        
    nature : core.Nature
    """
    
    def __init__(self, dim_vec, nature : natures):
        self.dim = dim_vec
        self.nature = nature
        
    def _parse_dim_to_message(self):
        message = field_definition_pb2.Dimensionality()
        message.size.extend(self.dim)
        message.nature = self.nature.value
        return message
    
    def __str__(self):
        return str(self.dim) + " "+ self.nature.name
    
    
    @staticmethod
    def scalar_dim():
        """Dimensionnality instance corresponding to a scalar field

        Returns
        -------
        dimensionnality : ansys.dpf.core.Dimensionnality
        """
        return Dimensionnality([1], natures.scalar)
    
    @staticmethod
    def vector_dim(size):
        """Dimensionnality instance corresponding to a vector field of size "size"
        
        Parameters
        ----------
        size : int
            number of components by entity
        
        Returns
        -------
        dimensionnality : ansys.dpf.core.Dimensionnality
        """
        return Dimensionnality([size], natures.vector)
    
    @staticmethod
    def vector_3d_dim():
        """Dimensionnality instance corresponding to a 3 dimensions vector field

        Returns
        -------
        dimensionnality : ansys.dpf.core.Dimensionnality
        """
        return Dimensionnality([3], natures.vector)
    
    @staticmethod
    def tensor_dim():
        """Dimensionnality instance corresponding to a symmetrical 3 3 tensor field

        Returns
        -------
        dimensionnality : ansys.dpf.core.Dimensionnality
        """
        return Dimensionnality([3,3], natures.symmatrix)

                 
class FieldDefinition:
    """Represent a Field definition with with its FieldDefinition message (if possible)"""

    def __init__(self, field_definition=None, server=None):          
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect(self._server.channel)
        if isinstance(field_definition, field_definition_pb2.FieldDefinition):
            self._messageDefinition = field_definition
        else:
            request = base_pb2.Empty()
            self._messageDefinition = self._stub.Create(request)
            
    @property
    def location(self):
        """
        Returns
        -------
        location : str
            where the data is located (Nodal, Elemental, TimeFreq_sets...)
        """
        out = self._stub.List(self._messageDefinition)
        return out.location.location

    @property
    def unit(self):
        """
        Returns
        -------
        unit : str
        """
        return self._stub.List(self._messageDefinition).unit.symbol
    

    @property
    def shell_layers(self):        
        """
        Returns
        -------
        shell_layers : dpf.core.shell_layer
            returns LayerIndependent for fields unrelated to layers
        """
        enum_val = self._stub.List(self._messageDefinition).shell_layers
        return shell_layers(enum_val.real-1) #+1 is added to the proto enum to have notset as 0
    
    @property
    def dimensionnality(self):
        """
        Returns
        -------
        dimensionnality : dpf.core.Dimensionnality
            nature and size of the elementary data
        """
        val = self._stub.List(self._messageDefinition).dimensionnality
        return Dimensionnality(val.size, natures(val.nature.real))
    
    @unit.setter
    def unit(self, value):
        self._modify_field_def(unit=value)
        
        
    @location.setter
    def location(self, value):
        self._modify_field_def(location=value)
        
        
    @shell_layers.setter
    def shell_layers(self, value):
        self._modify_field_def(shell_layer=value)
        
        
    @dimensionnality.setter
    def dimensionnality(self, value):
        self._modify_field_def(dimensionnality=value)
    
    
    def _modify_field_def(self, unit = None, location = None, dimensionnality = None, shell_layer=None):
        request = field_definition_pb2.FieldDefinitionUpdateRequest()
        request.field_definition.CopyFrom(self._messageDefinition)
        if unit != None:
            request.unit_symbol.symbol = unit
        if location != None:
            request.location.location = location
        if dimensionnality != None:
            if not isinstance(dimensionnality, Dimensionnality):
                raise TypeError("the dimensionnality needs to be of type Dimensionnsality")
            request.dimensionnality.CopyFrom(dimensionnality._parse_dim_to_message())
        if shell_layer != None:
            if isinstance(shell_layer, shell_layers):
                request.shell_layers = shell_layer.value+1
            else:                
                request.shell_layers = shell_layer+1
        self._stub.Update(request)
        
    
    def __del__(self):
        try:
            self._stub.Delete(self._messageDefinition)
        except:
            pass

    def _connect(self, channel):
        """Connect to the grpc service"""
        return field_definition_pb2_grpc.FieldDefinitionServiceStub(channel)
