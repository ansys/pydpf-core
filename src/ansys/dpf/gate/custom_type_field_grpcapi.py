from builtins import isinstance

import numpy as np
from ansys.dpf.gate.generated import custom_type_field_abstract_api
from ansys.dpf.gate import errors, field_grpcapi, grpc_stream_helpers

api_to_call = field_grpcapi.FieldGRPCAPI

# -------------------------------------------------------------------------------
# CustomTypeField
# -------------------------------------------------------------------------------

@errors.protect_grpc_class
class CustomTypeFieldGRPCAPI(custom_type_field_abstract_api.CustomTypeFieldAbstractAPI):
    @staticmethod
    def init_custom_type_field_environment(object):
        api_to_call.init_field_environment(object)

    @staticmethod
    def cscustom_type_field_get_data(field, data):
        return api_to_call.csfield_get_data(field, data)

    @staticmethod
    def cscustom_type_field_get_data_pointer(field, np_array):
        return api_to_call.csfield_get_data_pointer(field, np_array)

    @staticmethod
    def cscustom_type_field_get_entity_data(field, EntityIndex):
        out = api_to_call.csfield_get_entity_data(field, EntityIndex)
        if out is not None:
            return np.frombuffer(out, dtype=field._type)

    @staticmethod
    def cscustom_type_field_get_entity_data_by_id(field, EntityId):
        out = api_to_call.csfield_get_entity_data_by_id(field, EntityId)
        if out is not None:
            return np.frombuffer(out, dtype=field._type)

    @staticmethod
    def cscustom_type_field_get_cscoping(field):
        return api_to_call.csfield_get_cscoping(field)

    @staticmethod
    def cscustom_type_field_get_number_elementary_data(field):
        return api_to_call.csfield_get_number_elementary_data(field)

    @staticmethod
    def cscustom_type_field_get_number_of_components(field):
        return api_to_call.csfield_get_number_of_components(field)

    @staticmethod
    def cscustom_type_field_get_data_size(field):
        return api_to_call.csfield_get_data_size(field)

    @staticmethod
    def cscustom_type_field_set_data(field, size, data):
        if not isinstance(data, (np.ndarray, np.generic)):
            data = np.ndarray(data)
        data = data.view(np.byte)
        metadata = [("size_bytes", f"{data.size}")]
        return api_to_call.csfield_raw_set_data(field, data, metadata)

    @staticmethod
    def cscustom_type_field_set_data_pointer(field, size, data):
        return api_to_call.csfield_set_data_pointer(field, size, data)

    @staticmethod
    def cscustom_type_field_set_cscoping(field, scoping):
        return api_to_call.csfield_set_cscoping(field, scoping)

    @staticmethod
    def cscustom_type_field_push_back(field, EntityId, size, data):
        return api_to_call.csfield_push_back(field, EntityId, size, data)

    @staticmethod
    def cscustom_type_field_resize(field, dataSize, scopingSize):
        return api_to_call.csfield_resize(field, dataSize, scopingSize)

    @staticmethod
    def cscustom_type_field_get_type(field, type, unitarySize):
        type.set(
            field._internal_obj.custom_type_def.unitary_datatype
        )
        unitarySize.set(
            field._internal_obj.custom_type_def.num_bytes_unitary_data
        )

    @staticmethod
    def cscustom_type_field_get_shared_field_definition(field):
        return api_to_call.csfield_get_shared_field_definition(field)

    @staticmethod
    def cscustom_type_field_get_support(field):
        return api_to_call.csfield_get_support(field)

    @staticmethod
    def cscustom_type_field_set_field_definition(field, field_definition):
        api_to_call.csfield_set_field_definition(field, field_definition)

    @staticmethod
    def cscustom_type_field_set_support(field, support):
        api_to_call.csfield_set_support(field, support)

    @staticmethod
    def cscustom_type_field_new_on_client(client, type, unitarySize, numEntities, numUnitaryData):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.FieldRequest()
        request.size.scoping_size = numEntities
        request.size.data_size = numUnitaryData
        request.datatype = "custom"
        request.custom_type_def.num_bytes_unitary_data = unitarySize
        request.custom_type_def.unitary_datatype = type
        return field_grpcapi._get_stub(client).Create(request)

