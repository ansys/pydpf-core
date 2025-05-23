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

# -*- coding: utf-8 -*-
"""
StreamsContainer.

Contains classes associated with the DPF StreamsContainer.
"""

import traceback
import warnings

from ansys.dpf.core import data_sources, errors, server as server_module
from ansys.dpf.core.server_types import BaseServer
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
    streams_capi,
)


class StreamsContainer:
    """Python wrapper for operator input or output of streams.

    Streams define open, ready-to-use, data sources.
    Once the files in the streams are opened, they stay opened and
    they keep some data in cache to make the next evaluations faster.
    To close the opened files, release the handles.

    Note
    ----
    Only available for an InProcess server configuration.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.find_multishells_rst())
    >>> streams_provider = model.metadata.streams_provider
    >>> sc = streams_provider.outputs.streams_container()
    """

    def __init__(self, streams_container=None, server: BaseServer = None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            streams_container._server if isinstance(streams_container, StreamsContainer) else server
        )
        if self._server.has_client():
            txt = """
            StreamsContainer only available for server with InProcess communication protocol
            """
            raise errors.ServerTypeError(txt)

        # step2: if object exists, take the instance, else create it
        self._internal_obj = None
        if streams_container is not None:
            if isinstance(streams_container, StreamsContainer):
                self._server = streams_container._server
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(
                    streams_container
                )
            else:
                self._internal_obj = streams_container
        self.owned = False

    @property
    def _server(self):
        return self._server_instance

    @_server.setter
    def _server(self, value):
        self._server_instance = value
        # step 2: get api
        self._api = self._server.get_api_for_type(capi=streams_capi.StreamsCAPI, grpcapi=None)
        if not self._api:
            raise NotImplementedError("StreamsContainer unavailable for LegacyGrpc servers")
        # step3: init environment
        self._api.init_streams_environment(self)  # creates stub when gRPC

    @property
    def datasources(self):
        """Return the data sources."""
        return data_sources.DataSources(data_sources=self._api.streams_get_data_sources(self))

    def release_handles(self):
        """Release the streams."""
        self._api.streams_release_handles(self)

    def __del__(self):
        """Delete the entry."""
        try:
            # delete
            if not self.owned:
                self._deleter_func[0](self._deleter_func[1](self))
        except:  # pylint: disable=bare-except
            warnings.warn(traceback.format_exc())
