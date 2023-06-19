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

class Any:
    """Common wrapper representing any supported DPF Data Types.

    Parameters
    ----------
    any : ctypes.c_void_p, ansys.grpc.dpf.any_pb2.Any message, optional  # noqa: E501
    server : DPFServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Class available with server's version starting at 6.2 (Ansys 2024R1).
    """

    def __init__(self, any=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if any is None and not self._server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        self._api_instance = None

        # step 2: if object exists, take the instance, else create it
        if any is not None:
            self._internal_obj = any

        self._api.init_any_environment(self)  # creates stub when gRPC

        self._internal_type = None
        self._get_as_method = None

    @staticmethod
    def _type_to_new_from_get_as_method(any):
        from ansys.dpf.core import field, property_field, generic_data_container, string_field, \
            scoping

        return [
            (
                int,
                any._api.any_new_from_int,
                any._api.any_get_as_int,
                any._api.any_new_from_int_on_client,
            ),
            (
                str,
                any._api.any_new_from_string,
                any._api.any_get_as_string,
                any._api.any_new_from_string_on_client,
            ),
            (
                float,
                any._api.any_new_from_double,
                any._api.any_get_as_double,
                any._api.any_new_from_double_on_client,
            ),
            (field.Field, any._api.any_new_from_field, any._api.any_get_as_field),
            (
                property_field.PropertyField,
                any._api.any_new_from_property_field,
                any._api.any_get_as_property_field,
            ),
            (
                string_field.StringField,
                any._api.any_new_from_string_field,
                any._api.any_get_as_string_field,
            ),
            (
                generic_data_container.GenericDataContainer,
                any._api.any_new_from_generic_data_container,
                any._api.any_get_as_generic_data_container,
            ),
            (
                scoping.Scoping,
                any._api.any_new_from_scoping,
                any._api.any_get_as_scoping,
            )
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

        any = Any(server=innerServer)

        for type_tuple in Any._type_to_new_from_get_as_method(any):
            if isinstance(obj, type_tuple[0]):
                # call respective new_from function
                if isinstance(server, ansys.dpf.core.server_types.InProcessServer) or not (
                        isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, float)
                ):
                    any._internal_obj = type_tuple[1](obj)
                else:
                    any._internal_obj = type_tuple[3](innerServer.client, obj)
                # store get_as & type for casting back to original type
                any._internal_type = type_tuple[0]
                any._get_as_method = type_tuple[2]

                return any

        raise TypeError(f"{obj.__class__} is not currently supported by the Any class.")

    @property
    def _api(self):
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
        except:
            warnings.warn(traceback.format_exc())
