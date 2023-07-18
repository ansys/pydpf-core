import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import data_sources_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# DataSources
#-------------------------------------------------------------------------------

class DataSourcesCAPI(data_sources_abstract_api.DataSourcesAbstractAPI):

	@staticmethod
	def init_data_sources_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def data_sources_new(operatorName):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_new(utils.to_char_ptr(operatorName), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_delete(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_delete(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_result_file_path(dataSources, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetResultFilePath(dataSources._internal_obj if dataSources is not None else None, name, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_result_file_path_with_key(dataSources, name, sKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetResultFilePathWithKey(dataSources._internal_obj if dataSources is not None else None, name, utils.to_char_ptr(sKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_domain_result_file_path_with_key(dataSources, name, sKey, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetDomainResultFilePathWithKey(dataSources._internal_obj if dataSources is not None else None, name, utils.to_char_ptr(sKey), utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path(dataSources, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePath(dataSources._internal_obj if dataSources is not None else None, name, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path_with_key(dataSources, name, sKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePathWithKey(dataSources._internal_obj if dataSources is not None else None, name, utils.to_char_ptr(sKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path_for_specified_result(dataSources, name, sKey, sResultKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePathForSpecifiedResult(dataSources._internal_obj if dataSources is not None else None, name, utils.to_char_ptr(sKey), utils.to_char_ptr(sResultKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_result_file_path_utf8(dataSources, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetResultFilePathUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_result_file_path_with_key_utf8(dataSources, name, sKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetResultFilePathWithKeyUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_char_ptr(sKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_domain_result_file_path_utf8(dataSources, name, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetDomainResultFilePathUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_set_domain_result_file_path_with_key_utf8(dataSources, name, sKey, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_SetDomainResultFilePathWithKeyUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_char_ptr(sKey), utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path_utf8(dataSources, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePathUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path_with_key_utf8(dataSources, name, sKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePathWithKeyUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_char_ptr(sKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_domain_file_path_with_key_utf8(dataSources, name, sKey, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddDomainFilePathWithKeyUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_char_ptr(sKey), utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_file_path_for_specified_result_utf8(dataSources, name, sKey, sResultKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddFilePathForSpecifiedResultUtf8(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(name), utils.to_char_ptr(sKey), utils.to_char_ptr(sResultKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_upstream_data_sources(dataSources, upstreamDataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddUpstreamDataSources(dataSources._internal_obj if dataSources is not None else None, upstreamDataSources._internal_obj if upstreamDataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_upstream_data_sources_for_specified_result(dataSources, upstreamDataSources, sResultKey):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddUpstreamDataSourcesForSpecifiedResult(dataSources._internal_obj if dataSources is not None else None, upstreamDataSources._internal_obj if upstreamDataSources is not None else None, utils.to_char_ptr(sResultKey), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_add_upstream_domain_data_sources(dataSources, upstreamDataSources, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_AddUpstreamDomainDataSources(dataSources._internal_obj if dataSources is not None else None, upstreamDataSources._internal_obj if upstreamDataSources is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_result_key(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetResultKey(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_result_key_by_index(dataSources, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetResultKeyByIndex(dataSources._internal_obj if dataSources is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_num_result_keys(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetNumResultKeys(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_num_keys(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetNumKeys(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_key(dataSources, index, num_path):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetKey(dataSources._internal_obj if dataSources is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(num_path)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_path(dataSources, key, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetPath(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(key), utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_namespace(dataSources, key):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetNamespace(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(key), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_new_path_collection_for_key(dataSources, key):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetNewPathCollectionForKey(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(key), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_new_collection_for_results_path(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetNewCollectionForResultsPath(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_size(dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetSize(dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_path_by_path_index(dataSources, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetPathByPathIndex(dataSources._internal_obj if dataSources is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_key_by_path_index(dataSources, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetKeyByPathIndex(dataSources._internal_obj if dataSources is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def data_sources_get_label_space_by_path_index(dataSources, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_GetLabelSpaceByPathIndex(dataSources._internal_obj if dataSources is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_register_namespace(dataSources, result_key, ns):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_RegisterNamespace(dataSources._internal_obj if dataSources is not None else None, utils.to_char_ptr(result_key), utils.to_char_ptr(ns), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_new_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def data_sources_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.DataSources_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

