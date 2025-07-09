import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import dpf_vector_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# DpfVector
#-------------------------------------------------------------------------------

class DpfVectorCAPI(dpf_vector_abstract_api.DpfVectorAbstractAPI):

	@staticmethod
	def init_dpf_vector_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def dpf_vector_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_double_free(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_double_free(dpf_vector._internal_obj, utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_free(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_free(dpf_vector._internal_obj, utils.to_char_ptr_ptr(data), utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_int_free(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_int_free(dpf_vector._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_free_with_size(dpf_vector, data, sizes, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_free_with_size(dpf_vector._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_free_for_next_usage_with_size(dpf_vector, data, sizes, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_free_for_next_usage_with_size(dpf_vector._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_free(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_free(dpf_vector._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_free_for_next_usage(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_free_for_next_usage(dpf_vector._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_double_commit(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_double_commit(dpf_vector._internal_obj, utils.to_double_ptr(data), utils.to_int32(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_int_commit(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_int_commit(dpf_vector._internal_obj, utils.to_int32_ptr(data), utils.to_int32(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_commit(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_commit(dpf_vector._internal_obj, utils.to_char_ptr(data), utils.to_int32(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_commit(dpf_vector, data, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_commit(dpf_vector._internal_obj, utils.to_char_ptr_ptr(data), utils.to_int32(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_ptr_commit_with_size(dpf_vector, data, sizes, size, modified):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_ptr_commit_with_size(dpf_vector._internal_obj, utils.to_char_ptr_ptr(data), utils.to_uint64_ptr(sizes), utils.to_int32(size), modified, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_delete(dpf_vector):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_delete(dpf_vector._internal_obj, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_string_free(dpf_vector, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfString_free(dpf_vector, utils.to_char_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_duplicate_dpf_vector(dpf_vector):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_duplicate_dpf_vector(dpf_vector._internal_obj, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_double_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_double_extract_sub(init_dpf_vector._internal_obj, utils.to_double_ptr(init_data), utils.to_int32(init_size), dpf_vector_to_update._internal_obj, utils.to_int32(first_index), utils.to_int32(size), utils.to_double_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_int_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_int_extract_sub(init_dpf_vector._internal_obj, utils.to_int32_ptr(init_data), utils.to_int32(init_size), dpf_vector_to_update._internal_obj, utils.to_int32(first_index), utils.to_int32(size), utils.to_int32_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_char_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_char_extract_sub(init_dpf_vector._internal_obj, utils.to_char_ptr(init_data), utils.to_int32(init_size), dpf_vector_to_update._internal_obj, utils.to_int32(first_index), utils.to_int32(size), utils.to_char_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_vector_new_for_object(api_to_use):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfVector_new_for_object(api_to_use._internal_obj if api_to_use is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_string_free_for_object(api_to_use, dpf_vector, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfString_free_for_object(api_to_use._internal_obj if api_to_use is not None else None, dpf_vector, utils.to_char_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

