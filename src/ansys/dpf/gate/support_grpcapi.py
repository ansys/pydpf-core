from ansys.dpf.gate import errors, object_handler, data_processing_grpcapi
from ansys.dpf.gate.generated import support_abstract_api

# -------------------------------------------------------------------------------
# Support
# -------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(SupportGRPCAPI.STUBNAME)

@errors.protect_grpc_class
class SupportGRPCAPI(support_abstract_api.SupportAbstractAPI):
    STUBNAME = "support_stub"

    @staticmethod
    def init_support_environment(object):
        from ansys.grpc.dpf import support_service_pb2_grpc
        object._server.create_stub_if_necessary(SupportGRPCAPI.STUBNAME,
                                                support_service_pb2_grpc.SupportServiceStub)
        data_processing_grpcapi.DataProcessingGRPCAPI.init_data_processing_environment(object)
        if object._server.meet_version("4.0"):
            object._deleter_func = (
            data_processing_grpcapi._get_stub(object._server).Delete, lambda obj: obj._internal_obj)
        else:
            from ansys.dpf.gate import scoping_grpcapi
            scoping_grpcapi.ScopingGRPCAPI.init_scoping_environment(object)
            object._deleter_func = (
                scoping_grpcapi._get_stub(object._server).Delete, lambda obj: obj._internal_obj
            )


    @staticmethod
    def support_get_as_time_freq_support(support):
        from ansys.grpc.dpf import support_pb2, time_freq_support_pb2
        internal_obj = support.get_ownership()
        if isinstance(internal_obj, time_freq_support_pb2.TimeFreqSupport):
            message = support
        elif isinstance(internal_obj, support_pb2.Support):
            if hasattr(_get_stub(support._server), "GetSupport"):
                message = _get_stub(support._server).GetSupport(internal_obj).time_freq_support
            else:
                message = time_freq_support_pb2.TimeFreqSupport()
                if isinstance(message.id, int):
                    message.id = internal_obj.id
                else:
                    message.id.CopyFrom(internal_obj.id)
        else:
            raise NotImplementedError(f"Tried to get {support} as TimeFreqSupport.")
        return message

    @staticmethod
    def support_get_as_meshed_support(support):
        from ansys.grpc.dpf import support_pb2, meshed_region_pb2
        internal_obj = support.get_ownership()
        if isinstance(internal_obj, meshed_region_pb2.MeshedRegion):
            message = support
        elif isinstance(internal_obj, support_pb2.Support):
            message = meshed_region_pb2.MeshedRegion()
            if isinstance(message.id, int):
                message.id = internal_obj.id
            else:
                message.id.CopyFrom(internal_obj.id)
        else:
            raise NotImplementedError(f"Tried to get {internal_obj} as MeshedRegion.")
        return message

    @staticmethod
    def support_get_field_support_by_property(support, prop_name):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        request.specific_fields.append(prop_name)
        response = _get_stub(support._server).List(request).field_supports
        if prop_name in response:
            return response[prop_name]

    @staticmethod
    def support_get_property_field_support_by_property(support, prop_name):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        request.specific_prop_fields.append(prop_name)
        response = _get_stub(support._server).List(request).field_supports
        if prop_name in response:
            return response[prop_name]


    @staticmethod
    def support_get_string_field_support_by_property(support, prop_name):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        request.specific_string_fields.append(prop_name)
        response = _get_stub(support._server).List(request).field_supports
        if prop_name in response:
            return response[prop_name]


    @staticmethod
    def support_get_property_names_as_string_coll_for_fields(support):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        response = _get_stub(support._server).List(request).field_supports
        out = []
        for name, field in response.items():
            object_handler.ObjHandler(field)
            if field.datatype =="double":
                out.append(name)
        return out


    @staticmethod
    def support_get_property_names_as_string_coll_for_property_fields(support):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        response = _get_stub(support._server).List(request).field_supports
        out = []
        for name, field in response.items():
            object_handler.ObjHandler(field)
            if field.datatype =="int":
                out.append(name)
        return out

    @staticmethod
    def support_get_property_names_as_string_coll_for_string_fields(support):
        from ansys.grpc.dpf import support_service_pb2
        request = support_service_pb2.ListRequest()
        request.support.id.CopyFrom(support._internal_obj.id)
        response = _get_stub(support._server).List(request).field_supports
        out = []
        for name, field in response.items():
            object_handler.ObjHandler(field)
            if field.datatype =="string":
                out.append(name)
        return out

