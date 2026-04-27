# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Support."""

import traceback
import warnings

from ansys.dpf.core import collection_base, server as server_module
from ansys.dpf.core.check_version import version_requires
from ansys.dpf.gate import support_capi, support_grpcapi


class Support:
    """Base class for support (supporting Field's location, Scoping's location, Collection's labels...).

    Field, PropertyField and StringField support can be accessed generically via this base class.

    Parameters
    ----------
    support : ctypes.c_void_p, ansys.grpc.dpf.support_pb2.Support
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Create a time frequency support from a model.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = Model(transient)
    >>> time_freq_support = model.metadata.time_freq_support # printable
    >>> time_freq_support.available_field_supported_properties()
    ['time_freqs']
    >>> field = time_freq_support.field_support_by_property("time_freqs")

    """

    def __init__(self, support, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            support._server if isinstance(support, Support) else server
        )

        if not self._server.meet_version("3.0"):  # pragma: no cover
            return

        # step 2: get api
        self._support_api = self._server.get_api_for_type(
            capi=support_capi.SupportCAPI, grpcapi=support_grpcapi.SupportGRPCAPI
        )

        # step3: init environment
        self._support_api.init_support_environment(self)  # creates stub when gRPC

        # step4: take instance:
        # object_name -> protobuf.message, DPFObject*
        self._internal_obj = support

    @version_requires("5.0")
    def field_support_by_property(self, property_name: str):
        """Return a Field supporting (describing) a given property.

        Returns
        -------
        Field

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.field import Field

        out = self._support_api.support_get_field_support_by_property(self, property_name)
        if out is not None:
            return Field(field=out, server=self._server)

    @version_requires("5.0")
    def prop_field_support_by_property(self, property_name: str):
        """Return a PropertyField supporting (describing) a given property.

        Returns
        -------
        PropertyField

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.property_field import PropertyField

        out = self._support_api.support_get_property_field_support_by_property(self, property_name)
        if out is not None:
            return PropertyField(property_field=out, server=self._server)

    @version_requires("5.0")
    def string_field_support_by_property(self, property_name: str):
        """Return a StringField supporting (describing) a given property.

        Returns
        -------
        StringField

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.string_field import StringField

        out = self._support_api.support_get_string_field_support_by_property(self, property_name)
        if out is not None:
            return StringField(string_field=out, server=self._server)

    @version_requires("5.0")
    def available_field_supported_properties(self):
        """Return the list of property names supported by a Field.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection_base.StringCollection(
            collection=self._support_api.support_get_property_names_as_string_coll_for_fields(self),
            server=self._server,
        )
        return coll_obj.get_integral_entries()

    @version_requires("5.0")
    def available_prop_field_supported_properties(self):
        """Return the list of property names supported by a PropertyField.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection_base.StringCollection(
            collection=self._support_api.support_get_property_names_as_string_coll_for_property_fields(  # noqa: E501
                self
            ),
            server=self._server,
        )
        return coll_obj.get_integral_entries()

    @version_requires("5.0")
    def available_string_field_supported_properties(self):
        """Return the list of property names supported by a StringField.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection_base.StringCollection(
            collection=self._support_api.support_get_property_names_as_string_coll_for_string_fields(  # noqa: E501
                self
            ),
            server=self._server,
        )
        return coll_obj.get_integral_entries()

    @version_requires("12.0")
    def get_type(self) -> str:
        """Type of the support as a string.

        Returns
        -------
        out_type : str
            Type of the support as a string
        """
        out_type = ""
        self._support_api.support_get_type(self, out_type)
        return out_type

    @version_requires("12.0")
    def get_as_time_freq_support(self) -> "time_freq_support.TimeFreqSupport":
        """Get the support as a TimeFreqSupport object.

        Returns
        -------
        TimeFreqSupport : TimeFreqSupport
            TimeFreqSupport object
        """
        from ansys.dpf.core import time_freq_support

        tfsp = time_freq_support.TimeFreqSupport(
            time_freq_support=self._support_api.support_get_as_time_freq_support(self),
            server=self._server,
        )
        return tfsp

    @version_requires("12.0")
    def get_as_meshed_region(self) -> "meshed_region.MeshedRegion":
        """Get the support as a MeshedRegion object.

        Returns
        -------
        MeshedRegion : MeshedRegion
            MeshedRegion object
        """
        from ansys.dpf.core import meshed_region

        mesh = meshed_region.MeshedRegion(
            mesh=self._support_api.support_get_as_meshed_support(self), server=self._server
        )
        return mesh

    @version_requires("12.0")
    def get_as_cyclic_support(self) -> "cyclic_support.CyclicSupport":
        """Get the support as a CyclicSupport object.

        Returns
        -------
        CyclicSupport : CyclicSupport
            CyclicSupport object
        """
        from ansys.dpf.core import cyclic_support

        cyclic = cyclic_support.CyclicSupport(
            cyclic_support=self._support_api.support_get_as_cyclic_support(self),
            server=self._server,
        )
        return cyclic

    @version_requires("12.0")
    def get_as_generic_support(self) -> "generic_support.GenericSupport":
        """Get the support as a GenericSupport object.

        Returns
        -------
        GenericSupport : GenericSupport
            GenericSupport object
        """
        from ansys.dpf.core import generic_support

        generic = generic_support.GenericSupport(
            generic_support=self._support_api.support_get_as_generic_support(self),
            server=self._server,
        )
        return generic

    def __del__(self):
        """
        Clean up resources associated with the instance.

        This method calls the deleter function to release resources. If an exception
        occurs during deletion, a warning is issued.

        Raises
        ------
        Warning
            If an exception occurs while attempting to delete resources.
        """
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
