#-------------------------------------------------------------------------------
# RemoteOperator
#-------------------------------------------------------------------------------

class RemoteOperatorAbstractAPI:
	@staticmethod
	def init_remote_operator_environment(object):
		pass

	@staticmethod
	def finish_remote_operator_environment(object):
		pass

	@staticmethod
	def remote_operator_new(streams, remoteId):
		raise NotImplementedError

	@staticmethod
	def remote_operator_get_streams(remote_wf):
		raise NotImplementedError

	@staticmethod
	def remote_operator_get_operator_id(remote_wf):
		raise NotImplementedError

	@staticmethod
	def remote_operator_hold_streams(wf, streams):
		raise NotImplementedError

