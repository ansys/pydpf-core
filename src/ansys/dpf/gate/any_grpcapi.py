from ansys.dpf.gate import errors, data_processing_grpcapi
from ansys.dpf.gate.generated import any_abstract_api, any_capi


# -------------------------------------------------------------------------------
# Any
# ------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(AnyGRPCAPI.STUBNAME)


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
        from ansys.dpf.core import (
            field,
            property_field,
            generic_data_container,
            string_field,
            scoping,
            data_tree,
        )

        return [(int, base_pb2.Type.INT),
                (str, base_pb2.Type.STRING),
                (float, base_pb2.Type.DOUBLE),
                (field.Field, base_pb2.Type.FIELD),
                (property_field.PropertyField, base_pb2.Type.PROPERTY_FIELD),
                (string_field.StringField, base_pb2.Type.STRING_FIELD),
                (generic_data_container.GenericDataContainer, base_pb2.Type.GENERIC_DATA_CONTAINER),
                (scoping.Scoping, base_pb2.Type.SCOPING),
                (data_tree.DataTree, base_pb2.Type.DATA_TREE),
                ]

    @staticmethod
    def _get_as(any):
        from ansys.grpc.dpf import dpf_any_pb2
        request = dpf_any_pb2.GetAsRequest()

        request.any.CopyFrom(any._internal_obj)

        for type_tuple in AnyGRPCAPI._type_to_message_type():
            if any._internal_type == type_tuple[0]:
                request.type = type_tuple[1]
                return _get_stub(any._server.client).GetAs(request)

    @staticmethod
    def any_get_as_int(any):
        return AnyGRPCAPI._get_as(any).int_val

    @staticmethod
    def any_get_as_string(any):
        return AnyGRPCAPI._get_as(any).string_val

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
    def any_get_as_string_field(any):
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
    def _new_from(any, client=None):
        from ansys.grpc.dpf import dpf_any_pb2
        request = dpf_any_pb2.CreateRequest()

        if isinstance(any, int):
            request.int_val = any
        elif isinstance(any, str):
            request.string_val = any
        elif isinstance(any, float):
            request.double_val = any
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
    def any_new_from_double_on_client(client, any):
        return AnyGRPCAPI._new_from(any, client)

    @staticmethod
    def any_new_from_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_property_field(any):
        return AnyGRPCAPI._new_from(any, any._server)

    @staticmethod
    def any_new_from_string_field(any):
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

