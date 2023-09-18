#-------------------------------------------------------------------------------
# DataBase
#-------------------------------------------------------------------------------

class DataBaseAbstractAPI:
	@staticmethod
	def init_data_base_environment(object):
		pass

	@staticmethod
	def finish_data_base_environment(object):
		pass

	@staticmethod
	def data_base_create_and_hold(id):
		raise NotImplementedError

	@staticmethod
	def data_base_record_entity_by_db_id(dbid, obj):
		raise NotImplementedError

	@staticmethod
	def data_base_record_entity(db, obj):
		raise NotImplementedError

	@staticmethod
	def data_base_erase_entity(db, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_erase_entity_by_db_id(dbid, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_release_entity(db, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_release_by_db_id(dbid, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_get_entity(db, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_get_by_db_id(dbid, entityId):
		raise NotImplementedError

	@staticmethod
	def data_base_delete(dbid):
		raise NotImplementedError

	@staticmethod
	def data_base_erase_all_held_entities(db):
		raise NotImplementedError

