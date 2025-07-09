#-------------------------------------------------------------------------------
# StringField
#-------------------------------------------------------------------------------

class StringFieldAbstractAPI:
	@staticmethod
	def init_string_field_environment(object):
		pass

	@staticmethod
	def finish_string_field_environment(object):
		pass

	@staticmethod
	def string_field_delete(field):
		raise NotImplementedError

	@staticmethod
	def string_field_get_entity_data(field, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def string_field_get_number_entities(field):
		raise NotImplementedError

	@staticmethod
	def csstring_field_new(numEntities, data_size):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_data_for_dpf_vector(field, out, data, size):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def string_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def string_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_data_for_dpf_vector_with_size(field, out, data, sizes, size):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_entity_data_for_dpf_vector_with_size(dpf_object, out, data, sizes, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_entity_data_by_id_for_dpf_vector_with_size(dpf_object, vec, data, sizes, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def string_field_get_entity_data_for_dpf_vector_with_size(dpf_object, out, data, sizes, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def string_field_get_entity_data_by_id_for_dpf_vector_with_size(dpf_object, vec, data, sizes, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_cscoping(field):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_data_size(field):
		raise NotImplementedError

	@staticmethod
	def csstring_field_set_data(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csstring_field_set_data_with_size(field, size, data, sizes):
		raise NotImplementedError

	@staticmethod
	def csstring_field_set_cscoping(field, scoping):
		raise NotImplementedError

	@staticmethod
	def csstring_field_set_data_pointer(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csstring_field_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def string_field_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def csstring_field_push_back_with_size(field, EntityId, size, data, sizes):
		raise NotImplementedError

	@staticmethod
	def string_field_push_back_with_size(field, EntityId, size, data, sizes):
		raise NotImplementedError

	@staticmethod
	def csstring_field_resize(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def csstring_field_reserve(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def string_field_fast_access_ptr(field):
		raise NotImplementedError

	@staticmethod
	def csstring_field_new_on_client(client, numEntities, data_size):
		raise NotImplementedError

	@staticmethod
	def csstring_field_get_copy(id, client):
		raise NotImplementedError

