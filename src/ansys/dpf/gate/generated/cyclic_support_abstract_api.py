#-------------------------------------------------------------------------------
# CyclicSupport
#-------------------------------------------------------------------------------

class CyclicSupportAbstractAPI:
	@staticmethod
	def init_cyclic_support_environment(object):
		pass

	@staticmethod
	def finish_cyclic_support_environment(object):
		pass

	@staticmethod
	def cyclic_support_delete(support):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_num_sectors(support, istage):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_num_stages(support):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_sectors_scoping(support, istage):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_cyclic_phase(support):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_base_nodes_scoping(support, istage):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_base_elements_scoping(support, istage):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_expanded_node_ids(support, baseNodeId, istage, sectorsScoping):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_expanded_element_ids(support, baseElementId, istage, sectorsScoping):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_cs(support):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_low_high_map(support, istage):
		raise NotImplementedError

	@staticmethod
	def cyclic_support_get_high_low_map(support, istage):
		raise NotImplementedError

