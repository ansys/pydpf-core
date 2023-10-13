#-------------------------------------------------------------------------------
# Streams
#-------------------------------------------------------------------------------

class StreamsAbstractAPI:
	@staticmethod
	def init_streams_environment(object):
		pass

	@staticmethod
	def finish_streams_environment(object):
		pass

	@staticmethod
	def streams_delete(streams):
		raise NotImplementedError

	@staticmethod
	def streams_release_handles(streams):
		raise NotImplementedError

	@staticmethod
	def streams_new(dataSources):
		raise NotImplementedError

	@staticmethod
	def streams_add_external_stream(streams, streamTypeName, filePath, releaseFileFunc, deleteFunc, var1):
		raise NotImplementedError

	@staticmethod
	def streams_get_external_stream(streams, key):
		raise NotImplementedError

	@staticmethod
	def streams_add_external_stream_with_label_space(streams, streamTypeName, filePath, releaseFileFunc, deleteFunc, var1, labelspace):
		raise NotImplementedError

	@staticmethod
	def streams_get_external_stream_with_label_space(streams, labelspace):
		raise NotImplementedError

	@staticmethod
	def streams_get_data_sources(streams):
		raise NotImplementedError

	@staticmethod
	def streams_get_copy(id, client):
		raise NotImplementedError

