import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import field_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# Field
#-------------------------------------------------------------------------------

class FieldCAPI(field_abstract_api.FieldAbstractAPI):

	@staticmethod
	def init_field_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def field_delete(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_Delete(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_data(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetData(field, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_data_pointer(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetDataPointer(field, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_scoping(constfield, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetScoping(constfield, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_scoping_to_data_pointer_copy(field, scopingToDataPointer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetScopingToDataPointerCopy(field, utils.to_int32_ptr(scopingToDataPointer), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_entity_data(field, EntityIndex, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetEntityData(field, utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_entity_data_by_id(field, EntityId, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetEntityDataById(field, utils.to_int32(EntityId), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_unit(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetUnit(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def field_get_location(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetLocation(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def field_get_number_elementary_data(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetNumberElementaryData(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_number_elementary_data_by_index(field, entityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetNumberElementaryDataByIndex(field, utils.to_int32(entityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_number_elementary_data_by_id(field, entityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetNumberElementaryDataById(field, utils.to_int32(entityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_number_of_components(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetNumberOfComponents(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_number_of_entities(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetNumberOfEntities(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_elementary_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_ElementaryDataSize(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetDataSize(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_eshell_layers(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_GetEShellLayers(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_PushBack(field, utils.to_int32(EntityId), utils.to_int32(size), utils.to_double_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_delete(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_Delete(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetData(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_data(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetData(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_double_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_data_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetDataWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_data_pointer(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetDataPointer(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_data_pointer_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetDataPointerWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_entity_data(field, index, id, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetEntityData(field._internal_obj if field is not None else None, utils.to_int32(index), utils.to_int32(id), utils.to_int32(size), utils.to_double_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_support(field, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetSupport(field._internal_obj if field is not None else None, support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_unit(field, symbol):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetUnit(field._internal_obj if field is not None else None, utils.to_char_ptr(symbol), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_location(field, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetLocation(field._internal_obj if field is not None else None, utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_meshed_region_as_support(field, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetMeshedRegionAsSupport(field._internal_obj if field is not None else None, support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_update_entity_data_by_entity_index(field, EntityIndex, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_UpdateEntityDataByEntityIndex(field._internal_obj if field is not None else None, utils.to_int32(EntityIndex), utils.to_int32(size), utils.to_double_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_PushBack(field._internal_obj if field is not None else None, utils.to_int32(EntityId), utils.to_int32(size), utils.to_double_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_scoping(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetScoping(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data_ptr(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetDataPtr(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_cscoping(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetCScoping(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_shared_field_definition(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetSharedFieldDefinition(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_field_definition(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetFieldDefinition(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_support(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetSupport(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data_pointer(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetDataPointer(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_field_definition(field, field_definition):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetFieldDefinition(field._internal_obj if field is not None else None, field_definition._internal_obj if field_definition is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_fast_access_field_definition(field, field_definition):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetFastAccessFieldDefinition(field._internal_obj if field is not None else None, field_definition, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_scoping(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetScoping(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_cscoping(field, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetCScoping(field._internal_obj if field is not None else None, scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_data(field, EntityIndex, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityData(field._internal_obj if field is not None else None, utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_data_by_id(field, EntityId, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityDataById(field._internal_obj if field is not None else None, utils.to_int32(EntityId), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_unit(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetUnit(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_get_location(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetLocation(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_get_number_elementary_data(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetNumberElementaryData(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_number_elementary_data_by_index(field, entityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetNumberElementaryDataByIndex(field._internal_obj if field is not None else None, utils.to_int32(entityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_number_elementary_data_by_id(field, entityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetNumberElementaryDataById(field._internal_obj if field is not None else None, utils.to_int32(entityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_number_entities(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetNumberEntities(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_elementary_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_ElementaryDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_eshell_layers(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEShellLayers(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_set_eshell_layers(field, eshell_layer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetEShellLayers(field._internal_obj if field is not None else None, utils.to_int32(eshell_layer), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_resize_data(field, dataSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_ResizeData(field._internal_obj if field is not None else None, utils.to_int32(dataSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_resize_data_pointer(field, dataSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_ResizeDataPointer(field._internal_obj if field is not None else None, utils.to_int32(dataSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_number_of_components(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetNumberOfComponents(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_resize(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_Resize(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_reserve(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_Reserve(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_name(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetName(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csfield_set_name(field, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_SetName(field._internal_obj if field is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_string_property(field, key, sProp_ptr):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetStringProperty(field._internal_obj if field is not None else None, utils.to_char_ptr(key), utils.to_char_ptr_ptr(sProp_ptr), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_add_string_property(field, key, sProp):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_AddStringProperty(field._internal_obj if field is not None else None, utils.to_char_ptr(key), utils.to_char_ptr(sProp), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_del_string_property(field, key):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_DelStringProperty(field._internal_obj if field is not None else None, utils.to_char_ptr(key), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_support_as_meshed_region(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetSupportAsMeshedRegion(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_support_as_time_freq_support(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetSupportAsTimeFreqSupport(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_id(field, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityId(field._internal_obj if field is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_index(field, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityIndex(field._internal_obj if field is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data_for_dpf_vector(field, var1, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetData_For_DpfVector(field._internal_obj if field is not None else None, var1._internal_obj, utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_data_pointer_for_dpf_vector(field, var1, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetDataPointer_For_DpfVector(field._internal_obj if field is not None else None, var1._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityData_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, out._internal_obj, utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_GetEntityDataById_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, vec._internal_obj, utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new(fieldDimensionnality, numEntities, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_new(utils.to_int32(fieldDimensionnality), utils.to_int32(numEntities), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new_with_transformation(fieldDimensionnality, numEntities, location, wf, input_name, output_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_newWithTransformation(utils.to_int32(fieldDimensionnality), utils.to_int32(numEntities), utils.to_char_ptr(location), wf._internal_obj if wf is not None else None, utils.to_char_ptr(input_name), utils.to_char_ptr(output_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new_with1_ddimensionnality(fieldDimensionnality, numComp, numEntitiesToReserve, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_newWith1DDimensionnality(utils.to_int32(fieldDimensionnality), utils.to_int32(numComp), utils.to_int32(numEntitiesToReserve), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new_with2_ddimensionnality(fieldDimensionnality, numCompN, numCompM, numEntitiesToReserve, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_newWith2DDimensionnality(utils.to_int32(fieldDimensionnality), utils.to_int32(numCompN), utils.to_int32(numCompM), utils.to_int32(numEntitiesToReserve), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_copy(field, bAllocateData, bCopyData, bscopingHardCopy):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_getCopy(field._internal_obj if field is not None else None, bAllocateData, bCopyData, bscopingHardCopy, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_clone_to_different_dimension(field, fieldDimensionnality, numCompN, numCompM, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_CloneToDifferentDimension(field._internal_obj if field is not None else None, utils.to_int32(fieldDimensionnality), utils.to_int32(numCompN), utils.to_int32(numCompM), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csfield_cursor(f, index, data, id, size, n_comp, data_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSField_cursor(f._internal_obj if f is not None else None, utils.to_int32(index), utils.to_double_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(size), utils.to_int32_ptr(n_comp), utils.to_int32_ptr(data_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_fast_access_ptr(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_fast_access_ptr(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_fast_cursor(f, index, data, id, size, n_comp, data_index):
		res = capi.dll.Field_fast_cursor(f, utils.to_int32(index), utils.to_double_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(size), utils.to_int32_ptr(n_comp), utils.to_int32_ptr(data_index))
		return res

	@staticmethod
	def field_new_on_client(client, dimensions, reserved_number_of_entity, loc):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_new_on_client(client._internal_obj if client is not None else None, utils.to_int32(dimensions), utils.to_int32(reserved_number_of_entity), utils.to_char_ptr(loc), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new_with1_ddimensionnality_on_client(client, fieldDimensionnality, numComp, numEntitiesToReserve, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_newWith1DDimensionnality_on_client(client._internal_obj if client is not None else None, utils.to_int32(fieldDimensionnality), utils.to_int32(numComp), utils.to_int32(numEntitiesToReserve), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_new_with2_ddimensionnality_on_client(client, fieldDimensionnality, numCompN, numCompM, numEntitiesToReserve, location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_newWith2DDimensionnality_on_client(client._internal_obj if client is not None else None, utils.to_int32(fieldDimensionnality), utils.to_int32(numCompN), utils.to_int32(numCompM), utils.to_int32(numEntitiesToReserve), utils.to_char_ptr(location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def field_get_copy_on_client(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Field_getCopy_on_client(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

