#-------------------------------------------------------------------------------
# FieldDefinition
#-------------------------------------------------------------------------------

class FieldDefinitionAbstractAPI:
	@staticmethod
	def init_field_definition_environment(object):
		pass

	@staticmethod
	def finish_field_definition_environment(object):
		pass

	@staticmethod
	def field_definition_new():
		raise NotImplementedError

	@staticmethod
	def field_definition_wrap(var1):
		raise NotImplementedError

	@staticmethod
	def field_definition_delete(fielddef):
		raise NotImplementedError

	@staticmethod
	def field_definition_get_fast_access_ptr(fielddef):
		raise NotImplementedError

	@staticmethod
	def field_definition_get_unit(res, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def field_definition_fill_unit(fieldDef, symbol, size, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def field_definition_get_shell_layers(res):
		raise NotImplementedError

	@staticmethod
	def field_definition_get_location(res):
		raise NotImplementedError

	@staticmethod
	def field_definition_fill_location(fieldDef, location, size):
		raise NotImplementedError

	@staticmethod
	def field_definition_get_dimensionality(res, nature, size_vsize):
		raise NotImplementedError

	@staticmethod
	def field_definition_fill_dimensionality(res, dim, nature, size_vsize):
		raise NotImplementedError

	@staticmethod
	def field_definition_set_unit(fieldDef, symbol, ptrObject, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def field_definition_set_shell_layers(fieldDef, shellLayers):
		raise NotImplementedError

	@staticmethod
	def field_definition_set_location(fieldDef, location):
		raise NotImplementedError

	@staticmethod
	def field_definition_set_dimensionality(fieldDef, dim, ptrSize, size_vsize):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_unit(res, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_fill_unit(fieldDef, symbol, size, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_shell_layers(res):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_location(res):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_fill_location(fieldDef, location, size):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_dimensionality(res, nature, size_vsize):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_fill_dimensionality(res, dim, nature, size_vsize):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_unit(fieldDef, symbol, ptrObject, homogeneity, factor, shift):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_shell_layers(fieldDef, shellLayers):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_location(fieldDef, location):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_dimensionality(fieldDef, dim, ptrSize, size_vsize):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_quantity_type(fieldDef, quantityType):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_num_available_quantity_types(fieldDef):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_quantity_type(fieldDef, index):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_is_of_quantity_type(fieldDef, quantityType):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_get_name(res):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_set_name(fieldDef, name):
		raise NotImplementedError

	@staticmethod
	def csfield_definition_fill_name(fieldDef, name, size):
		raise NotImplementedError

	@staticmethod
	def dimensionality_get_num_comp(nature, size, vsize):
		raise NotImplementedError

	@staticmethod
	def field_definition_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def dimensionality_get_num_comp_for_object(api_to_use, nature, size, vsize):
		raise NotImplementedError

