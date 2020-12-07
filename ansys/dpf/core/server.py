"""Contains the directives necessary to start the dpf server."""
import logging
import time
import os
import signal
import socket
import subprocess
import grpc
import requests

from ansys import dpf
from ansys.dpf.core.core import BaseService

MAX_PORT = 65535

if 'ANSYS_PATH' in os.environ:
    ANSYS_PATH = os.environ['ANSYS_PATH']
else:
    ANSYS_PATH = None

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')

# default DPF server port
DPF_DEFAULT_PORT = 50054
LOCALHOST = '127.0.0.1'

# INSTANCES = []

# @atexit.register
# def exit_dpf():
#     for instance in INSTANCES:
#         pid = instance.pid
#         sys.kill(pid)


def _global_channel():
    """Return the global channel if it exists.

    If the global channel has not been specified, check if the user
    has specified the "DPF_START_SERVER" enviornment variable.  If
    ``True``, start the server locally.  If ``False``, connect to the
    existing server.
    """
    if dpf.core.CHANNEL is None:
        if 'DPF_START_SERVER' in os.environ:
            if os.environ['DPF_START_SERVER'].lower() == 'false':
                ip = os.environ.get('DPF_IP', '127.0.0.1')
                port = int(os.environ.get('DPF_PORT', DPF_DEFAULT_PORT))
                connect_to_server(ip, port)
        else:
            # start the local server...
            # raise NotImplementedError

            raise ValueError('Please start the dpf server with dpf.core.start_local_instance or dpf.core.start_instance_using_service_manager or set the Global DPF channel with dpf.core.CHANNEL =')

    return dpf.core.CHANNEL


def port_in_use(port):
    """Checks if a port is in use on localhost.  Returns True when
    port in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def check_valid_ip(ip):
    """Raises an error when an invalid ip is entered"""
    try:
        socket.inet_aton(ip)
    except OSError:
        raise ValueError(f'Invalid IP address "{ip}"')
        
def close_servers():
    if hasattr(dpf,'_server_instances'):
        for server in dpf.core._server_instances:
            server.shutdown()

def start_server_using_service_manager():
    if dpf.core.module_exists("grpc_interceptor_headers") :
        import grpc_interceptor_headers
        from  grpc_interceptor_headers.header_manipulator_client_interceptor import header_adder_interceptor    
    else:
        raise ValueError('Module grpc_interceptor_headers is missing to use service manager, please install it using pip install grpc_interceptor_headers')
        
    service_manager_url = "http://"+ip+":8089/v1"
    
    definition = requests.get(url=service_manager_url + "/definitions/dpf").json()
    rsp = requests.post(url=service_manager_url + "/jobs", json=definition)
    job = rsp.json()
    
    dpf_task = job['taskGroups'][0]['tasks'][0]
    dpf_service = dpf_task['services'][0]
    dpf_service_name = dpf_service['name']
    dpf_url = f"{dpf_service['host']}:{dpf_service['port']}"

        
    channel = channel = grpc.insecure_channel(dpf_url)
    header_adder =  header_adder_interceptor('service-name', dpf_service_name)
    intercept_channel = grpc.intercept_channel(channel, header_adder)
    dpf.core.CHANNEL = intercept_channel
    
    dpf.core._server_instances.append(DpfJob(service_manager_url, dpf_service_name))


def start_local_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT, dpf_path=None,
                       ansys_path=None):
    if dpf_path is None:
        if 'DPF_PATH' in os.environ:
            dpf_path = os.environ['DPF_PATH']

    if dpf_path is None:
        raise ValueError('Either specify the location of the dpf executable with '
                         '"dpf_path=" or set the location the enviornment variable '
                         '"DPF_PATH"')
    elif not os.path.isfile(dpf_path):
        raise FileNotFoundError(f'DPF gRPC executable not found at {dpf_path}')
        
    if os.name == 'posix':

        if ansys_path is None:
            ansys_path =  os.environ['ANSYS_PATH']
    
        if ansys_path is None:
            err_str = 'Must specify the location of the ansys with "ansys_path=".\n\n'
            if os.name == 'posix':
                err_str += 'For example: ansys_path="/ansys_inc/v212/"'
            else:
                err_str += 'For example: ansys_path="C:\\Program Files\\ANSYS INC\v212\\'
        elif not os.path.isdir(ansys_path):
            raise NotADirectoryError(f'Invalid ansys_path {ansys_path}')
    # set ansys path to default if unavailable
        

    # acquire an unused port
    while port_in_use(port):
        port += 1
        if port > MAX_PORT:
            raise RuntimeError(f'All ports up to {MAX_PORT} in use')

    # start server and store these values as global
    dpf.core._server_instances.append(DpfServer(dpf_path, ip, port, store_as_global=True))

class DpfJob:
    def __init__(self, service_manager_url, job_name):
        self.sm_url = service_manager_url
        self.job_name = job_name
        
    def shutdown(self):
        requests.delete(url=self.sm_url + "/jobs/"+self.job_name)

    def __del__(self):
        try:
            self.shutdown()
        except:
            pass
        
class DpfServer:
    """Starts the DPF server locally

    Parameters
    ----------
    server_bin : str
        Location of the dpf executable.

    ip : str
        IP address of the remote or local instance to connect to.

    port : int
        Port to connect to the remote instance on.  Defaults to 50054
        when request_instance is False.

    timeout : float, optional
        Fails when a connection takes longer than ``timeout`` seconds
        to initialize.
        
    store_as_global : bool, optional
        Stores this ip and port as global variables for the dpf
        module.  All DPF objects created in this Python session will
        use this IP and port.
        
    load_operators : bool, optional
        Automatically load the mesh and mapdl operators

    ansys_path : str, optional
        Path containing ansys.  For example ``/ansys_inc/v212/``
    """

    def __init__(self, server_bin=None, ip=None, port=None, timeout=10, store_as_global=True,
                 load_operators=True, ansys_path=None):
        """Start the dpf server server"""

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError('Port must be an integer')

       
        env = dict(os.environ)
        # TODO: This needs to be made cross-platform...
        if os.name == 'posix':
             # use global if none
            if ansys_path is None:
                ansys_path = ANSYS_PATH
    
            if ansys_path is None:
                raise ValueError('Please set the enviornmental variable "ANSYS_PATH" '
                                 'with the directory containing ANSYS.  For example:\n'
                                 'ANSYS_PATH="/ansys_inc/v212/"')
            lib_comp_path = os.path.join(ansys_path, 'ansys/syslib/AnsMechSolverMesh/')
            mkl_path = os.path.join(ansys_path, 'tp/IntelMKL/2020.0.166/linx64/lib/intel64')
            intel_compiler_path = os.path.join(ansys_path, 'tp/IntelCompiler/2019.3.199/linx64/lib/intel64')

            export_ld_library_path = 'LD_LIBRARY_PATH=%s:%s:%s:${LD_LIBRARY_PATH}' % (lib_comp_path, intel_compiler_path, mkl_path)
            export_ld_preload = 'LD_PRELOAD=%s/libiomp5.so:%s/libmkl_core.so:%s/libmkl_gnu_thread.so' % (intel_compiler_path, mkl_path, mkl_path)

            ld_library_path = '%s:%s:%s' % (lib_comp_path, intel_compiler_path, mkl_path)
            ld_preload = '%s/libiomp5.so:%s/libmkl_core.so:%s/libmkl_gnu_thread.so' % (intel_compiler_path, mkl_path, mkl_path)

            ld_libs = []
            ld_libs.append(os.path.join(intel_compiler_path, 'libiomp5.so'))
            ld_libs.append(os.path.join(mkl_path, 'libmkl_core.so'))
            ld_libs.append(os.path.join(mkl_path, 'libmkl_gnu_thread.so'))
            for filename in ld_libs:
                if not os.path.isfile(filename):
                    raise FileNotFoundError(f'Unable to locate {filename}')
            ld_preload = ':'.join(ld_libs)
            # ld_preload = '%s/libiomp5.so:%s/libmkl_core.so:%s/libmkl_gnu_thread.so' % (intel_compiler_path, mkl_path, mkl_path)

            if not os.path.isdir(intel_compiler_path):
                raise FileNotFoundError('Unable to locate intel compiler')
            if not os.path.isdir(mkl_path):
                raise FileNotFoundError('Unable to locate mkl')
            if not os.path.isdir(lib_comp_path):
                raise FileNotFoundError('Unable to locate "AnsMechSolverMesh"')

            cmd_export = '%s;%s' % (export_ld_library_path, export_ld_preload)
            cmd = f'{cmd_export};{server_bin} --address {ip} --port {port}'

            env['LD_LIBRARY_PATH'] = ld_library_path
            env['LD_PRELOAD'] = ld_preload
            
            self._process = subprocess.Popen(cmd, shell=True, env=env,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        else:
            if server_bin is None:
                raise ValueError('Either specify the location of the dpf executable with '
                                 '"dpf_path=" or set the location the enviornment variable '
                                 '"DPF_PATH"')
            args =f' --address {ip} --port {port}'
            self._process = subprocess.Popen(server_bin + args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        # INSTANCES.append(self._process)

        time.sleep(1.0)  # let the service start
        channel = grpc.insecure_channel('%s:%d' % (ip, port))
        BaseService(channel,timeout=1, load_operators=load_operators)

        if store_as_global:
            dpf.core.CHANNEL = channel
            
        print( f"server started at --address {ip} --port {port}")

    def shutdown(self):
        if hasattr(self, '_process'):
            if hasattr(signal, 'SIGKILL'):
                os.kill(self._process.pid, signal.SIGKILL)
            else :
                os.kill(self._process.pid, signal.SIGILL)

    def __del__(self):
        try:
            self.shutdown()
        except:
            pass


def connect_to_server(ip='127.0.0.1', port=50054, timeout=5):
    """Connect to an existing dpf server.

    Set this as the global default channel that will be used for the
    duration of dpf.

    Parameters
    ----------
    ip : str, optional
        IP address of the server.  Default to localhost.

    port : int
        Port of the server.  Defaults to the default DPF port
        ``50054``.

    timeout : float
        Maximum timeout to connect to the DPF server.

    Examples
    --------
    Connect to a remote server at a non-default port

    >>> from ansys import dpf
    >>> dpf.core.connect_to_server('10.0.0.1', 50055)

    Connect to the localhost at the default port

    >>> dpf.core.connect_to_server()
    """
    channel = grpc.insecure_channel(f'{ip}:{port}')
    state = grpc.channel_ready_future(channel)

    # verify connection has matured
    tstart = time.time()
    while ((time.time() - tstart) < timeout) and not state._matured:
        time.sleep(0.01)

    if not state._matured:
        raise TimeoutError(f'Failed to connect to {ip}:{port} in {timeout} seconds')

    LOG.debug('Established connection to MAPDL gRPC')
    dpf.core.CHANNEL = channel


# TODO: def _launch_linux_local()...


# TODO: def _launch_windows_local()...


# for testing
if __name__ == '__main__':
    server_bin = None  # set this
    ip = '127.0.1.1'
    port = 50054
    timeout = 1

    DpfServer(server_bin, ip, port, timeout=1)
    print('server active')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('exiting')
            break
