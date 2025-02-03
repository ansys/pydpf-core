from ansys.dpf.gate.generated import field_definition_abstract_api
from ansys.dpf.gate import errors
#-------------------------------------------------------------------------------
# FieldDefinition
#-------------------------------------------------------------------------------

def _get_stub(server):
    return server.get_stub(FieldDefinitionGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class FieldDefinitionGRPCAPI(field_definition_abstract_api.FieldDefinitionAbstractAPI):
    STUBNAME = "field_def_stub"

    @staticmethod
    def init_field_definition_environment(object):
        from ansys.grpc.dpf import field_definition_pb2_grpc
        object._server.create_stub_if_necessary(FieldDefinitionGRPCAPI.STUBNAME, field_definition_pb2_grpc.FieldDefinitionServiceStub)
        object._deleter_func = (_get_stub(object._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def csfield_definition_fill_unit(fieldDef, symbol, size, homogeneity, factor, shift):
        symbol.set_str(_get_stub(fieldDef._server).List(fieldDef._internal_obj).unit.symbol)

    
    @staticmethod
    def csfield_definition_get_quantity_type(fieldDef, index):
        return _get_stub(fieldDef._server).List(fieldDef._internal_obj).quantity_types.quantity_types[index]
    
    @staticmethod
    def csfield_definition_set_quantity_type(fieldDef, quantityType):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, quantity_type=quantityType)

    @staticmethod
    def csfield_definition_get_num_available_quantity_types(fieldDef):
        return len(_get_stub(fieldDef._server).List(fieldDef._internal_obj).quantity_types.quantity_types)

    @staticmethod
    def csfield_definition_is_of_quantity_type(fieldDef, quantityType):
        return quantityType in _get_stub(fieldDef._server).List(fieldDef._internal_obj).quantity_types.quantity_types
        
    @staticmethod
    def csfield_definition_get_shell_layers(fieldDef):
        return _get_stub(fieldDef._server).List(fieldDef._internal_obj).shell_layers - 1
    
    @staticmethod
    def csfield_definition_fill_location(fieldDef, location, size):
        out = _get_stub(fieldDef._server).List(fieldDef._internal_obj)
        location.set_str(out.location.location)

    @staticmethod
    def csfield_definition_fill_name(fieldDef, name, size):
        out = _get_stub(fieldDef._server).List(fieldDef._internal_obj)
        if hasattr(out, "name"):
            name.set_str(out.name.string)

    @staticmethod
    def csfield_definition_fill_dimensionality(fieldDef, dim, nature, size_vsize):
        val = _get_stub(fieldDef._server).List(
            fieldDef._internal_obj
        ).dimensionnality  # typo exists on server side
        nature.set(val.nature)
        dim.set(val.size)

    @staticmethod
    def csfield_definition_set_unit(fieldDef, symbol, dummy, dummy1, dummy2, dummy3):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, unit=symbol)

    @staticmethod
    def csfield_definition_set_shell_layers(fieldDef, shellLayers):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, shell_layer=shellLayers+1)

    @staticmethod
    def csfield_definition_set_location(fieldDef, location):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, location=location)

    @staticmethod
    def csfield_definition_set_name(fieldDef, name):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, name=name)

    @staticmethod
    def csfield_definition_set_dimensionality(fieldDef, dim, ptrSize, size_vsize):
        FieldDefinitionGRPCAPI._modify_field_def(fieldDef, dimensionality=(dim,ptrSize))

    @staticmethod
    def field_definition_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.Empty()
        return _get_stub(client).Create(request)

    @staticmethod
    def _modify_field_def(
            fieldDef, unit=None, location=None, dimensionality=None, shell_layer=None, name=None, quantity_type=None
    ):
        from ansys.grpc.dpf import field_definition_pb2
        request = field_definition_pb2.FieldDefinitionUpdateRequest()
        request.field_definition.CopyFrom(fieldDef._internal_obj)
        if unit != None:
            request.unit_symbol.symbol = unit
        if location != None:
            request.location.location = location
        if dimensionality != None:
            request.dimensionnality.size.extend(dimensionality[1])
            request.dimensionnality.nature = dimensionality[0]
        if shell_layer != None:
            request.shell_layers = shell_layer
        if name != None:
            request.name.string = name
        if quantity_type != None:
            request.quantity_types.quantity_types.append(quantity_type)

        _get_stub(fieldDef._server).Update(request)
