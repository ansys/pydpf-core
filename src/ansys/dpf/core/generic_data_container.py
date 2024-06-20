"""
.. _ref_generic_data_container:

GenericDataContainer
====================
"""
from __future__ import annotations
import traceback
import warnings
import builtins
from typing import Union, TYPE_CHECKING

from ansys.dpf.core.check_version import server_meet_version

if TYPE_CHECKING:  # pragma: no cover
    from ansys.dpf.core import Field, Scoping, StringField, GenericDataContainer

from ansys.dpf.core.dpf_operator import _write_output_type_to_type


from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors, types
from ansys.dpf.core.any import Any
from ansys.dpf.core import collection_base
from ansys.dpf.core.mapping_types import map_types_to_python


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
    Class available with server's version starting at 7.0 (Ansys 2024 R1 pre0).
    """

    def __init__(self, generic_data_container=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            generic_data_container._server if isinstance(
                generic_data_container, GenericDataContainer
            ) else server
        )

        if not self._server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        # step 2: if object exists, take the instance, else create it
        self._api_instance = None
        self._api.init_generic_data_container_environment(self)  # creates stub when gRPC

        self._api.init_generic_data_container_environment(self)

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
    def _api(self):
        from ansys.dpf.gate import (
            generic_data_container_capi,
            generic_data_container_grpcapi,
        )

        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=generic_data_container_capi.GenericDataContainerCAPI,
                grpcapi=generic_data_container_grpcapi.GenericDataContainerGRPCAPI,
            )
            self._api.init_generic_data_container_environment(self)  # creates stub when gRPC

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

    def set_property(
            self,
            property_name: str,
            prop: Union[int, float, str, Field, StringField, GenericDataContainer, Scoping]
    ):
        """Register given property with the given name.

        Parameters
        ----------
        property_name:
            Property name.
        prop:
            Property object.
        """

        if not isinstance(prop, (int, float, str, bytes)) and server_meet_version("8.1", self._server):
            self._api.generic_data_container_set_property_dpf_type(self, property_name, prop)
        else:
            any_dpf = Any.new_from(prop, self._server)
            self._api.generic_data_container_set_property_any(self, property_name, any_dpf)

    def get_property(self, property_name, output_type: Union[None, type, types] = None):
        """Get property with given name.

        Parameters
        ----------
        property_name : str
            Property name.

        output_type : None, type, types, optional
            Expected type of the output. By default, type is deduced using
            `GenericDataContainer.get_property_description`.

        Returns
        -------
        Property object instance.
        """
        any_ptr = self._api.generic_data_container_get_property_any(self, property_name)
        any_dpf = Any(any_ptr, self._server)
        if output_type is None:
            output_type = self.get_property_description()[property_name]
        else:
            if not isinstance(output_type, type):
                output_type = _write_output_type_to_type(output_type)

            output_type = str(output_type.__name__)

        class_ = getattr(builtins, output_type, None)
        if class_ is None:
            from ansys.dpf import core

            class_ = getattr(core, output_type)

        return any_dpf.cast(class_)

    def get_property_description(self):
        """Get a dictionary description of properties by name and data type

        Returns
        -------
        description: dict
            Description of the GenericDataContainer's contents
        """

        coll_obj = collection_base.StringCollection(
            collection=self._api.generic_data_container_get_property_names(self),
            server=self._server,
        )
        property_names = coll_obj.get_integral_entries()

        coll_obj = collection_base.StringCollection(
            collection=self._api.generic_data_container_get_property_types(self),
            server=self._server,
        )
        property_types = coll_obj.get_integral_entries()

        python_property_types = []
        for _, property_type in enumerate(property_types):
            python_property_types.append(map_types_to_python[property_type])

        return dict(zip(property_names, python_property_types))

    def __del__(self):
        if self._internal_obj is not None:
            try:
                self._deleter_func[0](self._deleter_func[1](self))
            except Exception as e:
                print(str(e.args), str(self._deleter_func[0]))
                warnings.warn(traceback.format_exc())
