import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import support_query_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# SupportQuery
#-------------------------------------------------------------------------------

class SupportQueryCAPI(support_query_abstract_api.SupportQueryAbstractAPI):

	@staticmethod
	def init_support_query_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def support_query_all_entities(supportQuery, requested_location):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_AllEntities(supportQuery, utils.to_char_ptr(requested_location), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_scoping_by_property(supportQuery, requested_location, prop_name, prop_number):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_ScopingByProperty(supportQuery, utils.to_char_ptr(requested_location), utils.to_char_ptr(prop_name), utils.to_int32(prop_number), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_rescoping_by_property(supportQuery, scoping, prop_name, prop_number):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_RescopingByProperty(supportQuery, scoping._internal_obj if scoping is not None else None, utils.to_char_ptr(prop_name), utils.to_int32(prop_number), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_scoping_by_named_selection(supportQuery, requested_location, namedSelection):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_ScopingByNamedSelection(supportQuery, utils.to_char_ptr(requested_location), namedSelection, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_transpose_scoping(supportQuery, scoping, bInclusive):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_TransposeScoping(supportQuery, scoping._internal_obj if scoping is not None else None, bInclusive, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_topology_by_scoping(supportQuery, scoping, topologyRequest):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_TopologyByScoping(supportQuery, scoping._internal_obj if scoping is not None else None, utils.to_char_ptr(topologyRequest), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_data_by_scoping(supportQuery, scoping, domainsDataRequest):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_DataByScoping(supportQuery, scoping._internal_obj if scoping is not None else None, utils.to_char_ptr(domainsDataRequest), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def support_query_string_field(supportQuery, strRequest):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.SupportQuery_StringField(supportQuery, utils.to_char_ptr(strRequest), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

