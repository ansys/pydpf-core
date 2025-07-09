from ansys.dpf.gate import errors, data_processing_grpcapi, grpc_stream_helpers
from ansys.dpf.gate.generated import any_abstract_api, any_capi
import numpy as np


# -------------------------------------------------------------------------------
# Any
# ------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(AnyGRPCAPI.STUBNAME)


def _set_array_to_request(request, bytes):
    request.array.array = bytes


@errors.protect_grpc_class
class AnyGRPCAPI(any_abstract_api.AnyAbstractAPI):
    STUBNAME = "any_stub"

    @staticmethod
    def init_any_environment(object):
        from ansys.grpc.dpf import dpf_any_pb2_grpc
        object._server.create_stub_if_necessary(AnyGRPCAPI.STUBNAME,
                                                dpf_any_pb2_grpc.DpfAnyServiceStub)
        data_processing_grpcapi.DataProcessingGRPCAPI.init_data_processing_environment(object)
        object._deleter_func = (data_processing_grpcapi._get_stub(object._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def _type_to_message_type():
        from ansys.grpc.dpf import base_pb2
        from ansys.dpf.gate import dpf_vector
        from ansys.dpf.core import (
            field,
            fields_container,
            property_field,
            generic_data_container,
            string_field,
            scoping,
            data_tree,
            custom_type_field,
            collection_base,
            workflow,
            dpf_operator,
        )

        return [(int, base_pb2.Type.INT),
                (str, base_pb2.Type.STRING),
                (float, base_pb2.Type.DOUBLE),
                (bytes, base_pb2.Type.STRING),
                (field.Field, base_pb2.Type.FIELD),
                (fields_container.FieldsContainer, base_pb2.Type.COLLECTION, base_pb2.Type.FIELD),
                (property_field.PropertyField, base_pb2.Type.PROPERTY_FIELD),
                (string_field.StringField, base_pb2.Type.STRING_FIELD),
                (custom_type_field.CustomTypeField, base_pb2.Type.CUSTOM_TYPE_FIELD),
                (generic_data_container.GenericDataContainer, base_pb2.Type.GENERIC_DATA_CONTAINER),
                (scoping.Scoping, base_pb2.Type.SCOPING),
                (data_tree.DataTree, base_pb2.Type.DATA_TREE),
                (workflow.Workflow, base_pb2.Type.WORKFLOW),
                (collection_base.CollectionBase, base_pb2.Type.COLLECTION, base_pb2.Type.ANY),
                (dpf_vector.DPFVectorInt, base_pb2.Type.COLLECTION, base_pb2.Type.INT),
                (dpf_operator.Operator, base_pb2.Type.OPERATOR),
                ]

    @staticmethod
    def _get_as(any):
        from ansys.grpc.dpf import dpf_any_pb2
        request = dpf_any_pb2.GetAsRequest()

        request.any.CopyFrom(any._internal_obj)

        for type_tuple in AnyGRPCAPI._type_to_message_type():
            if issubclass(any._internal_type, type_tuple[0]):
                request.type = type_tuple[1]
                if len(type_tuple) > 2:
                    request.subtype = type_tuple[2]
                return _get_stub(any._server.client).GetAs(request)

        raise KeyError(any._internal_type)

    @staticmethod
    def any_get_as_int(any):
        return AnyGRPCAPI._get_as(any).int_val

    @staticmethod
    def any_get_as_string(any):
        return AnyGRPCAPI._get_as(any).string_val

    @staticmethod
    def any_get_as_string_with_size(any, size):
        if any._server.meet_version("8.0"):
            from ansys.grpc.dpf import dpf_any_pb2, base_pb2
            request = dpf_any_pb2.GetAsRequest()
            request.any.CopyFrom(any._internal_obj)
            request.type = base_pb2.Type.STRING
            service = _get_stub(any._server).GetAsStreamed(request)
            dtype = np.byte
            out = grpc_stream_helpers._data_get_chunk_(dtype, service, True, get_array=lambda chunk: chunk.array.array)
            size.val = out.size
            return bytes(out)
        else:
            out = AnyGRPCAPI.any_get_as_string(any)
            size.val = out.size
            return out

    @staticmethod
    def any_get_as_double(any):
        return AnyGRPCAPI._get_as(any).double_val

    @staticmethod
    def any_get_as_field(any):
        return AnyGRPCAPI._get_as(any).field

    @staticmethod
    def any_get_as_property_field(any):
        return AnyGRPCAPI._get_as(any).field
    
    @staticmethod
    def any_get_as_fields_container(any):
        return AnyGRPCAPI._get_as(any).collection

    @staticmethod
    def any_get_as_string_field(any):
        return AnyGRPCAPI._get_as(any).field

    @staticmethod
    def any_get_as_custom_type_field(any):
        return AnyGRPCAPI._get_as(any).field

    @staticmethod
    def any_get_as_generic_data_container(any):
        return AnyGRPCAPI._get_as(any).generic_data_container

    @staticmethod
    def any_get_as_scoping(any):
        return AnyGRPCAPI._get_as(any).scoping

    @staticmethod
    def any_get_as_data_tree(any):
        return AnyGRPCAPI._get_as(any).data_tree

    @staticmethod
    def any_get_as_any_collection(any):
        return AnyGRPCAPI._get_as(any).collection

    @staticmethod
    def any_get_as_int_collection(any):
        return AnyGRPCAPI._get_as(any).collection

    @staticmethod
    def any_get_as_workflow(any):
        return AnyGRPCAPI._get_as(any).workflow

    @staticmethod
    def any_get_as_operator(any):
        return AnyGRPCAPI._get_as(any).operator

    @staticmethod
    def _new_from(any, client=None):
        from ansys.grpc.dpf import dpf_any_pb2
        request = dpf_any_pb2.CreateRequest()

        if isinstance(any, int):
            request.int_val = any
        elif isinstance(any, str):
            request.string_val = any
        elif isinstance(any, float):
            request.double_val = any
        elif isinstance(any, bytes):
            request.string_val = any.decode()
        else:
            request.id.CopyFrom(any._internal_obj.id)

        for type_tuple in AnyGRPCAPI._type_to_message_type():
            if isinstance(any, type_tuple[0]):
                request.type = type_tuple[1]
                return _get_stub(client).Create(request)

    @staticmethod
    def any_new_from_int_on_client(client, any):
        return AnyGRPCAPI._new_from(any, client)

    @staticmethod
    def any_new_from_string_on_client(client, any):
        return AnyGRPCAPI._new_from(any, client)

    @staticmethod
    def any_new_from_string_with_size_on_client(client, any, size):
        if client.meet_version("8.0"):
            from ansys.grpc.dpf import dpf_any_pb2, base_pb2
            request = dpf_any_pb2.CreateStreamedRequest()
            request.type = base_pb2.Type.STRING
            metadata = [("size_bytes", f"{size.val.value}")]
            return _get_stub(client).CreateStreamed(
                grpc_stream_helpers._data_chunk_yielder(
                    request,
                    any,
                    set_array=_set_array_to_request
                ),
                metadata=metadata)
        else:
            return AnyGRPCAPI.any_new_from_string_on_client(client, any)

    @staticmethod
    def any_new_from_double_on_client(client, any):
        return AnyGRPCAPI._new_from(any, client)

    @staticmethod
    def any_new_from_int_collection(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_property_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_fields_container(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_string_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_custom_type_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_generic_data_container(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_scoping(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_data_tree(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_workflow(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_operator(any):
        return AnyGRPCAPI._new_from(any, any._server)
