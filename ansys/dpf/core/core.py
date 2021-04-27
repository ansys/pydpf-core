"""
Core
====
"""
import os
import logging
import time

import grpc

from ansys import dpf
from ansys.grpc.dpf import base_pb2, base_pb2_grpc
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.errors import protect_grpc

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')
DEFAULT_FILE_CHUNK_SIZE =65536

if 'DPF_CONFIGURATION' in os.environ:
    CONFIGURATION = os.environ['DPF_CONFIGURATION']
else:
    CONFIGURATION = 'release'

def load_library(filename, name='', symbol="LoadOperators", server=None):
    """Dynamically load an operators library for dpf.core.

    Parameters
    ----------
    filename : str
        Filename of the operator library.

    name : str, optional
        Library name.  Probably optional
        
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    Load the mapdl operators for Linux

    >>> from ansys.dpf import core as dpf
    >>> dpf.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')

    Load a new operators library

    >>> dpf.load_library('someNewOperators.so', 'new_operators')

    """
    base = BaseService(server, load_operators=False)    
    base.load_library(filename, name, symbol)
    return name+ " successfully loaded";

def upload_file_in_tmp_folder(file_path, new_file_name=None, server=None):
    """Upload a file from the client to the server in a temporary folder 
    deleted when the server is shutdown
    
    Parameters
    ----------
    file_path : str
        file path on the client side to upload
        
    new_file_name : str, optional
        name to give to the file server side, 
        if no name is specified, the same name as the input file is given
        
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
        
    Returns
    -------
      server_file_path : str
           path generated server side
          
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> file_path = dpf.upload_file_in_tmp_folder(examples.static_rst)
    """
    base = BaseService(server, load_operators=False)    
    return base.upload_file_in_tmp_folder(file_path, new_file_name)

def download_file(server_file_path, to_client_file_path, server=None):
    """Download a file from the server to the target client file path
    
    Parameters
    ----------
    server_file_path : str
        file path to dowload on the server side
        
    to_client_file_path: str
        file path target where the file will be located client side
        
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> import os
    >>> file_path = dpf.upload_file_in_tmp_folder(examples.static_rst)
    >>> core.download_file(file_path, examples.static_rst)
    """
    base = BaseService(server, load_operators=False)    
    return base.download_file(server_file_path, to_client_file_path)

        
def upload_file(file_path, to_server_file_path, server=None):
    """Upload a file from the client to the target server file path
    
    Parameters
    ----------
    file_path : str
        file path on the client side to upload
        
    to_server_file_path: str
        file path target where the file will be located server side
    
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
        
    Returns
    -------
    server_file_path : str
        path generated server side
    """
    base = BaseService(server, load_operators=False)    
    return base.upload_file(file_path, to_server_file_path)
        
    

class BaseService():
    """Base service connection to dpf server.  Used to load operators.

    Parameters
    ----------
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    timeout : float, optional
        Fails when a connection takes longer than ``timeout`` seconds
        to initialize.
    
    load_operators : bool, optional
        Automatically load the math operators

    Examples
    --------
    Connect to an existing DPF server
    >>> from ansys.dpf import core as dpf
    >>> import grpc
    >>> server = dpf.connect_to_server(ip='127.0.0.1', port = 50054)
    >>> core.BaseService(server=server)
    """

    def __init__(self, server=None, load_operators=True, timeout=5):
        """Initialize base service"""

        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect(timeout)

        # these operators are included by default in v211
        if load_operators:
            self._load_math_operators()
            self._load_hdf5_operators()

    def _connect(self, timeout=5):
        """Connect to dpf service within a given timeout"""
        stub = base_pb2_grpc.BaseServiceStub(self._server.channel)

        # verify connected
        if timeout is not None:
            state = grpc.channel_ready_future(self._server.channel)
            tstart = time.time()
            while (time.time() - tstart) < timeout and not state._matured:
                time.sleep(0.01)

            if not state._matured:
                raise IOError(f'Unable to connect to DPF instance at {self._server._input_ip} {self._server._input_port}')

        return stub

    @protect_grpc
    def load_library(self, filename, name='', symbol="LoadOperators"):
        """Dynamically load an operators library for dpf.core.

        Parameters
        ----------
        filename : str
            Filename of the operator library.

        name : str, optional
            Library name.  Probably optional

        Examples
        --------
        Load the mapdl operators for Linux

        >>> from ansys.dpf import core as dpf
        >>> base = dpf.BaseService()
        >>> base.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')

        Load a new operators library

        >>> base.load_library('someNewOperators.so', 'new_operators')

        """
        request = base_pb2.PluginRequest()
        request.name = name
        request.dllPath = filename
        request.symbol = symbol
        try:
            self._stub.Load(request)
        except Exception as e:
            raise IOError(f'Unable to load library "{filename}". File may not exist or'
                          f' is missing dependencies:\n{str(e)}')


    def _load_hdf5_operators(self):
        """Load HDF5 operators"""
        operator_name = 'hdf5'
        try:
            self.load_library('libAns.Dpf.Hdf5.so', operator_name)
        except:
            pass

        if CONFIGURATION == "release":
            self.load_library('Ans.Dpf.Hdf5.dll', operator_name)
        else:
            self.load_library('Ans.Dpf.Hdf5D.dll', operator_name)

    def _load_math_operators(self):
        """Load math operators"""
        operator_name = 'math'
        try:
            self.load_library('libAns.Dpf.Math.so', operator_name)
        except:
            pass
        try:
            if CONFIGURATION == "release":
                self.load_library('Ans.Dpf.Math.dll', operator_name)
            else:
                self.load_library('Ans.Dpf.MathD.dll', operator_name)
        except:
            pass
    
    @property
    def server_info(self):
        """Send the request for server informations and keep 
           the info into a dictionnary
           
           Returns
           -------
           info : dictionnary
               dictionnary with "server_ip", "server_port", "server_process_id"
               "server_version" keys
        """
        request = base_pb2.ServerInfoRequest()
        try:
            response = self._stub.GetServerInfo(request)
        except Exception as e:
            raise IOError(f'Unable to recover informations from the server:\n{str(e)}')
        out = {"server_ip":response.ip, "server_port":response.port, "server_process_id":response.processId,
               "server_version": str(response.majorVersion) +"."+str(response.minorVersion)}
        return out
    
    
    def _description(self, dpf_entity_message):
        """Ask the server to describe the entity in input
        
        Parameters
        ----------
        dpf_entity_message : core.Operator._message, core.Workflow._message, core.Scoping._message, core.Field._message,
        core.FieldContainer._message, core.MeshedRegion._message...
        
        Returns
        -------
           description : str
        """
        request = base_pb2.DescribeRequest()
        request.dpf_type_id = dpf_entity_message.id
        return self._stub.Describe(request).description
    
    
    @protect_grpc
    def download_file(self, server_file_path, to_client_file_path):
        """Download a file from the server to the target client file path
        
        Parameters
        ----------
        server_file_path : str
            file path to dowload on the server side
            
        to_client_file_path: str
            file path target where the file will be located client side
        """
        request = base_pb2.DownloadFileRequest()
        request.server_file_path = server_file_path
        chunks = self._stub.DownloadFile(request)
        with open(to_client_file_path, 'wb') as f:
            for chunk in chunks:
                f.write(chunk.data.data)
    
    @protect_grpc
    def upload_file(self, file_path, to_server_file_path):
        """Upload a file from the client to the target server file path
        
        Parameters
        ----------
        file_path : str
            file path on the client side to upload
            
        to_server_file_path: str
            file path target where the file will be located server side
            
        Returns
        -------
           server_file_path : str
               path generated server side
        """
        if os.stat(file_path).st_size==0:
            raise ValueError(file_path+" is empty")
        return self._stub.UploadFile(self.__file_chunk_yielder(file_path, to_server_file_path)).server_file_path
        
    @protect_grpc
    def upload_file_in_tmp_folder(self, file_path, new_file_name=None):
        """Upload a file from the client to the server in a temporary folder 
        deleted when the server is shutdown
        
        Parameters
        ----------
        file_path : str
            file path on the client side to upload
            
        new_file_name (optional): str
            name to give to the file server side, 
            if no name is specified, the same name as the input file is given
            
        Returns
        -------
           server_file_path : str
               path generated server side
        """
        if new_file_name:
            file_name = new_file_name
        else:
            file_name = os.path.basename(file_path)
        if os.stat(file_path).st_size==0:
            raise ValueError(file_path+" is empty")
        return self._stub.UploadFile(self.__file_chunk_yielder(file_path=file_path, to_server_file_path=file_name, use_tmp_dir=True)).server_file_path
    
    def _prepare_shutdown(self):
        self._stub.PrepareShutdown(base_pb2.Empty())
        
        
        
    def __file_chunk_yielder(self,file_path, to_server_file_path, use_tmp_dir=False):
        request = base_pb2.UploadFileRequest()
        request.server_file_path = to_server_file_path
        request.use_temp_dir=use_tmp_dir
        
        with open(file_path, 'rb') as f:
            while True:
                piece = f.read(DEFAULT_FILE_CHUNK_SIZE)
                if len(piece)==0:
                    return
                request.data.data = piece
                yield request
                
                

        
        