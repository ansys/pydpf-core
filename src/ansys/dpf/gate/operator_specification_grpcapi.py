from ansys.dpf.gate.generated import operator_specification_abstract_api
from ansys.dpf.gate import errors
# -------------------------------------------------------------------------------
# OperatorSpecification
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(OperatorSpecificationGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class OperatorSpecificationGRPCAPI(
    operator_specification_abstract_api.OperatorSpecificationAbstractAPI):
    STUBNAME = "operator_specification_stub"

    @staticmethod
    def init_operator_specification_environment(obj):
        from ansys.grpc.dpf import base_pb2_grpc
        obj._server.create_stub_if_necessary(OperatorSpecificationGRPCAPI.STUBNAME,
                                             base_pb2_grpc.BaseServiceStub)

    @staticmethod
    def operator_specification_new_on_client(client, op_name):
        from ansys.dpf.gate.operator_grpcapi import _get_stub as _get_operator_stub
        from ansys.grpc.dpf import operator_pb2
        request = operator_pb2.Operator()
        if hasattr(op_name, "_internal_obj"):
            return op_name._internal_obj.spec
        elif client.meet_version("3.0"):
            request.name = op_name
            stub = _get_operator_stub(client)
            list = stub.List(request)
            return list.spec
        else:
            from ansys.dpf.gate import operator_grpcapi, object_handler, data_processing_grpcapi
            return object_handler.ObjHandler(
                data_processing_grpcapi.DataProcessingGRPCAPI,
                operator_grpcapi.OperatorGRPCAPI.operator_new_on_client(op_name, client)
            )._internal_obj.spec

    @staticmethod
    def operator_specification_get_description(specification):
        return specification._internal_obj.description

    @staticmethod
    def operator_specification_set_description(specification, text):
        specification._internal_obj.description = text

    @staticmethod
    def operator_specification_get_num_pins(specification, binput):
        if binput:
            return len(specification._internal_obj.map_input_pin_spec)
        else:
            return len(specification._internal_obj.map_output_pin_spec)

    @staticmethod
    def operator_specification_get_pin_name(specification, binput, numPin):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].name
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].name

    @staticmethod
    def operator_specification_get_pin_num_type_names(specification, binput, numPin):
        if binput:
            return len(specification._internal_obj.map_input_pin_spec[numPin].type_names)
        else:
            return len(specification._internal_obj.map_output_pin_spec[numPin].type_names)

    @staticmethod
    def operator_specification_fill_pin_numbers(specification, binput, pins):
        if binput:
            return pins.set([key for key in specification._internal_obj.map_input_pin_spec])
        else:
            return pins.set([key for key in specification._internal_obj.map_output_pin_spec])

    @staticmethod
    def operator_specification_get_pin_type_name(specification, binput, numPin, numType):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].type_names[numType]
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].type_names[numType]

    @staticmethod
    def operator_specification_get_pin_num_aliases(specification, binput, numPin):
        if not hasattr(specification._internal_obj.map_input_pin_spec[numPin], "aliases"):
            return 0
        if binput:
            return len(specification._internal_obj.map_input_pin_spec[numPin].aliases)
        else:
            return len(specification._internal_obj.map_output_pin_spec[numPin].aliases)

    @staticmethod
    def operator_specification_get_pin_alias(specification, binput, numPin, numAlias):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].aliases[numAlias]
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].aliases[numAlias]

    @staticmethod
    def operator_specification_get_pin_derived_class_type_name(specification, binput, numPin):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].name_derived_class
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].name_derived_class

    @staticmethod
    def operator_specification_is_pin_optional(specification, binput, numPin):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].optional
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].optional

    @staticmethod
    def operator_specification_get_pin_document(specification, binput, numPin):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].document
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].document

    @staticmethod
    def operator_specification_is_pin_ellipsis(specification, binput, numPin):
        if binput:
            return specification._internal_obj.map_input_pin_spec[numPin].ellipsis
        else:
            return specification._internal_obj.map_output_pin_spec[numPin].ellipsis

    @staticmethod
    def operator_specification_get_properties(specification, prop):
        return specification._internal_obj.properties[prop]

    @staticmethod
    def operator_specification_get_num_properties(specification):
        if hasattr(specification._internal_obj, "properties"):
            return len(specification._internal_obj.properties)
        else:
            return 0

    @staticmethod
    def operator_specification_get_property_key(specification, index):
        return list(specification._internal_obj.properties.keys())[index]

    @staticmethod
    def operator_specification_get_num_config_options(specification):
        return len(specification._internal_obj.config_spec.config_options_spec)

    @staticmethod
    def operator_specification_get_config_name(specification, numOption):
        option = specification._internal_obj.config_spec.config_options_spec[numOption]
        return option.name

    @staticmethod
    def operator_specification_get_config_num_type_names(specification, numOption):
        option = specification._internal_obj.config_spec.config_options_spec[numOption]
        return len(option.type_names)

    @staticmethod
    def operator_specification_get_config_type_name(specification, numOption, numType):
        option = specification._internal_obj.config_spec.config_options_spec[numOption]
        return option.type_names[numType]

    @staticmethod
    def operator_specification_get_config_printable_default_value(specification, numOption):
        option = specification._internal_obj.config_spec.config_options_spec[numOption]
        return option.default_value_str

    @staticmethod
    def operator_specification_get_config_description(specification, numOption):
        option = specification._internal_obj.config_spec.config_options_spec[numOption]
        return option.document
