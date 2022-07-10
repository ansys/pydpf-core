"""
PropertyField
=============
"""

from ansys.dpf.core.common import locations, natures
from ansys.dpf.core.field_base import _FieldBase, _LocalFieldBase


class PropertyField(_FieldBase):
    """Describes field properties such as connectivity.

    This class is a field with integer values instead of double values.

    Parameters
    ----------
    nentities: int
        Number of entities that the property field is to contain. The
        default is ``0``.
    nature: core.natures
        Nature of the property field, such as scalar or vector.
    location : str, optional
        Location of the property field. Options are ``"Nodal"`` or ``"Elemental"``.
        The default is ``"Nodal"``.
    property field : str, optional
        Name of the property field. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

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

    def __init__(
        self,
        nentities=0,
        nature=natures.scalar,
        location=locations.nodal,
        property_field=None,
        server=None,
    ):
        super().__init__(nentities, nature, location, True, property_field, server)

    @property
    def location(self):
        """Location of the property field.

        A property field contains a scoping, which is the location that is read.
        To update location, directly update the scoping location.

        Returns
        -------
        location : str
            Location string, which is either ``"Nodal"`` or ``"Elemental"``.

        Examples
        --------
        Create a property field and request the location.

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
            Location string, which is either ``"Nodal"`` or ``"Elemental"``.

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
            raise Exception(
                "Property field location is based on scoping, and scoping is not defined"
            )

    def as_local_field(self):
        """Create a deep copy of the field locally.

        This copy can then be accessed and modified locally, without a request
        being sent to the server. This method should be used in a ``with``
        statement so that the local field is released and the data is sent to
        the server in one action. If it's not used in a ``with`` statement, the
        method ``release_data()`` should be used to actually update the field.

        .. warning::
           If this ``as_local_field`` method is not used as a context manager in a
           `with` statement or if the method ``release_data()`` is not called,
           the data will not actually be updated.

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
        ...         print(f.get_entity_data(i-1))
        [1 2 3]
        [2 3 4]
        [3 4 5]
        [4 5 6]
        [5 6 7]


        """
        return _LocalPropertyField(self)


class _LocalPropertyField(_LocalFieldBase, PropertyField):
    """Caches the internal data of a field so that it can be modified locally.

    A single update request is sent to the server when the local field is deleted.

    Parameters
    ----------
    field : PropertyField
        Property field to copy.
    """

    def __init__(self, field):
        super().__init__(field)
