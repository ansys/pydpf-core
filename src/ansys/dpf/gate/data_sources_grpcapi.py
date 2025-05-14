from ansys.dpf.gate.generated import data_sources_abstract_api
from ansys.dpf.gate import errors
# -------------------------------------------------------------------------------
# DataSources
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(DataSourcesGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class DataSourcesGRPCAPI(data_sources_abstract_api.DataSourcesAbstractAPI):
    STUBNAME = "data_sources_stub"

    @staticmethod
    def init_data_sources_environment(obj):
        from ansys.grpc.dpf import data_sources_pb2_grpc
        obj._server.create_stub_if_necessary(DataSourcesGRPCAPI.STUBNAME,
                                             data_sources_pb2_grpc.DataSourcesServiceStub)
        obj._deleter_func = (_get_stub(obj._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def data_sources_new_on_client(server):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.Empty()
        return _get_stub(server).Create(request)

    @staticmethod
    def data_sources_delete(dataSources):
        _get_stub(dataSources._server).Delete(dataSources._internal_obj)

    @staticmethod
    def data_sources_set_result_file_path_utf8(dataSources, name):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_set_result_file_path_with_key_utf8(dataSources, name, sKey):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.key = sKey
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_set_domain_result_file_path_utf8(dataSources, name, id):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.domain.domain_path = True
        request.domain.domain_id = id
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_set_domain_result_file_path_with_key_utf8(dataSources, name, key, domain_id):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.result_path = True
        request.domain.domain_path = True
        request.domain.domain_id = domain_id
        request.path = name
        request.key = key
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_add_file_path_utf8(dataSources, name):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_add_file_path_with_key_utf8(dataSources, name, sKey):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.key = sKey
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_add_domain_file_path_with_key_utf8(dataSources, name, sKey, id):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.key = sKey
        request.path = name
        request.domain.domain_path = True
        request.domain.domain_id = id
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_add_file_path_for_specified_result_utf8(dataSources, name, sKey, sResultKey):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateRequest()
        request.key = sKey
        request.result_key = sResultKey
        request.path = name
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).Update(request)

    @staticmethod
    def data_sources_add_upstream_data_sources(dataSources, upstreamDataSources):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstreamDataSources._internal_obj)
        request.data_sources.CopyFrom(dataSources._internal_obj)
        _get_stub(dataSources._server).UpdateUpstream(request)

    @staticmethod
    def data_sources_add_upstream_data_sources_for_specified_result(dataSources,
                                                                    upstreamDataSources,
                                                                    sResultKey):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstreamDataSources._internal_obj)
        request.data_sources.CopyFrom(dataSources._internal_obj)
        request.result_key = sResultKey
        _get_stub(dataSources._server).UpdateUpstream(request)

    @staticmethod
    def data_sources_add_upstream_domain_data_sources(dataSources, upstreamDataSources, id):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateUpstreamRequest()
        request.upstream_data_sources.CopyFrom(upstreamDataSources._internal_obj)
        request.data_sources.CopyFrom(dataSources._internal_obj)
        request.domain.domain_path = True
        request.domain.domain_id = id
        _get_stub(dataSources._server).UpdateUpstream(request)

    @staticmethod
    def data_sources_register_namespace(dataSources, result_key, ns):
        from ansys.grpc.dpf import data_sources_pb2
        request = data_sources_pb2.UpdateNamespaceRequest()
        request.data_sources.CopyFrom(dataSources._internal_obj)
        request.key = result_key
        request.namespace = ns
        _get_stub(dataSources._server).UpdateNamespace(request)

    @staticmethod
    def data_sources_get_result_key(dataSources):
        response = _get_stub(dataSources._server).List(dataSources._internal_obj)
        return response.result_key

    @staticmethod
    def data_sources_get_num_keys(dataSources):
        response = _get_stub(dataSources._server).List(dataSources._internal_obj)
        if dataSources._server.meet_version("4.0"):
            return len(response.keys)
        else:
            return len(list(response.paths.keys()))

    @staticmethod
    def data_sources_get_key(dataSources, index, num_path):
        response = _get_stub(dataSources._server).List(dataSources._internal_obj)
        if dataSources._server.meet_version("4.0"):
            num_path.set(len(response.paths[response.keys[index]].paths))
            return response.keys[index]
        else :
            keys = list(response.paths.keys())
            num_path.set(len(response.paths[keys[index]].paths))
            return keys[index]

    @staticmethod
    def data_sources_get_path(dataSources, key, index):
        response = _get_stub(dataSources._server).List(dataSources._internal_obj)
        return list(response.paths[key].paths)[index]

    @staticmethod
    def data_sources_get_namespace(dataSources, key):
        response = _get_stub(dataSources._server).List(dataSources._internal_obj)
        return response.namespaces[key]