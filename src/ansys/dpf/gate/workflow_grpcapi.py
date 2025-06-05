from ansys.dpf.gate.generated import workflow_abstract_api
from ansys.dpf.gate.operator_grpcapi import OperatorGRPCAPI
from ansys.dpf.gate import errors, grpc_stream_helpers
import numpy as np

#-------------------------------------------------------------------------------
# Workflow
#-------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(WorkflowGRPCAPI.STUBNAME)

def _set_array_to_request(request, bytes):
    request.array.array = bytes


@errors.protect_grpc_class
class WorkflowGRPCAPI(workflow_abstract_api.WorkflowAbstractAPI):
    STUBNAME = "workflow_stub"

    @staticmethod
    def init_workflow_environment(object):
        from ansys.grpc.dpf import workflow_pb2_grpc
        object._server.create_stub_if_necessary(WorkflowGRPCAPI.STUBNAME,
                                                workflow_pb2_grpc.WorkflowServiceStub)
        object._deleter_func = (_get_stub(object._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def work_flow_new_on_client(client):
        from ansys.grpc.dpf import base_pb2, workflow_pb2
        request = base_pb2.Empty()
        if hasattr(workflow_pb2, "CreateRequest"):
            request = workflow_pb2.CreateRequest(empty=request)
        return _get_stub(client).Create(request)

    @staticmethod
    #TO DO: add @version_requires("3.0")
    def work_flow_get_copy_on_other_client(wf, address, protocol):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.RemoteCopyRequest()
        request.wf.CopyFrom(wf._internal_obj)
        request.address = address
        create_request = workflow_pb2.CreateRequest()
        create_request.remote_copy.CopyFrom(request)
        return _get_stub(wf._server).Create(create_request)

    @staticmethod
    def _connect_init(wf, pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdateConnectionRequest()
        request.wf.CopyFrom(wf._internal_obj)
        request.pin_name = pin_name
        return request

    @staticmethod
    def work_flow_connect_int(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.int = value
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_bool(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.bool = value
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_double(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.double = value
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_string(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.str = value
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_string_with_size(wf, pin_name, value, size):
        if wf._server.meet_version("8.0"):
            from ansys.grpc.dpf import workflow_pb2, base_pb2
            request = workflow_pb2.ArrayUpdateConnectionRequest()
            request.wf.CopyFrom(wf._internal_obj)
            request.pin_name = pin_name
            request.type = base_pb2.Type.Value("STRING")
            metadata = [("size_bytes", f"{size.val.value}")]
            _get_stub(wf._server).UpdateConnectionStreamed(
                grpc_stream_helpers._data_chunk_yielder(
                    request,
                    value,
                    set_array=_set_array_to_request
                ),
                metadata=metadata)
        else:
            WorkflowGRPCAPI.work_flow_connect_string(wf, pin_name, value)

    @staticmethod
    def work_flow_connect_scoping(wf, pin_name, scoping):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.scoping.CopyFrom(scoping._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_data_sources(wf, pin_name, dataSources):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_field(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.field.CopyFrom(value._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_collection(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.collection.CopyFrom(value._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_collection_as_vector(wf, pin_name, value):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.collection.CopyFrom(value._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_meshed_region(wf, pin_name, mesh):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.mesh.CopyFrom(mesh._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_property_field(wf, pin_name, field):
        return WorkflowGRPCAPI.work_flow_connect_field(wf, pin_name, field)

    @staticmethod
    def work_flow_connect_string_field(wf, pin_name, field):
        return WorkflowGRPCAPI.work_flow_connect_field(wf, pin_name, field)

    @staticmethod
    def work_flow_connect_custom_type_field(wf, pin_name, field):
        return WorkflowGRPCAPI.work_flow_connect_field(wf, pin_name, field)

    @staticmethod
    def work_flow_connect_cyclic_support(wf, pin_name, support):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.cyc_support.CopyFrom(support._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_time_freq_support(wf, pin_name, support):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.time_freq_support.CopyFrom(support._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_workflow(wf, pin_name, otherwf):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.workflow.CopyFrom(otherwf._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_label_space(wf, pin_name, labelspace):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.label_space.CopyFrom(labelspace._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_vector_int(wf, pin_name, ptrValue, size):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.vint.rep_int.extend(ptrValue)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_vector_double(wf, pin_name, ptrValue, size):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.vdouble.rep_double.extend(ptrValue)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_operator_output(wf, pin_name, value, output_pin):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.inputop.inputop.CopyFrom(value._internal_obj)
        request.inputop.pinOut = output_pin
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_data_tree(wf, pin_name, dataTree):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.data_tree.CopyFrom(dataTree._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_any(wf, pin_name, ptr):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.as_any.CopyFrom(ptr._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def work_flow_connect_generic_data_container(wf, pin_name, container):
        request = WorkflowGRPCAPI._connect_init(wf, pin_name)
        request.generic_data_container.CopyFrom(container._internal_obj)
        _get_stub(wf._server).UpdateConnection(request)

    @staticmethod
    def get_output_init(wf, pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.WorkflowEvaluationRequest()
        request.wf.CopyFrom(wf._internal_obj)
        request.pin_name = pin_name
        return request

    @staticmethod
    def get_output_finish(wf, request, stype, subtype=""):
        from ansys.grpc.dpf import base_pb2
        request.type = base_pb2.Type.Value(stype.upper())
        if subtype != "":
            request.subtype = base_pb2.Type.Value(subtype.upper())
        if hasattr(wf, "_progress_thread") and wf._progress_thread:
            out = _get_stub(wf._server).Get.future(request)
            wf._progress_thread.start()
            out = out.result()
        else:
            out = _get_stub(wf._server).Get(request)
        return OperatorGRPCAPI._take_out_of_get_response(out)

    @staticmethod
    def work_flow_getoutput_fields_container(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "collection"
        subtype = "field"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype, subtype)

    @staticmethod
    def work_flow_getoutput_scopings_container(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "collection"
        subtype = "scoping"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype, subtype)

    @staticmethod
    def work_flow_getoutput_meshes_container(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "collection"
        subtype = "meshed_region"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype, subtype)

    @staticmethod
    def work_flow_getoutput_field(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "field"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_scoping(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "scoping"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_time_freq_support(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "time_freq_support"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_meshed_region(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "meshed_region"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_result_info(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "result_info"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_property_field(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "property_field"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_string_field(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "string_field"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_custom_type_field(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "custom_type_field"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_cyclic_support(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "cyclic_support"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_data_sources(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "data_sources"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_workflow(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "workflow"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_generic_data_container(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "generic_data_container"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_int_collection(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "collection"
        subtype = "int"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype, subtype)

    @staticmethod
    def work_flow_getoutput_double_collection(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "collection"
        subtype = "double"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype, subtype)

    @staticmethod
    def work_flow_getoutput_operator(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "operator"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_data_tree(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "data_tree"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_as_any(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "any"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_string(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "string"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_string_with_size(wf, pin_name, size):
        if wf._server.meet_version("8.0"):
            from ansys.grpc.dpf import workflow_pb2
            request = workflow_pb2.WorkflowEvaluationRequest()
            request.wf.CopyFrom(wf._internal_obj)
            request.pin_name = pin_name
            service = _get_stub(wf._server).GetStreamed(request)
            dtype = np.byte
            out = grpc_stream_helpers._data_get_chunk_(dtype, service, True, get_array=lambda chunk: chunk.array.array)
            size.val = out.size
            return bytes(out)
        else:
            out = WorkflowGRPCAPI.work_flow_getoutput_string(wf, pin_name)
            size.val = out.size
            return out

    @staticmethod
    def work_flow_getoutput_int(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "int"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_double(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "double"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_getoutput_bool(wf, pin_name):
        request = WorkflowGRPCAPI.get_output_init(wf, pin_name)
        stype = "bool"
        return WorkflowGRPCAPI.get_output_finish(wf, request, stype)

    @staticmethod
    def work_flow_set_name_input_pin(wf, op, pin, pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(wf._internal_obj)
        input_request = workflow_pb2.OperatorNaming()
        input_request.name = pin_name
        input_request.pin = pin
        input_request.operator.CopyFrom(op._internal_obj)
        request.inputs_naming.extend([input_request])
        _get_stub(wf._server).UpdatePinNames(request)

    @staticmethod
    def work_flow_set_name_output_pin(wf, op, pin, pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(wf._internal_obj)
        output_request = workflow_pb2.OperatorNaming()
        output_request.name = pin_name
        output_request.pin = pin
        output_request.operator.CopyFrom(op._internal_obj)
        request.outputs_naming.extend([output_request])
        _get_stub(wf._server).UpdatePinNames(request)

    @staticmethod
    def work_flow_add_operator(wf, op):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.AddOperatorsRequest()
        request.wf.CopyFrom(wf._internal_obj)
        request.operators.extend([op._internal_obj])
        _get_stub(wf._server).AddOperators(request)

    @staticmethod
    def work_flow_record_instance(wf, user_name, transfer_ownership):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.RecordInInternalRegistryRequest()
        request.wf.CopyFrom(wf._internal_obj)
        if user_name:
            request.identifier = user_name
        request.transferOwnership = transfer_ownership
        return _get_stub(wf._server).RecordInInternalRegistry(request).id

    @staticmethod
    def work_flow_get_by_identifier_on_client(identifier, client):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.WorkflowFromInternalRegistryRequest()
        request.registry_id = identifier
        return _get_stub(client).GetFromInternalRegistry(request)

    @staticmethod
    def _info(wf):
        """Dictionary with the operator names and the exposed input and output names.

        Returns
        ----------
        info : dictionarry str->list str
            Dictionary with ``"operator_names"``, ``"input_names"``, and ``"output_names"`` key.
        """
        tmp = _get_stub(wf._server).List(wf._internal_obj)
        out = {"operator_names": [], "input_names": [], "output_names": []}
        for name in tmp.operator_names:
            out["operator_names"].append(name)
        for name in tmp.input_pin_names.pin_names:
            out["input_names"].append(name)
        for name in tmp.output_pin_names.pin_names:
            out["output_names"].append(name)
        return out

    @staticmethod
    def work_flow_number_of_operators(wf):
        return len(WorkflowGRPCAPI._info(wf)["operator_names"])

    @staticmethod
    def work_flow_operator_name_by_index(wf, op_index):
        return WorkflowGRPCAPI._info(wf)["operator_names"][op_index]

    @staticmethod
    def work_flow_number_of_input(wf):
        return len(WorkflowGRPCAPI._info(wf)["input_names"])

    @staticmethod
    def work_flow_number_of_output(wf):
        return len(WorkflowGRPCAPI._info(wf)["output_names"])

    @staticmethod
    def work_flow_input_by_index(wf, pin_index):
        return WorkflowGRPCAPI._info(wf)["input_names"][pin_index]

    @staticmethod
    def work_flow_output_by_index(wf, pin_index):
        return WorkflowGRPCAPI._info(wf)["output_names"][pin_index]

    @staticmethod
    def work_flow_connect_with(wf_right, wf2_left):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.ConnectRequest()
        request.right_wf.CopyFrom(wf_right._internal_obj)
        request.left_wf.CopyFrom(wf2_left._internal_obj)
        return _get_stub(wf_right._server).Connect(request)

    @staticmethod
    def work_flow_connect_with_specified_names(wf_right, wf2_left, map):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.ConnectRequest()
        request.right_wf.CopyFrom(wf_right._internal_obj)
        request.left_wf.CopyFrom(wf2_left._internal_obj)
        request.input_to_output.extend(map._internal_obj)
        return _get_stub(wf_right._server).Connect(request)

    @staticmethod
    def workflow_create_connection_map_for_object(obj):
        return []

    @staticmethod
    def workflow_add_entry_connection_map(map, out, in_):
        from ansys.grpc.dpf import workflow_pb2
        map._internal_obj.append(workflow_pb2.InputToOutputChainRequest(
            output_name=out,
            input_name=in_)
        )

    @staticmethod
    def work_flow_create_from_text_on_client(text, client):
        from ansys.grpc.dpf import workflow_pb2
        if isinstance(text, str):
            save_text = text
            text = workflow_pb2.TextStream()
            text.stream = save_text
        return _get_stub(client).LoadFromStream(text)

    @staticmethod
    def work_flow_write_to_text(wf):
        return _get_stub(wf._server).WriteToStream(wf._internal_obj)

    @staticmethod
    def work_flow_rename_input_pin(wf, pin_name, new_pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(wf._internal_obj)
        output_request = workflow_pb2.OperatorNaming()
        output_request.name = new_pin_name
        output_request.old_name = pin_name
        request.inputs_naming.extend([output_request])
        _get_stub(wf._server).UpdatePinNames(request)

    @staticmethod
    def work_flow_rename_output_pin(wf, pin_name, new_pin_name):
        from ansys.grpc.dpf import workflow_pb2
        request = workflow_pb2.UpdatePinNamesRequest()
        request.wf.CopyFrom(wf._internal_obj)
        output_request = workflow_pb2.OperatorNaming()
        output_request.name = new_pin_name
        output_request.old_name = pin_name
        request.outputs_naming.extend([output_request])
        _get_stub(wf._server).UpdatePinNames(request)
