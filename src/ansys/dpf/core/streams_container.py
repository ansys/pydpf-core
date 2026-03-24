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
StreamsContainer.

Contains classes associated with the DPF StreamsContainer.
"""

import traceback
import warnings

from ansys.dpf.core import errors, server as server_module
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.label_space import LabelSpace
from ansys.dpf.core.server_types import BaseServer
from ansys.dpf.core.stream import Stream
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
    integral_types,
    streams_capi,
)


class StreamsContainer:
    """Holds a collection of open, ready-to-use data streams.

    A :class:`StreamsContainer` wraps one or more
    :class:`~ansys.dpf.core.stream.Stream` objects (or the DPF-internal
    equivalent).  Because the underlying files stay open and keep cached
    data between evaluations, repeated reads are significantly faster than
    reopening from a
    :class:`~ansys.dpf.core.data_sources.DataSources`.

    There are three ways to obtain a :class:`StreamsContainer`:

    1. **From a Model** — DPF opens the file automatically; retrieve the
       container via ``model.metadata.streams_provider``.
    2. **From a DataSources** — wrap an existing
       :class:`~ansys.dpf.core.data_sources.DataSources` so that DPF
       manages the open handles.
    3. **From scratch** — create an empty container and register one or
       more custom :class:`~ansys.dpf.core.stream.Stream` objects with
       :meth:`add_stream`.  This is the entry point for Python custom
       plug-ins that provide their own ``streams_provider`` operator.

    To close the open files and release cached data, call
    :meth:`release_handles`.

    Note
    ----
    Only available with an InProcess server configuration.

    Examples
    --------
    Obtain a container from an existing model:

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.find_multishells_rst())
    >>> sc = model.metadata.streams_provider.outputs.streams_container()

    Create a container from a :class:`~ansys.dpf.core.data_sources.DataSources`:

    >>> ds = dpf.DataSources(examples.find_simple_bar())
    >>> sc = dpf.StreamsContainer(data_sources=ds)

    Create an empty container and register a custom stream:

    >>> from ansys.dpf.core.stream import Stream
    >>> class MyStream(Stream):
    ...     @property
    ...     def stream_type_name(self): return "rst"
    ...     @property
    ...     def time_freq_support(self): return dpf.TimeFreqSupport()
    ...     @property
    ...     def result_info(self): return dpf.ResultInfo()
    ...
    >>> sc = dpf.StreamsContainer()
    >>> sc.add_stream(MyStream(examples.find_simple_bar()), group=1, is_result=1, result=1)
    """

    def __init__(
        self,
        streams_container=None,
        server: BaseServer = None,
        data_sources: DataSources = None,
    ):
        """Create or wrap a DPF :class:`StreamsContainer`.

        Parameters
        ----------
        streams_container : StreamsContainer or internal object, optional
            * If a :class:`StreamsContainer` instance is given, a shallow
              duplicate reference to the same underlying object is created.
            * If a raw internal DPF object (void pointer) is given, it is
              adopted directly.  This is used internally when operators
              return a streams container.
            * If ``None`` (the default), a new container is allocated on the
              server.
        server : BaseServer, optional
            DPF server to use.  Must be an InProcess server.  Defaults to
            the global server.
        data_sources : DataSources, optional
            :class:`~ansys.dpf.core.data_sources.DataSources` to associate
            with the new container.  Ignored when *streams_container* is not
            ``None``.  When ``None`` and no *streams_container* is given, an
            empty :class:`~ansys.dpf.core.data_sources.DataSources` is
            created automatically.

        Raises
        ------
        ServerTypeError
            If the resolved server uses a gRPC communication protocol.
        """
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
        else:
            # Create a new StreamsContainer, optionally wrapping the given DataSources
            if data_sources is None:
                data_sources = DataSources(server=self._server)
            self._internal_obj = self._api.streams_new(data_sources)
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
        """DataSources associated with this container.

        Returns the :class:`~ansys.dpf.core.data_sources.DataSources` that
        lists the result files backing this container's open streams.

        Returns
        -------
        ansys.dpf.core.DataSources
            Data sources for this container.
        """
        return DataSources(data_sources=self._api.streams_get_data_sources(self))

    def release_handles(self):
        """Close all open files and release cached data.

        After calling this method all streams in the container are closed.
        The container object itself remains valid — files will be reopened
        automatically on the next evaluation that requires them.
        """
        self._api.streams_release_handles(self)

    def __del__(self):
        """Delete the entry."""
        try:
            # delete
            if not getattr(self, "owned", False):
                self._deleter_func[0](self._deleter_func[1](self))
        except:  # pylint: disable=bare-except
            warnings.warn(traceback.format_exc())

    def add_stream(
        self, stream: Stream, group: int = None, is_result: int = None, result: int = None
    ):
        """Add an external stream to the container.

        Two registration strategies are available depending on how the
        :class:`StreamsContainer` was created:

        **Label-space strategy** (``group`` / ``is_result`` / ``result`` supplied):
            The stream is registered under the given label values.  Use this
            when the container was created without a backing
            :class:`~ansys.dpf.core.data_sources.DataSources`, or when you want
            explicit control over the labels.  A
            :class:`~ansys.dpf.core.streams_container.StreamsContainer` created
            from scratch holds a fixed three-label schema: ``group``,
            ``is_result``, and ``result`` (all integers).

        **DataSources-lookup strategy** (no labels supplied):
            The stream's :attr:`~ansys.dpf.core.stream.Stream.file_path` is
            matched against the files already registered in the container's
            underlying :class:`~ansys.dpf.core.data_sources.DataSources`.  The
            label space stored there is reused automatically.  Use this when the
            container was created via
            ``StreamsContainer(data_sources=ds)`` and the file is already in
            ``ds``.

        Parameters
        ----------
        stream : Stream
            The stream to add.  Must be a concrete subclass of
            :class:`~ansys.dpf.core.stream.Stream` that implements at least
            :attr:`~ansys.dpf.core.stream.Stream.stream_type_name` and
            :attr:`~ansys.dpf.core.stream.Stream.file_path`.
        group : int, optional
            Value for the ``group`` label.  When *all* three label arguments are
            ``None`` (the default) the DataSources-lookup strategy is used
            instead.
        is_result : int, optional
            Value for the ``is_result`` label.  Use ``1`` for a result stream,
            ``0`` for an auxiliary stream.
        result : int, optional
            Value for the ``result`` label.

        Raises
        ------
        DPFServerException
            If the label-space strategy is used and the supplied labels do not
            match the container's schema, or if the DataSources-lookup strategy
            is used and the stream's file path is not found in the container's
            ``DataSources``.

        Examples
        --------
        **Label-space strategy** — container created without a DataSources:

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> from ansys.dpf.core.stream import Stream
        ...
        >>> class MyStream(Stream):
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
        >>> sc = dpf.StreamsContainer()
        >>> sc.add_stream(MyStream(rst_path), group=1, is_result=1, result=1)

        **DataSources-lookup strategy** — container created from a DataSources:

        >>> ds = dpf.DataSources(rst_path)
        >>> sc = dpf.StreamsContainer(data_sources=ds)
        >>> sc.add_stream(MyStream(rst_path))  # labels inferred from ds
        """
        import ctypes

        release_func_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
        delete_func_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
        stream_type_name = integral_types.MutableString(stream.stream_type_name.encode())

        def _release(_user_data):
            stream.release()

        def _delete(_user_data):
            stream.release()

        release_func = release_func_type(_release)
        delete_func = delete_func_type(_delete)
        # The C++ layer requires a non-null instance pointer; the closures above
        # capture 'stream' directly so the user-data value is not dereferenced.
        var1 = ctypes.c_void_p(1)

        # Keep the ctypes callbacks and the stream alive for as long as this
        # StreamsContainer exists; otherwise GC frees them before DPF calls them.
        if not hasattr(self, "_stream_callbacks"):
            self._stream_callbacks = []
        self._stream_callbacks.append((stream, release_func, delete_func))

        if group is None and is_result is None and result is None:
            # DataSources-lookup strategy: match file path against the
            # container's underlying DataSources to infer the label space.
            self._api.streams_add_external_stream(
                self,
                streamTypeName=stream_type_name,
                filePath=stream.file_path,
                releaseFileFunc=release_func,
                deleteFunc=delete_func,
                var1=var1,
            )
        else:
            # Label-space strategy: register under explicitly provided labels,
            # defaulting missing ones to 1.
            label_space = LabelSpace(
                label_space={
                    "group": group if group is not None else 1,
                    "is_result": is_result if is_result is not None else 1,
                    "result": result if result is not None else 1,
                },
                server=self._server,
            )
            self._api.streams_add_external_stream_with_label_space(
                self,
                streamTypeName=stream_type_name,
                filePath=stream.file_path,
                releaseFileFunc=release_func,
                deleteFunc=delete_func,
                var1=var1,
                labelspace=label_space,
            )
