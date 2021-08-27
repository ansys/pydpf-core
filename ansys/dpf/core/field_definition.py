"""
FieldDefinition
================
"""

from ansys import dpf
from ansys.grpc.dpf import (base_pb2,
                            field_definition_pb2, field_definition_pb2_grpc)
from ansys.dpf.core.common import natures, shell_layers
from ansys.dpf.core.dimensionality import Dimensionality


class FieldDefinition:
    """Contains the physical and mathematical description of the field.
    
    Parameters
    ----------
    field_definition : optional
        The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance. 
        The default is ``None``, in which case an attempt is made to use 
        the global server.
    """

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
        """Field location.
        
        Returns
        -------
        str
            Location string, such as ``"Nodal"``, ``"Elemental"``, 
            or ``"TimeFreq_sets"``. 
        """
        out = self._stub.List(self._messageDefinition)
        return out.location.location

    @property
    def unit(self):
        """Units of the field.

        Returns
        -------
        str
            Units of the field.
        """
        return self._stub.List(self._messageDefinition).unit.symbol
    

    @property
    def shell_layers(self):        
        """Order of the shell layers.
        
        Returns
        -------
        shell_layers : shell_layers
            ``LayerIndependent`` is returned for fields unrelated to layers.
        """
        enum_val = self._stub.List(self._messageDefinition).shell_layers
        return shell_layers(enum_val.real-1) #+1 is added to the proto enum to have notset as 0
    
    @property
    def dimensionality(self):
        """Dimensionality
        
        Returns
        -------
        dimensionality : Dimensionality
            Nature and size of the elementary data.
        """
        val = self._stub.List(self._messageDefinition).dimensionnality # typo exists on server side
        return Dimensionality(val.size, natures(val.nature.real))
    
    @unit.setter
    def unit(self, value):
        self._modify_field_def(unit=value)
        
        
    @location.setter
    def location(self, value):
        self._modify_field_def(location=value)
        
        
    @shell_layers.setter
    def shell_layers(self, value):
        self._modify_field_def(shell_layer=value)
        
        
    @dimensionality.setter
    def dimensionality(self, value):
        self._modify_field_def(dimensionality=value)
    
    
    def _modify_field_def(self, unit = None, location = None, dimensionality = None, shell_layer=None):
        request = field_definition_pb2.FieldDefinitionUpdateRequest()
        request.field_definition.CopyFrom(self._messageDefinition)
        if unit != None:
            request.unit_symbol.symbol = unit
        if location != None:
            request.location.location = location
        if dimensionality != None:
            if not isinstance(dimensionality, Dimensionality):
                raise TypeError("the dimensionality needs to be of type Dimensionality")
            request.dimensionnality.CopyFrom(dimensionality._parse_dim_to_message()) # typo is on server side
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
        """Connect to the gRPC service."""
        return field_definition_pb2_grpc.FieldDefinitionServiceStub(channel)
