import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import workflow_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# Workflow
#-------------------------------------------------------------------------------

class WorkflowCAPI(workflow_abstract_api.WorkflowAbstractAPI):

	@staticmethod
	def init_workflow_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def work_flow_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_copy(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getCopy(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_create_from_text(text):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_create_from_text(utils.to_char_ptr(text), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_copy_on_other_client(wf, client, protocol):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getCopy_on_other_client(wf._internal_obj if wf is not None else None, utils.to_char_ptr(client), utils.to_char_ptr(protocol), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_delete(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_delete(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_record_instance(wf, user_name, transfer_ownership):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_record_instance(wf._internal_obj if wf is not None else None, utils.to_char_ptr(user_name), transfer_ownership, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_replace_instance_at_id(wf, id, user_name, transfer_ownership):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_replace_instance_at_id(wf._internal_obj if wf is not None else None, utils.to_int32(id), utils.to_char_ptr(user_name), transfer_ownership, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_erase_instance(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_erase_instance(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_record_id(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_get_record_id(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_by_identifier(identifier):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_get_by_identifier(utils.to_int32(identifier), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_first_op(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_get_first_op(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_last_op(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_get_last_op(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_discover_operators(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_discover_operators(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_chain_with(wf, wf2):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_chain_with(wf._internal_obj if wf is not None else None, wf2._internal_obj if wf2 is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_chain_with_specified_names(wf, wf2, input_name, output_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_chain_with_specified_names(wf._internal_obj if wf is not None else None, wf2._internal_obj if wf2 is not None else None, utils.to_char_ptr(input_name), utils.to_char_ptr(output_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_create_connection_map():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_create_connection_map(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_add_entry_connection_map(map, out, in_):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_add_entry_connection_map(map._internal_obj if map is not None else None, utils.to_char_ptr(out), utils.to_char_ptr(in_), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_with(wf_right, wf2_left):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_with(wf_right._internal_obj if wf_right is not None else None, wf2_left._internal_obj if wf2_left is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_with_specified_names(wf_right, wf2_left, map):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_with_specified_names(wf_right._internal_obj if wf_right is not None else None, wf2_left._internal_obj if wf2_left is not None else None, map._internal_obj if map is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_add_operator(wf, op):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_add_operator(wf._internal_obj if wf is not None else None, op._internal_obj if op is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_number_of_operators(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_number_of_operators(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_operator_name_by_index(wf, op_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_operator_name_by_index(wf._internal_obj if wf is not None else None, utils.to_int32(op_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_set_name_input_pin(wf, op, pin, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_set_name_input_pin(wf._internal_obj if wf is not None else None, op._internal_obj if op is not None else None, utils.to_int32(pin), utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_set_name_output_pin(wf, op, pin, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_set_name_output_pin(wf._internal_obj if wf is not None else None, op._internal_obj if op is not None else None, utils.to_int32(pin), utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_rename_input_pin(wf, pin_name, new_pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_rename_input_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_char_ptr(new_pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_rename_output_pin(wf, pin_name, new_pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_rename_output_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_char_ptr(new_pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_erase_input_pin(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_erase_input_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_erase_output_pin(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_erase_output_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_has_input_pin(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_has_input_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_has_output_pin(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_has_output_pin(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_number_of_input(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_number_of_input(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_number_of_output(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_number_of_output(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_input_by_index(wf, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_input_by_index(wf._internal_obj if wf is not None else None, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_output_by_index(wf, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_output_by_index(wf._internal_obj if wf is not None else None, utils.to_int32(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_number_of_symbol(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_number_of_symbol(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_symbol_by_index(wf, symbol_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_symbol_by_index(wf._internal_obj if wf is not None else None, utils.to_int32(symbol_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_generate_all_derivatives_for(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_generate_all_derivatives_for(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_generate_derivatives_for(wf, pin_name, variable_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_generate_derivatives_for(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_char_ptr(variable_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_write_swf(wf, file_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_write_swf(wf._internal_obj if wf is not None else None, file_name, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_load_swf(wf, file_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_load_swf(wf._internal_obj if wf is not None else None, file_name, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_write_swf_utf8(wf, file_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_write_swf_utf8(wf._internal_obj if wf is not None else None, utils.to_char_ptr(file_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_load_swf_utf8(wf, file_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_load_swf_utf8(wf._internal_obj if wf is not None else None, utils.to_char_ptr(file_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_write_to_text(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_write_to_text(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_connect_dpf_type(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_DpfType(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value._internal_obj if value is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_int(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_int(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_int32(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_bool(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_bool(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_double(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_double(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.c_double(value) if isinstance(value, float) else value, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_string(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_string(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_char_ptr(value), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_string_with_size(wf, pin_name, value, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_string_with_size(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_char_ptr(value), utils.to_uint64(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_scoping(wf, pin_name, scoping):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Scoping(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), scoping._internal_obj if scoping is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_data_sources(wf, pin_name, dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_DataSources(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_streams(wf, pin_name, dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Streams(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_field(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Field(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value._internal_obj if value is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_collection(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Collection(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value._internal_obj if value is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_collection_as_vector(wf, pin_name, value):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Collection_as_vector(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value._internal_obj if value is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_meshed_region(wf, pin_name, mesh):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_MeshedRegion(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), mesh._internal_obj if mesh is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_property_field(wf, pin_name, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_PropertyField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_string_field(wf, pin_name, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_StringField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_custom_type_field(wf, pin_name, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_CustomTypeField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_support(wf, pin_name, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Support(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_cyclic_support(wf, pin_name, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_CyclicSupport(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_time_freq_support(wf, pin_name, support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_TimeFreqSupport(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_workflow(wf, pin_name, otherwf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Workflow(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), otherwf._internal_obj if otherwf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_remote_workflow(wf, pin_name, otherwf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_RemoteWorkflow(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), otherwf._internal_obj if otherwf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_vector_int(wf, pin_name, ptrValue, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_vector_int(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_int32_ptr(ptrValue), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_vector_double(wf, pin_name, ptrValue, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_vector_double(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_double_ptr(ptrValue), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_operator_output(wf, pin_name, value, output_pin):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_operator_output(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), value._internal_obj if value is not None else None, utils.to_int32(output_pin), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_external_data(wf, pin_name, dataSources):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_ExternalData(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), dataSources._internal_obj if dataSources is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_data_tree(wf, pin_name, dataTree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_DataTree(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), dataTree._internal_obj if dataTree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_any(wf, pin_name, any):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_Any(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), any._internal_obj if any is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_label_space(wf, pin_name, labelspace):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_LabelSpace(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), labelspace._internal_obj if labelspace is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_connect_generic_data_container(wf, pin_name, labelspace):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_connect_GenericDataContainer(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), labelspace._internal_obj if labelspace is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_fields_container(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_FieldsContainer(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_scopings_container(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_ScopingsContainer(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_field(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Field(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_scoping(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Scoping(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_time_freq_support(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_timeFreqSupport(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_meshes_container(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_meshesContainer(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_meshed_region(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_meshedRegion(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_result_info(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_resultInfo(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_property_field(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_propertyField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_any_support(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_anySupport(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_cyclic_support(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_CyclicSupport(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_data_sources(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_DataSources(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_streams(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Streams(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_workflow(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Workflow(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_external_data(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_ExternalData(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_as_any(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_as_any(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_int_collection(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_IntCollection(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_double_collection(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_DoubleCollection(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_operator(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Operator(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_string_field(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_StringField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_custom_type_field(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_CustomTypeField(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_custom_type_fields_container(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_CustomTypeFieldsContainer(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_data_tree(op, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_DataTree(op._internal_obj if op is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_generic_data_container(op, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_GenericDataContainer(op._internal_obj if op is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_unit(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_Unit(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_getoutput_string(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_string(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_getoutput_string_with_size(wf, pin_name, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_string_with_size(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), utils.to_uint64_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.string_at(res, size.val.value)
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def work_flow_getoutput_int(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_int(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_double(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_double(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_getoutput_bool(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getoutput_bool(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_has_output_when_evaluated(wf, pin_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_has_output_when_evaluated(wf._internal_obj if wf is not None else None, utils.to_char_ptr(pin_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_add_tag(wf, tag_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_add_tag(wf._internal_obj if wf is not None else None, utils.to_char_ptr(tag_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_has_tag(wf, tag_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_has_tag(wf._internal_obj if wf is not None else None, utils.to_char_ptr(tag_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_export_graphviz(wf, utf8_filename):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_export_graphviz(wf._internal_obj if wf is not None else None, utils.to_char_ptr(utf8_filename), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_export_json(wf, text, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_export_json(wf._internal_obj if wf is not None else None, utils.to_char_ptr_ptr(text), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_import_json(wf, text, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_import_json(wf._internal_obj if wf is not None else None, utils.to_char_ptr(text), utils.to_int32(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_make_from_template(template_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_make_from_template(utils.to_char_ptr(template_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_template_exists(template_name):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_template_exists(utils.to_char_ptr(template_name), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_get_operators_collection_for_input(wf, input_name, pin_indexes, size):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_get_operators_collection_for_input(wf._internal_obj if wf is not None else None, utils.to_char_ptr(input_name), utils.to_int32_ptr_ptr(pin_indexes), utils.to_int32_ptr(size), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_get_operator_for_output(wf, output_name, pin_index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_get_operator_for_output(wf._internal_obj if wf is not None else None, utils.to_char_ptr(output_name), utils.to_int32_ptr(pin_index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_get_client_id(wf):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_get_client_id(wf._internal_obj if wf is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_new_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_create_from_text_on_client(text, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_create_from_text_on_client(utils.to_char_ptr(text), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_copy_on_client(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_getCopy_on_client(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def work_flow_get_by_identifier_on_client(identifier, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.WorkFlow_get_by_identifier_on_client(utils.to_int32(identifier), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def workflow_create_connection_map_for_object(api_to_use):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.Workflow_create_connection_map_for_object(api_to_use._internal_obj if api_to_use is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

