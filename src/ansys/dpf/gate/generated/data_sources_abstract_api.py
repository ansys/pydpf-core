#-------------------------------------------------------------------------------
# DataSources
#-------------------------------------------------------------------------------

class DataSourcesAbstractAPI:
	@staticmethod
	def init_data_sources_environment(object):
		pass

	@staticmethod
	def finish_data_sources_environment(object):
		pass

	@staticmethod
	def data_sources_new(operatorName):
		raise NotImplementedError

	@staticmethod
	def data_sources_delete(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_result_file_path(dataSources, name):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_result_file_path_with_key(dataSources, name, sKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_domain_result_file_path_with_key(dataSources, name, sKey, id):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path(dataSources, name):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path_with_key(dataSources, name, sKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path_for_specified_result(dataSources, name, sKey, sResultKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_result_file_path_utf8(dataSources, name):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_result_file_path_with_key_utf8(dataSources, name, sKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_domain_result_file_path_utf8(dataSources, name, id):
		raise NotImplementedError

	@staticmethod
	def data_sources_set_domain_result_file_path_with_key_utf8(dataSources, name, sKey, id):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path_utf8(dataSources, name):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path_with_key_utf8(dataSources, name, sKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_domain_file_path_with_key_utf8(dataSources, name, sKey, id):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_file_path_for_specified_result_utf8(dataSources, name, sKey, sResultKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_upstream_data_sources(dataSources, upstreamDataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_upstream_data_sources_for_specified_result(dataSources, upstreamDataSources, sResultKey):
		raise NotImplementedError

	@staticmethod
	def data_sources_add_upstream_domain_data_sources(dataSources, upstreamDataSources, id):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_result_key(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_result_key_by_index(dataSources, index):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_num_result_keys(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_num_keys(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_key(dataSources, index, num_path):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_path(dataSources, key, index):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_namespace(dataSources, key):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_new_path_collection_for_key(dataSources, key):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_new_collection_for_results_path(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_size(dataSources):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_path_by_path_index(dataSources, index):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_key_by_path_index(dataSources, index):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_label_space_by_path_index(dataSources, index):
		raise NotImplementedError

	@staticmethod
	def data_sources_register_namespace(dataSources, result_key, ns):
		raise NotImplementedError

	@staticmethod
	def data_sources_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_sources_get_copy(id, client):
		raise NotImplementedError

