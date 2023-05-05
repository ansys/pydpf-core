"""
.. _ref_any:

Any
====================
"""
import traceback
import warnings

from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.gate import (
    any_abstract_api,
    any_capi,
    any_grpcapi
)


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
    Class available with server's version starting at 6.2 (Ansys 2023R2).
    """

    def __init__(self, any=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if not self._server.meet_version("6.2"):
            raise errors.DpfVersionNotSupported("6.2")

        # step 2: get api
        self._api_instance = self._server.get_api_for_type(
            capi=any_capi.AnyCAPI,
            grpcapi=any_grpcapi.AnyGRPCAPI
        )

        # step3: init environment
        self._api.init_any_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it

        # self._internal_obj = generic_data_container
        if any is not None:
            self._internal_obj = any
        # else:
        #     if self._server.has_client():
        #         self._internal_obj = self._api.generic_data_container_new_on_client(
        #             self._server.client
        #         )
        #     else:
        #         self._internal_obj = self._api.generic_data_container_new()

    @property
    def _api(self) -> any_abstract_api.AnyAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=any_capi.AnyCAPI,
                grpcapi=any_grpcapi.AnyGRPCAPI
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

    def cast(self, output_type):
        """TODO: document"""
        for type_tuple in self._type_to_get_as_method:
            if isinstance(output_type, type_tuple):
                return type_tuple[1](self)

    def _type_to_get_as_method(self):
        """TODO: document"""
        from ansys.dpf.core import (
            field,
            property_field,
            generic_data_container,
            string_field
        )

        return [(str, self._api.any_wrapped_type_string),
                (field.Field, self._api.any_get_as_field),
                (property_field.PropertyField, self._api.any_get_as_property_field),
                (string_field.StringField, self._api.any_get_as_string_field),
                (generic_data_container.GenericDataContainer, self._api.any_get_as_generic_data_container)
                ]

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except Exception as e:
            print(str(e.args), str(self._deleter_func[0]))
            warnings.warn(traceback.format_exc())

