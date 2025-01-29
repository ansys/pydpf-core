#-------------------------------------------------------------------------------
# Client
#-------------------------------------------------------------------------------

class ClientAbstractAPI:
	@staticmethod
	def init_client_environment(object):
		pass

	@staticmethod
	def finish_client_environment(object):
		pass

	@staticmethod
	def client_new(ip, port):
		raise NotImplementedError

	@staticmethod
	def client_new_full_address(address):
		raise NotImplementedError

	@staticmethod
	def client_get_full_address(client):
		raise NotImplementedError

	@staticmethod
	def client_get_protocol_name(client):
		raise NotImplementedError

	@staticmethod
	def client_has_local_server(client):
		raise NotImplementedError

	@staticmethod
	def client_set_local_server(client, server_streams):
		raise NotImplementedError

	@staticmethod
	def client_get_local_server(client):
		raise NotImplementedError

