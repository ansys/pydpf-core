"""
Field
=====
"""
import numpy as np

from ansys import dpf
from ansys.grpc.dpf import (field_pb2, field_pb2_grpc, base_pb2)
from ansys.dpf.core.common import natures, types, locations
from ansys.dpf.core import scoping, meshed_region, time_freq_support
from ansys.dpf.core.plotter import Plotter
from ansys.dpf.core import errors
from ansys.dpf.core.field_definition import FieldDefinition
from ansys.dpf.core.field_base import _FieldBase, _LocalFieldBase
from ansys.dpf.core.dimensionnality import Dimensionnality

class Field(_FieldBase):
    """Class representing evaluated data from a ``ansys.dpf.core.Operator``.

    Parameters
    ----------
    nentities : int
        Number of entities reserved

    nature : natures, optional
        Nature of the field.

    location : str, optional
        Location of the field.  For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ``"ElementalNodal"``

    field : ansys.grpc.dpf.field_pb2.Field, optional
        Field message generated from a grpc stub.
        
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    >>> # 1. Create a field from scratch
    >>> from ansys.dpf.core import fields_factory
    >>> from ansys.dpf.core import locations
    >>> from ansys.dpf import core as dpf
    >>> field_with_classic_api = dpf.Field()
    >>> field_with_classic_api.location = locations.nodal
    >>> field_with_factory = fields_factory.create_scalar_field(10)
    
    >>> # 2. Extract a displacement field from a transient result file.
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> fields_container = disp.outputs.fields_container()
    >>> field = fields_container[0]
    >>> len(field)
    11460
    >>> field.component_count
    3
    >>> field.elementary_data_count
    3820
        
    >>> # 3. Create a displacement field
    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
    >>> my_field.data = np.zeros(30)
    >>> my_field.scoping.ids = range(1,11)
    
    >>> # 4. Set data
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> fields_container = disp.outputs.fields_container()
    >>> field = fields_container[0]
    >>> field.data[2]
    array([-0.00672665, -0.03213735,  0.00016716])
    
    """
    
    def __init__(self, nentities=0, nature=natures.vector,
                 location=locations.nodal, field=None, server=None):
        """Initialize the field with either optional field message, or
        by connecting to a stub.
        """
        super().__init__(nentities, nature, location, False, field, server)
        self._field_definition = self._load_field_definition() 
        
        
    def as_local_field(self):
        """Creates a deep copy of the field locally so that the user can access 
        and modify it locally without any request sent to the server.
        This should be used in a with statement, so that the local field
        is released and the data is sent to the server in one shot.
        If it's not used in a with statement, the method release_data()
        should be used to actually update the field.
        
        Warning
        -------
        If this as_local_field metod is not used as a context manager in a 
        with statement or if the method release_data() is not called,
        the data will not be actually updated.
        
        Returns
        -------
        local_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities = 3
        >>> field_to_local = dpf.fields_factory.create_3d_vector_field(num_entities, location=dpf.locations.elemental_nodal)
        >>> with field_to_local.as_local_field() as f:    
        ...     for i in range(1,num_entities+1):
        ...         f.append([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]],i)
        ...         f.get_entity_data(i-1),[[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]
        (array([[0.1, 0.2, 0.3],
               [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        (array([[0.2, 0.4, 0.6],
               [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
        (array([[0.3, 0.6, 0.9],
               [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])
            
        """
        return _LocalField(self)  
    
   
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
        >>> s_op = model.results.stress()
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
        location : str or locations
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
        """Return the field's shell layers order (or lack of shell layers) 
        that defines how the field's data is ordered.

        Returns
        -------
        Enum : shell_layers
        """
        if self.field_definition:
            return self.field_definition.shell_layers
        
    @shell_layers.setter
    def shell_layers(self, value):
        """Change the field's shell layers.

        Parameters
        -------
        Enum : shell_layer
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
        nodal_field : Field 
            with ``location=='Nodal'``.
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

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> mesh = model.metadata.meshed_region
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> mesh.plot(field)
        [(1.675707321585373, 1.675707321585373, 2.425707321585373),
         (0.0, 0.0, 0.75),
         (0.0, 0.0, 1.0)]

        Parameters
        ----------
        notebook : bool, optional
            Bool, that specifies if the plotting is in the notebook as
            a static image or or as a dynamic plot outside of the
            notebook.

        shell_layers : shell_layers, optional
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
            return FieldDefinition(out.field_definition, self._server)
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
        """The Dimensionnality represents the shape of an elementary
        data contains in the Field.
        
        Returns
        -------
        dimensionnality : Dimensionnality
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
            
    def _set_support(self, support, support_type: str):
        """
        Set field support as time_freq_support or meshed_region.
        """
        request = field_pb2.SetSupportRequest()
        request.field.CopyFrom(self._message)
        request.support.type = base_pb2.Type.Value(support_type)
        request.support.id = support._message.id
        self._stub.SetSupport(request)

    @property
    def time_freq_support(self):
        """
        Time_freq_support of the associated field.
        
        Returns
        -------
        time_freq_support : TimeFreqSupport
            Describe the time frequency support of the field. 
        """
        return self._get_time_freq_support()
    
    @time_freq_support.setter
    def time_freq_support(self, value):
        """
        Set the time_freq_support of the associated field.
        
        Parameters
        ----------
        time_freq_support : TimeFreqSupport
            Describe the time frequency support of the field. 
        """
        self._set_support(value, "TIME_FREQ_SUPPORT")
        
    @property
    def meshed_region(self):
        """
        Meshed_region of the associated field.
        
        Return
        ------
        meshed_region : MeshedRegion
            Describe the mesh support of the field. 
        """
        return self._get_meshed_region()
    
    @meshed_region.setter
    def meshed_region(self, value):
        """
        Set the meshed_region of the associated field.
        
        Parameters
        ----------
        meshed_region : MeshedRegion
            Describe the mesh support of the field. 
        """
        self._set_support(value, "MESHED_REGION")

    def __add__(self, field_b):
        """Adds two fields together
                
        Returns
        -------
        add : operators.math.add
        """
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "add") :
            op= operators.math.add()
        else :
            op= dpf_operator.Operator("add")
        op.connect(0,self)        
        op.connect(1, field_b)
        return op

    def __pow__(self, value):
        if value != 2:
            raise ValueError('DPF only the value is "2" suppported')
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "sqr") :
            op= operators.math.sqr()
        else :
            op= dpf_operator.Operator("sqr")
        op.connect(0,self)        
        op.connect(1, value)
        return op
    
    def __mul__(self, value):
        """Multiplies two fields together"""
        from ansys.dpf.core import dpf_operator
        from ansys.dpf.core import operators
        if hasattr(operators, "math") and  hasattr(operators.math, "generalized_inner_product") :
            op= operators.math.generalized_inner_product()
        else :
            op= dpf_operator.Operator("generalized_inner_product")
        op.connect(0,self)        
        op.connect(1, value)
        return op


    def _min_max(self):
        from ansys.dpf.core import dpf_operator
        op = dpf_operator.Operator("min_max")
        op.connect(0, self)
        return op

    def min(self):
        """Component-wise minimum over this field

        Returns
        -------
        min : Field
            Component-wise minimum field.
        """
        return self._min_max().get_output(0, types.field)

    def max(self):
        """Component-wise maximum over this field

        Returns
        -------
        max : Field
            Component-wise maximum field.
        """
        return self._min_max().get_output(1, types.field)
    
    def deep_copy(self,server=None):
        """Creates a deep copy of the field's data on a given server.
        This can be usefull to pass data from one server instance to another.
        
        Parameters
        ----------
        server : DPFServer, optional
        
        Returns
        -------
        field_copy : Field
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> other_server = dpf.start_local_server(as_global=False)
        >>> deep_copy = field.deep_copy(server=other_server)
        
        """
        f = Field(nentities=len(self.scoping), location=self.location,nature=self.field_definition.dimensionnality.nature, server=server)
        f.scoping = self.scoping.deep_copy(server)
        f.data = self.data
        f.unit = self.unit
        f.location = self.location
       
        try:
            f._data_pointer = self._data_pointer
        except:
            pass
        try:
            f.meshed_region = self.meshed_region.deep_copy(server=server)
        except:
            pass
        try:
            f.time_freq_support = self.time_freq_support.deep_copy(server=server)
        except:
            pass
        return f
        
class _LocalField(_LocalFieldBase,Field):
    """Class only created by a field to cache the internal data of the field,
    modify it locallly, and send a single update request to the server 
    when the local field is deleted
    
    Parameters
    ----------
    field : Field
        field to copy
        
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> num_entities = 3
    >>> field_to_local = dpf.fields_factory.create_3d_vector_field(num_entities, location=dpf.locations.elemental_nodal)
    >>> with field_to_local.as_local_field() as f:    
    ...     for i in range(1,num_entities+1):
    ...         f.append(np.array([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]),i)
    ...         f.get_entity_data(i-1),[[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]
    (array([[0.1, 0.2, 0.3],
           [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    (array([[0.2, 0.4, 0.6],
           [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
    (array([[0.3, 0.6, 0.9],
           [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])

    """
    
    def __init__(self, field):
        super().__init__(field)
        