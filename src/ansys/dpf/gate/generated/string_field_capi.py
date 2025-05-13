import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import string_field_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# StringField
#-------------------------------------------------------------------------------

class StringFieldCAPI(string_field_abstract_api.StringFieldAbstractAPI):

	@staticmethod
	def init_string_field_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def string_field_delete(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_Delete(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_get_entity_data(field, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetEntityData(field, utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def string_field_get_number_entities(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetNumberEntities(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_new(numEntities, data_size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_new(utils.to_int32(numEntities), utils.to_int32(data_size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_data_for_dpf_vector(field, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetData_For_DpfVector(field._internal_obj if field is not None else None, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetEntityData_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetEntityDataById_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, vec._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetEntityData_For_DpfVector(dpf_object, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetEntityDataById_For_DpfVector(dpf_object, vec._internal_obj, utils.to_char_ptr_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_data_for_dpf_vector_with_size(field, out, data, sizes, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetData_For_DpfVector_with_size(field._internal_obj if field is not None else None, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_entity_data_for_dpf_vector_with_size(dpf_object, out, data, sizes, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetEntityData_For_DpfVector_with_size(dpf_object._internal_obj if dpf_object is not None else None, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_entity_data_by_id_for_dpf_vector_with_size(dpf_object, vec, data, sizes, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetEntityDataById_For_DpfVector_with_size(dpf_object._internal_obj if dpf_object is not None else None, vec._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_get_entity_data_for_dpf_vector_with_size(dpf_object, out, data, sizes, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetEntityData_For_DpfVector_with_size(dpf_object, out._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_get_entity_data_by_id_for_dpf_vector_with_size(dpf_object, vec, data, sizes, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_GetEntityDataById_For_DpfVector_with_size(dpf_object, vec._internal_obj, utils.to_char_ptr_ptr_ptr(data), sizes, utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_cscoping(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetCScoping(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_GetDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_set_data(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_SetData(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_char_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_set_data_with_size(field, size, data, sizes):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_SetData_with_size(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_char_ptr_ptr(data), utils.to_uint64_ptr(sizes), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_set_cscoping(field, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_SetCScoping(field._internal_obj if field is not None else None, scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_set_data_pointer(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_SetDataPointer(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_PushBack(field._internal_obj if field is not None else None, utils.to_int32(EntityId), utils.to_int32(size), utils.to_char_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_PushBack(field, utils.to_int32(EntityId), utils.to_int32(size), utils.to_char_ptr_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_push_back_with_size(field, EntityId, size, data, sizes):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_PushBack_with_size(field._internal_obj if field is not None else None, utils.to_int32(EntityId), utils.to_int32(size), utils.to_char_ptr_ptr(data), utils.to_uint64_ptr(sizes), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_push_back_with_size(field, EntityId, size, data, sizes):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_PushBack_with_size(field, utils.to_int32(EntityId), utils.to_int32(size), utils.to_char_ptr_ptr(data), utils.to_uint64_ptr(sizes), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_resize(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_Resize(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_reserve(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_Reserve(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def string_field_fast_access_ptr(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.StringField_fast_access_ptr(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_new_on_client(client, numEntities, data_size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_new_on_client(client._internal_obj if client is not None else None, utils.to_int32(numEntities), utils.to_int32(data_size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csstring_field_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSStringField_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

