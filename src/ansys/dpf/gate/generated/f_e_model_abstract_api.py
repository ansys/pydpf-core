#-------------------------------------------------------------------------------
# FEModel
#-------------------------------------------------------------------------------

class FEModelAbstractAPI:
	@staticmethod
	def init_f_e_model_environment(object):
		pass

	@staticmethod
	def finish_f_e_model_environment(object):
		pass

	@staticmethod
	def femodel_new():
		raise NotImplementedError

	@staticmethod
	def femodel_new_with_result_file(file_name):
		raise NotImplementedError

	@staticmethod
	def femodel_new_empty():
		raise NotImplementedError

	@staticmethod
	def femodel_delete(feModel):
		raise NotImplementedError

	@staticmethod
	def femodel_set_result_file_path(feModel, name):
		raise NotImplementedError

	@staticmethod
	def femodel_add_result(feModel, resDef):
		raise NotImplementedError

	@staticmethod
	def femodel_add_primary_result(feModel, res):
		raise NotImplementedError

	@staticmethod
	def femodel_add_result_with_scoping(feModel, res, scoping):
		raise NotImplementedError

	@staticmethod
	def femodel_delete_result(feModel, result):
		raise NotImplementedError

	@staticmethod
	def femodel_get_mesh_region(feModel):
		raise NotImplementedError

	@staticmethod
	def femodel_get_time_freq_support(feModel):
		raise NotImplementedError

	@staticmethod
	def femodel_get_support_query(feModel):
		raise NotImplementedError

