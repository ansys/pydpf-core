"""
Core
====
"""
import os
import logging
import time
import weakref
import pathlib

import grpc

from ansys.grpc.dpf import base_pb2, base_pb2_grpc
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core import server as serverlib
from ansys.dpf.core.misc import DEFAULT_FILE_CHUNK_SIZE
from ansys.dpf.core.common import _common_progress_bar

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")

if "DPF_CONFIGURATION" in os.environ:
    CONFIGURATION = os.environ["DPF_CONFIGURATION"]
else:
    CONFIGURATION = "release"


def load_library(filename, name="", symbol="LoadOperators", server=None):
    """Dynamically load an operators library for dpf.core.
    Code containing this library's operators is generated in
    ansys.dpf.core.operators

    Parameters
    ----------
    filename : str
        Filename of the operator library.

    name : str, optional
        Library name.  Probably optional

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Examples
    --------
    Load the mesh operators for Windows (for Linux, just use
    'libmeshOperatorsCore.so' instead of 'meshOperatorsCore.dll')

    >>> from ansys.dpf import core as dpf
    >>> # dpf.load_library('meshOperatorsCore.dll', 'mesh_operators')

    """
    base = BaseService(server, load_operators=False)
    base.load_library(filename, name, symbol)
    return name + " successfully loaded"


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

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Notes
    -----
    Print a progress bar

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


def upload_files_in_folder(
    to_server_folder_path, client_folder_path, specific_extension=None, server=None
):
    """Upload all the files from a folder of the client
    to the target server folder path.

    Parameters
    ----------
    to_server_folder_path : str
        folder path target where will be uploaded files on the server side

    client_folder_path: str
        folder path where the files that must be uploaded are located
        on client side

    specific_extension (optional) : str
        copies only the files with the given extension

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Returns
    -------
    paths : list of str
        new file paths server side
    """
    base = BaseService(server, load_operators=False)
    return base.upload_files_in_folder(
        to_server_folder_path, client_folder_path, specific_extension
    )


def download_file(server_file_path, to_client_file_path, server=None):
    """Download a file from the server to the target client file path

    Parameters
    ----------
    server_file_path : str
        file path to download on the server side

    to_client_file_path: str
        file path target where the file will be located client side

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Notes
    -----
    Print a progress bar

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> import os
    >>> file_path = dpf.upload_file_in_tmp_folder(examples.static_rst)
    >>> dpf.download_file(file_path, examples.static_rst)

    """
    base = BaseService(server, load_operators=False)
    return base.download_file(server_file_path, to_client_file_path)


def download_files_in_folder(
    server_folder_path, to_client_folder_path, specific_extension=None, server=None
):
    """Download all the files from a folder of the server
    to the target client folder path

    Parameters
    ----------
    server_folder_path : str
        folder path to download on the server side

    to_client_folder_path: str
        folder path target where the files will be located client side

    specific_extension (optional) : str
        copies only the files with the given extension

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Notes
    -----
    Print a progress bar

    Returns
    -------
    paths : list of str
        new file paths client side
    """
    base = BaseService(server, load_operators=False)
    return base.download_files_in_folder(
        server_folder_path, to_client_folder_path, specific_extension
    )


def upload_file(file_path, to_server_file_path, server=None):
    """Upload a file from the client to the target server file path

    Parameters
    ----------
    file_path : str
        file path on the client side to upload

    to_server_file_path: str
        file path target where the file will be located server side

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Notes
    -----
    Print a progress bar

    Returns
    -------
    server_file_path : str
        path generated server side
    """
    base = BaseService(server, load_operators=False)
    return base.upload_file(file_path, to_server_file_path)


def make_tmp_dir_server(server=None):
    """Create a temporary folder server side. Only one temporary folder can be created
    by server instance.
    The folder will be deleted when the server is stopped.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Returns
    -------
    path : str
        path to the temporary dir
    """
    base = BaseService(server, load_operators=False)
    return base.make_tmp_dir_server()


def _description(dpf_entity_message, server=None):
    """Ask the server to describe the entity in input

    Parameters
    ----------
    dpf_entity_message : core.Operator._message, core.Workflow._message,
                         core.Scoping._message, core.Field._message,
                         core.FieldContainer._message, core.MeshedRegion._message

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Returns
    -------
       description : str
    """
    return BaseService(server, load_operators=False)._description(dpf_entity_message)


class BaseService:
    """The Base Service class allows to make generic requests to dpf's server.
    For example, information about the server can be requested,
    uploading/downloading file from and to the server can be done,
    new operators plugins can be loaded...
    Most of the request done by the BaseService class are wrapped by
    functions.

    Parameters
    ----------
    server : server.DPFServer, optional
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
    >>> #server = dpf.connect_to_server(ip='127.0.0.1', port = 50054, as_global=False)
    >>> #base = dpf.BaseService(server=server)

    """

    def __init__(self, server=None, load_operators=True, timeout=5):
        """Initialize base service"""

        if server is None:
            server = serverlib._global_server()

        self._server = weakref.ref(server)
        self._stub = self._connect(timeout)

    def _connect(self, timeout=5):
        """Connect to dpf service within a given timeout"""
        stub = base_pb2_grpc.BaseServiceStub(self._server().channel)

        # verify connected
        if timeout is not None:
            state = grpc.channel_ready_future(self._server().channel)
            tstart = time.time()
            while (time.time() - tstart) < timeout and not state._matured:
                time.sleep(0.01)

            if not state._matured:
                raise IOError(
                    f"Unable to connect to DPF instance at {self._server()._input_ip} "
                    f"{self._server()._input_port}"
                )

        return stub

    def make_tmp_dir_server(self):
        """Create a temporary folder server side. Only one temporary folder can be created
        by server instance.
        The folder will be deleted when the server is stopped.

        Returns
        -------
        path : str
            path to the temporary dir
        """
        request = base_pb2.Empty()
        return self._stub.CreateTmpDir(request).server_file_path

    def load_library(self, filename, name="", symbol="LoadOperators"):
        """Dynamically load an operators library for dpf.core.
        Code containing this library's operators is generated in
        ansys.dpf.core.operators

        Parameters
        ----------
        filename : str
            Filename of the operator library.

        name : str, optional
            Library name.  Probably optional

        Examples
        --------
        Load the mesh operators for Windows (for Linux, just use
        'libmeshOperatorsCore.so' instead of 'meshOperatorsCore.dll')

        >>> from ansys.dpf import core as dpf
        >>> base = dpf.BaseService()
        >>> # base.load_library('meshOperatorsCore.dll', 'mesh_operators')

        """
        request = base_pb2.PluginRequest()
        request.name = name
        request.dllPath = filename
        request.symbol = symbol
        try:
            self._stub.Load(request)
        except Exception as e:
            raise IOError(
                f'Unable to load library "{filename}". File may not exist or'
                f" is missing dependencies:\n{str(e)}"
            )

        # TODO: fix code generation upload posix
        import os

        if os.name != "posix":
            local_dir = os.path.dirname(os.path.abspath(__file__))
            LOCAL_PATH = os.path.join(local_dir, "operators")

            # send local generated code
            TARGET_PATH = self.make_tmp_dir_server()
            self.upload_files_in_folder(TARGET_PATH, LOCAL_PATH, "py")

            # generate code
            from ansys.dpf.core.dpf_operator import Operator

            code_gen = Operator("python_generator")
            code_gen.connect(1, TARGET_PATH)
            code_gen.connect(0, filename)
            code_gen.connect(2, False)
            code_gen.run()

            self.download_files_in_folder(TARGET_PATH, LOCAL_PATH, "py")

    @property
    def server_info(self):
        """Send the request for server information and keep
        the info into a dictionary

        Returns
        -------
        info : dictionary
            dictionary with "server_ip", "server_port", "server_process_id"
            "server_version" keys
        """
        request = base_pb2.ServerInfoRequest()
        try:
            response = self._stub.GetServerInfo(request)
        except Exception as e:
            raise IOError(f"Unable to recover information from the server:\n{str(e)}")
        out = {
            "server_ip": response.ip,
            "server_port": response.port,
            "server_process_id": response.processId,
            "server_version": str(response.majorVersion)
            + "."
            + str(response.minorVersion),
        }
        return out

    def _description(self, dpf_entity_message):
        """Ask the server to describe the entity in input

        Parameters
        ----------
        dpf_entity_message : core.Operator._message, core.Workflow._message,
                             core.Scoping._message, core.Field._message,
        core.FieldContainer._message, core.MeshedRegion._message...

        Returns
        -------
           description : str
        """
        request = base_pb2.DescribeRequest()
        request.dpf_type_id = dpf_entity_message.id
        return self._stub.Describe(request).description

    def _get_separator(self, path):
        s1 = len(path.split("\\"))
        s2 = len(path.split("/"))
        if s2 > s1:
            # Linux case
            separator = "/"
        elif s1 > s2:
            # Windows case
            separator = "\\"
        return separator

    @protect_grpc
    def download_file(self, server_file_path, to_client_file_path):
        """Download a file from the server to the target client file path

        Notes
        -----
        Print a progress bar

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
        bar = _common_progress_bar("Downloading...", unit="KB")
        bar.start()
        i = 0
        with open(to_client_file_path, "wb") as f:
            for chunk in chunks:
                f.write(chunk.data.data)
                i += len(chunk.data.data) * 1e-3
                bar.update(i)
        bar.finish()

    @protect_grpc
    def download_files_in_folder(
        self, server_folder_path, to_client_folder_path, specific_extension=None
    ):
        """Download all the files from a folder of the server
        to the target client folder path

        Parameters
        ----------
        server_folder_path : str
            folder path to download on the server side

        to_client_folder_path: str
            folder path target where the files will be located client side

        specific_extension (optional) : str
            copies only the files with the given extension

        Notes
        -----
        Print a progress bar


        Returns
        -------
        paths : list of str
            new file paths client side
        """
        request = base_pb2.DownloadFileRequest()
        request.server_file_path = server_folder_path
        chunks = self._stub.DownloadFile(request)

        num_files = 1
        if chunks.initial_metadata()[0].key == "num_files":
            num_files = int(chunks.initial_metadata()[0].value)

        bar = _common_progress_bar("Downloading...", unit="files", tot_size=num_files)
        bar.start()

        server_path = ""

        import ntpath

        client_paths = []
        f = None
        for chunk in chunks:
            if chunk.data.server_file_path != server_path:
                server_path = chunk.data.server_file_path
                if (
                    specific_extension == None
                    or pathlib.Path(server_path).suffix == "." + specific_extension
                ):
                    separator = self._get_separator(server_path)
                    server_subpath = server_path.replace(
                        server_folder_path + separator, ""
                    )
                    subdir = ""
                    split = server_subpath.split(separator)
                    n = len(split)
                    i = 0
                    to_client_folder_path_copy = to_client_folder_path
                    if n > 1:
                        while i < (n - 1):
                            subdir = split[i]
                            subdir_path = os.path.join(
                                to_client_folder_path_copy, subdir
                            )
                            if not os.path.exists(subdir_path):
                                os.mkdir(subdir_path)
                            to_client_folder_path_copy = subdir_path
                            i += 1
                    cient_path = os.path.join(
                        to_client_folder_path_copy, ntpath.basename(server_path)
                    )
                    client_paths.append(cient_path)
                    f = open(cient_path, "wb")
                    try:
                        bar.update(len(client_paths))
                    except:
                        pass
                else:
                    f = None
            if f is not None:
                f.write(chunk.data.data)
        try:
            bar.finish()
        except:
            pass
        return client_paths

    @protect_grpc
    def upload_files_in_folder(
        self, to_server_folder_path, client_folder_path, specific_extension=None
    ):
        """Upload all the files from a folder of the client
        to the target server folder path.

        Parameters
        ----------
        to_server_folder_path : str
            folder path target where will be uploaded files on the server side

        client_folder_path: str
            folder path where the files that must be uploaded are located
            on client side

        specific_extension (optional) : str
            copies only the files with the given extension

        Returns
        -------
        paths : list of str
            new file paths server side
        """
        server_paths = []
        for root, subdirectories, files in os.walk(client_folder_path):
            for subdirectory in subdirectories:
                subdir = os.path.join(root, subdirectory)
                for filename in os.listdir(subdir):
                    f = os.path.join(subdir, filename)
                    server_paths = self._upload_and_get_server_path(
                        specific_extension,
                        f,
                        filename,
                        server_paths,
                        to_server_folder_path,
                        subdirectory,
                    )
            for file in files:
                f = os.path.join(root, file)
                server_paths = self._upload_and_get_server_path(
                    specific_extension, f, file, server_paths, to_server_folder_path
                )
            break
        return server_paths

    def _upload_and_get_server_path(
        self,
        specific_extension,
        f,
        filename,
        server_paths,
        to_server_folder_path,
        subdirectory=None,
    ):
        separator = self._get_separator(to_server_folder_path)

        if subdirectory is not None:
            to_server_file_path = (
                to_server_folder_path + separator + subdirectory + separator + filename
            )
        else:
            to_server_file_path = to_server_folder_path + separator + filename
        if ((specific_extension is not None) and (f.endswith(specific_extension))) or (
            specific_extension is None
        ):
            server_path = self._stub.UploadFile(
                self.__file_chunk_yielder(
                    file_path=f, to_server_file_path=to_server_file_path
                )
            ).server_file_path
            server_paths.append(server_path)
        return server_paths

    @protect_grpc
    def upload_file(self, file_path, to_server_file_path):
        """Upload a file from the client to the target server file path

        Parameters
        ----------
        file_path : str
            file path on the client side to upload

        to_server_file_path: str
            file path target where the file will be located server side

        Notes
        -----
        Print a progress bar

        Returns
        -------
           server_file_path : str
               path generated server side
        """
        if os.stat(file_path).st_size == 0:
            raise ValueError(file_path + " is empty")
        return self._stub.UploadFile(
            self.__file_chunk_yielder(file_path, to_server_file_path)
        ).server_file_path

    @protect_grpc
    def upload_file_in_tmp_folder(self, file_path, new_file_name=None):
        """Upload a file from the client to the server in a temporary folder
        deleted when the server is shutdown

        Parameters
        ----------
        file_path : str
            file path on the client side to upload

        new_file_name : str, optional
            name to give to the file server side,
            if no name is specified, the same name as the input file is given

        Notes
        -----
        Print a progress bar

        Returns
        -------
           server_file_path : str
               path generated server side
        """
        if new_file_name:
            file_name = new_file_name
        else:
            file_name = os.path.basename(file_path)
        if os.stat(file_path).st_size == 0:
            raise ValueError(file_path + " is empty")
        return self._stub.UploadFile(
            self.__file_chunk_yielder(
                file_path=file_path, to_server_file_path=file_name, use_tmp_dir=True
            )
        ).server_file_path

    def _prepare_shutdown(self):
        self._stub.PrepareShutdown(base_pb2.Empty())

    def __file_chunk_yielder(self, file_path, to_server_file_path, use_tmp_dir=False):
        request = base_pb2.UploadFileRequest()
        request.server_file_path = to_server_file_path
        request.use_temp_dir = use_tmp_dir

        tot_size = os.path.getsize(file_path) * 1e-3

        need_progress_bar = tot_size > 10000
        if need_progress_bar:
            bar = _common_progress_bar("Uploading...", "KB", tot_size)
            bar.start()
        i = 0
        with open(file_path, "rb") as f:
            while True:
                piece = f.read(DEFAULT_FILE_CHUNK_SIZE)
                if len(piece) == 0:
                    break
                request.data.data = piece
                yield request
                i += len(piece) * 1e-3
                if need_progress_bar:
                    try:
                        bar.update(min(i, tot_size))
                    except:
                        pass

        if need_progress_bar:
            try:
                bar.finish()
            except:
                pass
