import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import dpf_data_tree_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# DpfDataTree
#-------------------------------------------------------------------------------

class DpfDataTreeCAPI(dpf_data_tree_abstract_api.DpfDataTreeAbstractAPI):

	@staticmethod
	def init_dpf_data_tree_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def dpf_data_tree_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_delete(data_tree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_delete(data_tree._internal_obj if data_tree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_has_sub_tree(data_tree, sub_tree_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_hasSubTree(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(sub_tree_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_sub_tree(data_tree, sub_tree_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getSubTree(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(sub_tree_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_make_sub_tree(data_tree, sub_tree_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_makeSubTree(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(sub_tree_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_has_attribute(data_tree, attribute_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_hasAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_available_attributes_names_in_string_collection(data_tree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getAvailableAttributesNamesInStringCollection(data_tree._internal_obj if data_tree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_available_sub_tree_names_in_string_collection(data_tree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getAvailableSubTreeNamesInStringCollection(data_tree._internal_obj if data_tree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_int_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32_ptr(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_unsigned_int_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getUnsignedIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), value, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_double_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getDoubleAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_double_ptr(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_string_attribute(data_tree, attribute_name, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getStringAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_char_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_vec_int_attribute(data_tree, attribute_name, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getVecIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_vec_double_attribute(data_tree, attribute_name, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getVecDoubleAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_int_attribute_with_check(data_tree, attribute_name, value, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getIntAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32_ptr(value), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_unsigned_int_attribute_with_check(data_tree, attribute_name, value, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getUnsignedIntAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), value, value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_double_attribute_with_check(data_tree, attribute_name, value, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getDoubleAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_double_ptr(value), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_string_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getStringAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_char_ptr_ptr(data), utils.to_int32_ptr(size), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_vec_int_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getVecIntAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(size), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_vec_double_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getVecDoubleAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_double_ptr_ptr(data), utils.to_int32_ptr(size), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_string_collection_attribute(data_tree, attribute_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getStringCollectionAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_get_string_collection_attribute_with_check(data_tree, attribute_name, value_found):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_getStringCollectionAttributeWithCheck(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), value_found, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_int_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_unsigned_int_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setUnsignedIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), value, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_vec_int_attribute(data_tree, attribute_name, value, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setVecIntAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_int32_ptr(value), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_double_attribute(data_tree, attribute_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setDoubleAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), ctypes.c_double(value) if isinstance(value, float) else value, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_vec_double_attribute(data_tree, attribute_name, value, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setVecDoubleAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_double_ptr(value), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_string_collection_attribute(data_tree, attribute_name, collection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setStringCollectionAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), collection._internal_obj if collection is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_string_attribute(data_tree, attribute_name, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setStringAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), utils.to_char_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_set_sub_tree_attribute(data_tree, attribute_name, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_setSubTreeAttribute(data_tree._internal_obj if data_tree is not None else None, utils.to_char_ptr(attribute_name), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_save_to_txt(dataSources, text, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_saveToTxt(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr_ptr(text), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_read_from_text(dataSources, filename, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_readFromText(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(filename), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_save_to_json(dataSources, text, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_saveToJson(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr_ptr(text), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_read_from_json(dataSources, filename):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_readFromJson(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(filename), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def dpf_data_tree_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DpfDataTree_new_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

