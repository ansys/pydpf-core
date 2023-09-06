import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import field_definition_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# FieldDefinition
#-------------------------------------------------------------------------------

class FieldDefinitionCAPI(field_definition_abstract_api.FieldDefinitionAbstractAPI):

	@staticmethod
	def init_field_definition_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def field_definition_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_wrap(var1):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_wrap(var1, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_delete(fielddef):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_Delete(fielddef._internal_obj if fielddef is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_get_fast_access_ptr(fielddef):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_GetFastAccessPtr(fielddef._internal_obj if fielddef is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_get_unit(res, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_GetUnit(res, ctypes.byref(utils.to_int32(homogeneity)), ctypes.byref(ctypes.c_double(factor) if isinstance(factor, float) else factor), ctypes.byref(ctypes.c_double(shift) if isinstance(shift, float) else shift), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def field_definition_fill_unit(fieldDef, symbol, size, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_FillUnit(fieldDef, utils.to_char_ptr(symbol), utils.to_int32_ptr(size), utils.to_int32_ptr(homogeneity), utils.to_double_ptr(factor), utils.to_double_ptr(shift), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_get_shell_layers(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_GetShellLayers(res, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_get_location(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_GetLocation(res, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def field_definition_fill_location(fieldDef, location, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_FillLocation(fieldDef, utils.to_char_ptr(location), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_get_dimensionality(res, nature, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_GetDimensionality(res, ctypes.byref(utils.to_int32(nature)), ctypes.byref(utils.to_int32(size_vsize)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_fill_dimensionality(res, dim, nature, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_FillDimensionality(res, utils.to_int32_ptr(dim), utils.to_int32_ptr(nature), utils.to_int32_ptr(size_vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_set_unit(fieldDef, symbol, ptrObject, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_SetUnit(fieldDef, utils.to_char_ptr(symbol), utils.to_double_ptr(ptrObject), utils.to_int32(homogeneity), ctypes.c_double(factor) if isinstance(factor, float) else factor, ctypes.c_double(shift) if isinstance(shift, float) else shift, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_set_shell_layers(fieldDef, shellLayers):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_SetShellLayers(fieldDef, utils.to_int32(shellLayers), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_set_location(fieldDef, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_SetLocation(fieldDef, utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_set_dimensionality(fieldDef, dim, ptrSize, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_SetDimensionality(fieldDef, utils.to_int32(dim), utils.to_int32_ptr(ptrSize), utils.to_int32(size_vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_unit(res, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetUnit(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(homogeneity)), ctypes.byref(ctypes.c_double(factor) if isinstance(factor, float) else factor), ctypes.byref(ctypes.c_double(shift) if isinstance(shift, float) else shift), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_definition_fill_unit(fieldDef, symbol, size, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_FillUnit(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(symbol), utils.to_int32_ptr(size), utils.to_int32_ptr(homogeneity), utils.to_double_ptr(factor), utils.to_double_ptr(shift), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_shell_layers(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetShellLayers(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_location(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetLocation(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_definition_fill_location(fieldDef, location, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_FillLocation(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(location), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_dimensionality(res, nature, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetDimensionality(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(nature)), ctypes.byref(utils.to_int32(size_vsize)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_fill_dimensionality(res, dim, nature, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_FillDimensionality(res._internal_obj if res is not None else None, utils.to_int32_ptr(dim), utils.to_int32_ptr(nature), utils.to_int32_ptr(size_vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_set_unit(fieldDef, symbol, ptrObject, homogeneity, factor, shift):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetUnit(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(symbol), utils.to_double_ptr(ptrObject), utils.to_int32(homogeneity), ctypes.c_double(factor) if isinstance(factor, float) else factor, ctypes.c_double(shift) if isinstance(shift, float) else shift, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_set_shell_layers(fieldDef, shellLayers):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetShellLayers(fieldDef._internal_obj if fieldDef is not None else None, utils.to_int32(shellLayers), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_set_location(fieldDef, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetLocation(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_set_dimensionality(fieldDef, dim, ptrSize, size_vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetDimensionality(fieldDef._internal_obj if fieldDef is not None else None, utils.to_int32(dim), utils.to_int32_ptr(ptrSize), utils.to_int32(size_vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_set_quantity_type(fieldDef, quantityType):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetQuantityType(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(quantityType), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_num_available_quantity_types(fieldDef):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetNumAvailableQuantityTypes(fieldDef._internal_obj if fieldDef is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_quantity_type(fieldDef, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetQuantityType(fieldDef._internal_obj if fieldDef is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_definition_is_of_quantity_type(fieldDef, quantityType):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_IsOfQuantityType(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(quantityType), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_get_name(res):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_GetName(res._internal_obj if res is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_definition_set_name(fieldDef, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_SetName(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_definition_fill_name(fieldDef, name, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSFieldDefinition_FillName(fieldDef._internal_obj if fieldDef is not None else None, utils.to_char_ptr(name), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dimensionality_get_num_comp(nature, size, vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Dimensionality_GetNumComp(utils.to_int32(nature), utils.to_int32_ptr(size), utils.to_int32(vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_definition_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldDefinition_new_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dimensionality_get_num_comp_for_object(api_to_use, nature, size, vsize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Dimensionality_GetNumComp_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_int32(nature), utils.to_int32_ptr(size), utils.to_int32(vsize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

