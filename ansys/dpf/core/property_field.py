"""
PropertyField
=============
"""

from ansys.dpf.core.common import natures, locations
from ansys.dpf.core.field_base import _FieldBase,_LocalFieldBase

class PropertyField(_FieldBase):
    """Property field class is a Field that describes properties such as connectivity. 
    It is a Field with integer values instead of double values.
    
    Parameters
    ----------
    nentities: int
        Number of entities that the property field will contain. 
        
    nature: core.natures
        Nature of the field (scalar, vector...)
        
    Returns
    -------
    property_field: PropertyField
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> pfield = dpf.PropertyField()
    >>> list_ids = [1, 2, 4, 6, 7]
    >>> scop = dpf.Scoping(ids = list_ids, location = dpf.locations.nodal)
    >>> pfield.scoping = scop
    >>> list_data = [20, 30, 50, 70, 80]
    >>> pfield.data = list_data
    
    """
    
    def __init__(self, nentities=0, nature=natures.scalar, location=locations.nodal, 
                 property_field=None, server=None):
        super().__init__(nentities, nature, location, True, property_field, server)
        
    @property
    def location(self):
        """Return the property field location. Property field contains a scoping and this 
        is the location that is read. To upadte location, directly update the scoping 
        location. 

        Returns
        -------
        location : str
            Location string.  Either ``'Nodal'`` or ``'Elemental'``.

        Examples
        --------
        Create a property field and request location
        
        >>> from ansys.dpf import core as dpf
        >>> pfield = dpf.PropertyField()
        >>> list_ids = [1, 2, 4, 6, 7]
        >>> scop = dpf.Scoping(ids = list_ids, location = dpf.locations.nodal)
        >>> pfield.scoping = scop
        >>> pfield.scoping.location = dpf.locations.nodal
        >>> pfield.location
        'Nodal'
        
        """
        if self.scoping:
            return self.scoping.location
        else:
            return None
        
    @location.setter
    def location(self, value):
        """Change the property field location.

        Parameters
        ----------
        location : str or locations
            Location string.  Either ``'Nodal'``, ``'Elemental'``.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> pfield = dpf.PropertyField()
        >>> scop = dpf.Scoping(ids = list_ids, location = dpf.locations.nodal)
        >>> pfield.scoping = scop
        >>> pfield.location = 'Nodal'
        >>> pfield.location
        'Nodal'
        
        """
        if self.scoping:
            self.scoping.location = value
        else:
            raise Exception("Property field location is based on scoping, and scoping is not defined")
            
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
        local_field : PropertyField
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities = 5
        >>> field_to_local = dpf.PropertyField(num_entities, dpf.natures.scalar)
        >>> with field_to_local.as_local_field() as f:    
        ...     for i in range(1,num_entities+1):
        ...         f.append(list(range(i,i+3)),i)
        ...         f.get_entity_data(i-1)
        array([1, 2, 3])
        array([2, 3, 4])
        array([3, 4, 5])
        array([4, 5, 6])
        array([5, 6, 7])
        
        """
        return _LocalPropertyField(self)  


class _LocalPropertyField(_LocalFieldBase,PropertyField):
    """Class only created by a field to cache the internal data of the field,
    modify it locallly, and send a single update request to the server 
    when the local field is deleted
    
    Parameters
    ----------
    field : PropertyField
        property field to copy

    """
    
    def __init__(self, field):
        super().__init__(field)
        