#-------------------------------------------------------------------------------
# FbsRef
#-------------------------------------------------------------------------------

class FbsRefAbstractAPI:
	@staticmethod
	def init_fbs_ref_environment(object):
		pass

	@staticmethod
	def finish_fbs_ref_environment(object):
		pass

	@staticmethod
	def fbs_ref_new(client, channel_address, req_slice, req_offset):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_get_from_db(id):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_get_id(obj):
		raise NotImplementedError

	@staticmethod
	def any_get_as_fbs_ref(obj, client, channel_address, req_slice, req_offset):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_start_or_get_thread_server(get_existing, ip, port, address):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_new_on_client(client, channel, channel_address, req_slice, req_offset):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_start_or_get_thread_server_on_client(client, get_existing, ip, port, address):
		raise NotImplementedError

