#-------------------------------------------------------------------------------
# RemoteWorkflow
#-------------------------------------------------------------------------------

class RemoteWorkflowAbstractAPI:
	@staticmethod
	def init_remote_workflow_environment(object):
		pass

	@staticmethod
	def finish_remote_workflow_environment(object):
		pass

	@staticmethod
	def remote_workflow_new(streams, remoteId):
		raise NotImplementedError

	@staticmethod
	def remote_workflow_get_workflow_id(remote_wf):
		raise NotImplementedError

	@staticmethod
	def remote_workflow_get_streams(remote_wf):
		raise NotImplementedError

	@staticmethod
	def remote_work_flow_delete(remote_wf):
		raise NotImplementedError

