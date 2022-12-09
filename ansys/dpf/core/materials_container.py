# -*- coding: utf-8 -*-
"""
MaterialsContainer
==================
Contains classes associated with the DPF MaterialsContainer.
"""
import warnings
# from ansys.dpf.core import material
from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.gate import (
    materials_container_capi,
)


class MaterialsContainer:

    def __init__(self, materials_container=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if not self._server.meet_version("4.0"):
            raise errors.DpfVersionNotSupported("4.0")

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=materials_container_capi.MaterialsContainerCAPI,
            grpcapi=None
        )
        # step3: init environment
        self._api.init_materials_container_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if materials_container is not None:
            # init environment
            pass
        else:
            # init environment
            self._api.init_materials_container_environment(self)
            # if self._server.has_client():
            #     self._internal_obj = self._api.(self._server.client)
            # else:
            #     self._internal_obj = self._api.()

    def __del__(self):
        """Delete the entry."""
        try:
            # delete
            if not self.owned:
                self._deleter_func[0](self._deleter_func[1](self))
        except:  # pylint: disable=bare-except
            warnings.warn(traceback.format_exc())
