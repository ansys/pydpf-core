# -*- coding: utf-8 -*-
"""
MaterialsContainer
==================
Contains classes associated with the DPF MaterialsContainer.
"""
# from ansys.dpf.core import material
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    materials_container_capi
)


class MaterialsContainer:

    def __init__(self, materials_container=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)
        self._api = self._server.get_api_for_type(
            capi=materials_container_capi.ScopingCAPI,
            grpcapi=materials_container_grpcapi.ScopingGRPCAPI
        )
        # step3: init environment
        self._api.init_materials_container_environment(self)  # creates stub when gRPC

        # step2: if object exists, take the instance, else create it
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = self._api.collection_of_mesh_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.collection_of_mesh_new()
