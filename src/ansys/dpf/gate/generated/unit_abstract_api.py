#-------------------------------------------------------------------------------
# Unit
#-------------------------------------------------------------------------------

class UnitAbstractAPI:
	@staticmethod
	def init_unit_environment(object):
		pass

	@staticmethod
	def finish_unit_environment(object):
		pass

	@staticmethod
	def unit_get_homogeneity(pre_allocated_char_64, symbol):
		raise NotImplementedError

	@staticmethod
	def unit_get_conversion_factor(from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_get_conversion_shift(from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_are_homogeneous(from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_get_symbol(pre_allocated_char_64, homogeneity, unit_system_id):
		raise NotImplementedError

	@staticmethod
	def unit_get_homogeneity_for_object(api_to_use, pre_allocated_char_64, symbol):
		raise NotImplementedError

	@staticmethod
	def unit_get_conversion_factor_for_object(api_to_use, from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_get_conversion_shift_for_object(api_to_use, from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_are_homogeneous_for_object(api_to_use, from_, to):
		raise NotImplementedError

	@staticmethod
	def unit_get_symbol_for_object(api_to_use, pre_allocated_char_64, homogeneity, unit_system_id):
		raise NotImplementedError

