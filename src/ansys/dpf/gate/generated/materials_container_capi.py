import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import materials_container_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# MaterialsContainer
#-------------------------------------------------------------------------------

class MaterialsContainerCAPI(materials_container_abstract_api.MaterialsContainerAbstractAPI):

	@staticmethod
	def init_materials_container_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def materials_container_delete(materialscontainer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_delete(materialscontainer._internal_obj if materialscontainer is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_dpf_mat_ids(materialscontainer, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetDpfMatIds(materialscontainer._internal_obj if materialscontainer is not None else None, ctypes.byref(utils.to_int32(size)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_vuuidat_dpf_mat_id(materialscontainer, dpfMatId):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetVUUIDAtDpfMatId(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_int32(dpfMatId), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def materials_container_get_num_of_materials(materialscontainer):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetNumOfMaterials(materialscontainer._internal_obj if materialscontainer is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_num_available_properties_at_vuuid(materialscontainer, vuuid):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetNumAvailablePropertiesAtVUUID(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_char_ptr(vuuid), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_property_scripting_name_of_dpf_mat_id_at_index(materialscontainer, dpfmatID, idx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetPropertyScriptingNameOfDpfMatIdAtIndex(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_int32(dpfmatID), utils.to_int32(idx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def materials_container_get_num_available_properties_at_dpf_mat_id(materialscontainer, dpfmatID):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetNumAvailablePropertiesAtDpfMatId(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_int32(dpfmatID), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_material_physic_name_at_vuuid(materialscontainer, vuuid):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetMaterialPhysicNameAtVUUID(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_char_ptr(vuuid), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def materials_container_get_material_physic_name_at_dpf_mat_id(materialscontainer, dpfmatID):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetMaterialPhysicNameAtDpfMatId(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_int32(dpfmatID), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def materials_container_get_dpf_mat_id_at_material_physic_name(materialscontainer, physicname):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetDpfMatIdAtMaterialPhysicName(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_char_ptr(physicname), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def materials_container_get_dpf_mat_id_at_vuuid(materialscontainer, vuuid):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MaterialsContainer_GetDpfMatIdAtVUUID(materialscontainer._internal_obj if materialscontainer is not None else None, utils.to_char_ptr(vuuid), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

