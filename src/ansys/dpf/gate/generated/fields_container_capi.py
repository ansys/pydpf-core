import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import fields_container_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# FieldsContainer
#-------------------------------------------------------------------------------

class FieldsContainerCAPI(fields_container_abstract_api.FieldsContainerAbstractAPI):

	@staticmethod
	def init_fields_container_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def fields_container_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fields_container_delete(fieldContainer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_Delete(fieldContainer._internal_obj if fieldContainer is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fields_container_at(fieldContainer, i, ic):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_at(fieldContainer._internal_obj if fieldContainer is not None else None, utils.to_int32(i), utils.to_int32(ic), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fields_container_set_field(fieldContainer, field, fieldId, ic):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_setField(fieldContainer._internal_obj if fieldContainer is not None else None, field._internal_obj if field is not None else None, utils.to_int32(fieldId), utils.to_int32(ic), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fields_container_get_scoping(fieldContainer, ic, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_GetScoping(fieldContainer._internal_obj if fieldContainer is not None else None, utils.to_int32(ic), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def fields_container_num_fields(fieldContainer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.FieldsContainer_numFields(fieldContainer._internal_obj if fieldContainer is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

