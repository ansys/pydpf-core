import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import custom_type_field_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# CustomTypeField
#-------------------------------------------------------------------------------

class CustomTypeFieldCAPI(custom_type_field_abstract_api.CustomTypeFieldAbstractAPI):

	@staticmethod
	def init_custom_type_field_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def cscustom_type_field_new(type, unitarySize, numEntities, numUnitaryData):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_new(utils.to_char_ptr(type), utils.to_int32(unitarySize), utils.to_int32(numEntities), utils.to_int32(numUnitaryData), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_data_for_dpf_vector(field, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetData_For_DpfVector(field._internal_obj if field is not None else None, out._internal_obj, utils.to_void_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_data_pointer_for_dpf_vector(field, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetDataPointer_For_DpfVector(field._internal_obj if field is not None else None, out._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetEntityData_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, out._internal_obj, utils.to_void_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetEntityDataById_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, vec._internal_obj, utils.to_void_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_cscoping(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetCScoping(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_number_elementary_data(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetNumberElementaryData(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_number_of_components(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetNumberOfComponents(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_number_entities(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetNumberEntities(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_property_data_tree(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetPropertyDataTree(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_data(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetData(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_void_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_data_pointer(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetDataPointer(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_cscoping(field, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetCScoping(field._internal_obj if field is not None else None, scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_PushBack(field._internal_obj if field is not None else None, utils.to_int32(EntityId), utils.to_int32(size), utils.to_void_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_data_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetDataWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_data_pointer_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetDataPointerWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_resize(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_Resize(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_resize_data_pointer(field, dataSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_ResizeDataPointer(field._internal_obj if field is not None else None, utils.to_int32(dataSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_reserve(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_Reserve(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_type(field, type, unitarySize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetType(field._internal_obj if field is not None else None, utils.to_char_ptr(type), utils.to_int32_ptr(unitarySize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_shared_field_definition(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetSharedFieldDefinition(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_support(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetSupport(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_field_definition(field, field_definition):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetFieldDefinition(field._internal_obj if field is not None else None, field_definition._internal_obj if field_definition is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_support(field, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetSupport(field._internal_obj if field is not None else None, support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_set_entity_data(field, index, id, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetEntityData(field._internal_obj if field is not None else None, utils.to_int32(index), utils.to_int32(id), utils.to_int32(size), utils.to_void_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_name(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetName(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def cscustom_type_field_set_name(field, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_SetName(field._internal_obj if field is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_entity_id(field, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetEntityId(field._internal_obj if field is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_entity_index(field, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_GetEntityIndex(field._internal_obj if field is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_new_on_client(client, type, unitarySize, numEntities, numUnitaryData):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_new_on_client(client._internal_obj if client is not None else None, utils.to_char_ptr(type), utils.to_int32(unitarySize), utils.to_int32(numEntities), utils.to_int32(numUnitaryData), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def cscustom_type_field_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSCustomTypeField_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

