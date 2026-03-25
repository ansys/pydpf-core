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
from pathlib import Path

import ansys.dpf.core as dpf


class Stream(ABC):
    """Abstract base class for a DPF external stream.

    A stream is an open, ready-to-use data source.  Once the underlying file
    is opened it stays open and keeps data in cache so that subsequent
    evaluations are faster.  To close the file and free the cache, call
    :meth:`release`.

    Subclasses must override :attr:`stream_type_name`, :attr:`time_freq_support`,
    and :attr:`result_info`.  They may also override :meth:`_create_handle` and
    :meth:`_release_handle` to manage a custom resource instead of the default
    binary file handle.

    Once instantiated, a stream can be registered with a
    :class:`~ansys.dpf.core.streams_container.StreamsContainer` via
    :meth:`~ansys.dpf.core.streams_container.StreamsContainer.add_stream` so
    that DPF operators can consume it.

    Note
    ----
    Streams are only meaningful when used with a
    :class:`~ansys.dpf.core.streams_container.StreamsContainer`, which itself
    requires an InProcess server configuration.

    Examples
    --------
    Define a minimal concrete stream for an RST result file:

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> from ansys.dpf.core.stream import Stream
    ...
    >>> class RstStream(Stream):
    ...     @property
    ...     def stream_type_name(self) -> str:
    ...         return "rst"
    ...     @property
    ...     def time_freq_support(self):
    ...         return dpf.TimeFreqSupport()
    ...     @property
    ...     def result_info(self):
    ...         return dpf.ResultInfo()
    ...
    >>> rst_path = examples.find_simple_bar()
    >>> stream = RstStream(rst_path)
    >>> sc = dpf.StreamsContainer()
    >>> sc.add_stream(stream, group=1, is_result=1, result=1)
    """

    def __init__(self, file_path: str | Path):
        """
        Create a stream for the given file.

        Parameters
        ----------
        file_path : str or pathlib.Path
            Absolute or relative path to the result file.  The file must
            exist on disk at construction time.

        Raises
        ------
        FileNotFoundError
            If *file_path* does not point to an existing file.
        """
        self._path = Path(file_path)
        if not self._path.exists():
            raise FileNotFoundError(f"File {self._path} does not exist.")
        self._handle = self._create_handle()

    def _create_handle(self):
        """Open the file and return its handle.

        The default implementation opens the file in binary read mode.
        Override this method in subclasses that manage a different kind of
        resource (e.g. a memory-mapped buffer or a network socket).

        Returns
        -------
        object
            An open file handle or equivalent resource.
        """
        return self._path.open("rb")

    def _release_handle(self):
        """Close the resource handle.

        The default implementation calls ``close()`` on the handle returned by
        :meth:`_create_handle`.  Override this method in subclasses that
        manage a different kind of resource.
        """
        if self._handle:
            self._handle.close()

    def release(self):
        """Close the file and release cached data.

        After calling this method the stream is no longer usable.  Any
        subsequent read requests routed through a
        :class:`~ansys.dpf.core.streams_container.StreamsContainer` that
        references this stream will fail.
        """
        self._release_handle()
        self._handle = None

    @property
    def stream_type_name(self) -> str:
        """Type identifier recognised by the DPF server for this stream.

        The value must match a stream type registered on the server side
        (for example ``"rst"``, ``"d3plot"``, ``"cgns"``).
        Subclasses **must** override this property to return the correct type
        string; the base-class implementation returns the placeholder
        ``"stream_type"``.

        Returns
        -------
        str
            Stream type identifier.
        """
        return "stream_type"

    @property
    def file_path(self) -> str:
        """Absolute path to the file backing this stream.

        Returns
        -------
        str
            Path to the result file as a string.
        """
        return str(self._path)

    @property
    @abstractmethod
    def time_freq_support(self) -> dpf.TimeFreqSupport:
        """Time/frequency support describing the available time steps.

        Returns
        -------
        ansys.dpf.core.TimeFreqSupport
            Object describing the time and frequency sets available in this
            stream.
        """
        pass

    @property
    @abstractmethod
    def result_info(self) -> dpf.ResultInfo:
        """Metadata describing the results available in this stream.

        Returns
        -------
        ansys.dpf.core.ResultInfo
            Object containing solver type, available result quantities, and
            unit system information.
        """
        pass

    def __delete__(self):
        """Release resources when the descriptor protocol deletes this object."""
        self.release()
