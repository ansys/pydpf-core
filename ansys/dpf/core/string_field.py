"""
StringField
===========
"""

import numpy as np
from ansys.dpf.core.common import natures, locations, _get_size_of_list
from ansys.dpf.core import scoping
from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.core.field_base import _FieldBase
from ansys.dpf.gate import (
    string_field_abstract_api,
    string_field_capi,
    string_field_grpcapi,
    dpf_vector,
    integral_types
)


class StringField(_FieldBase):
    """Describes string data scoped on entities such as names.

    This class is a field with string values instead of double values.

    Parameters
    ----------
    nentities: int
        Number of entities that the string field is to contain (reserved). The
        default is ``0``.
    string_field : Field, ansys.grpc.dpf.field_pb2.Field, ctypes.c_void_p, optional
        Field message generated from a gRPC stub, or returned by DPF's C clients.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> pfield = dpf.StringField()
    >>> list_ids = [1, 2, 4, 6, 7]
    >>> scop = dpf.Scoping(ids = list_ids, location = dpf.locations.nodal)
    >>> pfield.scoping = scop
    >>> list_data = ["water", "oil", "gaz", "paint", "air"]
    >>> pfield.data = list_data

    Notes
    -----
    Class available with server's version starting at 5.0.
    """

    def __init__(
        self,
        nentities=0,
        string_field=None,
        server=None,
    ):
        self._server = server_module.get_or_create_server(server)
        if string_field is None and not self._server.meet_version("5.0"):
            raise errors.DpfVersionNotSupported("5.0")
        super().__init__(nentities, nature=natures.scalar, field=string_field, server=server)

    @property
    def _api(self) -> string_field_abstract_api.StringFieldAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=string_field_capi.StringFieldCAPI,
                grpcapi=string_field_grpcapi.StringFieldGRPCAPI
            )
        return self._api_instance

    @staticmethod
    def _field_create_internal_obj(api: string_field_abstract_api.StringFieldAbstractAPI,
                                   client, nature, nentities,
                                   location=locations.nodal, ncomp_n=0, ncomp_m=0):
        if client is not None:
            return api.csstring_field_new_on_client(
                client, nentities, nentities
            )
        else:
            return api.csstring_field_new(nentities, nentities)

    @property
    def location(self):
        """Location of the string field.

        A property field contains a scoping, which is the location that is read.
        To update location, directly update the scoping location.

        Returns
        -------
        location : str
            Location string, can be found in ``dpf.locations``: ie.
            ``dpf.locations.nodal`` or ``dpf.locations.elemental``.

        Examples
        --------
        Create a string field and request the location.

        >>> from ansys.dpf import core as dpf
        >>> pfield = dpf.StringField()
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
        >>> pfield = dpf.StringField()
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
        return 1

    @property
    def elementary_data_count(self):
        return self._api.csstring_field_get_data_size(self)

    @property
    def size(self):
        return self._api.csstring_field_get_data_size(self)

    def _set_scoping(self, scoping):
        self._api.csstring_field_set_cscoping(self, scoping)

    def _get_scoping(self):
        return scoping.Scoping(
            scoping=self._api.csstring_field_get_cscoping(self),
            server=self._server
        )

    def get_entity_data(self, index):
        try:
            vec = dpf_vector.DPFVectorString(client=self._server.client)
            self._api.csstring_field_get_entity_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, index
            )
            return vec
        except NotImplementedError:
            data = self._api.csstring_field_get_entity_data(self, index)
            return data

    def get_entity_data_by_id(self, id):
        try:
            vec = dpf_vector.DPFVectorString(client=self._server.client)
            self._api.csstring_field_get_entity_data_by_id_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, id)
            return vec
        except NotImplementedError:
            index = self.scoping.index(id)
            if index < 0:
                raise ValueError(f"The ID {id} must be greater than 0.")
            data = self.get_entity_data(index)
            return data

    def append(self, data, scopingid):
        string_list = integral_types.MutableListString(data)
        self._api.csstring_field_push_back(self, scopingid, _get_size_of_list(data), string_list)

    def _get_data(self, np_array=True):
        try:
            vec = dpf_vector.DPFVectorString(client=self._server.client)
            self._api.csstring_field_get_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return vec
        except NotImplementedError:
            data = self._api.csstring_field_get_data(self, np_array)
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
        string_list = integral_types.MutableListString(data)
        return self._api.csstring_field_set_data(self, _get_size_of_list(data), string_list)
