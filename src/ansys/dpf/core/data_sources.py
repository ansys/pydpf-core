"""
.. _ref_data_sources:

Data Sources
============
"""
from __future__ import annotations
import os
import warnings
import traceback
from typing import List, Union

from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    data_sources_capi,
    data_sources_grpcapi,
    integral_types,
    data_processing_capi,
    data_processing_grpcapi,
)

from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core import errors
from ansys.dpf.core.label_space import LabelSpace


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

    def __init__(self, result_path: Union[str, os.PathLike] = None, data_sources=None, server=None):
        """Initialize a connection with the server."""
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=data_sources_capi.DataSourcesCAPI,
            grpcapi=data_sources_grpcapi.DataSourcesGRPCAPI,
        )

        # step3: init environment
        self._api.init_data_sources_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if data_sources is not None:
            if isinstance(data_sources, DataSources):
                # Make a Copy
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(
                    data_sources
                )
            elif hasattr(data_sources, "DESCRIPTOR") or isinstance(data_sources, int):
                # It should be a message (usually from a call to operator_getoutput_data_sources)
                self._internal_obj = data_sources
            else:
                self._internal_obj = None
                raise errors.DpfValueError("Data source must be gRPC data sources message type")
        else:
            if self._server.has_client():
                self._internal_obj = self._api.data_sources_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.data_sources_new("data_sources")

        if result_path is not None:
            self.set_result_file_path(result_path)

    def set_result_file_path(self, filepath: Union[str, os.PathLike], key: str = ""):
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
        # Handle no key given and no file extension
        if key == "" and os.path.splitext(filepath)[1] == "":
            key = self.guess_result_key(str(filepath))
        if key == "":
            self._api.data_sources_set_result_file_path_utf8(self, str(filepath))
        else:
            self._api.data_sources_set_result_file_path_with_key_utf8(self, str(filepath), key)

    @staticmethod
    def guess_result_key(filepath: Union[str, os.PathLike]) -> str:
        """Guess result key for files without a file extension."""
        result_keys = ["d3plot", "binout"]
        base_name = os.path.basename(filepath)
        # Handle files without extension
        for result_key in result_keys:
            if result_key in base_name:
                return result_key
        return ""

    def set_domain_result_file_path(self, path: Union[str, os.PathLike], domain_id: int, key: Union[str, None] = None):
        """Associate a result file path to a spatial domain for distributed results.

        This method is used to handle files created by a
        distributed solve.

        Parameters
        ----------
        path:
            Path to the file.
        domain_id:
            Spatial domain ID associated to the file.
        key:
            Override key to associate to the file when the detected key is wrong.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_sources = dpf.DataSources()
        >>> data_sources.set_domain_result_file_path('/tmp/file0.sub', 0)
        >>> data_sources.set_domain_result_file_path('/tmp/file1.sub', 1)

        """
        if key:
            self._api.data_sources_set_domain_result_file_path_with_key_utf8(self, str(path), key, domain_id)
        else:
            self._api.data_sources_set_domain_result_file_path_utf8(self, str(path), domain_id)

    def add_file_path(self, filepath: Union[str, os.PathLike], key: str = "", is_domain: bool = False, domain_id: int = 0):
        """Add a file path to the data sources.

        Files not added as result files are accessory files, which contain accessory
        information not present in the result files.

        Parameters
        ----------
        filepath:
            Path of the file.
        key:
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        is_domain:
            Whether the file path is the domain path. The default is ``False``.
        domain_id:
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
                self._api.data_sources_add_domain_file_path_with_key_utf8(
                    self, str(filepath), key, domain_id
                )
        else:
            if key == "":
                self._api.data_sources_add_file_path_utf8(self, str(filepath))
            else:
                self._api.data_sources_add_file_path_with_key_utf8(self, str(filepath), key)

    def add_file_path_for_specified_result(self, filepath: Union[str, os.PathLike], key: str = "", result_key: str = ""):
        """Add a file path for a specified result file key to the data sources.

        This method can be used when results files with different keys (extensions) are
        contained in the data sources. For example, a solve using two different solvers
        could generate two different sets of files.

        Parameters
        ----------
        filepath:
            Path of the file.
        key:
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        result_key:
            Extension of the results file that the specified file path belongs to.
            The default is ``""``, in which case the key is found directly.
        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))

        self._api.data_sources_add_file_path_for_specified_result_utf8(
            self, str(filepath), key, result_key
        )

    def add_upstream(self, upstream_data_sources: DataSources, result_key: str = ""):
        """Add upstream data sources.

        This is used to add a set of path creating an upstream for
        recursive workflows.

        Parameters
        ----------
        upstream_data_sources:
            Set of paths creating an upstream for recursive workflows.

        result_key:
            Extension of the result file group with which this upstream belongs

        """
        if result_key == "":
            self._api.data_sources_add_upstream_data_sources(self, upstream_data_sources)
        else:
            self._api.data_sources_add_upstream_data_sources_for_specified_result(
                self, upstream_data_sources, result_key
            )

    def add_upstream_for_domain(self, upstream_data_sources: DataSources, domain_id: int):
        """Add an upstream data sources for a given domain.

        This is used to add a set of path creating an upstream for
        recursive workflows in a distributed solve.

        Parameters
        ----------
        upstream_data_sources:
            Set of paths creating an upstream for recursive workflows.

        domain_id:
            Domain id for distributed files.

        """
        self._api.data_sources_add_upstream_domain_data_sources(
            self, upstream_data_sources, domain_id
        )

    @property
    def result_key(self) -> str:
        """Main (first) result key used by the data sources.

        Returns
        -------
        Main result key (first if several exist).

        """
        return self._api.data_sources_get_result_key(self)

    @property
    def result_files(self) -> Union[list[str], None]:
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

    @version_requires("7.0")
    def register_namespace(self, result_key: str, namespace: str):
        """Adds a link from this ``result_key`` to this ``namespace`` in the DataSources.
        This ``result_key`` to ``namespace`` mapping is used by source operators
        to find internal operators to call.

        Notes
        -----
        Available with server's version starting at 7.0.
        """
        self._api.data_sources_register_namespace(self, result_key, namespace)

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

    def __eq__(self, other: DataSources):
        if not isinstance(other, DataSources):
            return False
        if self.result_key != other.result_key:
            return False
        if len(self) != len(other):
            return False
        if self.result_files != other.result_files:
            return False
        # TODO: add namespace check for each key
        # TODO: add domain check
        return True

    def get_result_key(self, index: int = 0) -> str:
        """Get the result key at the given index in the DataSources.

        Parameters
        ----------
        index:
            Index of the result key in the DataSources.

        Returns
        -------

        """
        return self._api.data_sources_get_result_key_by_index(self, index)

    def get_num_result_keys(self) -> int:
        """

        Returns
        -------

        """
        return self._api.data_sources_get_num_result_keys(self)

    @property
    def result_keys(self) -> List[str]:
        """List of result keys in the DataSources"""
        # TODO: create server query for list of result keys, vectorize this request
        out = []
        for i in range(self.get_num_result_keys()):
            out.append(self.get_result_key(i))
        return out

    def get_namespace(self, key: str) -> str:
        """Retrieves the namespace currently associated to the given key.

        The namespace associated to a key defines which version of the operators
        to use with this file. The "rst" key is for example typically associated
        with the "mapdl" version of the operators.

        Parameters
        ----------
        key:
            Key of which to get the associated namespace.

        Returns
        -------
        namespace:
            Current namespace associated to the key.
        """
        return self._api.data_sources_get_namespace(self, key)

    def get_new_path_collection_for_key(self, key: str):
        """

        Parameters
        ----------
        key:
            Key of which to get the associated path collection.

        Returns
        -------

        """
        from ansys.dpf.core.collection import StringCollection
        return StringCollection(collection=self._api.data_sources_get_new_path_collection_for_key(self, key))

    def get_new_collection_for_results_path(self):
        """

        Returns
        -------

        """
        from ansys.dpf.core.collection import StringCollection
        return StringCollection(collection=self._api.data_sources_get_new_collection_for_results_path(self))

    def __len__(self) -> int:
        return self.get_size()

    def get_size(self) -> int:
        """Get the number of paths in the DataSources.

        Returns
        -------

        """
        return self._api.data_sources_get_size(self)

    def __getitem__(self, item) -> str:
        return self.get_path_by_path_index(item)

    def get_path_by_path_index(self, index) -> str:
        """Get the path at the given index in the DataSources.

        Parameters
        ----------
        index:
            Index of the path in the DataSources.

        Returns
        -------

        """
        return self._api.data_sources_get_path_by_path_index(self, index)

    def get_key_by_path_index(self, index) -> str:
        """Get the key for the path at the given index in the DataSources.

        Parameters
        ----------
        index:
            Index of the path in the DataSources.

        Returns
        -------
        key:
            Key of the path at the given index in the DataSources.
        """
        return self._api.data_sources_get_key_by_path_index(self, index)

    def get_label_space_by_path_index(self, index) -> LabelSpace:
        """

        Parameters
        ----------
        index:
            Index of the path in the DataSources.

        Returns
        -------
        label_space:
            LabelSpace associated to the path at the given index.
        """
        from ansys.dpf.core.label_space import LabelSpace
        return LabelSpace(self._api.data_sources_get_label_space_by_path_index(self, index))


