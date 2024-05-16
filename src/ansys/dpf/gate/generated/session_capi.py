import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import session_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# Session
#-------------------------------------------------------------------------------

class SessionCAPI(session_abstract_api.SessionAbstractAPI):

	@staticmethod
	def init_session_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def session_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.sessionNew(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def delete_session(session):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.deleteSession(session._internal_obj if session is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def get_session_id(session):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.getSessionId(session._internal_obj if session is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def add_workflow(session, workflow_identifier, workflow):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addWorkflow(session._internal_obj if session is not None else None, utils.to_char_ptr(workflow_identifier), workflow._internal_obj if workflow is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def get_workflow(session, workflow_identifier):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.getWorkflow(session._internal_obj if session is not None else None, utils.to_char_ptr(workflow_identifier), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def get_workflow_by_index(session, index):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.getWorkflowByIndex(session._internal_obj if session is not None else None, utils.to_int32(index), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def flush_workflows(session):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.flushWorkflows(session._internal_obj if session is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def get_num_workflow(session):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.getNumWorkflow(session._internal_obj if session is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def set_logger(session, callback):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.setLogger(session._internal_obj if session is not None else None, callback, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def set_event_system(session, progress_callback, op_state_callback):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.setEventSystem(session._internal_obj if session is not None else None, progress_callback, op_state_callback, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_breakpoint(session, workflow, operator_ptr, isAfterExe):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addBreakpoint(session._internal_obj if session is not None else None, workflow._internal_obj if workflow is not None else None, operator_ptr._internal_obj if operator_ptr is not None else None, isAfterExe, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def remove_breakpoint(session, workflow, id):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.removeBreakpoint(session._internal_obj if session is not None else None, workflow._internal_obj if workflow is not None else None, utils.to_int32(id), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def resume(session):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.resume(session._internal_obj if session is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_event_handler(session, event_handler):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addEventHandler(session._internal_obj if session is not None else None, event_handler._internal_obj if event_handler is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def create_signal_emitter_in_session(session, identifier):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.createSignalEmitterInSession(session._internal_obj if session is not None else None, utils.to_char_ptr(identifier), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_external_event_handler(session, event_handler, cb):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addExternalEventHandler(session._internal_obj if session is not None else None, utils.to_void_ptr(event_handler), cb, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def notify_external_event_handler_destruction(event_handler):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.NotifyExternalEventHandlerDestruction(utils.to_void_ptr(event_handler), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_workflow_without_identifier(session, workflow):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addWorkflowWithoutIdentifier(session._internal_obj if session is not None else None, workflow._internal_obj if workflow is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		newres = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8") if res else None
		capi.dll.DataProcessing_String_post_event(res, ctypes.byref(errorSize), ctypes.byref(sError))
		return newres

	@staticmethod
	def emit_signal(eventEmitter, type, message):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.emitSignal(eventEmitter._internal_obj if eventEmitter is not None else None, utils.to_int32(type), utils.to_char_ptr(message), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_event_handler_type(session, type, datatree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addEventHandlerType(session._internal_obj if session is not None else None, utils.to_char_ptr(type), datatree._internal_obj if datatree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def add_signal_emitter_type(session, type, identifier, datatree):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.addSignalEmitterType(session._internal_obj if session is not None else None, utils.to_char_ptr(type), utils.to_char_ptr(identifier), datatree._internal_obj if datatree is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def session_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.sessionNew_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

