"""
.. _ref_any:

Any
====================
"""
import traceback
import warnings

import ansys.dpf.core.server_types
from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.core.common import type_to_internal_object_keyword
from ansys.dpf.gate import any_abstract_api


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
        self._server = server_module.get_or_create_server(server)

        if any_dpf is None and not self._server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        self._api_instance = None

        # step 2: if object exists, take the instance, else create it
        if any_dpf is not None:
            self._internal_obj = any_dpf

        self._api.init_any_environment(self)  # creates stub when gRPC

        self._internal_type = None
        self._get_as_method = None

    @staticmethod
    def _type_to_new_from_get_as_method(any_dpf):
        from ansys.dpf.core import (
            field,
            property_field,
            generic_data_container,
            string_field,
            scoping,
            data_tree,
        )

        return [
            (
                int,
                any_dpf._api.any_new_from_int,
                any_dpf._api.any_get_as_int,
                any_dpf._api.any_new_from_int_on_client,
            ),
            (
                str,
                any_dpf._api.any_new_from_string,
                any_dpf._api.any_get_as_string,
                any_dpf._api.any_new_from_string_on_client,
            ),
            (
                float,
                any_dpf._api.any_new_from_double,
                any_dpf._api.any_get_as_double,
                any_dpf._api.any_new_from_double_on_client,
            ),
            (field.Field, any_dpf._api.any_new_from_field, any_dpf._api.any_get_as_field),
            (
                property_field.PropertyField,
                any_dpf._api.any_new_from_property_field,
                any_dpf._api.any_get_as_property_field,
            ),
            (
                string_field.StringField,
                any_dpf._api.any_new_from_string_field,
                any_dpf._api.any_get_as_string_field,
            ),
            (
                generic_data_container.GenericDataContainer,
                any_dpf._api.any_new_from_generic_data_container,
                any_dpf._api.any_get_as_generic_data_container,
            ),
            (
                scoping.Scoping,
                any_dpf._api.any_new_from_scoping,
                any_dpf._api.any_get_as_scoping,
            ),
            (
                data_tree.DataTree,
                any_dpf._api.any_new_from_data_tree,
                any_dpf._api.any_get_as_data_tree,
            ),
        ]

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

        innerServer = server if server is not None else obj._server

        if not innerServer.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        any_dpf = Any(server=innerServer)

        for type_tuple in Any._type_to_new_from_get_as_method(any_dpf):
            if isinstance(obj, type_tuple[0]):
                # call respective new_from function
                if isinstance(server, ansys.dpf.core.server_types.InProcessServer) or not (
                    isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, float)
                ):
                    any_dpf._internal_obj = type_tuple[1](obj)
                else:
                    any_dpf._internal_obj = type_tuple[3](innerServer.client, obj)
                # store get_as & type for casting back to original type
                any_dpf._internal_type = type_tuple[0]
                any_dpf._get_as_method = type_tuple[2]

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

        for type_tuple in Any._type_to_new_from_get_as_method(self):
            if self._internal_type == type_tuple[0]:
                # call the get_as function for the appropriate type
                internal_obj = type_tuple[2](self)
                if (
                    self._internal_type is int
                    or self._internal_type is str
                    or self._internal_type is float
                ):
                    obj = internal_obj
                else:
                    # get current type's constructors' variable keyword for passing the internal_obj
                    internal_obj_keyword = type_to_internal_object_keyword()[type_tuple[0]]

                    # wrap parameters in a dictionary for parameters expansion when calling
                    # constructor
                    keyword_args = {internal_obj_keyword: internal_obj, "server": self._server}
                    # call constructor
                    obj = type_tuple[0](**keyword_args)

                return obj

        raise TypeError(f"{output_type} is not currently supported by the Any class.")

    def __del__(self):
        try:
            if hasattr(self, "_deleter_func"):
                obj = self._deleter_func[1](self)
                if obj is not None:
                    self._deleter_func[0](obj)
        except Exception:
            warnings.warn(traceback.format_exc())
