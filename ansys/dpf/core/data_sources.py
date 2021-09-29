"""
.. _ref_data_sources:

Data Sources
============
"""
import os

from ansys import dpf
from ansys.grpc.dpf import data_sources_pb2, data_sources_pb2_grpc, base_pb2
from ansys.dpf.core.errors import protect_grpc


class DataSources:
    """Contains files with analysis results.

    An extension key (``'rst'`` for example) is used to choose which files represent
    results files versus accessory files. You can set a result file path when
    initializing this class.


    Parameters
    ----------
    result_path : str, optional
        Path of the result. The default is ``None``.
    data_sources : ansys.grpc.dpf.data_sources_pb2.DataSources
        gRPC data sources message. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Initialize a model from a result path.

    >>> from ansys.dpf import core as dpf
    >>> my_data_sources = dpf.DataSources('file.rst')
    >>> my_data_sources.result_files
    ['file.rst']

    """

    def __init__(self, result_path=None, data_sources=None, server=None):
        """Initialize a connection with the server."""
        if server is None:
            server = dpf.core._global_server()

        self._server = server
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
        """Connect to the gRPC service."""
        return data_sources_pb2_grpc.DataSourcesServiceStub(self._server.channel)

    def set_result_file_path(self, filepath, key=""):
        """Add a result file path to the data sources.

        Parameters
        ----------
        filepath : str
            Path to the result file.
        key : str, optional
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.

        Examples
        --------
        Create a data source and set the result file path.

        >>> from ansys.dpf import core as dpf
        >>> data_sources = dpf.DataSources()
        >>> data_sources.set_result_file_path('/tmp/file.rst')
        >>> data_sources.result_files
        ['/tmp/file.rst']

        """
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.key = key
        request.path = filepath
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def set_domain_result_file_path(self, path, domain_id):
        """Add a result file path by domain.

        This method is used to handle files created by a
        distributed solve.

        Parameters
        ----------
        path: str
            Path to the file.
        domain_id: int, optional
            Domain ID for the distributed files.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_sources = dpf.DataSources()
        >>> data_sources.set_domain_result_file_path('/tmp/file0.sub', 0)
        >>> data_sources.set_domain_result_file_path('/tmp/file1.sub', 1)

        """
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.domain.domain_path = True
        request.domain.domain_id = domain_id
        request.path = path
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def add_file_path(self, filepath, key="", is_domain: bool = False, domain_id=0):
        """Add a file path to the data sources.

        Files not added as result files are accessory files, which contain accessory
        information not present in the result files.

        Parameters
        ----------
        filepath : str
            Path of the file.
        key : str, optional
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        is_domain: bool, optional
            Whether the file path is the domain path. The default is ``False``.
        domain_id: int, optional
            Domain ID for the distributed files. The default is ``0``. For this
            parameter to be taken into account, ``domain_path=True`` must be set.
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
        if is_domain:
            request.domain.domain_path = True
            request.domain.domain_id = domain_id
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def add_file_path_for_specified_result(self, filepath, key="", result_key=""):
        """Add a file path for a specified result file key to the data sources.

        This method can be used when results files with different keys (extensions) are
        contained in the data sources. For example, a solve using two different solvers
        could generate two different sets of files.

        Parameters
        ----------
        filepath : str
            Path of the file.
        key : str, optional
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        result_key: str, optional
            Extension of the results file that the specified file path belongs to.
            The default is ``""``, in which case the key is found directly.
        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))

        request = data_sources_pb2.UpdateRequest()
        request.key = key
        request.result_key = result_key
        request.path = filepath
        request.data_sources.CopyFrom(self._message)
        self._stub.Update(request)

    def add_upstream(self, upstream_data_sources):
        """Add upstream data sources.

        Parameters
        ----------
        upstream_data_sources : DataSources
            Set of paths creating an upstream for recursive workflows.

        """
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstream_data_sources._message)
        request.data_sources.CopyFrom(self._message)
        self._stub.UpdateUpstream(request)

    @property
    def result_key(self):
        """Result key used by the data sources.

        Returns
        -------
        str
           Result key.

        """
        return self._info["result_key"]

    @property
    def result_files(self):
        """List of result files contained in the data sources.

        Returns
        ----------
        list
            List of result files.
        """
        key = self.result_key
        if key == "":
            return None
        else:
            return self._info["paths"][key]

    @property
    def _info(self):
        list = self._stub.List(self._message)
        paths = {}
        for key in list.paths:
            key_paths = []
            for path in list.paths[key].paths:
                key_paths.append(path)
            paths[key] = key_paths
        out = {"result_key": list.result_key, "paths": paths}
        return out

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

    def __del__(self):
        try:  # should silently fail
            self._stub.Delete(self._message)
        except:
            pass
