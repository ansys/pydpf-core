#-------------------------------------------------------------------------------
# SupportQuery
#-------------------------------------------------------------------------------

class SupportQueryAbstractAPI:
	@staticmethod
	def init_support_query_environment(object):
		pass

	@staticmethod
	def finish_support_query_environment(object):
		pass

	@staticmethod
	def support_query_all_entities(supportQuery, requested_location):
		raise NotImplementedError

	@staticmethod
	def support_query_scoping_by_property(supportQuery, requested_location, prop_name, prop_number):
		raise NotImplementedError

	@staticmethod
	def support_query_rescoping_by_property(supportQuery, scoping, prop_name, prop_number):
		raise NotImplementedError

	@staticmethod
	def support_query_scoping_by_named_selection(supportQuery, requested_location, namedSelection):
		raise NotImplementedError

	@staticmethod
	def support_query_transpose_scoping(supportQuery, scoping, bInclusive):
		raise NotImplementedError

	@staticmethod
	def support_query_topology_by_scoping(supportQuery, scoping, topologyRequest):
		raise NotImplementedError

	@staticmethod
	def support_query_data_by_scoping(supportQuery, scoping, domainsDataRequest):
		raise NotImplementedError

	@staticmethod
	def support_query_string_field(supportQuery, strRequest):
		raise NotImplementedError

