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

import weakref


class DataSourcesOrStreamsConnector:
    def __init__(self, metadata):
        self._metadata = weakref.ref(metadata)

    @property
    def streams_provider(self):
        if self._metadata():
            return self._metadata().streams_provider
        return None

    @property
    def time_freq_support(self):
        if self._metadata():
            return self._metadata().time_freq_support
        return None

    @property
    def mesh_provider(self):
        if self._metadata():
            return self._metadata()._mesh_provider_cached
        return None

    @property
    def data_sources(self):
        if self._metadata():
            return self._metadata().data_sources
        return None

    def named_selection(self, name):
        if self._metadata():
            return self._metadata().named_selection(name)
        return None

    def __connect_op__(self, op, mesh_by_default=True):
        """Connect the data sources or the streams to the operator."""
        if self.streams_provider is not None and hasattr(op.inputs, "streams"):
            op.inputs.streams.connect(self.streams_provider.outputs)
        elif self.streams_provider is not None and hasattr(op.inputs, "streams_container"):
            op.inputs.streams_container.connect(self.streams_provider.outputs)
        elif self.data_sources is not None and hasattr(op.inputs, "data_sources"):
            op.inputs.data_sources.connect(self.data_sources)

        if mesh_by_default and self.mesh_provider and hasattr(op.inputs, "mesh"):
            op.inputs.mesh.connect(self.mesh_provider)
