"""
.. _ref_data_sources:

Data Sources
============
"""
import os
import warnings
import traceback

from ansys.dpf.core import server as server_module
from ansys.dpf.gate import data_sources_capi, data_sources_grpcapi, integral_types, \
    data_processing_capi, data_processing_grpcapi


class DataSources:
    """Contains files with analysis results.

    An extension key (``'rst'`` for example) is used to choose which files represent
    results files versus accessory files. You can set a result file path when
    initializing this class.


    Parameters
    ----------
    result_path : str or os.PathLike object, optional
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
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(capi=data_sources_capi.DataSourcesCAPI,
                                                  grpcapi=data_sources_grpcapi.DataSourcesGRPCAPI)

        # step3: init environment
        self._api.init_data_sources_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if data_sources is not None:
            if isinstance(data_sources, DataSources):
                # Make a Copy
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI)
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(
                    data_sources)
            else:
                # It should be a message (usually from a call to operator_getoutput_data_sources)
                self._internal_obj = data_sources
        else:
            if self._server.has_client():
                self._internal_obj = self._api.data_sources_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.data_sources_new("data_sources")

        if result_path is not None:
            self.set_result_file_path(result_path)

    def set_result_file_path(self, filepath, key=""):
        """Add a result file path to the data sources.

        Parameters
        ----------
        filepath : str or os.PathLike object
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
        if key == "":
            self._api.data_sources_set_result_file_path_utf8(self, str(filepath))
        else:
            self._api.data_sources_set_result_file_path_with_key_utf8(self, str(filepath), key)

    def set_domain_result_file_path(self, path, domain_id):
        """Add a result file path by domain.

        This method is used to handle files created by a
        distributed solve.

        Parameters
        ----------
        path: str or os.PathLike object
            Path to the file.
        domain_id: int
            Domain ID for the distributed files.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_sources = dpf.DataSources()
        >>> data_sources.set_domain_result_file_path('/tmp/file0.sub', 0)
        >>> data_sources.set_domain_result_file_path('/tmp/file1.sub', 1)

        """
        self._api.data_sources_set_domain_result_file_path_utf8(self, str(path), domain_id)

    def add_file_path(self, filepath, key="", is_domain: bool = False, domain_id=0):
        """Add a file path to the data sources.

        Files not added as result files are accessory files, which contain accessory
        information not present in the result files.

        Parameters
        ----------
        filepath : str or os.PathLike object
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
        if is_domain:
            if key == "":
                raise NotImplementedError("A key must be given when using is_domain=True.")
            else:
                self._api.data_sources_add_domain_file_path_with_key_utf8(self, str(filepath),
                                                                          key, domain_id)
        else:
            if key == "":
                self._api.data_sources_add_file_path_utf8(self, str(filepath))
            else:
                self._api.data_sources_add_file_path_with_key_utf8(self, str(filepath), key)

    def add_file_path_for_specified_result(self, filepath, key="", result_key=""):
        """Add a file path for a specified result file key to the data sources.

        This method can be used when results files with different keys (extensions) are
        contained in the data sources. For example, a solve using two different solvers
        could generate two different sets of files.

        Parameters
        ----------
        filepath : str or os.PathLike object
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

        self._api.data_sources_add_file_path_for_specified_result_utf8(self, str(filepath),
                                                                       key, result_key)

    def add_upstream(self, upstream_data_sources, result_key=""):
        """Add upstream data sources.

        This is used to add a set of path creating an upstream for
        recursive workflows.

        Parameters
        ----------
        upstream_data_sources : DataSources
            Set of paths creating an upstream for recursive workflows.

        result_key: str, optional
            Extension of the result file group with which this upstream belongs

        """
        if result_key == "":
            self._api.data_sources_add_upstream_data_sources(self, upstream_data_sources)
        else:
            self._api.data_sources_add_upstream_data_sources_for_specified_result(self,
                                                                            upstream_data_sources,
                                                                                  result_key)

    def add_upstream_for_domain(self, upstream_data_sources, domain_id):
        """Add an upstream data sources for a given domain.

        This is used to add a set of path creating an upstream for
        recursive workflows in a distributed solve.

        Parameters
        ----------
        upstream_data_sources : DataSources
            Set of paths creating an upstream for recursive workflows.

        domain_id: int
            Domain id for distributed files.

        """
        self._api.data_sources_add_upstream_domain_data_sources(self,
                                                                upstream_data_sources, domain_id)

    @property
    def result_key(self):
        """Result key used by the data sources.

        Returns
        -------
        str
           Result key.

        """
        return self._api.data_sources_get_result_key(self)

    @property
    def result_files(self):
        """List of result files contained in the data sources.

        Returns
        ----------
        list
            List of result files.
        """
        result_key = self.result_key
        if result_key == "":
            return None
        else:
            response = []
            num_keys = self._api.data_sources_get_num_keys(self)
            for i_key in range(num_keys):
                num_paths = integral_types.MutableInt32()
                key = self._api.data_sources_get_key(self, i_key, num_paths)
                if key == result_key:
                    for i_path in range(int(num_paths)):
                        path = self._api.data_sources_get_path(self, key, i_path)
                        response.append(path)
            return response

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
            pass
