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
	def fbs_ref_new_with_fbs_client(client, req_slice):
		raise NotImplementedError

	@staticmethod
	def fbs_client_new(channel_address):
		raise NotImplementedError

	@staticmethod
	def fbs_client_new_with_channel(channel):
		raise NotImplementedError

	@staticmethod
	def any_get_as_fbs_ref(obj, client, channel_address, req_slice, req_offset):
		raise NotImplementedError

	@staticmethod
	def fbs_client_start_or_get_thread_server(get_existing, ip, port, address):
		raise NotImplementedError

	@staticmethod
	def fbs_get_bytes_buffer_from_slice(req_slice, req_offset, size_out):
		raise NotImplementedError

	@staticmethod
	def fbs_create_slice_from_bytes_buffer(req_slice, size):
		raise NotImplementedError

	@staticmethod
	def fbs_delete_channel(client):
		raise NotImplementedError

	@staticmethod
	def fbs_delete_slice(req_slice):
		raise NotImplementedError

	@staticmethod
	def fbs_ref_new_with_fbs_client_on_client(client, fbs_client, req_slice):
		raise NotImplementedError

	@staticmethod
	def fbs_client_new_on_client(client, channel_address):
		raise NotImplementedError

	@staticmethod
	def fbs_client_start_or_get_thread_server_on_client(client, get_existing, ip, port, address):
		raise NotImplementedError

