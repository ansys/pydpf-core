#-------------------------------------------------------------------------------
# MeshedRegion
#-------------------------------------------------------------------------------

class MeshedRegionAbstractAPI:
	@staticmethod
	def init_meshed_region_environment(object):
		pass

	@staticmethod
	def finish_meshed_region_environment(object):
		pass

	@staticmethod
	def meshed_region_new():
		raise NotImplementedError

	@staticmethod
	def meshed_region_delete(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_reserve(meshedRegion, numNodes, numElements):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_nodes(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_elements(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_faces(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_shared_nodes_scoping(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_shared_elements_scoping(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_shared_faces_scoping(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_unit(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_solid_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_gasket_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_shell_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_skin_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_only_skin_elements(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_point_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_beam_region(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_polygons(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_has_polyhedrons(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_node_id(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_node_index(meshedRegion, id):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_element_id(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_element_index(meshedRegion, id):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_nodes_of_element(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_corner_nodes_of_element(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_adjacent_nodes_of_mid_node_in_element(meshedRegion, eleIndex, indMidodInEle, indCornerNod1InEle, indCornerNod2InEle):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_node_id_of_element(meshedRegion, eidx, nidx):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_node_coord(meshedRegion, index, coordinate):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_element_type(meshedRegion, id, type, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_element_shape(meshedRegion, id, shape, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_set_unit(meshedRegion, unit):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_available_named_selection(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_named_selection_name(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_named_selection_scoping(meshedRegion, name):
		raise NotImplementedError

	@staticmethod
	def meshed_region_add_node(meshedRegion, xyz, id):
		raise NotImplementedError

	@staticmethod
	def meshed_region_add_element(meshedRegion, id, size, conn, type):
		raise NotImplementedError

	@staticmethod
	def meshed_region_add_element_by_shape(meshedRegion, id, size, conn, shape):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_property_field(meshedRegion, property_type):
		raise NotImplementedError

	@staticmethod
	def meshed_region_has_property_field(meshedRegion, property_type):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_num_available_property_field(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_property_field_name(meshedRegion, index):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_coordinates_field(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fill_name(field, name, size):
		raise NotImplementedError

	@staticmethod
	def meshed_region_set_name(field, name):
		raise NotImplementedError

	@staticmethod
	def meshed_region_set_property_field(meshedRegion, name, prop_field):
		raise NotImplementedError

	@staticmethod
	def meshed_region_set_coordinates_field(meshedRegion, field):
		raise NotImplementedError

	@staticmethod
	def meshed_region_set_named_selection_scoping(meshedRegion, name, scoping):
		raise NotImplementedError

	@staticmethod
	def meshed_region_cursor(f, index, data, id, el_type, size):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fast_access_ptr(meshedRegion):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fast_add_node(meshedRegion, xyz, id):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fast_add_element(meshedRegion, id, size, conn, type):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fast_reserve(meshedRegion, n_nodes, n_elements):
		raise NotImplementedError

	@staticmethod
	def meshed_region_fast_cursor(f, index, data, id, el_type, size):
		raise NotImplementedError

	@staticmethod
	def meshed_region_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def meshed_region_get_copy(id, client):
		raise NotImplementedError

