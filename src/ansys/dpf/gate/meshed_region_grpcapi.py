from ansys.dpf.gate.generated import meshed_region_abstract_api
from ansys.dpf.gate import errors
# -------------------------------------------------------------------------------
# MeshedRegion
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(MeshedRegionGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class MeshedRegionGRPCAPI(meshed_region_abstract_api.MeshedRegionAbstractAPI):
    STUBNAME = "meshed_region_stub"

    @staticmethod
    def init_meshed_region_environment(obj):
        from ansys.grpc.dpf import meshed_region_pb2_grpc
        obj._server.create_stub_if_necessary(MeshedRegionGRPCAPI.STUBNAME,
                                             meshed_region_pb2_grpc.MeshedRegionServiceStub)
        obj._deleter_func = (_get_stub(obj._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def meshed_region_new_on_client(client):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.CreateRequest()
        return _get_stub(client).Create(request)

    @staticmethod
    def meshed_region_reserve(meshedRegion, numNodes, numElements):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.CreateRequest()
        if numNodes:
            request.num_nodes_reserved = numNodes
        if numElements:
            request.num_elements_reserved = numElements
        return _get_stub(meshedRegion._server).Create(request)

    @staticmethod
    def meshed_region_get_num_nodes(meshedRegion):
        return MeshedRegionGRPCAPI.list(meshedRegion).num_nodes

    @staticmethod
    def meshed_region_get_num_elements(meshedRegion):
        return MeshedRegionGRPCAPI.list(meshedRegion).num_element

    @staticmethod
    def meshed_region_get_num_faces(meshedRegion):
        return MeshedRegionGRPCAPI.list(meshedRegion).num_faces

    @staticmethod
    def meshed_region_get_shared_nodes_scoping(meshedRegion):
        from ansys.grpc.dpf import meshed_region_pb2
        from ansys.dpf.gate.common import locations
        request = meshed_region_pb2.GetScopingRequest(mesh=meshedRegion._internal_obj)
        request.loc.location = locations.nodal
        return _get_stub(meshedRegion._server).GetScoping(request)

    @staticmethod
    def meshed_region_get_shared_elements_scoping(meshedRegion):
        from ansys.grpc.dpf import meshed_region_pb2
        from ansys.dpf.gate.common import locations
        request = meshed_region_pb2.GetScopingRequest(mesh=meshedRegion._internal_obj)
        request.loc.location = locations.elemental
        return _get_stub(meshedRegion._server).GetScoping(request)

    @staticmethod
    def meshed_region_get_shared_faces_scoping(meshedRegion):
        from ansys.grpc.dpf import meshed_region_pb2
        from ansys.dpf.gate.common import locations
        request = meshed_region_pb2.GetScopingRequest(mesh=meshedRegion._internal_obj)
        request.loc.location = locations.elemental_nodal
        return _get_stub(meshedRegion._server).GetScoping(request)

    @staticmethod
    def list(meshedRegion):
        return _get_stub(meshedRegion._server).List(meshedRegion._internal_obj)

    @staticmethod
    def meshed_region_get_unit(meshedRegion):
        return MeshedRegionGRPCAPI.list(meshedRegion).unit

    @staticmethod
    def meshed_region_get_has_solid_region(meshedRegion):
        return MeshedRegionGRPCAPI.list(
            meshedRegion).element_shape_info.has_solid_elements

    @staticmethod
    def meshed_region_get_has_shell_region(meshedRegion):
        return MeshedRegionGRPCAPI.list(
            meshedRegion).element_shape_info.has_shell_elements

    @staticmethod
    def meshed_region_get_has_point_region(meshedRegion):
        return MeshedRegionGRPCAPI.list(
            meshedRegion).element_shape_info.has_point_elements

    @staticmethod
    def meshed_region_get_has_beam_region(meshedRegion):
        return MeshedRegionGRPCAPI.list(
            meshedRegion).element_shape_info.has_beam_elements

    @staticmethod
    def meshed_region_get_node_id(meshedRegion, index):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        return _get_stub(meshedRegion._server).GetNode(request).id

    @staticmethod
    def meshed_region_get_node_index(meshedRegion, id):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.id = id
        return _get_stub(meshedRegion._server).GetNode(request).index

    @staticmethod
    def meshed_region_get_element_id(meshedRegion, index):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        return _get_stub(meshedRegion._server).GetElement(request).id

    @staticmethod
    def meshed_region_get_element_index(meshedRegion, id):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.id = id
        return _get_stub(meshedRegion._server).GetElement(request).index

    @staticmethod
    def meshed_region_get_num_nodes_of_element(meshedRegion, index):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        element = _get_stub(meshedRegion._server).GetElement(request)
        return len(element.nodes)

    @staticmethod
    def meshed_region_get_node_id_of_element(meshedRegion, eidx, nidx):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = eidx
        element = _get_stub(meshedRegion._server).GetElement(request)
        return element.nodes[nidx].id

    @staticmethod
    def meshed_region_get_node_coord(meshedRegion, index, coordinate):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        node = _get_stub(meshedRegion._server).GetNode(request)
        return node.coordinates[coordinate]

    @staticmethod
    def meshed_region_get_element_type(meshedRegion, id, type, index):
        from ansys.grpc.dpf import meshed_region_pb2
        from ansys.dpf.gate.common import elemental_property_type_dict
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        request.id = id
        if hasattr(request, "property_name"):
            request.property_name.property_name = "eltype"
        else:
            if "eltype" in elemental_property_type_dict:
                request.property = meshed_region_pb2.ElementalPropertyType.Value(
                    elemental_property_type_dict["eltype"]
                )
            else:
                raise ValueError(type + " property is not supported")
        prop = _get_stub(meshedRegion._server).GetElementalProperty(request).prop
        type.set(prop)

    @staticmethod
    def meshed_region_get_element_shape(meshedRegion, id, shape, index):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.index = index
        if hasattr(request, "property_name"):
            request.property_name.property_name = "elshape"
        else:
            from ansys.dpf.gate.common import elemental_property_type_dict
            if "elshape" in elemental_property_type_dict:
                request.property = meshed_region_pb2.ElementalPropertyType.Value(
                    elemental_property_type_dict["elshape"]
                )
            else:
                raise ValueError(type + " property is not supported")
        prop = _get_stub(meshedRegion._server).GetElementalProperty(request).prop
        shape.set(prop)

    @staticmethod
    def update(meshedRegion, request):
        return _get_stub(meshedRegion._server).UpdateRequest(request)

    @staticmethod
    def meshed_region_set_unit(meshedRegion, unit):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.UpdateMeshedRegionRequest()
        request.meshed_region.CopyFrom(meshedRegion._internal_obj)
        request.unit = unit
        return MeshedRegionGRPCAPI.update(meshedRegion, request)

    @staticmethod
    def get_named_selections(meshedRegion):
        from ansys.grpc.dpf import meshed_region_pb2
        if hasattr(_get_stub(meshedRegion._server), "ListNamedSelections"):
            request = meshed_region_pb2.ListNamedSelectionsRequest()
            request.mesh.CopyFrom(meshedRegion._internal_obj)
            res = _get_stub(meshedRegion._server).ListNamedSelections(request).named_selections
        else:
            res = MeshedRegionGRPCAPI.list(meshedRegion).named_selections
        return res

    @staticmethod
    def meshed_region_get_num_available_named_selection(meshedRegion):
        return len(MeshedRegionGRPCAPI.get_named_selections(meshedRegion))

    @staticmethod
    def meshed_region_get_named_selection_name(meshedRegion, index):
        return MeshedRegionGRPCAPI.get_named_selections(meshedRegion)[index]

    @staticmethod
    def meshed_region_get_named_selection_scoping(meshedRegion, name):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.GetScopingRequest(mesh=meshedRegion._internal_obj)
        request.named_selection = name
        return _get_stub(meshedRegion._server).GetScoping(request)

    @staticmethod
    def meshed_region_set_named_selection_scoping(meshedRegion, name, scoping):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.SetNamedSelectionRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.named_selection = name
        request.scoping.CopyFrom(scoping._internal_obj)
        return _get_stub(meshedRegion._server).SetNamedSelection(request)

    @staticmethod
    def meshed_region_add_node(meshedRegion, xyz, id):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.AddRequest(mesh=meshedRegion._internal_obj)
        node_request = meshed_region_pb2.NodeRequest(id=id)
        node_request.coordinates.extend(xyz)
        request.nodes.append(node_request)
        _get_stub(meshedRegion._server).Add(request)

    @staticmethod
    def meshed_region_add_element_by_shape(meshedRegion, id, size, conn, shape):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.AddRequest(mesh=meshedRegion._internal_obj)
        element_request = meshed_region_pb2.ElementRequest(id=id)
        element_request.connectivity.extend(conn)
        element_request.shape = shape
        request.elements.extend([element_request])
        _get_stub(meshedRegion._server).Add(request)

    @staticmethod
    def meshed_region_get_property_field(meshedRegion, property_type):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        if hasattr(request, "property_type"):
            request.property_type.property_name.property_name = property_type
        else:
            from ansys.dpf.gate.common import nodal_property_type_dict, elemental_property_type_dict
            if property_type in nodal_property_type_dict:
                request.nodal_property = meshed_region_pb2.NodalPropertyType.Value(
                    nodal_property_type_dict[property_type])
            elif property_type in elemental_property_type_dict:
                request.elemental_property = meshed_region_pb2.ElementalPropertyType.Value(
                    elemental_property_type_dict[property_type])
            else:
                raise ValueError(property_type + " property is not supported")
        return _get_stub(meshedRegion._server).ListProperty(request)

    @staticmethod
    def meshed_region_has_property_field(meshedRegion, property_type):
        return property_type in MeshedRegionGRPCAPI.list(meshedRegion).available_prop

    @staticmethod
    def meshed_region_get_num_available_property_field(meshedRegion):
        return len(MeshedRegionGRPCAPI.list(meshedRegion).available_prop)

    @staticmethod
    def meshed_region_get_property_field_name(meshedRegion, index):
        property_type = MeshedRegionGRPCAPI.list(meshedRegion).available_prop[index]
        return property_type

    @staticmethod
    def meshed_region_set_property_field(meshedRegion, name, prop_field):
        from ansys.grpc.dpf import meshed_region_pb2
        request = meshed_region_pb2.SetFieldRequest()
        request.mesh.CopyFrom(meshedRegion._internal_obj)
        request.property_type.property_name.property_name = name
        request.field.CopyFrom(prop_field._internal_obj)
        return _get_stub(meshedRegion._server).SetField(request)

    @staticmethod
    def meshed_region_get_coordinates_field(meshedRegion):
        return MeshedRegionGRPCAPI.meshed_region_get_property_field(meshedRegion,
                                                                    "coordinates")

    @staticmethod
    def meshed_region_set_coordinates_field(meshedRegion, field):
        return MeshedRegionGRPCAPI.meshed_region_set_property_field(meshedRegion, "coordinates",
                                                                    field)
