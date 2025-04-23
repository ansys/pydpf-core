import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import operator_specification_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# OperatorSpecification
#-------------------------------------------------------------------------------

class OperatorSpecificationCAPI(operator_specification_abstract_api.OperatorSpecificationAbstractAPI):

	@staticmethod
	def init_operator_specification_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def operator_specification_new(op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_new(utils.to_char_ptr(op), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_empty_specification_new():
		res = capi.dll.Operator_empty_specification_new()
		return res

	@staticmethod
	def operator_specification_delete(var1):
		res = capi.dll.Operator_specification_delete(var1._internal_obj if var1 is not None else None)
		return res

	@staticmethod
	def operator_specification_get_description(specification):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetDescription(specification._internal_obj if specification is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_set_description(specification, text):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetDescription(specification._internal_obj if specification is not None else None, utils.to_char_ptr(text), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_set_property(specification, key, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetProperty(specification._internal_obj if specification is not None else None, utils.to_char_ptr(key), utils.to_char_ptr(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_num_pins(specification, binput):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetNumPins(specification._internal_obj if specification is not None else None, binput, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_pin_name(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinName(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_pin_num_type_names(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinNumTypeNames(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_fill_pin_numbers(specification, binput, pins):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_FillPinNumbers(specification._internal_obj if specification is not None else None, binput, utils.to_int32_ptr(pins), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_pin_type_name(specification, binput, numPin, numType):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinTypeName(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), utils.to_int32(numType), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_is_pin_optional(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_IsPinOptional(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_pin_document(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinDocument(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_is_pin_ellipsis(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_IsPinEllipsis(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_is_pin_in_place(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_IsPinInPlace(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_properties(specification, prop):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetProperties(specification._internal_obj if specification is not None else None, utils.to_char_ptr(prop), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_num_properties(specification):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetNumProperties(specification._internal_obj if specification is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_property_key(specification, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPropertyKey(specification._internal_obj if specification is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_set_pin(specification, var1, position, name, description, n_types, types, is_optional, is_ellipsis):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetPin(specification._internal_obj if specification is not None else None, var1, utils.to_int32(position), utils.to_char_ptr(name), utils.to_char_ptr(description), utils.to_int32(n_types), utils.to_char_ptr_ptr(types), is_optional, is_ellipsis, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_set_pin_derived_class(specification, var1, position, name, description, n_types, types, is_optional, is_ellipsis, derived_type_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetPinDerivedClass(specification._internal_obj if specification is not None else None, var1, utils.to_int32(position), utils.to_char_ptr(name), utils.to_char_ptr(description), utils.to_int32(n_types), utils.to_char_ptr_ptr(types), is_optional, is_ellipsis, utils.to_char_ptr(derived_type_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_set_pin_aliases(specification, var1, position, n_aliases, aliases):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetPinAliases(specification._internal_obj if specification is not None else None, var1, utils.to_int32(position), utils.to_int32(n_aliases), utils.to_char_ptr_ptr(aliases), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_add_pin_alias(specification, var1, position, alias):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_AddPinAlias(specification._internal_obj if specification is not None else None, var1, utils.to_int32(position), utils.to_char_ptr(alias), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_add_bool_config_option(specification, option_name, default_value, description):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_AddBoolConfigOption(specification._internal_obj if specification is not None else None, utils.to_char_ptr(option_name), default_value, utils.to_char_ptr(description), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_add_int_config_option(specification, option_name, default_value, description):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_AddIntConfigOption(specification._internal_obj if specification is not None else None, utils.to_char_ptr(option_name), utils.to_int32(default_value), utils.to_char_ptr(description), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_add_double_config_option(specification, option_name, default_value, description):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_AddDoubleConfigOption(specification._internal_obj if specification is not None else None, utils.to_char_ptr(option_name), ctypes.c_double(default_value) if isinstance(default_value, float) else default_value, utils.to_char_ptr(description), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_num_config_options(specification):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetNumConfigOptions(specification._internal_obj if specification is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_config_name(specification, numOption):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetConfigName(specification._internal_obj if specification is not None else None, utils.to_int32(numOption), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_config_num_type_names(specification, numOption):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetConfigNumTypeNames(specification._internal_obj if specification is not None else None, utils.to_int32(numOption), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_config_type_name(specification, numOption, numType):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetConfigTypeName(specification._internal_obj if specification is not None else None, utils.to_int32(numOption), utils.to_int32(numType), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_config_printable_default_value(specification, numOption):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetConfigPrintableDefaultValue(specification._internal_obj if specification is not None else None, utils.to_int32(numOption), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_config_description(specification, numOption):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetConfigDescription(specification._internal_obj if specification is not None else None, utils.to_int32(numOption), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_get_pin_derived_class_type_name(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinDerivedClassTypeName(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_set_version(specification, semver):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_SetVersion(specification._internal_obj if specification is not None else None, semver._internal_obj if semver is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_version(specification):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetVersion(specification._internal_obj if specification is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_pin_num_aliases(specification, binput, numPin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinNumAliases(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def operator_specification_get_pin_alias(specification, binput, numPin, numAlias):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_GetPinAlias(specification._internal_obj if specification is not None else None, binput, utils.to_int32(numPin), utils.to_int32(numAlias), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def operator_specification_new_on_client(client, op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Operator_specification_new_on_client(client._internal_obj if client is not None else None, utils.to_char_ptr(op), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

