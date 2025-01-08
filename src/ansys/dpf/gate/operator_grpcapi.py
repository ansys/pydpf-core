from ansys.dpf.gate.generated import operator_abstract_api
from ansys.dpf.gate import errors, grpc_stream_helpers
import numpy as np
# -------------------------------------------------------------------------------
# Operator
# -------------------------------------------------------------------------------


def _get_stub(server):
    from ansys.grpc.dpf import operator_pb2_grpc
    server.create_stub_if_necessary(OperatorGRPCAPI.STUBNAME,
                                             operator_pb2_grpc.OperatorServiceStub)
    return server.get_stub(OperatorGRPCAPI.STUBNAME)


def _set_array_to_request(request, bytes):
    request.array.array = bytes


@errors.protect_grpc_class
class OperatorGRPCAPI(operator_abstract_api.OperatorAbstractAPI):
    STUBNAME = "operator_stub"

    @staticmethod
    def init_operator_environment(obj):
        from ansys.grpc.dpf import operator_pb2_grpc
        obj._server.create_stub_if_necessary(OperatorGRPCAPI.STUBNAME,
                                             operator_pb2_grpc.OperatorServiceStub)
        obj._deleter_func = (_get_stub(obj._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def operator_new_on_client(operatorName, client):
        from ansys.grpc.dpf import operator_pb2
        request = operator_pb2.CreateOperatorRequest()
        request.name = operatorName
        return _get_stub(client).Create(request)

    @staticmethod
    def operator_set_config(op, config):
        from ansys.grpc.dpf import operator_pb2
        request = operator_pb2.UpdateConfigRequest()
        request.op.CopyFrom(op._internal_obj)
        request.config.CopyFrom(config._internal_obj)
        _get_stub(op._server).UpdateConfig(request)

    @staticmethod
    def get_list(op):
        return _get_stub(op._server).List(op._internal_obj)

    @staticmethod
    def operator_get_config(op):
        return OperatorGRPCAPI.get_list(op).config

    @staticmethod
    def operator_name(op):
        return OperatorGRPCAPI.get_list(op).op_name

    @staticmethod
    def update_init(op, pin):
        from ansys.grpc.dpf import operator_pb2
        request = operator_pb2.UpdateRequest()
        request.op.CopyFrom(op._internal_obj)
        request.pin = pin
        return request

    @staticmethod
    def update(op, request):
        _get_stub(op._server).Update(request)

    @staticmethod
    def operator_connect_int(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.int = value
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_bool(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.bool = value
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_double(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.double = value
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_string(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.str = value
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_string_with_size(op, pin, value, size):
        if op._server.meet_version("8.0"):
            from ansys.grpc.dpf import operator_pb2, base_pb2
            request = operator_pb2.ArrayUpdateRequest()
            request.op.CopyFrom(op._internal_obj)
            request.pin = pin
            request.type = base_pb2.Type.Value("STRING")
            metadata = [("size_bytes", f"{size.val.value}")]
            _get_stub(op._server).UpdateStreamed(
                grpc_stream_helpers._data_chunk_yielder(
                    request,
                    value,
                    set_array=_set_array_to_request
                ),
                metadata=metadata)
        else:
            OperatorGRPCAPI.operator_connect_string(op, pin, value)


    @staticmethod
    def operator_connect_scoping(op, pin, scoping):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.scoping.CopyFrom(scoping._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_data_sources(op, pin, dataSources):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.data_sources.CopyFrom(dataSources._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_field(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.field.CopyFrom(value._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_collection(op, pin, value):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.collection.CopyFrom(value._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_meshed_region(op, pin, mesh):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.mesh.CopyFrom(mesh._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_vector_int(op, pin, ptrValue, size):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.vint.rep_int.extend(ptrValue)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_vector_double(op, pin, ptrValue, size):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.vdouble.rep_double.extend(ptrValue)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_collection_as_vector(op, pin, collection):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.collection.CopyFrom(collection._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_operator_output(op, pin, value, outputIndex):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.inputop.inputop.CopyFrom(value._internal_obj)
        request.inputop.pinOut = outputIndex
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_property_field(op, pin, streams):
        return OperatorGRPCAPI.operator_connect_field(op, pin, streams)

    @staticmethod
    def operator_connect_string_field(op, pin, value):
        return OperatorGRPCAPI.operator_connect_field(op, pin, value)

    @staticmethod
    def operator_connect_custom_type_field(op, pin, value):
        return OperatorGRPCAPI.operator_connect_field(op, pin, value)

    @staticmethod
    def operator_connect_time_freq_support(op, pin, support):
        if not op._server.meet_version("3.0"):
            raise errors.DpfVersionNotSupported("3.0")
        request = OperatorGRPCAPI.update_init(op, pin)
        request.time_freq_support.CopyFrom(support._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_workflow(op, pin, wf):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.workflow.CopyFrom(wf._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_cyclic_support(op, pin, sup):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.cyc_support.CopyFrom(sup._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_data_tree(op, pin, ptr):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.data_tree.CopyFrom(ptr._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_label_space(op, pin, ptr):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.label_space.CopyFrom(ptr._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_any(op, pin, ptr):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.as_any.CopyFrom(ptr._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_generic_data_container(op, pin, ptr):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.generic_data_container.CopyFrom(ptr._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def operator_connect_operator_as_input(op, pin, ptr):
        request = OperatorGRPCAPI.update_init(op, pin)
        request.operator_as_input.CopyFrom(ptr._internal_obj)
        OperatorGRPCAPI.update(op, request)

    @staticmethod
    def get_output_init(op, iOutput):
        from ansys.grpc.dpf import operator_pb2
        request = operator_pb2.OperatorEvaluationRequest()
        request.op.CopyFrom(op._internal_obj)
        request.pin = iOutput
        return request

    @staticmethod
    def get_output_finish(op, request, stype, subtype):
        from ansys.grpc.dpf import base_pb2
        request.type = base_pb2.Type.Value(stype.upper())
        if subtype != "":
            request.subtype = base_pb2.Type.Value(subtype.upper())
        if hasattr(op, "_progress_thread") and op._progress_thread:
            out = _get_stub(op._server).Get.future(request)
            op._progress_thread.start()
            out = out.result()
        else:
            out = _get_stub(op._server).Get(request)
        return OperatorGRPCAPI._take_out_of_get_response(out)

    @staticmethod
    def _take_out_of_get_response(response):
        if response.HasField("str"):
            return response.str
        elif response.HasField("int"):
            return response.int
        elif response.HasField("double"):
            return response.double
        elif response.HasField("bool"):
            return response.bool
        elif response.HasField("field"):
            return response.field
        elif response.HasField("collection"):
            return response.collection
        elif response.HasField("scoping"):
            return response.scoping
        elif response.HasField("mesh"):
            return response.mesh
        elif response.HasField("result_info"):
            return response.result_info
        elif response.HasField("time_freq_support"):
            return response.time_freq_support
        elif response.HasField("data_sources"):
            return response.data_sources
        elif response.HasField("cyc_support"):
            return response.cyc_support
        elif hasattr(response, "workflow") and response.HasField("workflow"):
            return response.workflow
        elif hasattr(response, "data_tree") and response.HasField("data_tree"):
            return response.data_tree
        elif hasattr(response, "any") and response.HasField("any"):
            return response.any
        elif hasattr(response, "generic_data_container") and response.HasField("generic_data_container"):
            return response.generic_data_container
        else:
            raise KeyError(response)

    @staticmethod
    def operator_getoutput_fields_container(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "collection"
        subtype = "field"
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_scopings_container(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "collection"
        subtype = "scoping"
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_field(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "field"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_scoping(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "scoping"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_data_sources(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "data_sources"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_meshes_container(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "collection"
        subtype = "meshed_region"
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_cyclic_support(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "cyclic_support"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_workflow(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "workflow"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_string(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "string"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_string_with_size(op, iOutput, size):
        if op._server.meet_version("8.0"):
            from ansys.grpc.dpf import operator_pb2
            request = operator_pb2.OperatorEvaluationRequest()
            request.op.CopyFrom(op._internal_obj)
            request.pin = iOutput
            service = _get_stub(op._server).GetStreamed(request)
            dtype = np.byte
            out = grpc_stream_helpers._data_get_chunk_(dtype, service, True, get_array=lambda chunk: chunk.array.array)
            size.val = out.size
            return bytes(out)
        else:
            out = OperatorGRPCAPI.operator_getoutput_string(op, iOutput, size)
            size.val = out.size
            return out

    @staticmethod
    def operator_getoutput_int(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "int"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_double(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "double"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_bool(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "bool"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_time_freq_support(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "time_freq_support"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_meshed_region(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "meshed_region"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_result_info(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "result_info"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_streams(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "streams"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_property_field(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "property_field"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_string_field(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "string_field"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_custom_type_field(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "custom_type_field"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_data_tree(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "data_tree"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_operator(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "operator"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_external_data(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "model"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_int_collection(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "collection"
        subtype = "int"
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_double_collection(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "collection"
        subtype = "double"
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_generic_data_container(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "generic_data_container"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_getoutput_as_any(op, iOutput):
        request = OperatorGRPCAPI.get_output_init(op, iOutput)
        stype = "any"
        subtype = ""
        return OperatorGRPCAPI.get_output_finish(op, request, stype, subtype)

    @staticmethod
    def operator_run(op):
        from ansys.grpc.dpf import base_pb2
        request = OperatorGRPCAPI.get_output_init(op, 0)
        request.type = base_pb2.Type.Value("RUN")
        if hasattr(op, "_progress_thread") and op._progress_thread:
            out = _get_stub(op._server).Get.future(request)
            op._progress_thread.start()
            out = out.result()
        else:
            out = _get_stub(op._server).Get(request)
