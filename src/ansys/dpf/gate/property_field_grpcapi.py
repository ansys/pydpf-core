import sys
import numpy as np
from ansys.dpf.gate.generated import property_field_abstract_api
from ansys.dpf.gate import errors, field_grpcapi

api_to_call = field_grpcapi.FieldGRPCAPI

# -------------------------------------------------------------------------------
# PropertyField
# -------------------------------------------------------------------------------

@errors.protect_grpc_class
class PropertyFieldGRPCAPI(property_field_abstract_api.PropertyFieldAbstractAPI):
    @staticmethod
    def init_property_field_environment(object):
        api_to_call.init_field_environment(object)

    @staticmethod
    def csproperty_field_new_on_client(client, numEntities, data_size):
        from ansys.grpc.dpf import field_pb2
        request = field_pb2.FieldRequest()
        request.size.scoping_size = numEntities
        request.size.data_size = data_size
        request.datatype = "int"
        return field_grpcapi._get_stub(client).Create(request)

    @staticmethod
    def csproperty_field_get_number_elementary_data(field):
        return api_to_call.csfield_get_number_elementary_data(field)

    @staticmethod
    def csproperty_field_get_number_of_components(field):
        return api_to_call.csfield_get_number_of_components(field)

    @staticmethod
    def csproperty_field_get_data_size(field):
        return api_to_call.csfield_get_data_size(field)

    @staticmethod
    def csproperty_field_set_cscoping(field, scoping):
        return api_to_call.csfield_set_cscoping(field, scoping)

    @staticmethod
    def csproperty_field_get_cscoping(field):
        return api_to_call.csfield_get_cscoping(field)

    @staticmethod
    def csproperty_field_get_entity_data(field, EntityIndex):
        return api_to_call.csfield_get_entity_data(field, EntityIndex)

    @staticmethod
    def csproperty_field_push_back(field, EntityId, size, data):
        return api_to_call.csfield_push_back(field, EntityId, size, data)

    @staticmethod
    def csproperty_field_get_data_pointer(field, np_array):
        return api_to_call.csfield_get_data_pointer(field, np_array)

    @staticmethod
    def csproperty_field_set_data_pointer(field, size, data):
        return api_to_call.csfield_set_data_pointer(field, size, data)

    @staticmethod
    def csproperty_field_get_data(field, np_array):
        return api_to_call.csfield_get_data(field, np_array)

    @staticmethod
    def csproperty_field_set_data(field, size, data):
        if not isinstance(data[0], (int, np.int32)):
            raise TypeError("data", "list of int")
        data = np.array(data, dtype=np.int32)
        metadata = [("size_int", f"{size}")]
        return api_to_call.csfield_raw_set_data(field, data, metadata)

    @staticmethod
    def csproperty_field_elementary_data_size(field):
        return api_to_call.csfield_get_number_of_components(field)

    @staticmethod
    def csproperty_field_get_shared_field_definition(field):
        return api_to_call.csfield_get_shared_field_definition(field)

    @staticmethod
    def csproperty_field_set_field_definition(field, field_definition):
        api_to_call.csfield_set_field_definition(field, field_definition)
