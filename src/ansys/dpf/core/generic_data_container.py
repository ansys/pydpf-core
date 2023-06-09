"""
.. _ref_generic_data_container:

GenericDataContainer
====================
"""
import traceback
import warnings

from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.gate import (
    generic_data_container_abstract_api,
    generic_data_container_capi,
    generic_data_container_grpcapi,
)
from ansys.dpf.core.any import Any
from ansys.dpf.core import collection


class GenericDataContainer:
    """Maps properties to their DPF supported Data Types.

    Parameters
    ----------
    generic_data_container : ctypes.c_void_p, ansys.grpc.dpf.generic_data_container_pb2.GenericDataContainer message, optional  # noqa: E501
    server : DPFServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Class available with server's version starting at 6.2 (Ansys 2023R2).
    """

    def __init__(self, generic_data_container=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if not self._server.meet_version("6.2"):
            raise errors.DpfVersionNotSupported("6.2")

        # step 2: get api
        self._api_instance = self._server.get_api_for_type(
            capi=generic_data_container_capi.GenericDataContainerCAPI,
            grpcapi=generic_data_container_grpcapi.GenericDataContainerGRPCAPI,
        )

        # step3: init environment
        self._api.init_generic_data_container_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it

        # self._internal_obj = generic_data_container
        if generic_data_container is not None:
            self._internal_obj = generic_data_container
        else:
            if self._server.has_client():
                self._internal_obj = self._api.generic_data_container_new_on_client(
                    self._server.client
                )
            else:
                self._internal_obj = self._api.generic_data_container_new()

    @property
    def _api(self) -> generic_data_container_abstract_api.GenericDataContainerAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=generic_data_container_capi.GenericDataContainerCAPI,
                grpcapi=generic_data_container_grpcapi.GenericDataContainerGRPCAPI,
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

    def set_property(self, property_name, prop):
        """ Register given property with the given name.

        Parameters
        ----------
        property_name : str
            Property name.
        prop : type
            object instance.
        """

        any = Any.new_from(prop, self._server)
        self._api.generic_data_container_set_property_any(self, property_name, any)

    def get_property(self, property_name, output_type):
        """ Get property with given name.

        Parameters
        ----------
        property_name : str
            Property name.
        output_type :  :class:`ansys.dpf.core.common.types`

        Returns
        -------
        type
            Property object instance.
        """
        any_ptr = self._api.generic_data_container_get_property_any(self, property_name)
        any = Any(any_ptr, self._server)
        return any.cast(output_type)

    def get_property_description(self):
        """
        TODO
        Returns
        -------

        """

        coll_obj = collection.StringCollection(
            collection=self._api.generic_data_container_get_property_names(self),
            server=self._server,
        )
        property_names = coll_obj.get_integral_entries()

        coll_obj = collection.StringCollection(
            collection=self._api.generic_data_container_get_property_types(self),
            server=self._server,
        )
        property_types = coll_obj.get_integral_entries()

        return dict(zip(property_names, property_types))

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except Exception as e:
            print(str(e.args), str(self._deleter_func[0]))
            warnings.warn(traceback.format_exc())
