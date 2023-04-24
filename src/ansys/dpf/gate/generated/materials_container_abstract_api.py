#-------------------------------------------------------------------------------
# MaterialsContainer
#-------------------------------------------------------------------------------

class MaterialsContainerAbstractAPI:
	@staticmethod
	def init_materials_container_environment(object):
		pass

	@staticmethod
	def finish_materials_container_environment(object):
		pass

	@staticmethod
	def materials_container_delete(materialscontainer):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_dpf_mat_ids(materialscontainer, size):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_vuuidat_dpf_mat_id(materialscontainer, dpfMatId):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_num_of_materials(materialscontainer):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_num_available_properties_at_vuuid(materialscontainer, vuuid):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_property_scripting_name_of_dpf_mat_id_at_index(materialscontainer, dpfmatID, idx):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_num_available_properties_at_dpf_mat_id(materialscontainer, dpfmatID):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_material_physic_name_at_vuuid(materialscontainer, vuuid):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_material_physic_name_at_dpf_mat_id(materialscontainer, dpfmatID):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_dpf_mat_id_at_material_physic_name(materialscontainer, physicname):
		raise NotImplementedError

	@staticmethod
	def materials_container_get_dpf_mat_id_at_vuuid(materialscontainer, vuuid):
		raise NotImplementedError

