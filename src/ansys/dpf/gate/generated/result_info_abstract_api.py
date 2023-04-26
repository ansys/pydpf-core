#-------------------------------------------------------------------------------
# ResultInfo
#-------------------------------------------------------------------------------

class ResultInfoAbstractAPI:
	@staticmethod
	def init_result_info_environment(object):
		pass

	@staticmethod
	def finish_result_info_environment(object):
		pass

	@staticmethod
	def result_info_new(analysis_type, physics_type):
		raise NotImplementedError

	@staticmethod
	def result_info_delete(res):
		raise NotImplementedError

	@staticmethod
	def result_info_get_analysis_type(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_physics_type(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_analysis_type_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_physics_type_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_ansys_unit_system_enum(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_custom_unit_system_strings(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_unit_system_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_number_of_results(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_number_of_components(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_dimensionality_nature(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_homogeneity(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_homogeneity_name(resultInfo, idx, name):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_location(resultInfo, idx, name):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_description(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_name(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_physics_name(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_scripting_name(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_result_unit_symbol(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_number_of_sub_results(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_sub_result_name(resultInfo, idx, idx_sub):
		raise NotImplementedError

	@staticmethod
	def result_info_get_sub_result_operator_name(resultInfo, idx, idx_sub, nqme):
		raise NotImplementedError

	@staticmethod
	def result_info_get_sub_result_description(resultInfo, idx, idx_sub):
		raise NotImplementedError

	@staticmethod
	def result_info_get_cyclic_support(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_cyclic_symmetry_type(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_has_cyclic_symmetry(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_fill_result_dimensionality(resultInfo, idx, dim, nature, size_vsize):
		raise NotImplementedError

	@staticmethod
	def result_info_get_solver_version(resultInfo, majorVersion, minorVersion):
		raise NotImplementedError

	@staticmethod
	def result_info_get_solve_date_and_time(resultInfo, date, time):
		raise NotImplementedError

	@staticmethod
	def result_info_get_user_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_job_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_product_name(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_get_main_title(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_set_unit_system(resultInfo, unit_system):
		raise NotImplementedError

	@staticmethod
	def result_info_set_custom_unit_system(resultInfo, unit_strings):
		raise NotImplementedError

	@staticmethod
	def result_info_add_result(resultInfo, operator_name, scripting_name, dim, size_dim, dimnature, location, homogeneity, description):
		raise NotImplementedError

	@staticmethod
	def result_info_add_qualifiers_for_result(resultInfo, operator_name, qualifiers):
		raise NotImplementedError

	@staticmethod
	def result_info_add_qualifiers_for_all_results(resultInfo, qualifiers):
		raise NotImplementedError

	@staticmethod
	def result_info_add_qualifiers_support(resultInfo, qualifier_name, support):
		raise NotImplementedError

	@staticmethod
	def result_info_get_qualifiers_for_result(resultInfo, idx):
		raise NotImplementedError

	@staticmethod
	def result_info_get_qualifier_label_support(resultInfo, qualifier):
		raise NotImplementedError

	@staticmethod
	def result_info_get_available_qualifier_labels_as_string_coll(resultInfo):
		raise NotImplementedError

	@staticmethod
	def result_info_add_string_property(resultInfo, property_name, property_value):
		raise NotImplementedError

	@staticmethod
	def result_info_add_int_property(resultInfo, property_name, property_value):
		raise NotImplementedError

	@staticmethod
	def result_info_get_string_property(resultInfo, property_name):
		raise NotImplementedError

	@staticmethod
	def result_info_get_int_property(resultInfo, property_name):
		raise NotImplementedError

