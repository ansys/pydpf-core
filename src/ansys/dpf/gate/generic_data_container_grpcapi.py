from ansys.dpf.gate import errors, data_processing_grpcapi, utils
from ansys.dpf.gate.generated import generic_data_container_abstract_api, \
	generic_data_container_abstract_api


# -------------------------------------------------------------------------------
# GenericDataContainer
# ------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(GenericDataContainerGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class GenericDataContainerGRPCAPI(generic_data_container_abstract_api.GenericDataContainerAbstractAPI):
	STUBNAME = "generic_data_container_stub"

	@staticmethod
	def init_generic_data_container_environment(object):
		from ansys.grpc.dpf import generic_data_container_pb2_grpc
		object._server.create_stub_if_necessary(GenericDataContainerGRPCAPI.STUBNAME,
											 generic_data_container_pb2_grpc.GenericDataContainerServiceStub)
		data_processing_grpcapi.DataProcessingGRPCAPI.init_data_processing_environment(object)
		object._deleter_func = (data_processing_grpcapi._get_stub(object._server).Delete, lambda obj: obj._internal_obj)

	@staticmethod
	def generic_data_container_get_property_any(container, name):
		from ansys.grpc.dpf import generic_data_container_pb2
		request = generic_data_container_pb2.GetPropertyRequest()
		request.gdc.CopyFrom(container._internal_obj)
		request.property_name.extend([name])
		s = dir(_get_stub(container._server).GetProperty(request).any)
		return _get_stub(container._server).GetProperty(request).any[0]

	@staticmethod
	def generic_data_container_set_property_any(container, name, any):
		from ansys.grpc.dpf import generic_data_container_pb2
		request = generic_data_container_pb2.SetPropertyRequest()
		request.gdc.CopyFrom(container._internal_obj)
		request.property_name.extend([name])
		request.any.add().CopyFrom(any._internal_obj)
		return _get_stub(container._server).SetProperty(request)

	@staticmethod
	def generic_data_container_set_property_dpf_type(container, name, any):
		from ansys.grpc.dpf import generic_data_container_pb2
		request = generic_data_container_pb2.SetPropertyRequest()
		request.gdc.CopyFrom(container._internal_obj)
		request.property_name.extend([name])
		request.any.add().id.CopyFrom(any._internal_obj.id)
		return _get_stub(container._server).SetProperty(request)

	@staticmethod
	def generic_data_container_new_on_client(client):
		from ansys.grpc.dpf import generic_data_container_pb2, base_pb2
		return _get_stub(client).Create(base_pb2.Empty())

	@staticmethod
	def generic_data_container_get_property_names(client):
		from ansys.grpc.dpf import generic_data_container_pb2, base_pb2
		request = generic_data_container_pb2.GetPropertyNamesRequest()
		request.gdc.CopyFrom(client._internal_obj)
		response = _get_stub(client._server).GetPropertyNames(request).property_names
		string = dir(response)
		return utils.to_array(response)

	@staticmethod
	def generic_data_container_get_property_types(client):
		from ansys.grpc.dpf import generic_data_container_pb2, base_pb2
		request = generic_data_container_pb2.GetPropertyTypesRequest()
		request.gdc.CopyFrom(client._internal_obj)
		response = _get_stub(client._server).GetPropertyTypes(request).property_types
		return utils.to_array(response)
