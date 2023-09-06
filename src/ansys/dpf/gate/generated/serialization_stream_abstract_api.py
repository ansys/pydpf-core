#-------------------------------------------------------------------------------
# SerializationStream
#-------------------------------------------------------------------------------

class SerializationStreamAbstractAPI:
	@staticmethod
	def init_serialization_stream_environment(object):
		pass

	@staticmethod
	def finish_serialization_stream_environment(object):
		pass

	@staticmethod
	def serialization_stream_get_output_string(stream, dataSize):
		raise NotImplementedError

