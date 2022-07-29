"""
RuntimeConfig
=============
"""
from ansys.dpf.core.data_tree import DataTree
from ansys.dpf.core.common import types
from ansys.dpf.core import misc


class _RuntimeConfig:
    """ Parent class for configuration options.
    """

    def __init__(self, data_tree, server=None):
        if isinstance(data_tree, DataTree):
            self._data_tree = data_tree
        else:
            self._data_tree = DataTree(data_tree=data_tree, server=server)


class RuntimeClientConfig(_RuntimeConfig):
    """Enables to access and set runtime configuration
    options to gRPC client. Mostly used to configurate gRPC streaming and calls options.

    Parameters
    ----------
    data_tree: ctypes.cvoid_p
        DataTree pointer describing the existing parameters configuration
        of DataprocessingCore.
    server : BaseServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Available from 4.0 server version.

    Examples
    --------
    Get runtime configuration for Client.

    >>> from ansys.dpf import core as dpf
    >>> server = dpf.start_local_server(config=dpf.server_factory.AvailableServerConfigs.GrpcServer
    ...    , as_global=False)
    >>> client_config = dpf.settings.get_runtime_client_config(server=server)
    >>> cache_enabled = client_config.cache_enabled
    >>> stream_floats_instead_of_doubles = client_config.stream_floats_instead_of_doubles
    >>> streaming_buffer_size = client_config.streaming_buffer_size
    >>> return_arrays = client_config.return_arrays
    >>> client_config.return_arrays = return_arrays # or True/False
    >>> client_config.cache_enabled = cache_enabled # or True/False
    >>> client_config.stream_floats_instead_of_doubles = stream_floats_instead_of_doubles
    ... # or True/False
    >>> client_config.streaming_buffer_size = streaming_buffer_size # or 10000, 2000 ...
    """
    def __init__(self, data_tree, server=None):
        super().__init__(data_tree=data_tree, server=server)
        if not self._data_tree.has("return_arrays"):
            self._data_tree.add(return_arrays=int(misc.RETURN_ARRAYS))

    @property
    def cache_enabled(self):
        """Whether gRPC requests and responses are intercepted
        to cache them and retrieve them when appropriate.

        Returns
        -------
        bool

        Notes
        -----
        Can only be used for a gRPC communication.

        """
        return bool(self._data_tree.get_as("use_cache", types.int))

    @cache_enabled.setter
    def cache_enabled(self, value):
        self._data_tree.add(use_cache=int(value))

    @property
    def streaming_buffer_size(self):
        """Sets the chunk size (in bytes) used in gRPC streaming calls.

        Returns
        -------
        int

        Notes
        -----
        Can only be used for a gRPC communication.

        """
        return self._data_tree.get_as("streaming_buffer_size", types.int)

    @streaming_buffer_size.setter
    def streaming_buffer_size(self, value):
        self._data_tree.add(streaming_buffer_size=int(value))

    @property
    def stream_floats_instead_of_doubles(self):
        """Sets whether double values (8 bytes) should be converted and streamed as float values
         (4 bytes) in gRPC streaming calls.

        Returns
        -------
        bool

        Notes
        -----
        Can only be used for a gRPC communication.

        """
        return bool(self._data_tree.get_as("stream_floats", types.int))

    @stream_floats_instead_of_doubles.setter
    def stream_floats_instead_of_doubles(self, value):
        self._data_tree.add(stream_floats=int(value))

    @property
    def return_arrays(self):
        """All methods will return :class:`ansys.dpf.core.DPFArray` (instead of lists)
        when possible. Default is ``True``.
        See for example, :func:`ansys.dpf.core.Scoping.ids`.

        Returns
        -------
        bool
        """
        return bool(self._data_tree.get_as("return_arrays", types.int))

    @return_arrays.setter
    def return_arrays(self, value):
        self._data_tree.add(return_arrays=int(value))


class RuntimeCoreConfig(_RuntimeConfig):
    """Enables to access and set runtime configuration
    options to DataProcessingCore.

    Parameters
    ----------
    data_tree: ctypes.cvoid_p
        DataTree pointer describing the existing parameters configuration
        of DataprocessingCore.
    server : BaseServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Available from 4.0 server version.

    Examples
    --------
    Get runtime configuration for DataProcessingCore.

    >>> from ansys.dpf import core as dpf
    >>> server = dpf.start_local_server(config=dpf.server_factory.AvailableServerConfigs.GrpcServer
    ...    , as_global=False) # doctest: +SKIP
    >>> core_config = dpf.settings.get_runtime_core_config(server=server) # doctest: +SKIP
    >>> num_threads = core_config.num_threads # doctest: +SKIP
    >>> core_config.num_threads = num_threads # or 3, 6, ... # doctest: +SKIP
    """
    def __init__(self, data_tree, server=None):
        super().__init__(data_tree=data_tree, server=server)

    @property
    def num_threads(self):
        """Sets the default number of threads to use for all operators,
        default is omp_get_num_threads.

        Returns
        -------
        int
        """
        return self._data_tree.get_as("num_threads", types.int)

    @num_threads.setter
    def num_threads(self, value):
        self._data_tree.add(num_threads=int(value))
