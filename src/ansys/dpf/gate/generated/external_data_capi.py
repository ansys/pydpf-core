import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import external_data_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# ExternalData
#-------------------------------------------------------------------------------

class ExternalDataCAPI(external_data_abstract_api.ExternalDataAbstractAPI):

	@staticmethod
	def init_external_data_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def external_data_wrap(external_data, deleter):
		res = capi.dll.ExternalData_wrap(external_data, deleter)
		return res

	@staticmethod
	def external_data_free(var1):
		res = capi.dll.ExternalData_free(var1._internal_obj if var1 is not None else None)
		return res

	@staticmethod
	def external_data_get(external_data):
		res = capi.dll.ExternalData_get(external_data._internal_obj if external_data is not None else None)
		return res

