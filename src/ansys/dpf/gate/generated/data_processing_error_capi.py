import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import data_processing_error_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# DataProcessingError
#-------------------------------------------------------------------------------

class DataProcessingErrorCAPI(data_processing_error_abstract_api.DataProcessingErrorAbstractAPI):

	@staticmethod
	def init_data_processing_error_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def data_processing_parse_error(size, error_message):
		res = capi.dll.DataProcessing_parse_error(utils.to_int32(size), error_message)
		return res

	@staticmethod
	def data_processing_parse_error_to_str(size, error_message):
		res = capi.dll.DataProcessing_parse_error_to_str(utils.to_int32(size), error_message)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def dpf_error_new():
		res = capi.dll.DpfError_new()
		return res

	@staticmethod
	def dpf_error_set_throw(error, must_throw):
		res = capi.dll.DpfError_set_throw(error, must_throw)
		return res

	@staticmethod
	def dpf_error_set_code(error, code_value):
		res = capi.dll.DpfError_set_code(error, utils.to_int32(code_value))
		return res

	@staticmethod
	def dpf_error_set_message_text(error, code_value):
		res = capi.dll.DpfError_set_message_text(error, utils.to_char_ptr(code_value))
		return res

	@staticmethod
	def dpf_error_set_message_template(error, code_value):
		res = capi.dll.DpfError_set_message_template(error, utils.to_char_ptr(code_value))
		return res

	@staticmethod
	def dpf_error_set_message_id(error, code_value):
		res = capi.dll.DpfError_set_message_id(error, utils.to_char_ptr(code_value))
		return res

	@staticmethod
	def dpf_error_delete(error):
		res = capi.dll.DpfError_delete(error)
		return res

	@staticmethod
	def dpf_error_duplicate(error):
		res = capi.dll.DpfError_duplicate(error)
		return res

	@staticmethod
	def dpf_error_code(error):
		res = capi.dll.DpfError_code(error)
		return res

	@staticmethod
	def dpf_error_to_throw(error):
		res = capi.dll.DpfError_to_throw(error)
		return res

	@staticmethod
	def dpf_error_message_text(error):
		res = capi.dll.DpfError_message_text(error)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def dpf_error_message_template(error):
		res = capi.dll.DpfError_message_template(error)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def dpf_error_message_id(error):
		res = capi.dll.DpfError_message_id(error)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_processing_parse_error_to_str_for_object(api_to_use, size, error_message):
		res = capi.dll.DataProcessing_parse_error_to_str_for_object(api_to_use._internal_obj if api_to_use is not None else None, utils.to_int32(size), error_message)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

