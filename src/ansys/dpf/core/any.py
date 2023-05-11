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

        self._internal_type = None
        self._get_as_method = None

    @staticmethod
    def _type_to_new_from_get_as_method(any):
        """TODO: document"""
        from ansys.dpf.core import (
            field,
            property_field,
            generic_data_container,
            string_field
        )

        return [
            #(str, any._api.any_wrapped_type_string),
            (field.Field, any._api.any_new_from_field, any._api.any_get_as_field),
            (property_field.PropertyField, any._api.any_new_from_property_field, any._api.any_get_as_property_field),
            (string_field.StringField, any._api.any_new_from_string_field, any._api.any_get_as_string_field),
            (generic_data_container.GenericDataContainer, any._api.any_new_from_generic_data_container, any._api.any_get_as_generic_data_container)
        ]

    @staticmethod
    def new_from(obj):
        """TODO: document"""
        any = Any(server=obj._server)
        for type_tuple in Any._type_to_new_from_get_as_method(any):
            if isinstance(obj, type_tuple[0]):
                # call respective new_from function
                any._internal_obj = type_tuple[1](obj)
                # store get_as & type for casting back to original type
                any._internal_type = type_tuple[0]
                any._get_as_method = type_tuple[2]

                return any
        # TODO: check match

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

    def cast(self, output_type=None):
        """TODO: document"""

        self._internal_type = output_type if output_type is not None else self._internal_type

        for type_tuple in Any._type_to_new_from_get_as_method(self):
            if self._internal_type == type_tuple[0]:
                # call the get_as function for the appropriate type
                internal_obj = type_tuple[2](self)
                # get the current type's constructors' variable keyword for passing the internal_obj
                internal_obj_keyword = type_tuple[0].__init__.__code__.co_varnames[-2]
                # wrap parameters in a dictionary for keyword parameters expansion when calling constructor
                keyword_args = {internal_obj_keyword: internal_obj, "server": self._server}
                # call constructor
                obj = type_tuple[0](**keyword_args)

                return obj

        # TODO: check match

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except Exception as e:
            print(str(e.args), str(self._deleter_func[0]))
            warnings.warn(traceback.format_exc())

