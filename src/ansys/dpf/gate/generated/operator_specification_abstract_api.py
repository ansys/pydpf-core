#-------------------------------------------------------------------------------
# OperatorSpecification
#-------------------------------------------------------------------------------

class OperatorSpecificationAbstractAPI:
	@staticmethod
	def init_operator_specification_environment(object):
		pass

	@staticmethod
	def finish_operator_specification_environment(object):
		pass

	@staticmethod
	def operator_specification_new(op):
		raise NotImplementedError

	@staticmethod
	def operator_empty_specification_new():
		raise NotImplementedError

	@staticmethod
	def operator_specification_delete(var1):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_description(specification):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_description(specification, text):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_property(specification, key, value):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_num_pins(specification, binput):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_name(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_num_type_names(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_fill_pin_numbers(specification, binput, pins):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_type_name(specification, binput, numPin, numType):
		raise NotImplementedError

	@staticmethod
	def operator_specification_is_pin_optional(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_document(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_is_pin_ellipsis(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_is_pin_in_place(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_properties(specification, prop):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_num_properties(specification):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_property_key(specification, index):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_pin(specification, var1, position, name, description, n_types, types, is_optional, is_ellipsis):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_pin_derived_class(specification, var1, position, name, description, n_types, types, is_optional, is_ellipsis, derived_type_name):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_pin_aliases(specification, var1, position, n_aliases, aliases):
		raise NotImplementedError

	@staticmethod
	def operator_specification_add_pin_alias(specification, var1, position, alias):
		raise NotImplementedError

	@staticmethod
	def operator_specification_add_bool_config_option(specification, option_name, default_value, description):
		raise NotImplementedError

	@staticmethod
	def operator_specification_add_int_config_option(specification, option_name, default_value, description):
		raise NotImplementedError

	@staticmethod
	def operator_specification_add_double_config_option(specification, option_name, default_value, description):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_num_config_options(specification):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_config_name(specification, numOption):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_config_num_type_names(specification, numOption):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_config_type_name(specification, numOption, numType):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_config_printable_default_value(specification, numOption):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_config_description(specification, numOption):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_derived_class_type_name(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_set_version(specification, semver):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_version(specification):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_num_aliases(specification, binput, numPin):
		raise NotImplementedError

	@staticmethod
	def operator_specification_get_pin_alias(specification, binput, numPin, numAlias):
		raise NotImplementedError

	@staticmethod
	def operator_specification_new_on_client(client, op):
		raise NotImplementedError

