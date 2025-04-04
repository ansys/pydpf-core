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

"""GenericSupport."""

from ansys.dpf.core import errors, field, property_field, string_field
from ansys.dpf.core.support import Support
from ansys.dpf.gate import generic_support_capi, generic_support_grpcapi


class GenericSupport(Support):
    """Can support a location or label to describe its domain with its scope and properties.

    Parameters
    ----------
    generic_support : ctypes.c_void_p, ansys.grpc.dpf.tgeneric_support_pb2.GenericSupport
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Create a generic support.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import GenericSupport
    >>> support = GenericSupport("phase")
    >>> field = dpf.Field(location="phase", nature=dpf.natures.scalar)
    >>> support.set_support_of_property("viscosity", field)
    >>> field = dpf.StringField()
    >>> support.set_support_of_property("names", field)
    >>> field = dpf.PropertyField(location="phase", nature=dpf.natures.scalar)
    >>> support.set_support_of_property("type", field)
    >>> support.available_field_supported_properties()
    ['viscosity']
    >>> support.available_string_field_supported_properties()
    ['names']
    >>> support.available_prop_field_supported_properties()
    ['type']
    >>> field = support.field_support_by_property("viscosity")

    Notes
    -----
    Class available with server's version starting at 5.0 (Ansys 2023R1).
    """

    def __init__(self, name: str = "", generic_support=None, server=None):
        super(GenericSupport, self).__init__(support=generic_support, server=server)

        if not self._server.meet_version("5.0"):
            raise errors.DpfVersionNotSupported("5.0")

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=generic_support_capi.GenericSupportCAPI,
            grpcapi=generic_support_grpcapi.GenericSupportGRPCAPI,
        )

        # step3: init environment
        self._api.init_generic_support_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if generic_support is not None:
            self._internal_obj = generic_support
        else:
            if self._server.has_client():
                self._internal_obj = self._api.generic_support_new_on_client(
                    self._server.client, name
                )
            else:
                self._internal_obj = self._api.generic_support_new(name)

    def set_support_of_property(self, property_name: str, field_support) -> None:
        """Support a Property by Field data.

        Parameters
        ----------
        property_name: str
            Name of the Property.

        field_support: Field, PropertyField, StringField
            Data supporting this property.
        """
        if isinstance(field_support, field.Field):
            self._api.generic_support_set_field_support_of_property(
                self, property_name, field_support
            )
        elif isinstance(field_support, property_field.PropertyField):
            self._api.generic_support_set_property_field_support_of_property(
                self, property_name, field_support
            )
        elif isinstance(field_support, string_field.StringField):
            self._api.generic_support_set_string_field_support_of_property(
                self, property_name, field_support
            )
        else:
            raise TypeError("Field, PropertyField or StringField is expected")
