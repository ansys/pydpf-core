#-------------------------------------------------------------------------------
# Scoping
#-------------------------------------------------------------------------------

class ScopingAbstractAPI:
	@staticmethod
	def init_scoping_environment(object):
		pass

	@staticmethod
	def finish_scoping_environment(object):
		pass

	@staticmethod
	def scoping_new():
		raise NotImplementedError

	@staticmethod
	def scoping_new_with_data(location, ids, size):
		raise NotImplementedError

	@staticmethod
	def scoping_delete(scoping):
		raise NotImplementedError

	@staticmethod
	def scoping_set_data(scoping, location, ids, size):
		raise NotImplementedError

	@staticmethod
	def scoping_get_data(scoping, location, size):
		raise NotImplementedError

	@staticmethod
	def scoping_set_ids(scoping, ids, size):
		raise NotImplementedError

	@staticmethod
	def scoping_set_ids_with_collection(scoping, ids):
		raise NotImplementedError

	@staticmethod
	def scoping_get_ids(scoping, size):
		raise NotImplementedError

	@staticmethod
	def scoping_get_ids_for_dpf_vector(scoping, out, data, size):
		raise NotImplementedError

	@staticmethod
	def scoping_get_size(scoping):
		raise NotImplementedError

	@staticmethod
	def scoping_set_location(scoping, location):
		raise NotImplementedError

	@staticmethod
	def scoping_get_location(scoping):
		raise NotImplementedError

	@staticmethod
	def scoping_set_entity(scoping, id, index):
		raise NotImplementedError

	@staticmethod
	def scoping_id_by_index(scoping, index):
		raise NotImplementedError

	@staticmethod
	def scoping_index_by_id(scoping, id):
		raise NotImplementedError

	@staticmethod
	def scoping_resize(scoping, size):
		raise NotImplementedError

	@staticmethod
	def scoping_reserve(scoping, size):
		raise NotImplementedError

	@staticmethod
	def scoping_get_ids_hash(scoping, hash):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_access_ptr(scoping):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_get_ids(scoping, size):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_set_entity(scoping, id, index):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_id_by_index(scoping, index):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_index_by_id(scoping, id):
		raise NotImplementedError

	@staticmethod
	def scoping_fast_get_size(scoping):
		raise NotImplementedError

	@staticmethod
	def scoping_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def scoping_get_copy(id, client):
		raise NotImplementedError

