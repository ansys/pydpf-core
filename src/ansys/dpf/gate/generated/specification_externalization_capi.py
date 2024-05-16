import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import specification_externalization_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# SpecificationExternalization
#-------------------------------------------------------------------------------

class SpecificationExternalizationCAPI(specification_externalization_abstract_api.SpecificationExternalizationAbstractAPI):

	@staticmethod
	def init_specification_externalization_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def specification_xml_export(filepath):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Specification_xml_export(utils.to_char_ptr(filepath), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def specification_xml_import(filepath):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Specification_xml_import(utils.to_char_ptr(filepath), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def set_specification_in_core(registry):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.setSpecificationInCore(registry, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

