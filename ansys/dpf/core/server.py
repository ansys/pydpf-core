"""Contains the directives necessary to start the dpf server."""
from threading import Thread
import io
import platform
import logging
import time
import os
import socket
import subprocess
import grpc
import requests

from ansys import dpf
from ansys.dpf.core.errors import InvalidPortError
from ansys.dpf.core.misc import find_ansys, is_ubuntu
from ansys.dpf.core.core import BaseService
from ansys.dpf.core import errors

MAX_PORT = 65535

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')

# default DPF server port
DPF_DEFAULT_PORT = 50054
LOCALHOST = '127.0.0.1'


def _global_channel():
    """Return the global channel if it exists.

    If the global channel has not been specified, check if the user
    has specified the "DPF_START_SERVER" environment variable.  If
    ``True``, start the server locally.  If ``False``, connect to the
    existing server.
    """
    if dpf.core.CHANNEL is None:
        if os.environ.get('DPF_START_SERVER', '').lower() == 'false':
            ip = os.environ.get('DPF_IP', LOCALHOST)
            port = int(os.environ.get('DPF_PORT', DPF_DEFAULT_PORT))
            connect_to_server(ip, port)
        else:
            start_local_server()

    return dpf.core.CHANNEL


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


def close_servers():
    """Close all active servers created by this module"""
    from ansys.dpf.core import _server_instances
    for instance in _server_instances:
        instance.shutdown()


def start_local_server(ip=LOCALHOST, port=DPF_DEFAULT_PORT,
                       ansys_path=None, as_global=True):
    """Start a new local DPF server at a given port and ip.

    Requires Windows and ANSYS v211 or newer be installed.

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

    Returns
    -------
    port : int
        Port server was launched on.
    """
    if ansys_path is None:
        ansys_path = os.environ.get('AWP_ROOT211', find_ansys())
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
    except ValueError:
        raise ValueError(f'Unable to get version from the Ansys path "{ansys_path}"')
    if ver < 211:
        raise errors.InvalidANSYSVersionError(f'Ansys v{ver} does not support DPF')
    if ver == 211 and is_ubuntu():
        raise OSError('DPF on v211 does not support Ubuntu')

    # avoid using any ports in use from existing servers
    used_ports = [srv.port for srv in dpf.core._server_instances]
    while port in used_ports:
        port += 1

    # verify port is free
    while port_in_use(port):
        port += 1

    server = None
    n_attempts = 10
    for _ in range(n_attempts):
        try:
            server = DpfServer(ansys_path, ip, port, as_global, as_global)
            break
        except InvalidPortError:  # allow socket in use errors
            port += 1

    if server is None:
        raise OSError(f'Unable to launch the server after {n_attempts} attempts.  '
                      'Check the following path:\n{ansys_path}\n\n'
                      'or attempt to use a different port')

    dpf.core._server_instances.append(server)
    return server.port


class DpfServer:
    """Starts the DPF server locally

    Parameters
    ----------
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
        Automatically load the mesh and mapdl operators

    ansys_path : str, optional
        Path containing ansys.  For example ``/ansys_inc/v212/``
    """

    def __init__(self, ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT,
                 timeout=10, as_global=True, load_operators=True):
        """Start the dpf server server"""
        self._process = None

        # check valid ip and port
        check_valid_ip(ip)
        if not isinstance(port, int):
            raise ValueError('Port must be an integer')

        if os.name == 'posix':
            if 'ubuntu' in platform.platform().lower():
                raise OSError('DPF does not support Ubuntu')
            raise NotImplementedError()
            # self._process = launch_linux_local()
        elif os.name == 'nt':
            self._process = launch_dpf_windows(ansys_path, ip, port)
        else:
            NotImplementedError('OS {os.name} not supported')

        channel = grpc.insecure_channel('%s:%d' % (ip, port))
        BaseService(channel, timeout=1, load_operators=load_operators)

        # assign to global channel when requested
        if as_global:
            dpf.core.CHANNEL = channel

        # store port and ip for later reference
        self.ip = ip
        self.port = port
        self.live = True

    def shutdown(self):
        if self._process is not None:
            self._process.kill()
            self.live = False

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


def launch_dpf_windows(ansys_path, ip=LOCALHOST, port=DPF_DEFAULT_PORT, timeout=10):
    """Launch ANSYS DPF on Windows.

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
    # append ansys libs to path
    paths = [r'\tp\IntelMKL\2020.0.166\winx64\\',
             r'\tp\IntelCompiler\2019.3.203\winx64\\',
             r'\tp\hdf5\1.8.14\winx64\\',
             r'\tp\CFFSDK\lib\winx64']

    add_path = ';'.join([ansys_path + path for path in paths])
    run_cmd = f'Ans.Dpf.Grpc.exe --address {ip} --port {port}'

    # verify ansys path is valid
    dpf_run_dir = f'{ansys_path}/aisol/bin/winx64'
    if not os.path.isdir(dpf_run_dir):
        raise NotADirectoryError(f'Invalid ansys path at "{ansys_path}".  '
                                 'Unable to locate the directory containing DPF at '
                                 f'"{dpf_run_dir}"')

    dpf_bin = os.path.join(dpf_run_dir, 'Ans.Dpf.Grpc.exe')
    if not os.path.isfile(dpf_bin):
        raise FileNotFoundError('Unable to locate the DPF executable at '
                                f'"{dpf_bin}"')

    old_dir = os.getcwd()
    os.chdir(dpf_run_dir)
    env = dict(os.environ)
    env['PATH'] = add_path + env['PATH']
    process = subprocess.Popen(run_cmd, env=env,
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
            raise InvalidPortError(f'Port {port} in use')
        raise RuntimeError(errstr)

    return process
