import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import collection_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# Collection
#-------------------------------------------------------------------------------

class CollectionCAPI(collection_abstract_api.CollectionAbstractAPI):

	@staticmethod
	def init_collection_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def collection_of_int_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfIntNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_double_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfDoubleNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_string_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfStringNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_char_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfCharNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_data_as_int(collection, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDataAsInt(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_data_as_double(collection, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDataAsDouble(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_data_as_char(collection, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDataAsChar(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def collection_add_int_entry(collection, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddIntEntry(collection._internal_obj if collection is not None else None, utils.to_int32(obj), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_add_double_entry(collection, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddDoubleEntry(collection._internal_obj if collection is not None else None, ctypes.c_double(obj) if isinstance(obj, float) else obj, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_add_string_entry(collection, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddStringEntry(collection._internal_obj if collection is not None else None, utils.to_char_ptr(obj), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_int_entry(collection, index, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetIntEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), utils.to_int32(obj), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_double_entry(collection, index, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetDoubleEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.c_double(obj) if isinstance(obj, float) else obj, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_string_entry(collection, index, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetStringEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), utils.to_char_ptr(obj), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_int_entry(collection, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetIntEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_double_entry(collection, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDoubleEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_string_entry(collection, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetStringEntry(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def collection_set_data_as_int(collection, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetDataAsInt(collection._internal_obj if collection is not None else None, utils.to_int32_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_data_as_double(collection, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetDataAsDouble(collection._internal_obj if collection is not None else None, utils.to_double_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_data_as_int_for_dpf_vector(collection, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDataAsInt_For_DpfVector(collection._internal_obj if collection is not None else None, out._internal_obj, utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_data_as_double_for_dpf_vector(collection, out, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetDataAsDouble_For_DpfVector(collection._internal_obj if collection is not None else None, out._internal_obj, utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_scoping_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfScopingNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_field_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfFieldNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_mesh_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfMeshNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_custom_type_field_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfCustomTypeFieldNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_any_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfAnyNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_scoping_new_with_data(data, num_ids, labels, num_labels, ids):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfScopingNewWithData(data, utils.to_int32(num_ids), utils.to_char_ptr_ptr(labels), utils.to_int32(num_labels), utils.to_int32_ptr_ptr(ids), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_field_new_with_data(data, num_ids, labels, num_labels, ids):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfFieldNewWithData(data, utils.to_int32(num_ids), utils.to_char_ptr_ptr(labels), utils.to_int32(num_labels), utils.to_int32_ptr_ptr(ids), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_mesh_new_with_data(data, num_ids, labels, num_labels, ids):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfMeshNewWithData(data, utils.to_int32(num_ids), utils.to_char_ptr_ptr(labels), utils.to_int32(num_labels), utils.to_int32_ptr_ptr(ids), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_custom_type_field_new_with_data(data, num_ids, labels, num_labels, ids):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfCustomTypeFieldNewWithData(data, utils.to_int32(num_ids), utils.to_char_ptr_ptr(labels), utils.to_int32(num_labels), utils.to_int32_ptr_ptr(ids), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_any_new_with_data(data, num_ids, labels, num_labels, ids):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfAnyNewWithData(data, utils.to_int32(num_ids), utils.to_char_ptr_ptr(labels), utils.to_int32(num_labels), utils.to_int32_ptr_ptr(ids), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_num_labels(collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetNumLabels(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_label(collection, labelIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetLabel(collection._internal_obj if collection is not None else None, utils.to_int32(labelIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def collection_add_label(collection, label):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddLabel(collection._internal_obj if collection is not None else None, utils.to_char_ptr(label), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_add_label_with_default_value(collection, label, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddLabelWithDefaultValue(collection._internal_obj if collection is not None else None, utils.to_char_ptr(label), utils.to_int32(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_add_entry(collection, labelspace, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_AddEntry(collection._internal_obj if collection is not None else None, labelspace._internal_obj if labelspace is not None else None, obj._internal_obj if obj is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_push_back_entry(collection, labelspace, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_PushBackEntry(collection._internal_obj if collection is not None else None, labelspace._internal_obj if labelspace is not None else None, obj._internal_obj if obj is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_entry_by_index(collection, index, obj):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetEntryByIndex(collection._internal_obj if collection is not None else None, utils.to_int32(index), obj._internal_obj if obj is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_obj_by_index(collection, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetObjByIndex(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_obj(collection, space):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetObj(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_obj_label_space_by_index(collection, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetObjLabelSpaceByIndex(collection._internal_obj if collection is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_objs_for_label_space(collection, space, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetObjsForLabelSpace(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, utils.to_uint64_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_num_obj_for_label_space(collection, space):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetNumObjForLabelSpace(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_obj_by_index_for_label_space(collection, space, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetObjByIndexForLabelSpace(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_fill_obj_indeces_for_label_space(collection, space, indices):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_FillObjIndecesForLabelSpace(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, utils.to_int32_ptr(indices), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_label_scoping(collection, label):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetLabelScoping(collection._internal_obj if collection is not None else None, utils.to_char_ptr(label), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_name(collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetName(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def collection_set_name(collection, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetName(collection._internal_obj if collection is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_id(collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetId(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_id(collection, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetId(collection._internal_obj if collection is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_delete(collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_delete(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_size(collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetSize(collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_reserve(collection, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_reserve(collection._internal_obj if collection is not None else None, utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_resize(collection, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_resize(collection._internal_obj if collection is not None else None, utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_get_support(collection, label):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_GetSupport(collection._internal_obj if collection is not None else None, utils.to_char_ptr(label), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_set_support(collection, label, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_SetSupport(collection._internal_obj if collection is not None else None, utils.to_char_ptr(label), support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_create_sub_collection(collection, space):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_CreateSubCollection(collection._internal_obj if collection is not None else None, space._internal_obj if space is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_scoping_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfScopingNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_field_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfFieldNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_mesh_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfMeshNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_any_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfAnyNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_scoping_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfScoping_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_field_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfField_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_mesh_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfMesh_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_any_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfAny_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_int_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfIntNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_double_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfDoubleNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_string_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfStringNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def collection_of_string_new_local(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Collection_OfStringNew_local(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

