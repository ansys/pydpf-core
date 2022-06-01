"""
RuntimeConfig
=============
"""
from ansys.dpf.core.data_tree import DataTree
from ansys.dpf.core.common import types



class _RuntimeConfig:
    """ Parent class for configuration options.
    """

    def __init__(self, data_tree, server=None):
        if data_tree is not None:
            if isinstance(data_tree, int):
                self._data_tree = DataTree(data_tree=data_tree, server=server)
            else:
                raise TypeError("data_tree attribute expected type is pointer on DataTree")


class RuntimeClientConfig(_RuntimeConfig):
    """ Enables to access and set runtime configuration
    options to DataProcessingCore binary.

    Parameters
    ----------
    data_tree: ctypes.cvoid_p
        DataTree pointer describing the existing parameters configuration
        of DataprocessingCore.
    server : GrpcServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Notes
    -----
    Available from 4.0 server version. Can only be used for
    a gRPC communication protocol using DPF CLayer.

    Examples
    --------
    Get runtime configuration for DataProcessingCore.

    >>> from ansys.dpf import core as dpf
    >>> server = dpf.start_local_server(config=dpf.server_factory.AvailableServerConfigs.GrpcServer)
    >>> client_config = dpf.settings.get_runtime_client_config(server=server)
    >>> cache_enabled = client_config.cache_enabled
    """
    def __init__(self, data_tree, server=None):
        super().__init__(data_tree=data_tree, server=server)

    @property
    def cache_enabled(self):
        """Whether gRPC requests and responses are intercepted
        to cache them and retrieve them when appropriate.

        Returns
        -------
        bool
        """
        return bool(self._data_tree.get_as("use_cache", types.int))

    @cache_enabled.setter
    def cache_enabled(self, value):
        self._data_tree.add(use_cache=int(value))
