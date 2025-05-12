#-------------------------------------------------------------------------------
# SemanticVersion
#-------------------------------------------------------------------------------

class SemanticVersionAbstractAPI:
	@staticmethod
	def init_semantic_version_environment(object):
		pass

	@staticmethod
	def finish_semantic_version_environment(object):
		pass

	@staticmethod
	def semantic_version_new(major, minor, patch):
		raise NotImplementedError

	@staticmethod
	def semantic_version_get_components(ver, major, minor, patch):
		raise NotImplementedError

	@staticmethod
	def semantic_version_eq(ver, other):
		raise NotImplementedError

	@staticmethod
	def semantic_version_lt(ver, other):
		raise NotImplementedError

