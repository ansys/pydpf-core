import os

from ansys import dpf
from ansys.grpc.dpf import data_sources_pb2, data_sources_pb2_grpc, base_pb2
from ansys.dpf.core.errors import protect_grpc


class DataSources:
    """Represent the file sources of a model.

    Initialize the data_sources with either optional data_sources
    message, or by connecting to a stub.  Result path can also be
    directly set.

    Parameters
    ----------
    result_path : str, optional
        path of the result

    data_sources : ansys.grpc.dpf.data_sources_pb2.DataSources
        gRPC data sources message.

    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.

    Examples
    --------
    Initialize a model from a result path
    >>> import dpf
    >>> dpf.core.DataSources('file.rst')
    """

    def __init__(self, result_path=None, data_sources=None, channel=None):
        """Initialize connection with the server"""
        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        self._stub = self._connect()

        if data_sources is None:
            request = base_pb2.Empty()
            self._message = self._stub.Create(request)
        else:
            self._message = data_sources

        if result_path is not None:
            self.set_result_file_path(result_path)

    @protect_grpc
    def _connect(self):
        """Connect to the grpc service"""
        return data_sources_pb2_grpc.DataSourcesServiceStub(self._channel)

    def set_result_file_path(self, filepath, key=""):
        """Set the result file path

        Parameters
        ----------
        filepath : str
            Path to the result file.

        key : str, optional
            Extension of the file, found directly if it is not set.

        Examples
        --------
        Create a data source and set the result file path

        >>> import dpf
        >>> data_sources = dpf.core.DataSources()
        >>> data_sources.set_result_file_path('/tmp/file.rst')
        """
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.key = key
        request.path = filepath
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def add_file_path(self, filepath, key=""):
        """Add a file path.

        This is used for files other than the result file.

        Parameters
        ----------
        filepath : str
            Path of the file.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_sources = dpf.DataSources()
        >>> data_sources.add_file_path('/tmp/ds.dat')
        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))

        request = data_sources_pb2.UpdateRequest()
        request.key = key
        request.path = filepath
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def add_upstream(self, upstream_data_sources, upstream_id=-2):
        """Add an upstream datasources.

        This is used to add a set of path creating an upstram for
        recursive workflows.

        Parameters
        ----------
        datasources : DataSources

        """
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_id = upstream_id
        request.upstream_data_sources.CopyFrom(upstream_data_sources._message)
        request.data_sources.CopyFrom(self._message)
        self._stub.UpdateUpstream(request)

    @property
    def result_key(self):
        return self._info["result_key"]

    @property
    def result_files(self):
        return self._info["paths"][self.result_key]

    @property
    def _info(self):
        list = self._stub.List(self._message)
        paths = {}
        for key in list.paths:
            key_paths=[]
            for path in list.paths[key].paths:
                key_paths.append(path)
            paths[key] = key_paths
        out = {"result_key": list.result_key, "paths": paths}
        return out

    def __str__(self):
        info = self._info
        txt = f'DPF data_sources with result key: {self.result_key}\n'
        txt += f'paths: {info["paths"]}\n'
        return txt

    def __del__(self):
        try:  # should silently fail
            self._stub.Delete(self._message)
        except:
            pass
