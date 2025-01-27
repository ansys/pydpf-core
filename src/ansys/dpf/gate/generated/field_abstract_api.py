#-------------------------------------------------------------------------------
# Field
#-------------------------------------------------------------------------------

class FieldAbstractAPI:
	@staticmethod
	def init_field_environment(object):
		pass

	@staticmethod
	def finish_field_environment(object):
		pass

	@staticmethod
	def field_delete(field):
		raise NotImplementedError

	@staticmethod
	def field_get_data(field, size):
		raise NotImplementedError

	@staticmethod
	def field_get_data_pointer(field, size):
		raise NotImplementedError

	@staticmethod
	def field_get_scoping(constfield, size):
		raise NotImplementedError

	@staticmethod
	def field_get_scoping_to_data_pointer_copy(field, scopingToDataPointer):
		raise NotImplementedError

	@staticmethod
	def field_get_entity_data(field, EntityIndex, size):
		raise NotImplementedError

	@staticmethod
	def field_get_entity_data_by_id(field, EntityId, size):
		raise NotImplementedError

	@staticmethod
	def field_get_unit(field):
		raise NotImplementedError

	@staticmethod
	def field_get_location(field):
		raise NotImplementedError

	@staticmethod
	def field_get_number_elementary_data(field):
		raise NotImplementedError

	@staticmethod
	def field_get_number_elementary_data_by_index(field, entityIndex):
		raise NotImplementedError

	@staticmethod
	def field_get_number_elementary_data_by_id(field, entityId):
		raise NotImplementedError

	@staticmethod
	def field_get_number_of_components(field):
		raise NotImplementedError

	@staticmethod
	def field_get_number_of_entities(field):
		raise NotImplementedError

	@staticmethod
	def field_elementary_data_size(field):
		raise NotImplementedError

	@staticmethod
	def field_get_data_size(field):
		raise NotImplementedError

	@staticmethod
	def field_get_eshell_layers(field):
		raise NotImplementedError

	@staticmethod
	def field_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_delete(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data(field, size):
		raise NotImplementedError

	@staticmethod
	def csfield_set_data(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_data_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_data_pointer(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_data_pointer_with_collection(field, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_entity_data(field, index, id, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_support(field, support):
		raise NotImplementedError

	@staticmethod
	def csfield_set_unit(field, symbol):
		raise NotImplementedError

	@staticmethod
	def csfield_set_location(field, location):
		raise NotImplementedError

	@staticmethod
	def csfield_set_meshed_region_as_support(field, support):
		raise NotImplementedError

	@staticmethod
	def csfield_update_entity_data_by_entity_index(field, EntityIndex, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_push_back(field, EntityId, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_get_scoping(field, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data_ptr(field, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_cscoping(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_shared_field_definition(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_field_definition(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_support(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data_pointer(field, size):
		raise NotImplementedError

	@staticmethod
	def csfield_set_field_definition(field, field_definition):
		raise NotImplementedError

	@staticmethod
	def csfield_set_fast_access_field_definition(field, field_definition):
		raise NotImplementedError

	@staticmethod
	def csfield_set_scoping(field, size, data):
		raise NotImplementedError

	@staticmethod
	def csfield_set_cscoping(field, scoping):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_data(field, EntityIndex, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_data_by_id(field, EntityId, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_unit(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_location(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_number_elementary_data(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_number_elementary_data_by_index(field, entityIndex):
		raise NotImplementedError

	@staticmethod
	def csfield_get_number_elementary_data_by_id(field, entityId):
		raise NotImplementedError

	@staticmethod
	def csfield_get_number_entities(field):
		raise NotImplementedError

	@staticmethod
	def csfield_elementary_data_size(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data_size(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_eshell_layers(field):
		raise NotImplementedError

	@staticmethod
	def csfield_set_eshell_layers(field, eshell_layer):
		raise NotImplementedError

	@staticmethod
	def csfield_resize_data(field, dataSize):
		raise NotImplementedError

	@staticmethod
	def csfield_resize_data_pointer(field, dataSize):
		raise NotImplementedError

	@staticmethod
	def csfield_get_number_of_components(field):
		raise NotImplementedError

	@staticmethod
	def csfield_resize(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def csfield_reserve(field, dataSize, scopingSize):
		raise NotImplementedError

	@staticmethod
	def csfield_get_name(field):
		raise NotImplementedError

	@staticmethod
	def csfield_set_name(field, name):
		raise NotImplementedError

	@staticmethod
	def csfield_get_string_property(field, key, sProp_ptr):
		raise NotImplementedError

	@staticmethod
	def csfield_add_string_property(field, key, sProp):
		raise NotImplementedError

	@staticmethod
	def csfield_del_string_property(field, key):
		raise NotImplementedError

	@staticmethod
	def csfield_get_support_as_meshed_region(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_support_as_time_freq_support(field):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_id(field, index):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_index(field, id):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data_for_dpf_vector(field, var1, data, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_data_pointer_for_dpf_vector(field, var1, data, size):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		raise NotImplementedError

	@staticmethod
	def csfield_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		raise NotImplementedError

	@staticmethod
	def field_new(fieldDimensionnality, numEntities, location):
		raise NotImplementedError

	@staticmethod
	def field_new_with_transformation(fieldDimensionnality, numEntities, location, wf, input_name, output_name):
		raise NotImplementedError

	@staticmethod
	def field_new_with1_ddimensionnality(fieldDimensionnality, numComp, numEntitiesToReserve, location):
		raise NotImplementedError

	@staticmethod
	def field_new_with2_ddimensionnality(fieldDimensionnality, numCompN, numCompM, numEntitiesToReserve, location):
		raise NotImplementedError

	@staticmethod
	def field_get_copy(field, bAllocateData, bCopyData, bscopingHardCopy):
		raise NotImplementedError

	@staticmethod
	def field_clone_to_different_dimension(field, fieldDimensionnality, numCompN, numCompM, location):
		raise NotImplementedError

	@staticmethod
	def csfield_cursor(f, index, data, id, size, n_comp, data_index):
		raise NotImplementedError

	@staticmethod
	def field_fast_access_ptr(field):
		raise NotImplementedError

	@staticmethod
	def field_fast_cursor(f, index, data, id, size, n_comp, data_index):
		raise NotImplementedError

	@staticmethod
	def field_new_on_client(client, dimensions, reserved_number_of_entity, loc):
		raise NotImplementedError

	@staticmethod
	def field_new_with1_ddimensionnality_on_client(client, fieldDimensionnality, numComp, numEntitiesToReserve, location):
		raise NotImplementedError

	@staticmethod
	def field_new_with2_ddimensionnality_on_client(client, fieldDimensionnality, numCompN, numCompM, numEntitiesToReserve, location):
		raise NotImplementedError

	@staticmethod
	def field_get_copy_on_client(id, client):
		raise NotImplementedError

