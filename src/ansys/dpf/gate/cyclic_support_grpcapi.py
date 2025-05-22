from ansys.dpf.gate.generated import cyclic_support_abstract_api
from ansys.dpf.gate.data_processing_grpcapi import DataProcessingGRPCAPI
from ansys.dpf.gate.object_handler import ObjHandler
from ansys.dpf.gate import errors

# -------------------------------------------------------------------------------
# CyclicSupport
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(CyclicSupportGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class CyclicSupportGRPCAPI(cyclic_support_abstract_api.CyclicSupportAbstractAPI):
    STUBNAME = "cyclic_support_stub"

    @staticmethod
    def init_cyclic_support_environment(support):
        from ansys.grpc.dpf import cyclic_support_pb2_grpc
        support._server.create_stub_if_necessary(CyclicSupportGRPCAPI.STUBNAME,
                                                 cyclic_support_pb2_grpc.CyclicSupportServiceStub)

        support._deleter_func = (_get_stub(support._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def list(support):
        from types import SimpleNamespace
        server = support._server
        api = DataProcessingGRPCAPI

        # Get the ListResponse from the server
        list_response = _get_stub(support._server).List(support._internal_obj)

        # Wrap the ListResponse in a flat response with ObjHandlers to prevent memory leaks
        response = SimpleNamespace(num_stages=ObjHandler(api, list_response.num_stages, server))
        # add attributes to response
        setattr(response, "num_stages", list_response.num_stages)
        for i_stage in range(list_response.num_stages):
            setattr(response, "num_sectors_"+str(i_stage),
                    list_response.stage_infos[i_stage].num_sectors)
            setattr(response, "base_elements_scoping_"+str(i_stage),
                    ObjHandler(api, list_response.stage_infos[i_stage].base_elements_scoping,
                               server))
            setattr(response, "base_nodes_scoping_"+str(i_stage),
                    ObjHandler(api, list_response.stage_infos[i_stage].base_nodes_scoping, server))
            setattr(response, "sectors_for_expansion_"+str(i_stage),
                    ObjHandler(api, list_response.stage_infos[i_stage].sectors_for_expansion,
                               server))
        return response

    @staticmethod
    def cyclic_support_get_num_sectors(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "num_sectors_"+str(i_stage))

    @staticmethod
    def cyclic_support_get_num_stages(support):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "num_stages")

    @staticmethod
    def cyclic_support_get_sectors_scoping(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "sectors_for_expansion_"+str(i_stage)).get_ownership()

    @staticmethod
    def cyclic_support_get_base_nodes_scoping(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "base_nodes_scoping_"+str(i_stage)).get_ownership()

    @staticmethod
    def cyclic_support_get_base_elements_scoping(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "base_elements_scoping_"+str(i_stage)).get_ownership()

    @staticmethod
    def cyclic_support_get_low_high_map(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "low_high_map_"+str(i_stage)).get_ownership()

    @staticmethod
    def cyclic_support_get_high_low_map(support, i_stage):
        return getattr(CyclicSupportGRPCAPI.list(support),
                       "high_low_map_"+str(i_stage)).get_ownership()

    @staticmethod
    def get_expanded_ids(support, request):
        return _get_stub(support._server).GetExpandedIds(request).expanded_ids

    @staticmethod
    def init_get_expanded_ids(support, i_stage, sectorsScoping):
        from ansys.grpc.dpf import cyclic_support_pb2
        request = cyclic_support_pb2.GetExpandedIdsRequest()
        request.support.CopyFrom(support._internal_obj)
        request.stage_num = i_stage
        if sectorsScoping:
            request.sectors_to_expand.CopyFrom(sectorsScoping._internal_obj)
        return request

    @staticmethod
    def cyclic_support_get_expanded_node_ids(support, baseNodeId, i_stage, sectorsScoping):
        request = CyclicSupportGRPCAPI.init_get_expanded_ids(support, i_stage, sectorsScoping)
        request.node_id = baseNodeId
        return CyclicSupportGRPCAPI.get_expanded_ids(support, request)

    @staticmethod
    def cyclic_support_get_expanded_element_ids(support, baseElementId, i_stage, sectorsScoping):
        request = CyclicSupportGRPCAPI.init_get_expanded_ids(support, i_stage, sectorsScoping)
        request.element_id = baseElementId
        return CyclicSupportGRPCAPI.get_expanded_ids(support, request)

    @staticmethod
    def get_cs(support, request):
        return _get_stub(support._server).GetCS(request).cs

    @staticmethod
    def init_get_cs(support):
        from ansys.grpc.dpf import cyclic_support_pb2
        request = cyclic_support_pb2.GetCSRequest()
        request.support.CopyFrom(support._internal_obj)
        return request

    @staticmethod
    def cyclic_support_get_cs(support):
        request = CyclicSupportGRPCAPI.init_get_cs(support)
        return CyclicSupportGRPCAPI.get_cs(support, request)