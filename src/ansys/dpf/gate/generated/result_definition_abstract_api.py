#-------------------------------------------------------------------------------
# ResultDefinition
#-------------------------------------------------------------------------------

class ResultDefinitionAbstractAPI:
	@staticmethod
	def init_result_definition_environment(object):
		pass

	@staticmethod
	def finish_result_definition_environment(object):
		pass

	@staticmethod
	def result_definition_new():
		raise NotImplementedError

	@staticmethod
	def result_definition_delete(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_criteria(resDef, criteria):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_criteria(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_sub_criteria(resDef, subCriteria):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_sub_criteria(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_location(resDef, location):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_location(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_field_cslocation(resDef, CSlocation):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_field_cslocation(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_user_cs(resDef, userCS):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_user_cs(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_mesh_scoping(resDef, scoping):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_mesh_scoping(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_cyclic_sectors_scoping(resDef, scoping, stageNum):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_cyclic_sectors_scoping(resDef, stageNum):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_scoping_by_ids(resDef, location, ids, size):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_unit(resDef, unit):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_unit(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_result_file_path(resDef, name):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_result_file_path(resDef):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_index_param(resDef, sKeyParam, iParameter):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_index_param(resDef, sKeyParam, iParameter):
		raise NotImplementedError

	@staticmethod
	def result_definition_set_coef_param(resDef, sKeyParam, dParameter):
		raise NotImplementedError

	@staticmethod
	def result_definition_get_coef_param(resDef, sKeyParam, dParameter):
		raise NotImplementedError

