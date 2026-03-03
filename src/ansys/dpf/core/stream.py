# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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
Stream.

Contains classes used to populate a StreamsContainer.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import os

import ansys.dpf.core as dpf


class Stream(ABC):
    """Python wrapper for a DPF Stream.

    A Stream is a data source that is open and ready to be used. Once the files in the stream are opened, they stay opened and they keep some data in cache to make the next evaluations faster. To close the opened files, release the handles.

    Note
    ----
    Only available for an InProcess server configuration.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    """

    def __init__(self, file_path: str | os.PathLike):
        self._path = str(file_path)
        if not os.path.exists(self._path):
            raise FileNotFoundError(f"File {self._path} does not exist.")
        self._handle = self._create_handle()

    def _create_handle(self):
        """Create and return the resource handle. Subclasses must implement."""
        return open(self._path, "rb")

    def _release_handle(self):
        """Release the resource handle. Subclasses must implement."""
        if self._handle:
            self._handle.close()

    def release(self):
        """Release the handles of the stream to close the opened files."""
        self._release_handle()
        self._handle = None

    @property
    def stream_type_name(self) -> str:
        """Get the type name of the stream."""
        return "stream_type"

    @property
    def file_path(self) -> str:
        """Get the file name of the stream."""
        return str(self._path)

    @property
    @abstractmethod
    def time_freq_support(self) -> dpf.TimeFreqSupport:
        """Get the time and frequency support of the stream."""
        pass

    @property
    @abstractmethod
    def result_info(self) -> dpf.ResultInfo:
        """Get the result info of the stream."""
        pass

    def __delete__(self):
        self.release()
