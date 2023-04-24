from ansys.dpf.gate.generated import operator_config_abstract_api
from ansys.dpf.gate import errors
# -------------------------------------------------------------------------------
# OperatorConfig
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(OperatorConfigGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class OperatorConfigGRPCAPI(operator_config_abstract_api.OperatorConfigAbstractAPI):
    STUBNAME = "operator_config_stub"

    @staticmethod
    def init_operator_config_environment(obj):
        from ansys.grpc.dpf import operator_config_pb2_grpc
        obj._server.create_stub_if_necessary(OperatorConfigGRPCAPI.STUBNAME,
                                             operator_config_pb2_grpc.OperatorConfigServiceStub)
        obj._deleter_func = (_get_stub(obj._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def operator_config_default_new_on_client(client, operator_name):
        from ansys.grpc.dpf import operator_config_pb2
        request = operator_config_pb2.CreateRequest()
        request.operator_name.operator_name = operator_name
        return _get_stub(client).Create(request)

    @staticmethod
    def operator_config_empty_new_on_client(client):
        from ansys.grpc.dpf import operator_config_pb2
        request = operator_config_pb2.CreateRequest()
        return _get_stub(client).Create(request)

    @staticmethod
    def operator_config_get_int(config, option):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return int(tmp.options[option].value_str)

    @staticmethod
    def operator_config_get_double(config, option):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return float(tmp.options[option].value_str)

    @staticmethod
    def operator_config_get_bool(config, option):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return bool(tmp.options[option].value_str)

    @staticmethod
    def update_init(config, option_name):
        from ansys.grpc.dpf import operator_config_pb2
        request = operator_config_pb2.UpdateRequest()
        request.config.CopyFrom(config._internal_obj)
        option_request = operator_config_pb2.ConfigOption()
        option_request.option_name = option_name
        return request, option_request

    @staticmethod
    def update(config, request, option_request):
        request.options.extend([option_request])
        _get_stub(config._server).Update(request)

    @staticmethod
    def operator_config_set_int(config, option_name, value):
        request, option_request = OperatorConfigGRPCAPI.update_init(config, option_name)
        option_request.int = value
        OperatorConfigGRPCAPI.update(config, request, option_request)

    @staticmethod
    def operator_config_set_double(config, option_name, value):
        request, option_request = OperatorConfigGRPCAPI.update_init(config, option_name)
        option_request.double = value
        OperatorConfigGRPCAPI.update(config, request, option_request)

    @staticmethod
    def operator_config_set_bool(config, option_name, value):
        request, option_request = OperatorConfigGRPCAPI.update_init(config, option_name)
        option_request.bool = value
        OperatorConfigGRPCAPI.update(config, request, option_request)

    @staticmethod
    def get_list(config):
        return _get_stub(config._server).List(config._internal_obj)

    @staticmethod
    def operator_config_get_num_config(config):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return len(tmp.options)

    @staticmethod
    def operator_config_get_config_option_name(config, index):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return tmp.options[index].option_name

    @staticmethod
    def operator_config_get_config_option_printable_value(config, index):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return tmp.options[index].value_str

    @staticmethod
    def operator_config_has_option(config, option):
        tmp = OperatorConfigGRPCAPI.get_list(config)
        return option in tmp.options
