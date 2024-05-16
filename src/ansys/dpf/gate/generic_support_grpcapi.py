from ansys.dpf.gate import errors, data_processing_grpcapi
from ansys.dpf.gate.generated import generic_support_abstract_api

# -------------------------------------------------------------------------------
# GenericSupport
# ------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(GenericSupportGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class GenericSupportGRPCAPI(generic_support_abstract_api.GenericSupportAbstractAPI):
	STUBNAME = "generic_support_stub"

	@staticmethod
	def init_generic_support_environment(object):
		from ansys.grpc.dpf import generic_support_pb2_grpc
		object._server.create_stub_if_necessary(GenericSupportGRPCAPI.STUBNAME,
											 generic_support_pb2_grpc.GenericSupportServiceStub)
		data_processing_grpcapi.DataProcessingGRPCAPI.init_data_processing_environment(object)
		object._deleter_func = (data_processing_grpcapi._get_stub(object._server).Delete, lambda obj: obj._internal_obj)

	@staticmethod
	def _generic_support_set_field_support_of_property(support, name, field):
		from ansys.grpc.dpf import generic_support_pb2
		request = generic_support_pb2.UpdateRequest()
		request.support.CopyFrom(support._internal_obj)
		request.field_supports.get_or_create(name).CopyFrom(field._internal_obj)
		return _get_stub(support._server).Update(request)

	@staticmethod
	def generic_support_set_field_support_of_property(support, name, field):
		return GenericSupportGRPCAPI._generic_support_set_field_support_of_property(
			support, name, field
		)

	@staticmethod
	def generic_support_set_property_field_support_of_property(support, name, field):
		return GenericSupportGRPCAPI._generic_support_set_field_support_of_property(
			support, name, field
		)

	@staticmethod
	def generic_support_set_string_field_support_of_property(support, name, field):
		return GenericSupportGRPCAPI._generic_support_set_field_support_of_property(
			support, name, field
		)

	@staticmethod
	def generic_support_new_on_client(client, name):
		from ansys.grpc.dpf import generic_support_pb2
		request = generic_support_pb2.CreateRequest()
		request.location = name
		return _get_stub(client).Create(request)