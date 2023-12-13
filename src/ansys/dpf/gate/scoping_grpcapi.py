import numpy as np
from ansys.dpf.gate.generated import scoping_abstract_api
from ansys.dpf.gate import grpc_stream_helpers, errors

# -------------------------------------------------------------------------------
# Scoping
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(ScopingGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class ScopingGRPCAPI(scoping_abstract_api.ScopingAbstractAPI):
    STUBNAME = "scoping_stub"

    @staticmethod
    def init_scoping_environment(object):
        from ansys.grpc.dpf import scoping_pb2_grpc
        object._server.create_stub_if_necessary(ScopingGRPCAPI.STUBNAME,
                                                scoping_pb2_grpc.ScopingServiceStub)
        object._deleter_func = (_get_stub(object._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def scoping_new_on_client(server):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.Empty()
        return _get_stub(server).Create(request)

    @staticmethod
    def scoping_set_ids(scoping, ids, size):
        from ansys.grpc.dpf import scoping_pb2
        # must convert to a list for gRPC
        if isinstance(ids, range):
            ids = np.array(list(ids), dtype=np.int32)
        elif not isinstance(ids, (np.ndarray, np.generic)):
            ids = np.array(ids, dtype=np.int32)
        else:
            ids = np.array(list(ids), dtype=np.int32)
        metadata = [("size_int", f"{len(ids)}")]
        request = scoping_pb2.UpdateIdsRequest()
        request.scoping.CopyFrom(scoping._internal_obj)
        if scoping._server.meet_version("2.1"):
            _get_stub(scoping._server).UpdateIds(grpc_stream_helpers._data_chunk_yielder(request, ids), metadata=metadata)
        else:
            _get_stub(scoping._server).UpdateIds(
                grpc_stream_helpers._data_chunk_yielder(request, ids, 8.0e6), metadata=metadata
            )

    @staticmethod
    def scoping_get_ids(scoping, np_array):
        #TO DO: make it more generic
        if scoping._server.meet_version("2.1"):
            service = _get_stub(scoping._server).List(scoping._internal_obj)
            dtype = np.int32
            return grpc_stream_helpers._data_get_chunk_(dtype, service, np_array)
        else:
            out = []

            service = _get_stub(scoping._server).List(scoping._internal_obj)
            for chunk in service:
                out.extend(chunk.ids.rep_int)
            if np_array:
                return np.array(out, dtype=np.int32)
            else:
                return out

    @staticmethod
    def scoping_get_size(scoping):
        from ansys.grpc.dpf import scoping_pb2, base_pb2
        request = scoping_pb2.CountRequest()
        request.entity = base_pb2.NUM_ELEMENTARY_DATA
        request.scoping.CopyFrom(scoping._internal_obj)
        return _get_stub(scoping._server).Count(request).count

    @staticmethod
    def scoping_get_location(scoping):
        return _get_stub(scoping._server).GetLocation(scoping._internal_obj).loc.location

    @staticmethod
    def scoping_set_location(scoping, location):
        from ansys.grpc.dpf import scoping_pb2
        request = scoping_pb2.UpdateRequest()
        request.location.location = location
        request.scoping.CopyFrom(scoping._internal_obj)
        _get_stub(scoping._server).Update(request)

    @staticmethod
    def scoping_set_entity(scoping, id, index):
        from ansys.grpc.dpf import scoping_pb2
        request = scoping_pb2.UpdateRequest()
        request.index_id.id = id
        request.index_id.index = index
        request.scoping.CopyFrom(scoping._internal_obj)
        _get_stub(scoping._server).Update(request)

    @staticmethod
    def scoping_id_by_index(scoping, index):
        from ansys.grpc.dpf import scoping_pb2
        request = scoping_pb2.GetRequest()
        request.index = index
        request.scoping.CopyFrom(scoping._internal_obj)
        return _get_stub(scoping._server).Get(request).id

    @staticmethod
    def scoping_index_by_id(scoping, id):
        from ansys.grpc.dpf import scoping_pb2
        request = scoping_pb2.GetRequest()
        request.id = id
        request.scoping.CopyFrom(scoping._internal_obj)
        return _get_stub(scoping._server).Get(request).index
