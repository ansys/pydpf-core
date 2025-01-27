# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Core."""

import logging
import os
from pathlib import Path
import warnings
import weakref

from ansys.dpf.core import errors, misc, server as server_module
from ansys.dpf.core.check_version import server_meet_version, version_requires
from ansys.dpf.core.runtime_config import (
    RuntimeClientConfig,
    RuntimeCoreConfig,
)
from ansys.dpf.gate import (
    collection_capi,
    collection_grpcapi,
    data_processing_capi,
    data_processing_grpcapi,
    integral_types,
    object_handler,
    tmp_dir_capi,
    tmp_dir_grpcapi,
)

try:
    from grpc import _channel  # noqa: F401

    # weirdly necessary to delete LegacyGrpcError
except ImportError:
    pass

LOG = logging.getLogger(__name__)
LOG.setLevel("DEBUG")

if "DPF_CONFIGURATION" in os.environ:
    CONFIGURATION = os.environ["DPF_CONFIGURATION"]
else:
    CONFIGURATION = "release"


def load_library(filename, name="", symbol="LoadOperators", server=None, generate_operators=False):
    """Dynamically load an operators library for dpf.core.

    Code containing this library's operators is generated in
    ansys.dpf.core.operators

    Parameters
    ----------
    filename : str or os.PathLike
        Filename of the operator library.

    name : str, optional
        Library name.  Probably optional

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    generate_operators : bool, optional
        Whether operators code generation should be done or not (default is False).

    Examples
    --------
    Load the mesh operators for Windows (for Linux, just use
    'libmeshOperatorsCore.so' instead of 'meshOperatorsCore.dll')

    >>> from ansys.dpf import core as dpf
    >>> # dpf.load_library('meshOperatorsCore.dll', 'mesh_operators')

    """
    base = BaseService(server, load_operators=False)
    base.load_library(filename, name, symbol, generate_operators)
    return name + " successfully loaded"


def upload_file_in_tmp_folder(file_path, new_file_name=None, server=None):
    """Upload a file from the client to a temporary server folder deleted on server shutdown.

    Parameters
    ----------
    file_path : str or os.PathLike
        file path on the client side to upload

    new_file_name : str, optional
        name to give to the file server side,
        if no name is specified, the same name as the input file is given

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
      server_file_path : str
           path generated server side

    Notes
    -----
    Is not implemented for usage with type(server)=
    :class:`ansys.dpf.core.server_types.InProcessServer`.
    """
    base = BaseService(server, load_operators=False)
    return base.upload_file_in_tmp_folder(file_path, new_file_name)


def upload_files_in_folder(
    to_server_folder_path, client_folder_path, specific_extension=None, server=None
):
    """Upload all the files from a folder of the client to the target server folder path.

    Parameters
    ----------
    to_server_folder_path : str or os.PathLike
        folder path target where will be uploaded files on the server side

    client_folder_path: str or os.PathLike
        folder path where the files that must be uploaded are located
        on client side

    specific_extension (optional) : str
        copies only the files with the given extension

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

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
    """Download a file from the server to the target client file path.

    Parameters
    ----------
    server_file_path : str or os.PathLike
        file path to download on the server side

    to_client_file_path: str or os.PathLike
        file path target where the file will be located client side

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Notes
    -----
    Is not implemented for usage with type(server)=
    :class:`ansys.dpf.core.server_types.InProcessServer`.
    """
    base = BaseService(server, load_operators=False)
    return base.download_file(server_file_path, to_client_file_path)


def download_files_in_folder(
    server_folder_path, to_client_folder_path, specific_extension=None, server=None
):
    """Download all the files from a folder of the server to the target client folder path.

    Parameters
    ----------
    server_folder_path : str or os.PathLike
        folder path to download on the server side

    to_client_folder_path: str or os.PathLike
        folder path target where the files will be located client side

    specific_extension (optional) : str
        copies only the files with the given extension

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

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
    """Upload a file from the client to the target server file path.

    Parameters
    ----------
    file_path : str or os.PathLike
        file path on the client side to upload

    to_server_file_path: str or os.PathLike
        file path target where the file will be located server side

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
    server_file_path : str
        path generated server side
    """
    base = BaseService(server, load_operators=False)
    return base.upload_file(file_path, to_server_file_path)


def make_tmp_dir_server(server=None):
    """Create a temporary folder server side. Only one temporary folder can be created by server instance.

    The folder will be deleted when the server is stopped.

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
    path : str
        path to the temporary dir
    """
    base = BaseService(server, load_operators=False)
    return base.make_tmp_dir_server()


def _description(dpf_entity_message, server=None):
    """Ask the server to describe the entity in input.

    Parameters
    ----------
    dpf_entity_message : core.Operator._message, core.Workflow._message,
                         core.Scoping._message, core.Field._message,
                         core.FieldContainer._message, core.MeshedRegion._message

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
       description : str
    """
    try:
        return BaseService(server, load_operators=False)._description(dpf_entity_message)
    except:
        return ""


def _deep_copy(dpf_entity, server=None):
    """Return a copy of the entity in the requested server.

    Parameters
    ----------
    dpf_entity: core.Operator, core.Workflow, core.Scoping,
                core.Field, core.FieldsContainer, core.MeshedRegion...
        Dpf entity to deep_copy

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Returns
    -------
       deep_copy of dpf_entity: core.Operator, core.Workflow, core.Scoping,
                                core.Field, core.FieldsContainer, core.MeshedRegion...
    """
    from ansys.dpf.core.common import types, types_enum_to_types
    from ansys.dpf.core.operators.serialization import serializer_to_string, string_deserializer

    entity_server = dpf_entity._server if hasattr(dpf_entity, "_server") else None
    serializer = serializer_to_string(server=entity_server)
    serializer.connect(1, dpf_entity)
    deserializer = string_deserializer(server=server)
    stream_type = 1 if server_meet_version("8.0", serializer._server) else 0
    serializer.connect(-1, stream_type)
    if stream_type == 1:
        out = serializer.get_output(0, types.bytes)
    else:
        out = serializer.outputs.serialized_string  # Required for retro with 241
    deserializer.connect(-1, stream_type)
    deserializer.connect(0, out)
    type_map = types_enum_to_types()
    output_type = list(type_map.keys())[list(type_map.values()).index(dpf_entity.__class__)]
    return deserializer.get_output(1, output_type)


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
        ``None``, attempts to use the global server.

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
        """Initialize base service."""
        # step 1: get server
        if server is None:
            server = server_module.get_or_create_server(server)
        self._server = weakref.ref(server)
        self._collection_api = None

        # step 2: get api
        self._api = self._server().get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
        )
        self._api_tmp_dir = self._server().get_api_for_type(
            capi=tmp_dir_capi.TmpDirCAPI, grpcapi=tmp_dir_grpcapi.TmpDirGRPCAPI
        )

        # step3: init environment
        self._api.init_data_processing_environment(self)  # creates stub when gRPC

    def make_tmp_dir_server(self):
        """Create a temporary folder server side. Only one temporary folder can be created by server instance.

        The folder will be deleted when the server is stopped.

        Returns
        -------
        path : str
            path to the temporary dir
        """
        if self._server().has_client():
            return self._api_tmp_dir.tmp_dir_get_dir_on_client(client=self._server().client)
        else:
            return self._api_tmp_dir.tmp_dir_get_dir()

    def load_library(self, file_path, name="", symbol="LoadOperators", generate_operators=False):
        """Dynamically load an operators library for dpf.core.

        Code containing this library's operators is generated in
        ansys.dpf.core.operators

        Parameters
        ----------
        file_path : str or os.PathLike
            file_path of the operator library.

        name : str, optional
            Library name.  Probably optional

        generate_operators : bool, optional
            Whether operators code generation should be done or not (default is False).

        Examples
        --------
        Load the mesh operators for Windows (for Linux, just use
        'libmeshOperatorsCore.so' instead of 'meshOperatorsCore.dll')

        >>> from ansys.dpf import core as dpf
        >>> base = dpf.BaseService()
        >>> # base.load_library('meshOperatorsCore.dll', 'mesh_operators')

        """
        file_path = str(file_path)
        if self._server().has_client():
            self._internal_obj = self._api.data_processing_load_library_on_client(
                sLibraryKey=name,
                sDllPath=file_path,
                sloader_symbol=symbol,
                client=self._server().client,
            )
        else:
            self._internal_obj = self._api.data_processing_load_library(
                name=name, dllPath=file_path, symbol=symbol
            )
        if generate_operators:
            # TODO: fix code generation upload posix
            # https://github.com/ansys/pydpf-core/issues/1984, todo was added in this PR

            def __generate_code(TARGET_PATH, filename, name, symbol):
                from ansys.dpf.core.dpf_operator import Operator

                try:
                    code_gen = Operator("python_generator")
                    code_gen.connect(1, TARGET_PATH)
                    code_gen.connect(0, filename)
                    code_gen.connect(2, symbol)
                    code_gen.connect(3, name)
                    code_gen.run()
                except Exception as e:
                    warnings.warn("Unable to generate the python code with error: " + str(e.args))

            local_dir = Path(__file__).parent
            LOCAL_PATH = local_dir / "operators"
            if not self._server().local_server:
                if self._server().os != "posix" or (not self._server().os and os.name != "posix"):
                    # send local generated code
                    TARGET_PATH = self.make_tmp_dir_server()
                    self.upload_files_in_folder(TARGET_PATH, LOCAL_PATH, "py")

                    # generate code
                    __generate_code(TARGET_PATH, file_path, name, symbol)

                    try:
                        self.download_files_in_folder(TARGET_PATH, LOCAL_PATH, "py")
                    except Exception as e:
                        warnings.warn(
                            f"Unable to download the python generated code with error: {e.args}"
                        )
            else:
                __generate_code(
                    TARGET_PATH=LOCAL_PATH, filename=file_path, name=name, symbol=symbol
                )

    @version_requires("6.0")
    def apply_context(self, context):
        """Define the settings that will be used to load DPF's plugins.

        A DPF xml file can be used to list the plugins and set up variables.

        Parameters
        ----------
        context : ServerContext
            The context allows to choose which capabilities are available server side.

        Notes
        -----
        Available with server's version starting at 6.0 (Ansys 2023R2).
        """
        if not self._server().meet_version("6.0"):
            raise errors.DpfVersionNotSupported("6.0")
        if self._server().has_client():
            self._api.data_processing_apply_context_on_client(
                self._server().client,
                int(context.licensing_context_type),
                context.xml_path,
            )
        else:
            self._api.data_processing_apply_context(
                int(context.licensing_context_type), context.xml_path
            )

    def initialize_with_context(self, context):
        """Define the settings that will be used to initialize DPF.

        A DPF xml file can be used to list the plugins and set up variables.

        Parameters
        ----------
        context : ServerContext
            The context allows to choose which capabilities are available server side.

        Notes
        -----
        Available with server's version starting at 4.0 (Ansys 2022R2) for InProcess Server
        and starting at 6.0 (Ansys 2023R2) for Grpc Servers.
        """
        if self._server().has_client():
            if not self._server().meet_version("6.0"):
                raise errors.DpfVersionNotSupported("6.0")
            self._api.data_processing_initialize_with_context_on_client(
                self._server().client,
                int(context.licensing_context_type),
                context.xml_path,
            )
        else:
            if not self._server().meet_version("4.0"):
                raise errors.DpfVersionNotSupported("4.0")
            self._api.data_processing_initialize_with_context(
                int(context.licensing_context_type), context.xml_path
            )

    def initialize(self):
        """Initialize a DPF server without a context."""
        if self._server().has_client():
            self._api.data_processing_initialization_on_client(self._server().client)
        else:
            self._api.data_processing_initialization()

    @version_requires("6.0")
    def release_dpf(self):
        """Clear the available Operators and release licenses when necessary.

        Notes
        -----
        Available with server's version starting at 6.0 (Ansys 2023R2).
        """
        if self._server().has_client():
            error = self._api.data_processing_release_on_client(self._server().client, 1)
        else:
            error = self._api.data_processing_release(1)

    @version_requires("4.0")
    def get_runtime_core_config(self):
        """Determine runtime configuration.

        Returns
        -------
        RuntimeCoreConfig
            Runtime configuration options in DataProcessingCore
        """
        if self._server().has_client():
            data_tree_tmp = self._api.data_processing_get_global_config_as_data_tree_on_client(
                self._server().client
            )

        else:
            data_tree_tmp = self._api.data_processing_get_global_config_as_data_tree()
        return RuntimeCoreConfig(data_tree=data_tree_tmp, server=self._server())

    @property
    def server_info(self):
        """Send the request for server information and keep the info into a dictionary.

        Returns
        -------
        info : dictionary
            dictionary with "server_ip", "server_port", "server_process_id"
            "server_version" keys
        """
        return self._get_server_info()

    def _get_server_info(self):
        serv_ip = ""
        serv_port = integral_types.MutableInt32(-1)
        proc_id = ""
        serv_ver_maj = integral_types.MutableInt32(-1)
        serv_ver_min = integral_types.MutableInt32(-1)
        serv_os = ""
        # ip/port
        if self._server().has_client():
            serv_ip = self._api.data_processing_get_server_ip_and_port(
                client=self._server().client, port=serv_port
            )
            serv_port = int(serv_port)
        else:
            serv_ip = ""
            serv_port = None
        # process id
        if self._server().has_client():
            proc_id = self._api.data_processing_process_id_on_client(client=self._server().client)
        else:
            proc_id = self._api.data_processing_process_id()
        # server version
        if self._server().has_client():
            self._api.data_processing_get_server_version_on_client(
                client=self._server().client, major=serv_ver_maj, minor=serv_ver_min
            )
        else:
            self._api.data_processing_get_server_version(major=serv_ver_maj, minor=serv_ver_min)
        # server os
        if self._server().has_client():
            serv_os = self._api.data_processing_get_os_on_client(client=self._server().client)
        else:
            serv_os = self._api.data_processing_get_os()

        out = {
            "server_ip": serv_ip,
            "server_port": serv_port,
            "server_process_id": proc_id,
            "server_version": str(int(serv_ver_maj)) + "." + str(int(serv_ver_min)),
            "os": serv_os,
        }

        return out

    def _description(self, dpf_entity_message):
        """Ask the server to describe the entity in input.

        Parameters
        ----------
        dpf_entity_message : core.Operator._message, core.Workflow._message,
                             core.Scoping._message, core.Field._message,
        core.FieldContainer._message, core.MeshedRegion._message...

        Returns
        -------
           description : str
        """
        data = object_handler.ObjHandler(
            data_processing_api=self._api,
            internal_obj=dpf_entity_message,
            server=self._server(),
        )
        data.get_ownership()
        try:
            if server_meet_version("8.1", self._server()):
                size = integral_types.MutableUInt64(0)
                out = self._api.data_processing_description_string_with_size(data, size)
                if out is not None and not isinstance(out, str):
                    return out.decode("utf-8")
            else:
                return self._api.data_processing_description_string(data=data)
        except Exception as e:
            warnings.warn(str(e.args))
            return ""

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

    def download_file(self, server_file_path, to_client_file_path):
        """Download a file from the server to the target client file path.

        Parameters
        ----------
        server_file_path : str or os.PathLike
            file path to download on the server side

        to_client_file_path: str or os.PathLike
            file path target where the file will be located client side
        """
        if not self._server().has_client():
            txt = """
            download service only available for server with gRPC communication protocol
            """
            raise errors.ServerTypeError(txt)
        client_path = self._api.data_processing_download_file(
            client=self._server().client,
            server_file_path=str(server_file_path),
            to_client_file_path=str(to_client_file_path),
        )

    def _set_collection_api(self):
        if self._collection_api is None:
            self._collection_api = self._server().get_api_for_type(
                capi=collection_capi.CollectionCAPI,
                grpcapi=collection_grpcapi.CollectionGRPCAPI,
            )
            self._collection_api.init_collection_environment(self)
        return self._collection_api

    def download_files_in_folder(
        self, server_folder_path, to_client_folder_path, specific_extension=None
    ):
        """Download all the files from a folder of the server to the target client folder path.

        Parameters
        ----------
        server_folder_path : str or os.PathLike
            folder path to download on the server side

        to_client_folder_path: str or os.PathLike
            folder path target where the files will be located client side

        specific_extension (optional) : str
            copies only the files with the given extension

        Returns
        -------
        paths : list of str
            new file paths client side

        """
        if not self._server().has_client():
            txt = """
            download service only available for server with gRPC communication protocol
            """
            raise ValueError(txt)
        if specific_extension is None:
            specific_extension = ""
        client_paths_ptr = self._api.data_processing_download_files(
            client=self._server().client,
            server_file_path=str(server_folder_path),
            to_client_file_path=str(to_client_folder_path),
            specific_extension=specific_extension,
        )
        if not isinstance(client_paths_ptr, list):
            from ansys.dpf.gate import object_handler

            # collection of string
            client_paths = object_handler.ObjHandler(
                data_processing_api=self._api,
                internal_obj=client_paths_ptr,
                server=self._server(),
            )
            coll_api = self._set_collection_api()
            size = coll_api.collection_get_size(client_paths)
            out = [0] * size
            for i in range(0, size):
                entry = coll_api.collection_get_string_entry(client_paths, i)
                out[i] = entry
            return out
        return client_paths_ptr

    def upload_files_in_folder(
        self, to_server_folder_path, client_folder_path, specific_extension=None
    ):
        """Upload all the files from a folder of the client to the target server folder path.

        Parameters
        ----------
        to_server_folder_path : str or os.PathLike
            folder path target where will be uploaded files on the server side

        client_folder_path: str or os.PathLike
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
            root = Path(root)
            for subdirectory in subdirectories:
                subdir = root / subdirectory
                for filename in subdir.iterdir():
                    f = subdir / filename
                    server_paths = self._upload_and_get_server_path(
                        specific_extension,
                        str(f),
                        filename.name,
                        server_paths,
                        str(to_server_folder_path),
                        subdirectory,
                    )
            for file in files:
                f = root / file
                server_paths = self._upload_and_get_server_path(
                    specific_extension,
                    str(f),
                    file,
                    server_paths,
                    str(to_server_folder_path),
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
            if not self._server().has_client():
                txt = """
                download service only available for server with gRPC communication protocol
                """
                raise errors.ServerTypeError(txt)
            server_path = self._api.data_processing_upload_file(
                client=self._server().client,
                file_path=f,
                to_server_file_path=to_server_file_path,
                use_tmp_dir=False,
            )
            server_paths.append(server_path)
        return server_paths

    def upload_file(self, file_path, to_server_file_path):
        """Upload a file from the client to the target server file path.

        Parameters
        ----------
        file_path : str or os.PathLike
            file path on the client side to upload

        to_server_file_path: str or os.PathLike
            file path target where the file will be located server side

        Returns
        -------
           server_file_path : str
               path generated server side
        """
        file_path = Path(file_path)
        if file_path.stat().st_size == 0:
            raise ValueError(file_path + " is empty")
        if not self._server().has_client():
            txt = """
            download service only available for server with gRPC communication protocol
            """
            raise errors.ServerTypeError(txt)
        return self._api.data_processing_upload_file(
            client=self._server().client,
            file_path=str(file_path),
            to_server_file_path=str(to_server_file_path),
            use_tmp_dir=False,
        )

    def upload_file_in_tmp_folder(self, file_path, new_file_name=None):
        """Upload a file from the client to a temporary server folder deleted on shutdown.

        Parameters
        ----------
        file_path : str or os.PathLike
            file path on the client side to upload

        new_file_name : str, optional
            name to give to the file server side,
            if no name is specified, the same name as the input file is given

        Returns
        -------
           server_file_path : str
               path generated server side
        """
        file_path = Path(file_path)
        if new_file_name:
            file_name = new_file_name
        else:
            file_name = Path(file_path).name
        if file_path.stat().st_size == 0:
            raise ValueError(file_path + " is empty")
        if not self._server().has_client():
            txt = """
            download service only available for server with gRPC communication protocol
            """
            raise errors.ServerTypeError(txt)
        return self._api.data_processing_upload_file(
            client=self._server().client,
            file_path=str(file_path),
            to_server_file_path=str(file_name),
            use_tmp_dir=True,
        )

    def _prepare_shutdown(self):
        if self._server().has_client():
            self._api.data_processing_prepare_shutdown(client=self._server().client)

    # @version_requires("4.0")
    def _release_server(self):
        """
        Release the reference taken by this client on the server.

        Notes
        -----
        Should be used only if the server was started by this client's instance.
        To use only with server version > 4.0
        """
        if self._server().has_client():
            self._api.data_processing_release_server(client=self._server().client)
