# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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
Internal Usage
"""

import warnings
import traceback
from typing import Dict
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
        self._server = server_module.get_or_create_server(
            label_space._server if isinstance(label_space, LabelSpace) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=label_space_capi.LabelSpaceCAPI,
            grpcapi=label_space_grpcapi.LabelSpaceGRPCAPI,
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
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        core_api.init_data_processing_environment(self)
        return core_api

    def fill(self, label_space: Dict[str, int]):
        for key, index in label_space.items():
            self._api.label_space_add_data(self, key, index)

    def __str__(self):
        return str(dict(self))

    def __iter__(self):
        yield from [
            (
                self._api.label_space_get_labels_name(self, i),
                self._api.label_space_get_labels_value(self, i),
            )
            for i in range(self._api.label_space_get_size(self))
        ]

    def __dict__(self):
        if isinstance(self._internal_obj, dict):
            return self._internal_obj
        out = {}

        for i in range(0, self._api.label_space_get_size(self)):
            out[self._api.label_space_get_labels_name(self, i)] = (
                self._api.label_space_get_labels_value(self, i)
            )
        return out

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
