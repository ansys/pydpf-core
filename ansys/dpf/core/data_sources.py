"""
.. _ref_data_sources:
    
DataSources
===========
"""
import os

from ansys import dpf
from ansys.grpc.dpf import data_sources_pb2, data_sources_pb2_grpc, base_pb2
from ansys.dpf.core.errors import protect_grpc


class DataSources:
    """The data sources is a container of files on which the analysis results can be found.
     An extension key ('rst' for example) is used to choose which files represent results files,
     the other one being accessory files.
     A result file path can be set in the DataSOurces initializer.
   
    Parameters
    ----------
    result_path : str, optional
        path of the result

    data_sources : ansys.grpc.dpf.data_sources_pb2.DataSources
        gRPC data sources message.

    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    Initialize a model from a result path
    >>> from ansys.dpf import core as dpf
    >>> my_data_sources = dpf.DataSources('file.rst')
    >>> my_data_sources.result_files
    ['file.rst']
    
    """

    def __init__(self, result_path=None, data_sources=None, server=None):
        """Initialize connection with the server"""
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
        """Connect to the grpc service"""
        return data_sources_pb2_grpc.DataSourcesServiceStub(self._server.channel)

    def set_result_file_path(self, filepath, key=""):
        """Add a result file path to the datasources. 
        The result file path key is used to choose the right plugin 
        when a result is asked with an Operator. 

        Parameters
        ----------
        filepath : str
            Path to the result file.

        key : str, optional
            Extension of the file, found directly if it is not set.

        Examples
        --------
        Create a data source and set the result file path

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
        """Add a result file path by domain. This method can be called to 
        to handle files created by a distributed solve.
        
        Parameters
        ----------
        path: str
            Path to the file.
                
        domain_id: int, optional, default is 0
            Domain id for distributed files.
            
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

    def add_file_path(self, filepath, key="", is_domain: bool = False, domain_id = 0):
        """Add a file path to the data sources. The files not added as
        result files are accessory files used to access accessory information
        not present in the result files.

        Parameters
        ----------
        filepath : str
            Path of the file.
            
        key : str, optional
            Extension of the file, found directly if it is not set.
            
        is_domain: bool
            file_path is domain_path

        domain_id: int, optional, default is 0
            Domain id for distributed files.
            Must be set with domain_path = True to be taken into account. 

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
        
    def add_file_path_for_specified_result(self, filepath, key="", result_key = ""):
        """Add a file path to the data sources. The files not added as
        result files are accessory files used to access accessory information
        not present in the result files. Using the ``'specified_result'`` option
        is used when several results files with different results keys are used 
        in the data sources. For example, if a solve used 2 different solvers
        which generated 2 different sets of files, this method can be used.

        Parameters
        ----------
        filepath : str
            Path of the file.
            
        key : str, optional
            Extension of the file, found directly if it is not set.
            
        result_key: str, optional
            Extension of the result file with which this file path belongs.
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

    def add_upstream(self, upstream_data_sources, result_key=""):
        """Add an upstream datasources.

        This is used to add a set of path creating an upstream for
        recursive workflows.

        Parameters
        ----------
        upstream_data_sources : DataSources
        
        result_key: str, optional
            Extension of the result file group with which this upstream belongs

        """
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstream_data_sources._message)
        request.data_sources.CopyFrom(self._message)
        if hasattr(request, "result_key"):
            request.result_key = result_key
        self._stub.UpdateUpstream(request)
        
    def add_upstream_for_domain(self, upstream_data_sources, domain_id):
        """Add an upstream datasources.

        This is used to add a set of path creating an upstream for
        recursive workflows.

        Parameters
        ----------
        upstream_data_sources : DataSources
        
        domain_id: int
            Domain id for distributed files.

        """
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstream_data_sources._message)
        request.data_sources.CopyFrom(self._message)
        request.domain.domain_path = True
        request.domain.domain_id = domain_id
        self._stub.UpdateUpstream(request)

    @property
    def result_key(self):
        """Returns the result key used by the data sources
        
        Returns
        ----------
        result_key : str
        """
        return self._info["result_key"]

    @property
    def result_files(self):
        """Returns the list of result files contained
        by the data sources
        
        Returns
        ----------
        result_files : list of str
        """
        key = self.result_key
        if (key == ''): 
            return None
        else: 
            return self._info["paths"][key]

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
        """Describe the entity
        
        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description
        return _description(self._message, self._server)

    def __del__(self):
        try:  # should silently fail
            self._stub.Delete(self._message)
        except:
            pass
