import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import remote_operator_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# RemoteOperator
#-------------------------------------------------------------------------------

class RemoteOperatorCAPI(remote_operator_abstract_api.RemoteOperatorAbstractAPI):

	@staticmethod
	def init_remote_operator_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def remote_operator_new(streams, remoteId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.RemoteOperator_new(streams._internal_obj if streams is not None else None, utils.to_int32(remoteId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def remote_operator_get_streams(remote_wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.RemoteOperator_get_streams(remote_wf._internal_obj if remote_wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def remote_operator_get_operator_id(remote_wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.RemoteOperator_get_operator_id(remote_wf._internal_obj if remote_wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def remote_operator_hold_streams(wf, streams):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.RemoteOperator_hold_streams(wf._internal_obj if wf is not None else None, utils.to_int32(streams), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

