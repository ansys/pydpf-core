#-------------------------------------------------------------------------------
# CustomTypeField
#-------------------------------------------------------------------------------

class CustomTypeFieldAbstractAPI:
	@staticmethod
	def init_custom_type_field_environment(object):
		pass

	@staticmethod
	def finish_custom_type_field_environment(object):
		pass

	@staticmethod
	def cscustom_type_field_new(type, unitarySize, numEntities, numUnitaryData):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_data_for_dpf_vector(field, out, data, size):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_data_pointer_for_dpf_vector(field, out, data, size):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_cscoping(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_number_elementary_data(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_number_of_components(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_data_size(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_number_entities(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_property_data_tree(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_data(field, size, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_data_pointer(field, size, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_cscoping(field, scoping):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_data_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_data_pointer_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_resize(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_resize_data_pointer(field, dataSize):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_reserve(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_type(field, type, unitarySize):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_shared_field_definition(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_support(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_field_definition(field, field_definition):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_support(field, support):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_entity_data(field, index, id, size, data):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_name(field):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_set_name(field, name):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_entity_id(field, index):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_entity_index(field, id):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_new_on_client(client, type, unitarySize, numEntities, numUnitaryData):
		raise NotImplementedError

	@staticmethod
	def cscustom_type_field_get_copy(id, client):
		raise NotImplementedError

