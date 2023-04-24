#-------------------------------------------------------------------------------
# Session
#-------------------------------------------------------------------------------

class SessionAbstractAPI:
	@staticmethod
	def init_session_environment(object):
		pass

	@staticmethod
	def finish_session_environment(object):
		pass

	@staticmethod
	def session_new():
		raise NotImplementedError

	@staticmethod
	def delete_session(session):
		raise NotImplementedError

	@staticmethod
	def get_session_id(session):
		raise NotImplementedError

	@staticmethod
	def add_workflow(session, workflow_identifier, workflow):
		raise NotImplementedError

	@staticmethod
	def get_workflow(session, workflow_identifier):
		raise NotImplementedError

	@staticmethod
	def get_workflow_by_index(session, index):
		raise NotImplementedError

	@staticmethod
	def flush_workflows(session):
		raise NotImplementedError

	@staticmethod
	def get_num_workflow(session):
		raise NotImplementedError

	@staticmethod
	def set_logger(session, callback):
		raise NotImplementedError

	@staticmethod
	def set_event_system(session, progress_callback, op_state_callback):
		raise NotImplementedError

	@staticmethod
	def add_breakpoint(session, workflow, operator_ptr, isAfterExe):
		raise NotImplementedError

	@staticmethod
	def remove_breakpoint(session, workflow, id):
		raise NotImplementedError

	@staticmethod
	def resume(session):
		raise NotImplementedError

	@staticmethod
	def add_event_handler(session, event_handler):
		raise NotImplementedError

	@staticmethod
	def create_signal_emitter_in_session(session, identifier):
		raise NotImplementedError

	@staticmethod
	def add_external_event_handler(session, event_handler, cb):
		raise NotImplementedError

	@staticmethod
	def notify_external_event_handler_destruction(event_handler):
		raise NotImplementedError

	@staticmethod
	def add_workflow_without_identifier(session, workflow):
		raise NotImplementedError

	@staticmethod
	def emit_signal(eventEmitter, type, message):
		raise NotImplementedError

	@staticmethod
	def add_event_handler_type(session, type, datatree):
		raise NotImplementedError

	@staticmethod
	def add_signal_emitter_type(session, type, identifier, datatree):
		raise NotImplementedError

	@staticmethod
	def session_new_on_client(client):
		raise NotImplementedError

