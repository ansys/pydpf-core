#-------------------------------------------------------------------------------
# Collection
#-------------------------------------------------------------------------------

class CollectionAbstractAPI:
	@staticmethod
	def init_collection_environment(object):
		pass

	@staticmethod
	def finish_collection_environment(object):
		pass

	@staticmethod
	def collection_of_int_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_double_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_string_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_char_new():
		raise NotImplementedError

	@staticmethod
	def collection_get_data_as_int(collection, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_data_as_double(collection, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_data_as_char(collection, size):
		raise NotImplementedError

	@staticmethod
	def collection_add_int_entry(collection, obj):
		raise NotImplementedError

	@staticmethod
	def collection_add_double_entry(collection, obj):
		raise NotImplementedError

	@staticmethod
	def collection_add_string_entry(collection, obj):
		raise NotImplementedError

	@staticmethod
	def collection_set_int_entry(collection, index, obj):
		raise NotImplementedError

	@staticmethod
	def collection_set_double_entry(collection, index, obj):
		raise NotImplementedError

	@staticmethod
	def collection_set_string_entry(collection, index, obj):
		raise NotImplementedError

	@staticmethod
	def collection_get_int_entry(collection, index):
		raise NotImplementedError

	@staticmethod
	def collection_get_double_entry(collection, index):
		raise NotImplementedError

	@staticmethod
	def collection_get_string_entry(collection, index):
		raise NotImplementedError

	@staticmethod
	def collection_set_data_as_int(collection, data, size):
		raise NotImplementedError

	@staticmethod
	def collection_set_data_as_double(collection, data, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_data_as_int_for_dpf_vector(collection, out, data, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_data_as_double_for_dpf_vector(collection, out, data, size):
		raise NotImplementedError

	@staticmethod
	def collection_of_scoping_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_field_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_mesh_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_custom_type_field_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_any_new():
		raise NotImplementedError

	@staticmethod
	def collection_of_scoping_new_with_data(data, num_ids, labels, num_labels, ids):
		raise NotImplementedError

	@staticmethod
	def collection_of_field_new_with_data(data, num_ids, labels, num_labels, ids):
		raise NotImplementedError

	@staticmethod
	def collection_of_mesh_new_with_data(data, num_ids, labels, num_labels, ids):
		raise NotImplementedError

	@staticmethod
	def collection_of_custom_type_field_new_with_data(data, num_ids, labels, num_labels, ids):
		raise NotImplementedError

	@staticmethod
	def collection_of_any_new_with_data(data, num_ids, labels, num_labels, ids):
		raise NotImplementedError

	@staticmethod
	def collection_get_num_labels(collection):
		raise NotImplementedError

	@staticmethod
	def collection_get_label(collection, labelIndex):
		raise NotImplementedError

	@staticmethod
	def collection_add_label(collection, label):
		raise NotImplementedError

	@staticmethod
	def collection_add_label_with_default_value(collection, label, value):
		raise NotImplementedError

	@staticmethod
	def collection_add_entry(collection, labelspace, obj):
		raise NotImplementedError

	@staticmethod
	def collection_push_back_entry(collection, labelspace, obj):
		raise NotImplementedError

	@staticmethod
	def collection_set_entry_by_index(collection, index, obj):
		raise NotImplementedError

	@staticmethod
	def collection_get_obj_by_index(collection, index):
		raise NotImplementedError

	@staticmethod
	def collection_get_obj(collection, space):
		raise NotImplementedError

	@staticmethod
	def collection_get_obj_label_space_by_index(collection, index):
		raise NotImplementedError

	@staticmethod
	def collection_get_objs_for_label_space(collection, space, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_num_obj_for_label_space(collection, space):
		raise NotImplementedError

	@staticmethod
	def collection_get_obj_by_index_for_label_space(collection, space, index):
		raise NotImplementedError

	@staticmethod
	def collection_fill_obj_indeces_for_label_space(collection, space, indices):
		raise NotImplementedError

	@staticmethod
	def collection_get_label_scoping(collection, label):
		raise NotImplementedError

	@staticmethod
	def collection_get_name(collection):
		raise NotImplementedError

	@staticmethod
	def collection_set_name(collection, name):
		raise NotImplementedError

	@staticmethod
	def collection_get_id(collection):
		raise NotImplementedError

	@staticmethod
	def collection_set_id(collection, id):
		raise NotImplementedError

	@staticmethod
	def collection_delete(collection):
		raise NotImplementedError

	@staticmethod
	def collection_get_size(collection):
		raise NotImplementedError

	@staticmethod
	def collection_reserve(collection, size):
		raise NotImplementedError

	@staticmethod
	def collection_resize(collection, size):
		raise NotImplementedError

	@staticmethod
	def collection_get_support(collection, label):
		raise NotImplementedError

	@staticmethod
	def collection_set_support(collection, label, support):
		raise NotImplementedError

	@staticmethod
	def collection_create_sub_collection(collection, space):
		raise NotImplementedError

	@staticmethod
	def collection_of_scoping_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_field_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_mesh_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_any_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_scoping_get_copy(id, client):
		raise NotImplementedError

	@staticmethod
	def collection_of_field_get_copy(id, client):
		raise NotImplementedError

	@staticmethod
	def collection_of_mesh_get_copy(id, client):
		raise NotImplementedError

	@staticmethod
	def collection_of_any_get_copy(id, client):
		raise NotImplementedError

	@staticmethod
	def collection_of_int_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_double_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_string_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def collection_of_string_new_local(client):
		raise NotImplementedError

