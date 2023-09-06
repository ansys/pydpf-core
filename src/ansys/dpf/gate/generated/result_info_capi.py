import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import result_info_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# ResultInfo
#-------------------------------------------------------------------------------

class ResultInfoCAPI(result_info_abstract_api.ResultInfoAbstractAPI):

	@staticmethod
	def init_result_info_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def result_info_new(analysis_type, physics_type):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_new(utils.to_int32(analysis_type), utils.to_int32(physics_type), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_delete(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_delete(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_analysis_type(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetAnalysisType(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_physics_type(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetPhysicsType(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_analysis_type_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetAnalysisTypeName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_physics_type_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetPhysicsTypeName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_ansys_unit_system_enum(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetAnsysUnitSystemEnum(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_custom_unit_system_strings(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetCustomUnitSystemStrings(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_unit_system_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetUnitSystemName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_number_of_results(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetNumberOfResults(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_number_of_components(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultNumberOfComponents(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_dimensionality_nature(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultDimensionalityNature(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_homogeneity(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultHomogeneity(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_homogeneity_name(resultInfo, idx, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultHomogeneityName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_location(resultInfo, idx, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultLocation(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_result_description(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultDescription(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_result_name(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_result_physics_name(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultPhysicsName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_result_scripting_name(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultScriptingName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_result_unit_symbol(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetResultUnitSymbol(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_number_of_sub_results(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetNumberOfSubResults(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_sub_result_name(resultInfo, idx, idx_sub):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetSubResultName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_int32(idx_sub), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_sub_result_operator_name(resultInfo, idx, idx_sub, nqme):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetSubResultOperatorName(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_int32(idx_sub), utils.to_char_ptr(nqme), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_sub_result_description(resultInfo, idx, idx_sub):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetSubResultDescription(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_int32(idx_sub), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_cyclic_support(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetCyclicSupport(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_cyclic_symmetry_type(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetCyclicSymmetryType(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_has_cyclic_symmetry(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_HasCyclicSymmetry(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_fill_result_dimensionality(resultInfo, idx, dim, nature, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_FillResultDimensionality(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), utils.to_int32_ptr(dim), utils.to_int32_ptr(nature), utils.to_int32_ptr(size_vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_solver_version(resultInfo, majorVersion, minorVersion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetSolverVersion(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32_ptr(majorVersion), utils.to_int32_ptr(minorVersion), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_solve_date_and_time(resultInfo, date, time):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetSolveDateAndTime(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32_ptr(date), utils.to_int32_ptr(time), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_user_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetUserName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_job_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetJobName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_product_name(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetProductName(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_main_title(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetMainTitle(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_set_unit_system(resultInfo, unit_system):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_SetUnitSystem(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(unit_system), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_set_custom_unit_system(resultInfo, unit_strings):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_SetCustomUnitSystem(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(unit_strings), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_result(resultInfo, operator_name, scripting_name, dim, size_dim, dimnature, location, homogeneity, description):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddResult(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(operator_name), utils.to_char_ptr(scripting_name), utils.to_int32_ptr(dim), utils.to_int32(size_dim), utils.to_int32(dimnature), utils.to_char_ptr(location), utils.to_char_ptr(homogeneity), utils.to_char_ptr(description), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_qualifiers_for_result(resultInfo, operator_name, qualifiers):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddQualifiersForResult(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(operator_name), qualifiers._internal_obj if qualifiers is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_qualifiers_for_all_results(resultInfo, qualifiers):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddQualifiersForAllResults(resultInfo._internal_obj if resultInfo is not None else None, qualifiers._internal_obj if qualifiers is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_qualifiers_support(resultInfo, qualifier_name, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddQualifiersSupport(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(qualifier_name), support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_qualifiers_for_result(resultInfo, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetQualifiersForResult(resultInfo._internal_obj if resultInfo is not None else None, utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_qualifier_label_support(resultInfo, qualifier):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetQualifierLabelSupport(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(qualifier), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_available_qualifier_labels_as_string_coll(resultInfo):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetAvailableQualifierLabelsAsStringColl(resultInfo._internal_obj if resultInfo is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_string_property(resultInfo, property_name, property_value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddStringProperty(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(property_name), utils.to_char_ptr(property_value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_add_int_property(resultInfo, property_name, property_value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_AddIntProperty(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(property_name), utils.to_int32(property_value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def result_info_get_string_property(resultInfo, property_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetStringProperty(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(property_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def result_info_get_int_property(resultInfo, property_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ResultInfo_GetIntProperty(resultInfo._internal_obj if resultInfo is not None else None, utils.to_char_ptr(property_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

