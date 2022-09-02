"""
Internal Usage
"""
import warnings
import traceback
from ansys.dpf.gate import (
    label_space_capi,
    label_space_grpcapi,
    data_processing_capi,
    data_processing_grpcapi,
)
from ansys.dpf.core import server as server_module


class LabelSpace:
    def __init__(self, label_space=None, obj=None, server=None):
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=label_space_capi.LabelSpaceCAPI,
            grpcapi=label_space_grpcapi.LabelSpaceGRPCAPI
        )
        # step3: init environment
        self._api.init_label_space_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if label_space is not None and not isinstance(label_space, dict):
            self._internal_obj = label_space
        else:
            self._internal_obj = self._api.label_space_new_for_object(obj)
            if isinstance(label_space, dict):
                self.fill(label_space)

    @property
    def _data_processing_core_api(self):
        core_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI)
        core_api.init_data_processing_environment(self)
        return core_api

    def fill(self, label_space):
        for key, index in label_space.items():
            self._api.label_space_add_data(self, key, index)

    def __dict__(self):
        if isinstance(self._internal_obj, dict):
            return self._internal_obj
        out = {}

        for i in range(0, self._api.label_space_get_size(self)):
            out[self._api.label_space_get_labels_name(self, i)] = \
                self._api.label_space_get_labels_value(self, i)
        return out

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())