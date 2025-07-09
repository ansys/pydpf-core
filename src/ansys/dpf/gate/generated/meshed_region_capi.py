import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import meshed_region_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# MeshedRegion
#-------------------------------------------------------------------------------

class MeshedRegionCAPI(meshed_region_abstract_api.MeshedRegionAbstractAPI):

	@staticmethod
	def init_meshed_region_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def meshed_region_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_New(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_delete(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_Delete(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_reserve(meshedRegion, numNodes, numElements):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_Reserve(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(numNodes), utils.to_int32(numElements), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_nodes(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumNodes(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_elements(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumElements(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_faces(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumFaces(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_shared_nodes_scoping(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetSharedNodesScoping(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_shared_elements_scoping(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetSharedElementsScoping(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_shared_faces_scoping(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetSharedFacesScoping(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_unit(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetUnit(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def meshed_region_get_has_solid_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasSolidRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_gasket_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasGasketRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_shell_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasShellRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_skin_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasSkinRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_only_skin_elements(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasOnlySkinElements(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_point_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasPointRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_beam_region(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasBeamRegion(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_polygons(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasPolygons(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_has_polyhedrons(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetHasPolyhedrons(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_node_id(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNodeId(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_node_index(meshedRegion, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNodeIndex(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_element_id(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetElementId(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_element_index(meshedRegion, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetElementIndex(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_nodes_of_element(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumNodesOfElement(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_corner_nodes_of_element(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumCornerNodesOfElement(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_adjacent_nodes_of_mid_node_in_element(meshedRegion, eleIndex, indMidodInEle, indCornerNod1InEle, indCornerNod2InEle):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetAdjacentNodesOfMidNodeInElement(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(eleIndex), utils.to_int32(indMidodInEle), ctypes.byref(utils.to_int32(indCornerNod1InEle)), ctypes.byref(utils.to_int32(indCornerNod2InEle)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_node_id_of_element(meshedRegion, eidx, nidx):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNodeIdOfElement(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(eidx), utils.to_int32(nidx), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_node_coord(meshedRegion, index, coordinate):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNodeCoord(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), utils.to_int32(coordinate), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_element_type(meshedRegion, id, type, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetElementType(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(type)), ctypes.byref(utils.to_int32(index)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_element_shape(meshedRegion, id, shape, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetElementShape(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(shape)), ctypes.byref(utils.to_int32(index)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_set_unit(meshedRegion, unit):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_SetUnit(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(unit), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_available_named_selection(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumAvailableNamedSelection(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_named_selection_name(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNamedSelectionName(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def meshed_region_get_named_selection_scoping(meshedRegion, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNamedSelectionScoping(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_add_node(meshedRegion, xyz, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_AddNode(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_double_ptr(xyz), utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_add_element(meshedRegion, id, size, conn, type):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_AddElement(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), utils.to_int32(size), utils.to_int32_ptr(conn), utils.to_int32(type), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_add_element_by_shape(meshedRegion, id, size, conn, shape):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_AddElementByShape(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(id), utils.to_int32(size), utils.to_int32_ptr(conn), utils.to_int32(shape), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_property_field(meshedRegion, property_type):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetPropertyField(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(property_type), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_has_property_field(meshedRegion, property_type):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_HasPropertyField(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(property_type), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_num_available_property_field(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetNumAvailablePropertyField(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_property_field_name(meshedRegion, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetPropertyFieldName(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def meshed_region_get_coordinates_field(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_GetCoordinatesField(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_fill_name(field, name, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_FillName(field._internal_obj if field is not None else None, utils.to_char_ptr(name), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_set_name(field, name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_SetName(field._internal_obj if field is not None else None, utils.to_char_ptr(name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_set_property_field(meshedRegion, name, prop_field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_SetPropertyField(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(name), prop_field._internal_obj if prop_field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_set_coordinates_field(meshedRegion, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_SetCoordinatesField(meshedRegion._internal_obj if meshedRegion is not None else None, field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_set_named_selection_scoping(meshedRegion, name, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_SetNamedSelectionScoping(meshedRegion._internal_obj if meshedRegion is not None else None, utils.to_char_ptr(name), scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_cursor(f, index, data, id, el_type, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_cursor(f._internal_obj if f is not None else None, utils.to_int32(index), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(el_type), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_fast_access_ptr(meshedRegion):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_fast_access_ptr(meshedRegion._internal_obj if meshedRegion is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_fast_add_node(meshedRegion, xyz, id):
		res = capi.dll.MeshedRegion_fast_add_node(meshedRegion, utils.to_double_ptr(xyz), utils.to_int32(id))
		return res

	@staticmethod
	def meshed_region_fast_add_element(meshedRegion, id, size, conn, type):
		res = capi.dll.MeshedRegion_fast_add_element(meshedRegion, utils.to_int32(id), utils.to_int32(size), utils.to_int32_ptr(conn), utils.to_int32(type))
		return res

	@staticmethod
	def meshed_region_fast_reserve(meshedRegion, n_nodes, n_elements):
		res = capi.dll.MeshedRegion_fast_reserve(meshedRegion, utils.to_int32(n_nodes), utils.to_int32(n_elements))
		return res

	@staticmethod
	def meshed_region_fast_cursor(f, index, data, id, el_type, size):
		res = capi.dll.MeshedRegion_fast_cursor(f, utils.to_int32(index), utils.to_int32_ptr_ptr(data), utils.to_int32_ptr(id), utils.to_int32_ptr(el_type), utils.to_int32_ptr(size))
		return res

	@staticmethod
	def meshed_region_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_New_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def meshed_region_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.MeshedRegion_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

