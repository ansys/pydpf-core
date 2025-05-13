import copy
import re
import weakref

import numpy as np

from ansys.dpf.gate.generated import data_processing_abstract_api
from ansys.dpf.gate import errors, object_handler, misc, grpc_stream_helpers


# -------------------------------------------------------------------------------
# DataProcessing
# -------------------------------------------------------------------------------

def _get_stub(server):
    from ansys.grpc.dpf import base_pb2_grpc
    server.create_stub_if_necessary(DataProcessingGRPCAPI.STUBNAME, base_pb2_grpc.BaseServiceStub)
    return server.get_stub(DataProcessingGRPCAPI.STUBNAME)


def _get_server_info_response(client):
    from ansys.grpc.dpf import base_pb2
    request = base_pb2.ServerInfoRequest()
    try:
        response = _get_stub(client).GetServerInfo(request)
    except Exception as e:
        raise IOError(f"Unable to recover information from the server:\n{str(e)}")
    return response


@errors.protect_grpc_class
class DataProcessingYielderHelper:
    @staticmethod
    def file_chunk_yielder(file_path, to_server_file_path, use_tmp_dir=False):
        import os
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.UploadFileRequest()
        request.server_file_path = to_server_file_path
        request.use_temp_dir = use_tmp_dir

        tot_size = os.path.getsize(file_path) * 1e-3

        need_progress_bar = tot_size > 10000 and misc.COMMON_PROGRESS_BAR is not None
        if need_progress_bar:
            bar = misc.COMMON_PROGRESS_BAR("Uploading...", "KB", tot_size)
            bar.start()
        i = 0
        with open(file_path, "rb") as f:
            while True:
                piece = f.read(misc.client_config()["streaming_buffer_size"])
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


@errors.protect_grpc_class
class DataProcessingGRPCAPI(data_processing_abstract_api.DataProcessingAbstractAPI):
    STUBNAME = "core_stub"

    @staticmethod
    def init_data_processing_environment(object):
        from ansys.grpc.dpf import base_pb2_grpc
        if not hasattr(object, "_server"):
            object.create_stub_if_necessary(DataProcessingGRPCAPI.STUBNAME,
                                      base_pb2_grpc.BaseServiceStub)
        elif isinstance(object._server, weakref.ref):
            object._server().create_stub_if_necessary(DataProcessingGRPCAPI.STUBNAME,
                                                      base_pb2_grpc.BaseServiceStub)
        else:
            object._server.create_stub_if_necessary(DataProcessingGRPCAPI.STUBNAME,
                                                    base_pb2_grpc.BaseServiceStub)

    @staticmethod
    def bind_delete_server_func(object):
        from ansys.grpc.dpf import base_pb2
        object._preparing_shutdown_func = (
            _get_stub(object).PrepareShutdown, base_pb2.Empty()
        )
        if hasattr(_get_stub(object), "ReleaseServer"):
            object._shutdown_func = (
                _get_stub(object).ReleaseServer, base_pb2.Empty()
            )
        else:
            object._shutdown_func = (
                None, None
            )

    @staticmethod
    def finish_data_processing_environment(object):
        pass

    @staticmethod
    def data_processing_delete_shared_object(data):
        if not data._server.meet_version("4.0"):
            # using the scoping API (same backend call than base_pb2.DeleteRequest())
            from ansys.grpc.dpf import scoping_pb2
            from ansys.dpf.gate import scoping_grpcapi
            request = scoping_pb2.Scoping()
            if isinstance(data._internal_obj.id, int):
                request.id = data._internal_obj.id
            else:
                request.id.CopyFrom(data._internal_obj.id)
            scoping_grpcapi.ScopingGRPCAPI.init_scoping_environment(data)
            scoping_grpcapi._get_stub(data._server).Delete(request)
        else:
            from ansys.grpc.dpf import base_pb2
            request = base_pb2.DeleteRequest()
            if isinstance(data, list):
                for obj in data:
                    request.dpf_type_id.append(obj._internal_obj.id)
                _get_stub(data[0]._server).Delete(request)
            else:
                request.dpf_type_id.append(data._internal_obj.id)
                _get_stub(data._server).Delete(request)

    @staticmethod
    def data_processing_duplicate_object_reference(base):
        from ansys.grpc.dpf import base_pb2
        if not hasattr(base_pb2, "DuplicateRefRequest"):
            if isinstance(base, object_handler.ObjHandler):
                return base.get_ownership()
            return base._internal_obj
        request = base_pb2.DuplicateRefRequest()
        request.dpf_type_id.CopyFrom(base._internal_obj.id)
        to_return = copy.deepcopy(base._internal_obj)
        to_return.id.CopyFrom(_get_stub(base._server).DuplicateRef(request).new_dpf_type_id)
        return to_return

    @staticmethod
    def data_processing_initialize_with_context_on_client(client, context,
                                                          dataProcessingCore_xml_path):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.InitializationRequest()
        request.context = context
        request.xml = dataProcessingCore_xml_path
        request.force_reinit = False
        _get_stub(client).Initialize(request)

    @staticmethod
    def data_processing_apply_context_on_client(client, context, dataProcessingCore_xml_path):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.InitializationRequest()
        request.context = context
        request.xml = dataProcessingCore_xml_path
        request.force_reinit = True
        response = _get_stub(client).Initialize(request)
        if response.error.ok != True:
            raise errors.DPFServerException(response.error.error_message)

    @staticmethod
    def data_processing_release_on_client(client, context):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.InitializationRequest()
        request.context = -context
        _get_stub(client).Initialize(request)

    @staticmethod
    def data_processing_load_library_on_client(sLibraryKey, sDllPath, sloader_symbol, client):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.PluginRequest()
        request.name = sLibraryKey
        request.dllPath = sDllPath
        request.symbol = sloader_symbol
        try:
            _get_stub(client).Load(request)
        except Exception as e:
            raise errors.DPFServerException(
                f'Unable to load library "{sDllPath}". File may not exist or'
                f" is missing dependencies:\n{str(e)}"
            )

    @staticmethod
    def data_processing_get_os_on_client(client):
        response = _get_server_info_response(client)
        if hasattr(response, "properties"):
            return response.properties["os"]
        else:
            return None

    @staticmethod
    def data_processing_get_server_ip_and_port(client, port):
        response = _get_server_info_response(client)
        port.set(response.port)
        return response.ip

    @staticmethod
    def data_processing_process_id_on_client(client):
        response = _get_server_info_response(client)
        return response.processId

    @staticmethod
    def data_processing_get_server_version_on_client(client, major, minor):
        response = _get_server_info_response(client)
        major.set(response.majorVersion)
        minor.set(response.minorVersion)

    @staticmethod
    def data_processing_description_string(data):
        data_obj = data._internal_obj
        from ansys.grpc.dpf import base_pb2, collection_message_pb2
        request = base_pb2.DescribeRequest()
        if isinstance(data_obj.id, int):
            request.dpf_type_id = data_obj.id
        else:
            request.dpf_type_id = data_obj.id.id
        serv_to_test = data._server
        if not serv_to_test:
            return ""
        client = None
        if serv_to_test.has_client():
            client = serv_to_test.client
        else:
            return ""
        if isinstance(data_obj, collection_message_pb2.Collection):
            from ansys.dpf.gate import collection_grpcapi
            collection_grpcapi.CollectionGRPCAPI.init_collection_environment(data)
            response = collection_grpcapi._get_stub(data._server.client).Describe(request)
        else:
            response = _get_stub(client).Describe(request)
        return response.description

    @staticmethod
    def data_processing_description_string_with_size(data, size):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.DescribeRequest()
        if isinstance(data._internal_obj.id, int):
            request.dpf_type_id = data._internal_obj.id
        else:
            request.dpf_type_id = data._internal_obj.id.id
        service = _get_stub(data._server.client).DescribeStreamed(request)
        dtype = np.byte
        out = grpc_stream_helpers._data_get_chunk_(dtype, service, True, get_array=lambda chunk: chunk.array.array)
        size.val = out.size
        return bytes(out)

    @staticmethod
    def data_processing_upload_file(client, file_path, to_server_file_path, use_tmp_dir):
        to_return = _get_stub(client).UploadFile(
            DataProcessingYielderHelper.file_chunk_yielder(
                file_path=file_path, to_server_file_path=to_server_file_path,
                use_tmp_dir=use_tmp_dir
            )
        ).server_file_path
        return to_return

    @staticmethod
    def data_processing_release_server(client):
        from ansys.grpc.dpf import base_pb2
        _get_stub(client).ReleaseServer(base_pb2.Empty())

    @staticmethod
    def data_processing_prepare_shutdown(client):
        from ansys.grpc.dpf import base_pb2
        _get_stub(client).PrepareShutdown(base_pb2.Empty())

    @staticmethod
    def data_processing_list_operators_as_collection_on_client(client):
        from ansys.grpc.dpf import operator_pb2
        from ansys.dpf.gate import operator_grpcapi
        service = operator_grpcapi._get_stub(client).ListAllOperators(
            operator_pb2.ListAllOperatorsRequest())
        arr = []
        for chunk in service:
            arr.extend(re.split(r'[\x00-\x08]', chunk.array.decode('utf-8')))
        return arr

    @staticmethod
    def data_processing_get_global_config_as_data_tree_on_client(client):
        from ansys.grpc.dpf import base_pb2, data_tree_pb2
        id = _get_stub(client).GetConfig(base_pb2.Empty()).runtime_core_config_data_tree_id
        out = data_tree_pb2.DataTree()
        out.id.CopyFrom(id)
        return out

    @staticmethod
    def data_processing_get_client_config_as_data_tree():
        return misc.client_config()

    @staticmethod
    def data_processing_download_file(client, server_file_path, to_client_file_path):
        from ansys.grpc.dpf import base_pb2
        import sys
        request = base_pb2.DownloadFileRequest()
        request.server_file_path = server_file_path
        chunks = _get_stub(client).DownloadFile(request)
        bar = None
        tot_size = sys.float_info.max
        from ansys.dpf.gate import misc
        _progress_bar_is_available = False
        if misc.COMMON_PROGRESS_BAR is not None:
            _progress_bar_is_available = True
        for i in range(0, len(chunks.initial_metadata())):
            if chunks.initial_metadata()[i].key == u"size_tot":
                tot_size = int(chunks.initial_metadata()[i].value) * 1E-3
                if _progress_bar_is_available:
                    bar = misc.COMMON_PROGRESS_BAR("Downloading...",
                                                   unit="KB",
                                                   tot_size=tot_size)
        if not bar and _progress_bar_is_available:
            bar = misc.COMMON_PROGRESS_BAR("Downloading...", unit="KB")
            bar.start()
        i = 0
        with open(to_client_file_path, "wb") as f:
            for chunk in chunks:
                f.write(chunk.data.data)
                i += len(chunk.data.data) * 1e-3
                try:
                    if bar is not None:
                        bar.update(min(i, tot_size))
                except:
                    pass
        if bar is not None:
            bar.finish()

    @staticmethod
    def data_processing_download_files(client, server_file_path, to_client_file_path,
                                       specific_extension):
        from ansys.grpc.dpf import base_pb2
        import os
        import pathlib
        request = base_pb2.DownloadFileRequest()
        request.server_file_path = server_file_path
        chunks = _get_stub(client).DownloadFile(request)
        from ansys.dpf.gate import misc
        _progress_bar_is_available = False
        if misc.COMMON_PROGRESS_BAR:
            _progress_bar_is_available = True
        num_files = 1
        if chunks.initial_metadata()[0].key == "num_files":
            num_files = int(chunks.initial_metadata()[0].value)
        if _progress_bar_is_available:
            bar = misc.COMMON_PROGRESS_BAR("Downloading...", unit="files", tot_size=num_files)
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
                        or not specific_extension
                        or pathlib.Path(server_path).suffix == "." + specific_extension
                ):
                    s1 = len(server_path.split("\\"))
                    s2 = len(server_path.split("/"))
                    if s2 > s1:
                        separator = "/"
                    elif s1 > s2:
                        separator = "\\"
                    server_subpath = server_path.replace(
                        server_file_path + separator, ""
                    )
                    subdir = ""
                    split = server_subpath.split(separator)
                    n = len(split)
                    i = 0
                    to_client_folder_path_copy = to_client_file_path
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
                        if bar is not None:
                            bar.update(len(client_paths))
                    except:
                        pass
                else:
                    f = None
            if f is not None:
                f.write(chunk.data.data)
        try:
            if bar is not None:
                bar.finish()
        except:
            pass
        return client_paths
