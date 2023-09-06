from ansys.dpf.gate.data_processing_grpcapi import DataProcessingGRPCAPI
from ansys.dpf.gate.generated import tmp_dir_abstract_api
#-------------------------------------------------------------------------------
# TmpDir
#-------------------------------------------------------------------------------

def _get_stub(server):
    from ansys.grpc.dpf import base_pb2_grpc
    server.create_stub_if_necessary(DataProcessingGRPCAPI.STUBNAME, base_pb2_grpc.BaseServiceStub)
    return server.get_stub(DataProcessingGRPCAPI.STUBNAME)

class TmpDirGRPCAPI(tmp_dir_abstract_api.TmpDirAbstractAPI):
    STUBNAME = "core_stub"

    @staticmethod
    def tmp_dir_get_dir_on_client(client):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.Empty()
        return _get_stub(client).CreateTmpDir(request).server_file_path