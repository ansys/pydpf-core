"""
PropertyField
=============
"""

import numpy as np
from ansys.dpf.core.common import natures, locations, _get_size_of_list
from ansys.dpf.core import scoping, dimensionality
from ansys.dpf.core.field_base import _FieldBase, _LocalFieldBase
from ansys.dpf.gate import (
    property_field_abstract_api,
    property_field_capi,
    property_field_grpcapi,
    dpf_array,
    dpf_vector
)


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
    property field : Field, ansys.grpc.dpf.field_pb2.Field, ctypes.c_void_p, optional
        Field message generated from a gRPC stub, or returned by DPF's C clients.
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
        super().__init__(nentities, nature, location, property_field, server)

    @property
    def _api(self) -> property_field_abstract_api.PropertyFieldAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=property_field_capi.PropertyFieldCAPI,
                grpcapi=property_field_grpcapi.PropertyFieldGRPCAPI
            )
        return self._api_instance

    @staticmethod
    def _field_create_internal_obj(api: property_field_abstract_api.PropertyFieldAbstractAPI,
                                   client, nature, nentities,
                                   location=locations.nodal, ncomp_n=0, ncomp_m=0):
        dim = dimensionality.Dimensionality([ncomp_n, ncomp_m], nature)
        if client is not None:
            return api.csproperty_field_new_on_client(
                client, nentities, nentities*dim.component_count
            )
        else:
            return api.csproperty_field_new(nentities, nentities * dim.component_count)

    @property
    def location(self):
        """Location of the property field.

        A property field contains a scoping, which is the location that is read.
        To update location, directly update the scoping location.

        Returns
        -------
        location : str
            Location string, can be found in ``dpf.locations``: ie.
            ``dpf.locations.nodal`` or ``dpf.locations.elemental``.

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

    @property
    def component_count(self):
        return self._api.csproperty_field_elementary_data_size(self)

    @property
    def elementary_data_count(self):
        return self._api.csproperty_field_get_number_elementary_data(self)

    @property
    def size(self):
        return self._api.csproperty_field_get_data_size(self)

    def _set_scoping(self, scoping):
        self._api.csproperty_field_set_cscoping(self, scoping)

    def _get_scoping(self):
        return scoping.Scoping(
            scoping=self._api.csproperty_field_get_cscoping(self),
            server=self._server
        )

    def get_entity_data(self, index):
        try:
            vec = dpf_vector.DPFVectorInt(client=self._server.client)
            self._api.csproperty_field_get_entity_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, index
            )
            data = dpf_array.DPFArray(vec)

        except NotImplementedError:
            data = self._api.csproperty_field_get_entity_data(self, index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def get_entity_data_by_id(self, id):
        try:
            vec = dpf_vector.DPFVectorInt(client=self._server.client)
            self._api.csproperty_field_get_entity_data_by_id_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, id)
            data = dpf_array.DPFArray(vec)
        except NotImplementedError:
            index = self.scoping.index(id)
            if index < 0:
                raise ValueError(f"The ID {id} must be greater than 0.")
            data = self.get_entity_data(index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def append(self, data, scopingid):
        self._api.csproperty_field_push_back(self, scopingid, _get_size_of_list(data), data)

    def _get_data_pointer(self):
        try:
            vec = dpf_vector.DPFVectorInt(client=self._server.client)
            self._api.csproperty_field_get_data_pointer_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return dpf_array.DPFArray(vec)

        except NotImplementedError:
            return self._api.csproperty_field_get_data_pointer(self, True)

    def _set_data_pointer(self, data):
        return self._api.csproperty_field_set_data_pointer(self, _get_size_of_list(data), data)

    def _get_data(self, np_array=True):
        try:
            vec = dpf_vector.DPFVectorInt(client=self._server.client)
            self._api.csproperty_field_get_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            data = dpf_array.DPFArray(vec) if np_array else dpf_array.DPFArray(vec).tolist()
        except NotImplementedError:
            data = self._api.csproperty_field_get_data(self, np_array)
        n_comp = self.component_count
        if np_array and n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def _set_data(self, data):
        if isinstance(data, (np.ndarray, np.generic)):
            if (
                    0 != self.size
                    and self.component_count > 1
                    and data.size // self.component_count
                    != data.size / self.component_count
            ):
                raise ValueError(
                    f"An array of shape {self.shape} is expected and "
                    f"shape {data.shape} was input"
                )

            if data.dtype != np.int32:
                copy = np.empty_like(data, shape=data.shape, dtype=np.int32)
                copy[:] = data
                data = copy
        return self._api.csproperty_field_set_data(self, _get_size_of_list(data), data)

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
        self._is_property_field = True
        PropertyField.__init__(self, property_field=field)
        _LocalFieldBase.__init__(self, field)
