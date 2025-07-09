#-------------------------------------------------------------------------------
# PropertyField
#-------------------------------------------------------------------------------

class PropertyFieldAbstractAPI:
	@staticmethod
	def init_property_field_environment(object):
		pass

	@staticmethod
	def finish_property_field_environment(object):
		pass

	@staticmethod
	def property_field_delete(field):
		raise NotImplementedError

	@staticmethod
	def property_field_get_data(field, size):
		raise NotImplementedError

	@staticmethod
	def property_field_get_data_pointer(field, size):
		raise NotImplementedError

	@staticmethod
	def property_field_get_scoping(field, size):
		raise NotImplementedError

	@staticmethod
	def property_field_get_entity_data(field, EntityIndex, size):
		raise NotImplementedError

	@staticmethod
	def property_field_get_entity_data_by_id(field, EntityId, size):
		raise NotImplementedError

	@staticmethod
	def property_field_get_location(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_new(numEntities, data_size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_new_with_transformation(numEntities, data_size, wf, input_name, output_name):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_delete(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_data(field, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_data_for_dpf_vector(field, out, data, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_data_pointer(field, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_data_pointer_for_dpf_vector(field, out, data, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_cscoping(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_data(field, EntityIndex, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_data_by_id(field, EntityId, size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_number_elementary_data(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_elementary_data_size(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_data(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_data_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_data_pointer_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_data_pointer(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_scoping(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_cscoping(field, scoping):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_entity_data(field, index, id, size, data):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_resize(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_reserve(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def csproperty_get_data_fast(f, index, data, id, size, n_comp):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_location(dpf_object):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_data_size(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_id(field, index):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_entity_index(field, id):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_shared_field_definition(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_field_definition(field, field_definition):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_name(field):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_set_name(field, name):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_fast_access_ptr(field):
		raise NotImplementedError

	@staticmethod
	def property_get_data_fast(f, index, data, id, size, n_comp):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_new_on_client(client, numEntities, data_size):
		raise NotImplementedError

	@staticmethod
	def csproperty_field_get_copy(id, client):
		raise NotImplementedError

