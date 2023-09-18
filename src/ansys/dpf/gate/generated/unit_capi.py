import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import unit_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# Unit
#-------------------------------------------------------------------------------

class UnitCAPI(unit_abstract_api.UnitAbstractAPI):

	@staticmethod
	def init_unit_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def unit_get_homogeneity(pre_allocated_char_64, symbol):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetHomogeneity(utils.to_char_ptr(pre_allocated_char_64), utils.to_char_ptr(symbol), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_conversion_factor(from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetConversionFactor(utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_conversion_shift(from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetConversionShift(utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_are_homogeneous(from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_AreHomogeneous(utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_symbol(pre_allocated_char_64, homogeneity, unit_system_id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_getSymbol(utils.to_char_ptr(pre_allocated_char_64), utils.to_char_ptr(homogeneity), utils.to_int32(unit_system_id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_homogeneity_for_object(api_to_use, pre_allocated_char_64, symbol):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetHomogeneity_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_char_ptr(pre_allocated_char_64), utils.to_char_ptr(symbol), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_conversion_factor_for_object(api_to_use, from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetConversionFactor_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_conversion_shift_for_object(api_to_use, from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_GetConversionShift_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_are_homogeneous_for_object(api_to_use, from_, to):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_AreHomogeneous_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_char_ptr(from_), utils.to_char_ptr(to), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def unit_get_symbol_for_object(api_to_use, pre_allocated_char_64, homogeneity, unit_system_id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Unit_getSymbol_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_char_ptr(pre_allocated_char_64), utils.to_char_ptr(homogeneity), utils.to_int32(unit_system_id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

