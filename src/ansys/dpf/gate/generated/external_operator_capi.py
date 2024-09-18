import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import external_operator_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# ExternalOperator
#-------------------------------------------------------------------------------

class ExternalOperatorCAPI(external_operator_abstract_api.ExternalOperatorAbstractAPI):

	@staticmethod
	def init_external_operator_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def external_operator_record(operator_main, func, operator_identifier, spec):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_record(utils.to_void_ptr(operator_main), func, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_with_derivative(operator_main, func, operator_deriv, deriv_callback, operator_identifier, spec):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_record_with_derivative(utils.to_void_ptr(operator_main), func, utils.to_void_ptr(operator_deriv), deriv_callback, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_with_abstract_core(operator_main, func, operator_identifier, spec, core):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordWithAbstractCore(utils.to_void_ptr(operator_main), func, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_with_abstract_core_with_derivative(operator_main, func, operator_deriv, deriv_callback, operator_identifier, spec, core):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordWithAbstractCore_with_derivative(utils.to_void_ptr(operator_main), func, utils.to_void_ptr(operator_deriv), deriv_callback, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_internal_with_abstract_core(operator_main, func, operator_identifier, spec, core, policy):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordInternalWithAbstractCore(utils.to_void_ptr(operator_main), func, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, policy, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_internal_with_abstract_core_with_derivative(operator_main, func, operator_deriv, deriv_callback, operator_identifier, spec, core, policy):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordInternalWithAbstractCore_with_derivative(utils.to_void_ptr(operator_main), func, utils.to_void_ptr(operator_deriv), deriv_callback, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, policy, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_with_abstract_core_and_wrapper(operator_main, func, operator_identifier, spec, core, wrapper):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordWithAbstractCoreAndWrapper(utils.to_void_ptr(operator_main), func, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, wrapper, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_record_with_abstract_core_and_wrapper_with_derivative(operator_main, func, operator_deriv, deriv_callback, operator_identifier, spec, core, wrapper):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_recordWithAbstractCoreAndWrapper_with_derivative(utils.to_void_ptr(operator_main), func, utils.to_void_ptr(operator_deriv), deriv_callback, utils.to_char_ptr(operator_identifier), spec._internal_obj if spec is not None else None, core, wrapper, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_status(operator_data, status):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putStatus(operator_data, utils.to_int32(status), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_exception(operator_data, error_code, message):
		res = capi.dll.ExternalOperator_putException(operator_data, utils.to_int32(error_code), utils.to_char_ptr(message))
		return res

	@staticmethod
	def external_operator_put_out_collection(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutCollection(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_num_inputs(operator_data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getNumInputs(operator_data, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_has_input(operator_data, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_hasInput(operator_data, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_field(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInField(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_field(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutField(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_fields_container(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInFieldsContainer(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_data_sources(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInDataSources(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_data_sources(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutDataSources(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_scoping(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInScoping(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_scoping(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutScoping(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_scopings_container(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInScopingsContainer(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_meshed_region(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInMeshedRegion(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_meshed_region(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutMeshedRegion(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_time_freq(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInTimeFreq(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_time_freq(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutTimeFreq(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_meshes_container(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInMeshesContainer(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_custom_type_fields_container(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInCustomTypeFieldsContainer(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_streams(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInStreams(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_streams(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutStreams(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_property_field(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInPropertyField(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_generic_data_container(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInGenericDataContainer(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_property_field(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutPropertyField(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_support(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInSupport(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_data_tree(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInDataTree(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_workflow(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInWorkflow(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_operator(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInOperator(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_external_data(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInExternalData(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_as_any(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInAsAny(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_remote_workflow(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInRemoteWorkflow(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_remote_operator(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInRemoteOperator(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_string_field(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInStringField(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_custom_type_field(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInCustomTypeField(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_label_space(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInLabelSpace(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_remote_workflow(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutRemoteWorkflow(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_operator(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutOperator(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_support(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutSupport(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_as_any(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutAsAny(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_bool(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInBool(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_bool(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutBool(operator_data, utils.to_int32(pin_index), data, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_int(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInInt(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_int(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutInt(operator_data, utils.to_int32(pin_index), utils.to_int32(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_double(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInDouble(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_double(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutDouble(operator_data, utils.to_int32(pin_index), ctypes.c_double(data) if isinstance(data, float) else data, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_long_long(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInLongLong(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_long_long(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutLongLong(operator_data, utils.to_int32(pin_index), utils.to_uint64(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_string(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInString(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def external_operator_put_out_string(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutString(operator_data, utils.to_int32(pin_index), utils.to_char_ptr(data), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_string_with_size(operator_data, pin_index, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInString_with_size(operator_data, utils.to_int32(pin_index), utils.to_uint64_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.string_at(res, size.val.value)
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def external_operator_put_out_string_with_size(operator_data, pin_index, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutString_with_size(operator_data, utils.to_int32(pin_index), utils.to_char_ptr(data), utils.to_uint64(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_vec_int(operator_data, pin_index, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInVecInt(operator_data, utils.to_int32(pin_index), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_vecint(operator_data, pin_index, data, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutVecint(operator_data, utils.to_int32(pin_index), utils.to_int32_ptr(data), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_vec_double(operator_data, pin_index, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInVecDouble(operator_data, utils.to_int32(pin_index), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_in_vec_string_as_collection(operator_data, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getInVecStringAsCollection(operator_data, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_data_tree(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutDataTree(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_workflow(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutWorkflow(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_generic_data_container(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutGenericDataContainer(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_result_info(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutResultInfo(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_string_field(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutStringField(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_custom_type_field(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutCustomTypeField(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_external_data(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutExternalData(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_put_out_collection_as_vector(operator_data, pin_index, data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_putOutCollectionAsVector(operator_data, utils.to_int32(pin_index), data._internal_obj if data is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_pin_is_of_type(operator_data, pin_index, type_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_pinIsOfType(operator_data, utils.to_int32(pin_index), utils.to_char_ptr(type_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_delegate_run(operator_data, other_op, forwardInputs):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_delegateRun(operator_data, other_op._internal_obj if other_op is not None else None, forwardInputs, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_instantiate_internal_operator(operator_data, op_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_instantiateInternalOperator(operator_data, utils.to_char_ptr(op_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_connect_all_inputs_to_operator(operator_data, other_op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_connectAllInputsToOperator(operator_data, other_op._internal_obj if other_op is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_operator_name(operator_data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getOperatorName(operator_data, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def external_operator_get_operator_config(operator_data):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getOperatorConfig(operator_data, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_get_derivative_of_input(deriv_data, input_pin, out_pin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_getDerivativeOfInput(deriv_data, utils.to_int32(input_pin), utils.to_int32_ptr(out_pin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_forward_input(deriv_data, input_pin_from_base, input_pin_from_op, op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_forwardInput(deriv_data, utils.to_int32(input_pin_from_base), utils.to_int32(input_pin_from_op), op._internal_obj if op is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_set_derivative(deriv_data, derivative):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_setDerivative(deriv_data, derivative._internal_obj if derivative is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_forward_output(deriv_data, output_pin_from_base, input_pin_from_op, op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_forwardOutput(deriv_data, utils.to_int32(output_pin_from_base), utils.to_int32(input_pin_from_op), op._internal_obj if op is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_assert_instantiate(deriv_data, op_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_assertInstantiate(deriv_data, utils.to_char_ptr(op_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_connect_to_upstream_derivative(deriv_data, current_op, out_pin, ancestor_pin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_connectToUpstreamDerivative(deriv_data, current_op._internal_obj if current_op is not None else None, utils.to_int32(out_pin), utils.to_int32(ancestor_pin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def external_operator_map_down_stream_derivative(deriv_data, in_pin, current_op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.ExternalOperator_mapDownStreamDerivative(deriv_data, utils.to_int32(in_pin), current_op._internal_obj if current_op is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

