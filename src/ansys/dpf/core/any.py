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

"""
Any.

Module containing the wrapper class representing all supported DPF datatypes.
"""

import traceback
import warnings

import numpy as np

from ansys.dpf.core import errors, server as server_module
from ansys.dpf.core.check_version import server_meet_version, server_meet_version_and_raise
from ansys.dpf.core.common import create_dpf_instance
import ansys.dpf.core.server_types
from ansys.dpf.gate import any_abstract_api, dpf_vector, integral_types


class Any:
    """Common wrapper representing any supported DPF Data Types.

    Parameters
    ----------
    any_dpf : ctypes.c_void_p, ansys.grpc.dpf.any_pb2.Any message, optional
    server : DPFServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Class available with server's version starting at 7.0 (Ansys 2024 R1 pre0).
    """

    def __init__(self, any_dpf=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            any_dpf._server if isinstance(any_dpf, Any) else server
        )

        if any_dpf is None and not self._server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        self._api_instance = None

        # step 2: if object exists, take the instance, else create it
        if any_dpf is not None:
            self._internal_obj = any_dpf

        self._api.init_any_environment(self)  # creates stub when gRPC

        self._internal_type = None
        self._get_as_method = None

    def _new_from_string(self, str):
        return self._new_from_string_as_bytes(str.encode("utf-8"))

    @staticmethod
    def _get_as_string(self):
        out = Any._get_as_string_as_bytes(self)
        if out is not None and not isinstance(out, str):
            return out.decode("utf-8")
        return out

    @staticmethod
    def _get_as_string_as_bytes(self):
        if server_meet_version("8.0", self._server):
            size = integral_types.MutableUInt64(0)
            return self._api.any_get_as_string_with_size(self, size)
        else:
            return self._api.any_get_as_string(self)

    def _new_from_string_on_client(self, client, str):
        return self._new_from_string_as_bytes_on_client(client, str.encode("utf-8"))

    def _new_from_string_as_bytes(self, str):
        if server_meet_version("8.0", self._server):
            size = integral_types.MutableUInt64(len(str))
            return self._api.any_new_from_string_with_size(str, size)
        else:
            return self._api.any_new_from_string(str)

    def _new_from_string_as_bytes_on_client(self, client, str):
        if server_meet_version("8.0", self._server):
            size = integral_types.MutableUInt64(len(str))
            return self._api.any_new_from_string_with_size_on_client(client, str, size)
        else:
            return self._api.any_new_from_string_on_client(client, str)

    def _type_to_new_from_get_as_method(self, obj):
        from ansys.dpf.core import (
            collection,
            custom_type_field,
            data_tree,
            dpf_operator,
            field,
            fields_container,
            generic_data_container,
            property_field,
            scoping,
            string_field,
            workflow,
        )

        if issubclass(obj, int):
            return (
                self._api.any_new_from_int,
                self._api.any_get_as_int,
                self._api.any_new_from_int_on_client,
            )
        elif issubclass(obj, str):
            return (
                self._new_from_string,
                self._get_as_string,
                self._new_from_string_on_client,
            )
        elif issubclass(obj, float):
            return (
                self._api.any_new_from_double,
                self._api.any_get_as_double,
                self._api.any_new_from_double_on_client,
            )
        elif issubclass(obj, bytes):
            return (
                self._new_from_string_as_bytes,
                self._get_as_string_as_bytes,
                self._new_from_string_as_bytes_on_client,
            )
        elif issubclass(obj, field.Field):
            return self._api.any_new_from_field, self._api.any_get_as_field
        elif issubclass(obj, property_field.PropertyField):
            return (
                self._api.any_new_from_property_field,
                self._api.any_get_as_property_field,
            )
        elif issubclass(obj, fields_container.FieldsContainer):
            return (
                self._api.any_new_from_fields_container,
                self._api.any_get_as_fields_container,
            )
        elif issubclass(obj, string_field.StringField):
            return (
                self._api.any_new_from_string_field,
                self._api.any_get_as_string_field,
            )
        elif issubclass(obj, generic_data_container.GenericDataContainer):
            return (
                self._api.any_new_from_generic_data_container,
                self._api.any_get_as_generic_data_container,
            )
        elif issubclass(obj, scoping.Scoping):
            return (
                self._api.any_new_from_scoping,
                self._api.any_get_as_scoping,
            )
        elif issubclass(obj, data_tree.DataTree):
            return (
                self._api.any_new_from_data_tree,
                self._api.any_get_as_data_tree,
            )
        elif issubclass(obj, custom_type_field.CustomTypeField):
            return (
                self._api.any_new_from_custom_type_field,
                self._api.any_get_as_custom_type_field,
            )
        elif issubclass(obj, collection.Collection):
            return (
                self._api.any_new_from_any_collection,
                self._api.any_get_as_any_collection,
            )
        elif issubclass(obj, workflow.Workflow):
            return (
                self._api.any_new_from_workflow,
                self._api.any_get_as_workflow,
            )
        elif issubclass(obj, dpf_vector.DPFVectorInt):
            return (
                self._api.any_new_from_int_collection,
                self._api.any_get_as_int_collection,
            )
        elif issubclass(obj, dpf_operator.Operator):
            return (
                self._api.any_new_from_operator,
                self._api.any_get_as_operator,
            )

    @staticmethod
    def new_from(obj, server=None):
        """Return an Any instance from the given object.

        Parameters
        ----------
        obj : Object wrap as an Any

        Returns
        -------
        any : Any
            Wrapped any type.
        """
        inner_server = server if server is not None else obj._server

        if not inner_server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        any_dpf = Any(server=inner_server)

        type_tuple = any_dpf._type_to_new_from_get_as_method(type(obj))
        if type_tuple is not None:
            # call respective new_from function
            if isinstance(server, ansys.dpf.core.server_types.InProcessServer) or not (
                isinstance(obj, (int, str, float, bytes))
            ):
                any_dpf._internal_obj = type_tuple[0](obj)
            else:
                any_dpf._internal_obj = type_tuple[2](inner_server.client, obj)
            # store get_as & type for casting back to original type
            any_dpf._internal_type = type(obj)
            any_dpf._get_as_method = type_tuple[1]

            return any_dpf
        elif isinstance(obj, (list, np.ndarray)):
            type_tuple = any_dpf._type_to_new_from_get_as_method(dpf_vector.DPFVectorInt)
            from ansys.dpf.core import collection

            if server_meet_version_and_raise(
                "9.0",
                inner_server,
                "Creating an Any from a list is only supported "
                "with"
                "server versions starting at 9.0",
            ):
                inpt = collection.CollectionBase.integral_collection(obj, inner_server)
                any_dpf._internal_obj = type_tuple[0](inpt)
                any_dpf._internal_type = dpf_vector.DPFVectorInt
                any_dpf._get_as_method = type_tuple[1]
                return any_dpf

        raise TypeError(f"{obj.__class__} is not currently supported by the Any class.")

    @property
    def _api(self) -> any_abstract_api.AnyAbstractAPI:
        from ansys.dpf.gate import any_capi, any_grpcapi

        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=any_capi.AnyCAPI, grpcapi=any_grpcapi.AnyGRPCAPI
            )

        return self._api_instance

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def cast(self, output_type=None):
        """Cast the Any back to its original type.

        Parameters
        ----------
        output_type: output_type, optional
            Used when the Any instance was retrieved from the server.
            Not necessary when the instance was created using the
            :func:`ansys.dpf.core.Any.new_from`

        Returns
        -------
        type
            Original object instance
        """
        self._internal_type = output_type if output_type is not None else self._internal_type

        type_tuple = self._type_to_new_from_get_as_method(self._internal_type)
        if type_tuple is not None:
            internal_obj = type_tuple[1](self)
            if (
                self._internal_type is int
                or self._internal_type is str
                or self._internal_type is float
                or self._internal_type is bytes
            ):
                obj = internal_obj
            else:
                return create_dpf_instance(self._internal_type, internal_obj, self._server)

            return obj

        raise TypeError(f"{output_type} is not currently supported by the Any class.")

    def __del__(self):
        """Delete the entry."""
        try:
            if hasattr(self, "_deleter_func"):
                obj = self._deleter_func[1](self)
                if obj is not None:
                    self._deleter_func[0](obj)
        except Exception:
            warnings.warn(traceback.format_exc())
