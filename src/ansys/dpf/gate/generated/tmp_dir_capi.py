import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import tmp_dir_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# TmpDir
#-------------------------------------------------------------------------------

class TmpDirCAPI(tmp_dir_abstract_api.TmpDirAbstractAPI):

	@staticmethod
	def init_tmp_dir_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def tmp_dir_get_dir():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TmpDir_getDir(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def tmp_dir_erase():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TmpDir_erase(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def tmp_dir_get_dir_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TmpDir_getDir_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

