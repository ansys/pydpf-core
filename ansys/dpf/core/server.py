"""
Server
======
Contains the directives necessary to start the dpf server.
"""
from threading import Thread
import io
import platform
import logging
import time
import os
import socket
import subprocess
import grpc
import psutil
import weakref
import atexit
import copy

from ansys import dpf
from ansys.dpf.core.misc import find_ansys, is_ubuntu
from ansys.dpf.core import errors

from ansys.dpf.core._version import __ansys_version__
from ansys.dpf.core import session

MAX_PORT = 65535

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')

# default DPF server port
DPF_DEFAULT_PORT =  int(os.environ.get('DPF_PORT',50054))
LOCALHOST = os.environ.get('DPF_IP','127.0.0.1')

def shutdown_global_server():
    try :
        if dpf.core.SERVER != None:
            del dpf.core.SERVER
    except:
        pass
        
atexit.register(shutdown_global_server)

def has_local_server():
    """Returns True when a local DPF gRPC server has been created"""
    return dpf.core.SERVER is not None

def _global_server():
    """Return the global server if it exists.

    If the global server has not been specified, check if the user
    has specified the "DPF_START_SERVER" environment variable.  If
    ``True``, start the server locally.  If ``False``, connect to the
    existing server.
    """
    if dpf.core.SERVER is None:
        if os.environ.get('DPF_START_SERVER', '').lower() == 'false':
            ip = os.environ.get('DPF_IP', LOCALHOST)
            port = int(os.environ.get('DPF_PORT', DPF_DEFAULT_PORT))
            connect_to_server(ip, port)
        else:
            start_local_server()
            
    return dpf.core.SERVER


def port_in_use(port, host=LOCALHOST):
    """Returns True when a port is in use at the given host.

    Must actually "bind" the address.  Just checking if we can create
    a socket is insufficient as it's possible to run into permission
    errors like:

    - An attempt was made to access a socket in a way forbidden by its
      access permissions.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
            return False
        except:
            return True


def check_valid_ip(ip):
    """Raises an error when an invalid ip is entered"""
    try:
        socket.inet_aton(ip)
    except OSError:
        raise ValueError(f'Invalid IP address "{ip}"')


def shutdown_all_session_servers():
    """Close all active servers created by this module"""
    from ansys.dpf.core import _server_instances
    copy_instances = copy.deepcopy(_server_instances)
    for instance in copy_instances:
        try:
            instance().shutdown()
        except Exception as e:
            print(e.args)
            pass


def start_local_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT,
                       ansys_path=None, as_global=True, load_operators=True):
    """Starts a new local DPF server at a given port and ip.
    Requires Windows and ANSYS v211 or newer be installed.
    If as_global is set to True (default) then the server is stored in the module
    (replacing the one stored before). Else, the user must keep a handle on 
    his/her server

    Parameters
    ----------
    ip : str
        IP address of the remote or local instance to connect to.

    port : int
        Port to connect to the remote instance on.

    ansys_path : str, optional
        Root path containing ansys.  For example ``/ansys_inc/v212/``.
        Defaults to the latest install of ANSYS.

    as_global : bool, optional
        Stores this ip and port as global variables for the dpf
        module.  All DPF objects created in this Python session will
        use this IP and port.  Default ``True``.
        
    load_operators : bool, optional
        Automatically load the math operators

    Returns
    -------
    server : server.DpfServer
    """
    if ansys_path is None:
        ansys_path = os.environ.get('AWP_ROOT'+__ansys_version__, find_ansys())
    if ansys_path is None:
        raise ValueError('Unable to automatically locate the Ansys path.  '
                         'Manually enter one when starting the server or set it '
                         'as the environment variable "ANSYS_PATH"')

    # verify path exists
    if not os.path.isdir(ansys_path):
        raise NotADirectoryError(f'Invalid Ansys path "{ansys_path}"')

    # parse the version to an int and check for supported
    try:
        ver = int(ansys_path[-3:])
        if ver < 211:
            raise errors.InvalidANSYSVersionError(f'Ansys v{ver} does not support DPF')
        if ver == 211 and is_ubuntu():
            raise OSError('DPF on v211 does not support Ubuntu')
    except ValueError:
        pass
    

    # avoid using any ports in use from existing servers    
    used_ports=[]
    if dpf.core._server_instances:
        for srv in dpf.core._server_instances:
            if srv():
                used_ports.append(srv().port)

    while port in used_ports:
        port += 1

    # verify port is free
    while port_in_use(port):
        port += 1

    server = None
    n_attempts = 10
    for _ in range(n_attempts):
        try:
            server = DpfServer(ansys_path, ip, port,as_global= as_global, load_operators = load_operators)
            break
        except errors.InvalidPortError:  # allow socket in use errors
            port += 1

    if server is None:
        raise OSError(f'Unable to launch the server after {n_attempts} attempts.  '
                      'Check the following path:\n{ansys_path}\n\n'
                      'or attempt to use a different port')

    dpf.core._server_instances.append(weakref.ref(server))
    return server


def connect_to_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT, as_global=True, timeout=5):
    """Connect to an existing dpf server.

    Set this as the global default channel that will be used for the
    duration of dpf.
    
    Parameters
    ----------
    ip : str
        IP address of the remote or local instance to connect to.

    port : int
        Port to connect to the remote instance on.
        
    as_global : bool, optional
        Stores this ip and port as global variables for the dpf
        module.  All DPF objects created in this Python session will
        use this IP and port.  Default ``True``.

    timeout : float
        Maximum timeout to connect to the DPF server.

    Examples
    --------
    
    >>> from ansys.dpf import core as dpf
        
    Create a server
    
    >>> #server = dpf.start_local_server(ip = '127.0.0.1')
    >>> #port = server.port
    
    Connect to a remote server at a non-default port

    >>> #specified_server = dpf.connect_to_server('127.0.0.1', port, as_global=False)

    Connect to the localhost at the default port

    >>> #unspecified_server = dpf.connect_to_server(as_global=False)
    
    """
    server = DpfServer(ip=ip, port=port, as_global=as_global, launch_server=False)
    dpf.core._server_instances.append(weakref.ref(server))
    return server


class DpfServer:
    """Instance of the DPF server
    
    Parameters
    -----------
    server_bin : str
        Location of the dpf executable.

    ip : str
        IP address of the remote or local instance to connect to.

    port : int
        Port to connect to the remote instance on.  Defaults to 50054.

    timeout : float, optional
        Fails when a connection takes longer than ``timeout`` seconds
        to initialize.

    as_global : bool, optional
        Stores this ip and port as global variables for the dpf
        module.  All DPF objects created in this Python session will
        use this IP and port.

    load_operators : bool, optional
        Automatically load the math operators

    ansys_path : str, optional
        Path containing ansys.  For example ``/ansys_inc/v212/``
        
   launch_server : bool, optional
        Launch the server on windows
    """

    def __init__(self, ansys_path="", ip=LOCALHOST, port=DPF_DEFAULT_PORT,
                 timeout=10, as_global=True, load_operators=True, launch_server=True):
        """Start the dpf server server"""
        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError('Port must be an integer')

        if os.name == 'posix' and 'ubuntu' in platform.platform().lower():
            raise OSError('DPF does not support Ubuntu')
        elif launch_server:
            launch_dpf(ansys_path, ip, port)        

        self.channel = grpc.insecure_channel('%s:%d' % (ip, port))
        
        if launch_server is False:
            state = grpc.channel_ready_future(self.channel)
            # verify connection has matured
            tstart = time.time()
            while ((time.time() - tstart) < timeout) and not state._matured:
                time.sleep(0.01)
        
            if not state._matured:
                raise TimeoutError(f'Failed to connect to {ip}:{port} in {timeout} seconds')
        
            LOG.debug('Established connection to DPF gRPC')
        
        # assign to global channel when requested
        if as_global:
            dpf.core.SERVER =self

        # TODO: add to PIDs ...

        # store port and ip for later reference
        self.live = True
        self.ansys_path=ansys_path
        self._input_ip = ip
        self._input_port = port
        self._own_process = launch_server
        self._session = session.Session(self)
        
    @property
    def _base_service(self):
        if not hasattr(self,"__base_service"):            
            from ansys.dpf.core.core import BaseService
            self.__base_service = BaseService(self, timeout=1)
        return self.__base_service
    
    @property
    def info(self):
        """Recover server information
           
           Returns
           -------
           info : dictionary
               dictionary with "server_ip", "server_port", "server_process_id"
               "server_version" keys
        """
        return self._base_service.server_info
    
    @property
    def ip(self):
        """Get the ip of the server
        
        Returns
        -------
        ip : str
        """
        try:
            return self._base_service.server_info["server_ip"]
        except:
            return ""
    
    @property
    def port(self):
        """Get the port of the server
        
        Returns
        -------
        port : int
        """
        try:
            return self._base_service.server_info["server_port"]
        except:
            return 0
    
    @property
    def version(self):
        """Get the version of the server
        
        Returns
        -------
        version : str
        """
        return self._base_service.server_info["server_version"]

    def __str__(self): 
        return f'DPF Server: {self.info}'

    def shutdown(self):
        if self._own_process and self.live and self._base_service:
            self._base_service._prepare_shutdown()
            p = psutil.Process(self._base_service.server_info["server_process_id"])
            p.kill()
            time.sleep(0.1)
            self.live = False
            try:
                if id(dpf.core.SERVER) == id(self):
                    dpf.core.SERVER =None
            except:
                pass
                
            try:
                for i, server in enumerate(dpf.core._server_instances):
                    if server() == self:
                        dpf.core._server_instances.remove(server)
            except:
                pass
                     
    def __eq__(self,other_server):
        """Return true, if the ip and the port are equals"""
        if isinstance(other_server, DpfServer):
            return self.ip == other_server.ip and self.port == other_server.port
        return False
    
    def __ne__(self,other_server):
        """Return true, if the ip or the port are different"""
        return not self.__eq__(other_server)
    

    
    def __del__(self):
        try:
            self.shutdown()
        except:
            pass
        
    def check_version(self, required_version, msg = None):
        """
        Check if the server version matches with a required version.
        
        Parameters
        ----------
        required_version : str
            Required version that will be compared with the server version.
        msg : str, optional
            Message to be contained in the raised Exception if versions are
            not meeting.
    
        Raises
        ------
        dpf_errors : errors
            errors.DpfVersionNotSupported is raised if failure.
    
        Returns
        -------
        bool : 
            True if the server version meets the requirement.
        """
        from ansys.dpf.core.check_version import server_meet_version_and_raise
        return server_meet_version_and_raise(required_version, self, msg)



def launch_dpf(ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10):
    """Launch ANSYS DPF.

    Parameters
    ----------
    ansys_path : str
        Full path to ANSYS.  For example:
        'C:\\Program Files\\ANSYS Inc\\v211'

    ip : str, optional
        IP address of the server.  Default to localhost.

    port : int
        Port of the server.  Defaults to the default DPF port
        ``50054``.

    Returns
    -------
    process : subprocess.Popen
        DPF Process.
    """
    if os.name == 'nt':
        run_cmd = f'Ans.Dpf.Grpc.bat --address {ip} --port {port}'
        path_in_install = "aisol/bin/winx64"
    else:
        run_cmd = ['./Ans.Dpf.Grpc.sh',f'--address {ip}',f'--port {port}']
        path_in_install = "aisol/bin/linx64"

    # verify ansys path is valid
    if os.path.isdir(f'{ansys_path}/{path_in_install}'):
        dpf_run_dir = f'{ansys_path}/{path_in_install}'
    else:
        dpf_run_dir = f'{ansys_path}'
    if not os.path.isdir(dpf_run_dir):
        raise NotADirectoryError(f'Invalid ansys path at "{ansys_path}".  '
                                 'Unable to locate the directory containing DPF at '
                                 f'"{dpf_run_dir}"')

    old_dir = os.getcwd()
    os.chdir(dpf_run_dir)
    process = subprocess.Popen(run_cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    os.chdir(old_dir)

    # check to see if the service started
    lines = []
    def read_stdout():
        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            LOG.debug(line)
            lines.append(line)

    errors = []
    def read_stderr():
        for line in io.TextIOWrapper(process.stderr, encoding="utf-8"):
            LOG.error(line)
            errors.append(line)


    # must be in the background since the process reader is blocking
    Thread(target=read_stdout, daemon=True).start()
    Thread(target=read_stderr, daemon=True).start()

    t_timeout = time.time() + timeout
    started = False
    while not started:
        started = any('server started' in line for line in lines)

        if time.time() > t_timeout:
            raise TimeoutError(f'Server did not start in {timeout} seconds')

    # verify there were no errors
    time.sleep(1)
    if errors:
        try:
            process.kill()
        except PermissionError:
            pass
        errstr = '\n'.join(errors)
        if 'Only one usage of each socket address' in errstr:
            raise errors.InvalidPortError(f'Port {port} in use')
        raise RuntimeError(errstr)
        
    
