import functools

from ansys.dpf.gate.generated import result_info_abstract_api
from ansys.dpf.gate.data_processing_grpcapi import DataProcessingGRPCAPI
from ansys.dpf.gate.object_handler import ObjHandler
from ansys.dpf.gate import errors

# -------------------------------------------------------------------------------
# ResultInfo
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(ResultInfoGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class ResultInfoGRPCAPI(result_info_abstract_api.ResultInfoAbstractAPI):
    STUBNAME = "result_info_stub"

    @staticmethod
    def init_result_info_environment(result_info):
        from ansys.grpc.dpf import result_info_pb2_grpc
        result_info._server.create_stub_if_necessary(ResultInfoGRPCAPI.STUBNAME,
                                                     result_info_pb2_grpc.ResultInfoServiceStub)
        result_info._deleter_func = (_get_stub(result_info._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    @functools.lru_cache(maxsize=50, typed=False)
    def list(result_info):
        from types import SimpleNamespace
        server = result_info._server
        api = DataProcessingGRPCAPI

        # Get the ListResponse from the server
        list_response = _get_stub(server).List(result_info._internal_obj)
        # Wrap the ListResponse in a flat response with ObjHandlers to prevent memory leaks
        response = SimpleNamespace()
        # add attributes to response
        setattr(response, "analysis_type", list_response.analysis_type)
        setattr(response, "physics_type", list_response.physics_type)
        setattr(response, "unit_system", list_response.unit_system)
        setattr(response, "nresult", list_response.nresult)
        setattr(response, "unit_system_name", list_response.unit_system_name)
        setattr(response, "solver_major_version", list_response.solver_major_version)
        setattr(response, "solver_minor_version", list_response.solver_minor_version)
        setattr(response, "solver_date", list_response.solver_date)
        setattr(response, "solver_time", list_response.solver_time)
        setattr(response, "user_name", list_response.user_name)
        setattr(response, "job_name", list_response.job_name)
        setattr(response, "product_name", list_response.product_name)
        setattr(response, "main_title", list_response.main_title)
        setattr(response, "cyc_support",
                ObjHandler(api, list_response.cyc_info.cyc_support, server))
        setattr(response, "cyclic_type", list_response.cyc_info.cyclic_type)
        setattr(response, "has_cyclic", list_response.cyc_info.has_cyclic)

        return response

    @staticmethod
    @functools.lru_cache(maxsize=50, typed=False)
    def list_result(result_info, idx):
        from ansys.grpc.dpf import result_info_pb2
        request = result_info_pb2.AvailableResultRequest()
        request.result_info.CopyFrom(result_info._internal_obj)
        request.numres = idx
        return _get_stub(result_info._server).ListResult(request)

    @staticmethod
    def result_info_get_analysis_type(result_info):
        return ResultInfoGRPCAPI.list(result_info).analysis_type

    @staticmethod
    def result_info_get_physics_type(result_info):
        return ResultInfoGRPCAPI.list(result_info).physics_type

    @staticmethod
    def result_info_get_analysis_type_name(result_info):
        from ansys.grpc.dpf import result_info_pb2
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "analysis_type")
        analysis_type = ResultInfoGRPCAPI.result_info_get_analysis_type(result_info)
        return result_info_pb2.AnalysisType.Name(analysis_type).lower()

    @staticmethod
    def result_info_get_physics_type_name(result_info):
        from ansys.grpc.dpf import result_info_pb2
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "physics_type")
        physics_type = ResultInfoGRPCAPI.result_info_get_physics_type(result_info)
        return result_info_pb2.PhysicsType.Name(physics_type).lower()

    @staticmethod
    def result_info_get_ansys_unit_system_enum(result_info):
        return ResultInfoGRPCAPI.list(result_info).unit_system

    @staticmethod
    def result_info_get_unit_system_name(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "unit_system_name")
        return ResultInfoGRPCAPI.list(result_info).unit_system_name

    @staticmethod
    def result_info_get_number_of_results(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_int_property(result_info, "results_count")
        return ResultInfoGRPCAPI.list(result_info).nresult

    @staticmethod
    def result_info_get_result_number_of_components(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).ncomp

    @staticmethod
    def result_info_get_result_dimensionality_nature(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).dimensionality

    @staticmethod
    def result_info_get_result_homogeneity(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).homogeneity

    @staticmethod
    def result_info_get_result_location(result_info, idx, location):
        res = ResultInfoGRPCAPI.list_result(result_info, idx)
        location.set_str(res.properties["location"])
        return res

    @staticmethod
    def result_info_get_result_name(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).name

    @staticmethod
    def result_info_get_result_physics_name(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).physicsname

    @staticmethod
    def result_info_get_result_scripting_name(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).properties["scripting_name"]

    @staticmethod
    def result_info_get_result_unit_symbol(result_info, idx):
        return ResultInfoGRPCAPI.list_result(result_info, idx).unit

    @staticmethod
    def result_info_get_qualifiers_for_result(result_info, idx):
        out = ResultInfoGRPCAPI.list_result(result_info, idx)
        if hasattr(out, "qualifiers"):
            return out.qualifiers
        return []

    @staticmethod
    def result_info_get_number_of_sub_results(result_info, idx):
        return len(ResultInfoGRPCAPI.list_result(result_info, idx).sub_res)

    @staticmethod
    def result_info_get_sub_result_name(result_info, idx, idx_sub):
        return ResultInfoGRPCAPI.list_result(result_info, idx).sub_res[idx_sub].name

    @staticmethod
    def result_info_get_sub_result_operator_name(result_info, idx, idx_sub, name):
        res = ResultInfoGRPCAPI.list_result(result_info, idx)
        name.set_str(res.sub_res[idx_sub].op_name)
        return res

    @staticmethod
    def result_info_get_sub_result_description(result_info, idx, idx_sub):
        return ResultInfoGRPCAPI.list_result(result_info, idx).sub_res[idx_sub].description

    @staticmethod
    def result_info_get_cyclic_support(result_info):
        return ResultInfoGRPCAPI.list(result_info).cyc_support.get_ownership()

    @staticmethod
    def result_info_get_cyclic_symmetry_type(result_info):
        return ResultInfoGRPCAPI.list(result_info).cyclic_type

    @staticmethod
    def result_info_has_cyclic_symmetry(result_info):
        return ResultInfoGRPCAPI.list(result_info).has_cyclic

    @staticmethod
    def result_info_get_solver_version(result_info, major, minor):
        if result_info._server.meet_version("3.0"):
            res = ResultInfoGRPCAPI.result_info_get_string_property(result_info, "solver_version")
            major.set(int(res.split(".")[0]))
            minor.set(int(res.split(".")[1]))
        listed = ResultInfoGRPCAPI.list(result_info)
        major.set(listed.solver_major_version)
        minor.set(listed.solver_minor_version)

    @staticmethod
    def result_info_get_solve_date_and_time(result_info, date, time):
        if result_info._server.meet_version("3.0"):
            res = ResultInfoGRPCAPI.result_info_get_int_property(result_info, "solver_date")
            res2 = ResultInfoGRPCAPI.result_info_get_int_property(result_info, "solver_time")
            date.set(int(res))
            time.set(int(res2))
        listed = ResultInfoGRPCAPI.list(result_info)
        date.set(listed.solver_date)
        time.set(listed.solver_time)

    @staticmethod
    def result_info_get_user_name(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "user_name")
        return ResultInfoGRPCAPI.list(result_info).user_name

    @staticmethod
    def result_info_get_job_name(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "job_name")
        return ResultInfoGRPCAPI.list(result_info).job_name

    @staticmethod
    def result_info_get_product_name(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "product_name")
        return ResultInfoGRPCAPI.list(result_info).product_name

    @staticmethod
    def result_info_get_main_title(result_info):
        if result_info._server.meet_version("3.0"):
            return ResultInfoGRPCAPI.result_info_get_string_property(result_info, "main_title")
        return ResultInfoGRPCAPI.list(result_info).main_title

    @staticmethod
    @functools.lru_cache(maxsize=50, typed=False)
    def result_info_get_string_property(result_info, property_name):
        from ansys.grpc.dpf import result_info_pb2
        request = result_info_pb2.GetStringPropertiesRequest()
        request.result_info.CopyFrom(result_info._internal_obj)
        request.property_names.extend([property_name])
        return _get_stub(result_info._server).GetStringProperties(request).properties[property_name]

    @staticmethod
    @functools.lru_cache(maxsize=50, typed=False)
    def result_info_get_int_property(result_info, property_name):
        from ansys.grpc.dpf import result_info_pb2
        request = result_info_pb2.GetStringPropertiesRequest()
        request.result_info.CopyFrom(result_info._internal_obj)
        request.property_names.extend([property_name])
        stub = _get_stub(result_info._server)
        return int(stub.GetStringProperties(request).properties[property_name])

    @staticmethod
    def result_info_get_qualifier_label_support(result_info, qualifier):
        from ansys.grpc.dpf import result_info_pb2
        request = result_info_pb2.ListQualifiersLabelsRequest()
        request.result_info.CopyFrom(result_info._internal_obj)
        stub = _get_stub(result_info._server)
        out = None
        supports = stub.ListQualifiersLabels(request).qualifier_labels
        api = DataProcessingGRPCAPI
        for key, entry in supports.items():
            if key == qualifier:
                out = entry
            else:
                ObjHandler(api, entry, result_info._server)
        return out

    @staticmethod
    def result_info_get_available_qualifier_labels_as_string_coll(result_info):
        from ansys.grpc.dpf import result_info_pb2
        request = result_info_pb2.ListQualifiersLabelsRequest()
        request.result_info.CopyFrom(result_info._internal_obj)
        stub = _get_stub(result_info._server)
        labels = []
        supports = stub.ListQualifiersLabels(request).qualifier_labels
        api = DataProcessingGRPCAPI
        for key, entry in supports.items():
            ObjHandler(api, entry, result_info._server)
            labels.append(key)
        return labels

