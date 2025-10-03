# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

from __future__ import annotations

from pathlib import Path

import ansys.dpf.core as dpf
from ansys.dpf.gate import data_processing_capi, data_processing_grpcapi


def start_debug_trace(path: str | Path, server: dpf.AnyServerType = None):
    server = dpf.server.get_or_create_server(server)
    api = server.get_api_for_type(
        capi=data_processing_capi.DataProcessingCAPI,
        grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
    )
    api.data_processing_set_debug_trace(text=str(path))


def stop_debug_trace(server: dpf.AnyServerType = None):
    server = dpf.server.get_or_create_server(server)
    api = server.get_api_for_type(
        capi=data_processing_capi.DataProcessingCAPI,
        grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
    )
    api.data_processing_set_debug_trace(text="")
