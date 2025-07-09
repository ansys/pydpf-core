import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import property_field_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# PropertyField
#-------------------------------------------------------------------------------

class PropertyFieldCAPI(property_field_abstract_api.PropertyFieldAbstractAPI):

	@staticmethod
	def init_property_field_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def property_field_delete(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_Delete(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_data(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetData(field, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_data_pointer(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetDataPointer(field, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_scoping(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetScoping(field, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_entity_data(field, EntityIndex, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetEntityData(field, utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_entity_data_by_id(field, EntityId, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetEntityDataById(field, utils.to_int32(EntityId), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_field_get_location(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.PropertyField_GetLocation(field, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csproperty_field_new(numEntities, data_size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_new(utils.to_int32(numEntities), utils.to_int32(data_size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_new_with_transformation(numEntities, data_size, wf, input_name, output_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_newWithTransformation(utils.to_int32(numEntities), utils.to_int32(data_size), wf._internal_obj if wf is not None else None, utils.to_char_ptr(input_name), utils.to_char_ptr(output_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_delete(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_Delete(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_data(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetData(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_data_for_dpf_vector(field, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetData_For_DpfVector(field._internal_obj if field is not None else None, out._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_data_pointer(field, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetDataPointer(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_data_pointer_for_dpf_vector(field, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetDataPointer_For_DpfVector(field._internal_obj if field is not None else None, out._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_cscoping(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetCScoping(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_data(field, EntityIndex, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityData(field._internal_obj if field is not None else None, utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_data_by_id(field, EntityId, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityDataById(field._internal_obj if field is not None else None, utils.to_int32(EntityId), ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_number_elementary_data(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetNumberElementaryData(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_elementary_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_ElementaryDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_push_back(field, EntityId, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_PushBack(field._internal_obj if field is not None else None, utils.to_int32(EntityId), utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_data(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetData(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_data_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetDataWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_data_pointer_with_collection(field, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetDataPointerWithCollection(field._internal_obj if field is not None else None, data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_data_pointer(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetDataPointer(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_scoping(field, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetScoping(field._internal_obj if field is not None else None, utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_cscoping(field, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetCScoping(field._internal_obj if field is not None else None, scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_entity_data(field, index, id, size, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetEntityData(field._internal_obj if field is not None else None, utils.to_int32(index), utils.to_int32(id), utils.to_int32(size), utils.to_int32_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_resize(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_Resize(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_reserve(field, dataSize, scopingSize):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_Reserve(field._internal_obj if field is not None else None, utils.to_int32(dataSize), utils.to_int32(scopingSize), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_data_for_dpf_vector(dpf_object, out, data, size, EntityIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityData_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, out._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_data_by_id_for_dpf_vector(dpf_object, vec, data, size, EntityId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityDataById_For_DpfVector(dpf_object._internal_obj if dpf_object is not None else None, vec._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), utils.to_int32(EntityId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_get_data_fast(f, index, data, id, size, n_comp):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSProperty_GetDataFast(f._internal_obj if f is not None else None, utils.to_int32(index), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(size), utils.to_int32_ptr(n_comp), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_location(dpf_object):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetLocation(dpf_object._internal_obj if dpf_object is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csproperty_field_get_data_size(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetDataSize(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_id(field, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityId(field._internal_obj if field is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_entity_index(field, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetEntityIndex(field._internal_obj if field is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_shared_field_definition(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetSharedFieldDefinition(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_set_field_definition(field, field_definition):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetFieldDefinition(field._internal_obj if field is not None else None, field_definition._internal_obj if field_definition is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_name(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetName(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def csproperty_field_set_name(field, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_SetName(field._internal_obj if field is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_fast_access_ptr(field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_GetFastAccessPtr(field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def property_get_data_fast(f, index, data, id, size, n_comp):
		res = capi.dll.Property_GetDataFast(f, utils.to_int32(index), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(size), utils.to_int32_ptr(n_comp))
		return res

	@staticmethod
	def csproperty_field_new_on_client(client, numEntities, data_size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_new_on_client(client._internal_obj if client is not None else None, utils.to_int32(numEntities), utils.to_int32(data_size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def csproperty_field_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.CSPropertyField_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

