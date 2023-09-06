from ansys.dpf.gate.generated import string_field_abstract_api
from ansys.dpf.gate import errors, field_grpcapi, grpc_stream_helpers

api_to_call = field_grpcapi.FieldGRPCAPI

# -------------------------------------------------------------------------------
# StringField
# -------------------------------------------------------------------------------

@errors.protect_grpc_class
class StringFieldGRPCAPI(string_field_abstract_api.StringFieldAbstractAPI):
	@staticmethod
	def init_string_field_environment(object):
		api_to_call.init_field_environment(object)

	@staticmethod
	def csstring_field_get_cscoping(field):
	    return api_to_call.csfield_get_cscoping(field)

	@staticmethod
	def csstring_field_get_data_size(field):
	    return api_to_call.csfield_get_data_size(field)

	@staticmethod
	def csstring_field_set_data(field, size, data):
		return api_to_call.csfield_set_data(field, size, data)

	@staticmethod
	def csstring_field_set_cscoping(field, scoping):
	    return api_to_call.csfield_set_cscoping(field, scoping)

	@staticmethod
	def csstring_field_push_back(field, EntityId, size, data):
		return api_to_call.csfield_push_back(field, EntityId, size, data)

	@staticmethod
	def csstring_field_resize(field, dataSize, scopingSize):
		raise api_to_call.csfield_resize(field, dataSize, scopingSize)

	@staticmethod
	def csstring_field_new_on_client(client, numEntities, data_size):
		from ansys.grpc.dpf import field_pb2
		request = field_pb2.FieldRequest()
		request.size.scoping_size = numEntities
		request.size.data_size = data_size
		request.datatype = "string"
		return field_grpcapi._get_stub(client).Create(request)

	@staticmethod
	def csstring_field_get_entity_data(field, EntityIndex):
		return api_to_call.csfield_get_entity_data(field, EntityIndex).tolist()

	@staticmethod
	def csstring_field_get_data(field, np_array):
		from ansys.grpc.dpf import field_pb2
		request = field_pb2.ListRequest()
		request.field.CopyFrom(field._internal_obj)
		service = field_grpcapi._get_stub(field._server).List(request)
		return grpc_stream_helpers._string_data_get_chunk_(service)

	@staticmethod
	def csstring_field_set_data(field, size, data):
		from ansys.grpc.dpf import field_pb2
		metadata = [("size_tot", f"{size}")]
		request = field_pb2.UpdateDataRequest()
		request.field.CopyFrom(field._internal_obj)
		field_grpcapi._get_stub(field._server).UpdateData(
			grpc_stream_helpers._string_data_chunk_yielder(request, data), metadata=metadata
		)
