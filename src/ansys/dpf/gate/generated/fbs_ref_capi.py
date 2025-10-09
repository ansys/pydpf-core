import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import fbs_ref_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# FbsRef
#-------------------------------------------------------------------------------

class FbsRefCAPI(fbs_ref_abstract_api.FbsRefAbstractAPI):

	@staticmethod
	def init_fbs_ref_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def fbs_ref_new(client, channel_address, req_slice, req_offset):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FbsRef_new(client, utils.to_char_ptr(channel_address), req_slice, req_offset, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_ref_get_from_db(ptr, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FbsRef_getFromDB(ptr, size, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def any_get_as_fbs_ref(obj, client, channel_address, req_slice, req_offset):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Any_getAs_FbsRef(obj._internal_obj if obj is not None else None, client, utils.to_char_ptr(channel_address), req_slice, req_offset, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_ref_start_or_get_thread_server(get_existing, ip, port, address):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FbsRef_StartOrGetThreadServer(get_existing, utils.to_char_ptr(ip), utils.to_int32(port), utils.to_char_ptr(address), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_get_bytes_buffer_from_slice(req_slice, req_offset, size_out):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Fbs_GetBytesBufferFromSlice(req_slice, req_offset, size_out, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_delete_channel(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Fbs_DeleteChannel(client, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_delete_slice(req_slice):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Fbs_DeleteSlice(req_slice, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_ref_new_on_client(client, channel, channel_address, req_slice, req_offset):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FbsRef_new_on_client(client._internal_obj if client is not None else None, channel, utils.to_char_ptr(channel_address), req_slice, req_offset, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fbs_ref_start_or_get_thread_server_on_client(client, get_existing, ip, port, address):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FbsRef_StartOrGetThreadServer_on_client(client._internal_obj if client is not None else None, get_existing, utils.to_char_ptr(ip), utils.to_int32(port), utils.to_char_ptr(address), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

