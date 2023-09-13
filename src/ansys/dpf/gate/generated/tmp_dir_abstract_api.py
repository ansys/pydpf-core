#-------------------------------------------------------------------------------
# TmpDir
#-------------------------------------------------------------------------------

class TmpDirAbstractAPI:
	@staticmethod
	def init_tmp_dir_environment(object):
		pass

	@staticmethod
	def finish_tmp_dir_environment(object):
		pass

	@staticmethod
	def tmp_dir_get_dir():
		raise NotImplementedError

	@staticmethod
	def tmp_dir_erase():
		raise NotImplementedError

	@staticmethod
	def tmp_dir_get_dir_on_client(client):
		raise NotImplementedError

