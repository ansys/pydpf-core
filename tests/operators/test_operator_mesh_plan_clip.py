import ansys.dpf.core as dpf
import conftest


def test_operator_mesh_plan_clip_rst(simple_bar):
    model = dpf.Model(simple_bar)
    main_mesh = model.metadata.meshed_region

    plane = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
    plane.append([0, 1, 0], 1)

    origin = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
    origin.append([0, 2.0, 0], 1)

    cut_mesh = dpf.operators.mesh.mesh_plan_clip(main_mesh, normal=plane, origin=origin).eval(2)
    node_scoping_ids = cut_mesh.nodes.scoping.ids
    assert len(node_scoping_ids) == 1331
    assert node_scoping_ids[-1] == 1331
    elements_scoping_ids = cut_mesh.elements.scoping.ids
    assert len(elements_scoping_ids) == 6000
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_2:
        assert elements_scoping_ids[-1] == 6000

    # Check clipping a field
    if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_8_2:
        disp = model.results.displacement.eval()[0]
        op = dpf.operators.mesh.mesh_plan_clip()
        op.inputs.mesh_or_field.connect(disp)
        op.inputs.normal.connect(plane)
        op.inputs.origin.connect(origin)
        field: dpf.Field = op.outputs.field()
        assert field.max().data[0] > 1.e-7
