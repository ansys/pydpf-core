# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""StringField."""

from typing import List

import numpy as np

from ansys.dpf.core import errors, scoping, server as server_module
from ansys.dpf.core.common import _get_size_of_list, locations, natures
from ansys.dpf.core.field_base import _FieldBase
from ansys.dpf.gate import (
    dpf_vector,
    integral_types,
    string_field_abstract_api,
    string_field_capi,
    string_field_grpcapi,
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
    Class available with server's version starting at 5.0 (Ansys 2023R1).
    """

    def __init__(
        self,
        nentities=0,
        string_field=None,
        server=None,
    ):
        self._server = server_module.get_or_create_server(
            string_field._server if isinstance(string_field, StringField) else server
        )
        if string_field is None and not self._server.meet_version("5.0"):
            raise errors.DpfVersionNotSupported("5.0")
        super().__init__(
            nentities=nentities,
            nature=natures.scalar,
            field=string_field,
            server=server,
        )

    @property
    def _api(self) -> string_field_abstract_api.StringFieldAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=string_field_capi.StringFieldCAPI,
                grpcapi=string_field_grpcapi.StringFieldGRPCAPI,
            )
        return self._api_instance

    def _init_api_env(self):
        self._api.init_string_field_environment(self)

    @staticmethod
    def _field_create_internal_obj(
        api: string_field_abstract_api.StringFieldAbstractAPI,
        client,
        nature,
        nentities,
        location=locations.nodal,
        ncomp_n=0,
        ncomp_m=0,
        with_type=None,
    ):
        if client is not None:
            return api.csstring_field_new_on_client(client, nentities, nentities)
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
            Location string in :class:`ansys.dpf.core.locations`.

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
        """Return the number of component, always 1."""
        return 1

    @property
    def elementary_data_count(self):
        """Return elementary data count."""
        return self._api.csstring_field_get_data_size(self)

    @property
    def size(self):
        """Return elementary data size."""
        return self._api.csstring_field_get_data_size(self)

    def _set_scoping(self, scoping):
        self._api.csstring_field_set_cscoping(self, scoping)

    def _get_scoping(self):
        return scoping.Scoping(
            scoping=self._api.csstring_field_get_cscoping(self), server=self._server
        )

    def get_entity_data(self, index):
        """Return entity data."""
        try:
            vec = dpf_vector.DPFVectorString(owner=self)
            self._api.csstring_field_get_entity_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, index
            )
            return vec
        except NotImplementedError:
            data = self._api.csstring_field_get_entity_data(self, index)
            return data

    def get_entity_data_by_id(self, id):
        """Return entity data corresponding to the provided id."""
        try:
            vec = dpf_vector.DPFVectorString(owner=self)
            self._api.csstring_field_get_entity_data_by_id_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, id
            )
            return vec
        except NotImplementedError:
            index = self.scoping.index(id)
            if index < 0:
                raise ValueError(f"The ID {id} must be greater than 0.")
            data = self.get_entity_data(index)
            return data

    def append(self, data: List[str], scopingid: int):
        """
        Append data to the string field.

        This method appends data to the string field for a specific scoping ID.
        """
        string_list = integral_types.MutableListString(data)
        self._api.csstring_field_push_back(self, scopingid, _get_size_of_list(data), string_list)

    def _get_data(self, np_array=True):
        try:
            vec = dpf_vector.DPFVectorString(owner=self)
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
                and data.size // self.component_count != data.size / self.component_count
            ):
                raise ValueError(
                    f"An array of shape {self.shape} is expected and "
                    f"shape {data.shape} was input"
                )
        string_list = integral_types.MutableListString(data)
        return self._api.csstring_field_set_data(self, _get_size_of_list(data), string_list)
