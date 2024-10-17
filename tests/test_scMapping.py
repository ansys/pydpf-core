from ast import operator
import os

import pytest

from ansys.dpf import core as dpf
from pytest import approx
import copy

from ansys.dpf.core.scopings_container import ScopingsContainer


class test_utils:
    ABSTOL = 1e-14
    RELTOL = 1e-2

    @staticmethod
    def get_sq_mesh(NX: int, NY: int, Ax: float):
        EX = NX - 1
        EY = NY - 1
        numNode = NX * NY
        numElem = EX * EY
        ref_mesh = dpf.MeshedRegion(num_nodes=numNode, num_elements=numElem)
        for j in range(NY):
            for i in range(NX):
                ref_mesh.nodes.add_node(NX * j + i + 1, [Ax * i, Ax * j, 0.0])

        for j in range(EY):
            for i in range(EX):
                ref_mesh.elements.add_shell_element(
                    EY * j + i + 1,
                    [NX * j + i, NX * j + (i + 1), NX * (j + 1) + (i + 1), NX * (j + 1) + i],
                )
        return ref_mesh

    @staticmethod
    def getPathToTestFile(test_file: str):
        cwd = os.getcwd()
        testFilePath = os.path.join(cwd, "testfiles", "sc_operators", test_file)
        return testFilePath


def try_load_sc_mapping_operators():
    try:
        if os.name == "posix":
            dpf.load_library("libAns.Dpf.SystemCouplingMapping.so", "sc_mapping")
        else:
            dpf.load_library("Ans.Dpf.SystemCouplingMapping.dll", "sc_mapping")
        return True
    except:
        return False


@pytest.fixture
def source_region():
    return test_utils.get_sq_mesh(3, 3, 0.1)


@pytest.fixture
def target_region():
    return test_utils.get_sq_mesh(5, 5, 0.05)


@pytest.fixture
def source_data():
    source_data = dpf.Field(9, dpf.natures.scalar, "Nodal")
    source_data.append([0.0], scopingid=1)
    source_data.append([1.0], scopingid=2)
    source_data.append([4.0], scopingid=3)
    source_data.append([-40.0], scopingid=4)
    source_data.append([25.0], scopingid=5)
    source_data.append([10.0], scopingid=6)
    source_data.append([4.5], scopingid=7)
    source_data.append([7.0], scopingid=8)
    source_data.append([-3.0], scopingid=9)
    source_data.unit = "K"

    return source_data


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_mapping1(source_region, target_region, source_data):
    dimensionality = 1
    op = dpf.operators.mapping.sysc_shape_function_wf()
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=1, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=False, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    op.inputs.options_data_tree.connect(my_options_data_tree)
    op.inputs.source_mesh.connect(source_region)
    op.inputs.target_mesh.connect(target_region)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", source_data)

    out_fc = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit = out_fc[0].unit
    assert unit == "K"

    target_data = out_fc[0].data

    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(0.5, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(-20.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(10.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[11] == approx(-7.5, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[16] == approx(-0.875, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    target_sco = out_fc[0].scoping

    assert target_sco.ids[0] == 1
    assert target_sco.ids[9] == 10


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_mapping2(source_region, target_region, source_data):
    op = dpf.operators.mapping.sysc_point_cloud_wf()
    op.inputs.source_mesh.connect(source_region)
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=1, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=False, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    op.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_mesh", target_region.nodes.coordinates_field)
    sc_map_wf.connect("source_data", source_data)

    out_fc = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit = out_fc[0].unit
    assert unit == "K"

    target_data = out_fc[0].data

    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(2.1354, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(-22.8321, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(12.4324, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[11] == approx(-7.761369, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[16] == approx(-0.0840, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    target_sco = out_fc[0].scoping

    assert target_sco.ids[0] == 1
    assert target_sco.ids[9] == 10


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_mapping3(source_region, target_region, source_data):
    dimensionality = 1
    # first operator
    op = dpf.operators.mapping.sysc_shape_function_wf()
    op.inputs.source_mesh.connect(source_region)
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=False, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    op.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_mesh", target_region)
    sc_map_wf.connect("source_data", source_data)

    out_fc = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit = out_fc[0].unit
    assert unit == "K"

    target_data = out_fc[0].data

    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(0.5, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(-20.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(10.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[11] == approx(-7.5, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[16] == approx(-0.875, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    # second operator
    op.inputs.target_mesh.connect(source_region)
    sc_map_wf2 = op.outputs.mapping_workflow()
    sc_map_wf2.connect("source_data", source_data)

    out_fc2 = sc_map_wf2.get_output("target_data", dpf.types.fields_container)
    target_data = out_fc2[0].data
    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(1.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[2] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[3] == approx(-40.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(25.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(10.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(-3.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert len(target_data) == 9

    # Back to the first operator and change mesh -> works
    sc_map_wf.connect("target_mesh", source_region)
    out_fc = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    target_data = out_fc[0].data
    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(1.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[2] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[3] == approx(-40.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(25.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(10.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(-3.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert len(target_data) == 9

    # Back to the second operator and change src data -> throws
    source_data.unit = "MPa"
    sc_map_wf2.connect("source_data", source_data)
    with pytest.raises(Exception):
        out_fc2 = sc_map_wf2.get_output("target_data", dpf.types.fields_container)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rst1():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    mesh_path_trg = test_utils.getPathToTestFile("modal_vol_hex_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("modal_vol_hex_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("modal_vol_hex_2.disp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=3, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=False, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = map_builder.outputs.mapping_workflow()

    sc_map_wf.connect("source_mesh", mesh_src)
    sc_map_wf.connect("target_mesh", mesh_trg)
    sc_map_wf.connect("source_data", fc_src)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit_str = fc_trg[0].unit
    assert unit_str == "m"
    assert len(fc_trg) == 6

    trg_sco = dpf.Scoping()
    trg_sco.location = dpf.locations.nodal
    trg_sco.ids = [754, 1891, 2223]

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(trg_sco)
    fc_trg = rescope_fc.outputs.fields_container()

    UX = [-7.2321e-2, 3.1753e-1, 1.1745e-1, -4.4466e-1, -6.9633e-2, 3.5033e-1]
    UY = [-1.5571e-1, 2.6725e-1, 4.081e-2, -6.4918e-2, 3.0302e-1, -1.0984e-1]
    UZ = [-4.6455e-3, 2.5556e-3, -2.0920e-1, 1.0610e-1, -7.0386e-3, 1.2782e-2]

    for i in range(6):
        vals = fc_trg[i].data
        assert vals[0][0] == approx(UX[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
        assert vals[1][1] == approx(UY[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
        assert vals[2][2] == approx(UZ[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rst2():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
    # map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_mesh = dpf.operators.mesh.from_scoping()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 3
    is_conservative = True

    mesh_path_trg = test_utils.getPathToTestFile("modal_surf_hex_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("modal_surf_hex_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("modal_surf_hex_1.disp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Elemental")
    map_builder.inputs.dimensionality.connect(dimensionality)
    # data_tree1 = dpf.DataTree()
    # data_tree1.add(dimensionality=dimensionality, location="Elemental", name="data_definition")
    # data_tree2 = dpf.DataTree()
    # data_tree2.add(conservative=is_conservative, name="mapping_options")
    # my_options_data_tree=dpf.DataTree()
    # my_options_data_tree.data_definition=data_tree1
    # my_options_data_tree.mapping_options=data_tree2

    # map_builder.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_mesh", mesh_src)
    sc_map_wf.connect("target_mesh", mesh_trg)
    sc_map_wf.connect("source_data", fc_src)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    assert fc_trg[0].elementary_data_count == mesh_trg.elements.n_elements

    sco_src = dpf.Scoping()
    sco_src.location = dpf.locations.nodal
    sco_src.ids = [1315, 1316, 1332, 1335]

    rescope_mesh.inputs.scoping.connect(sco_src)
    rescope_mesh.inputs.inclusive.connect(0)
    rescope_mesh.inputs.mesh.connect(mesh_src)
    sco_el_src = rescope_mesh.outputs.mesh().elements.scoping

    sco_trg = dpf.Scoping()
    sco_trg.location = dpf.locations.nodal
    sco_trg.ids = [1315, 1316, 1332, 1335, 6251, 6252, 6254, 6288]

    rescope_mesh.inputs.scoping.connect(sco_trg)
    rescope_mesh.inputs.mesh.connect(mesh_trg)
    sco_el_trg = rescope_mesh.outputs.mesh().elements.scoping

    rescope_fc.inputs.fields_container.connect(fc_src)
    rescope_fc.inputs.mesh_scoping.connect(sco_el_src)

    vals_src = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(sco_el_trg)

    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    for i in range(3):
        assert 1.0 == approx(
            vals_src[0, i] / vals_trg[0, i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )

    # Same comparison, but with target_scoping
    sc_map_wf.connect("target_scoping", sco_el_trg)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    vals_trg = copy.deepcopy(fc_trg[0].data)

    for i in range(3):
        assert 1.0 == approx(
            vals_src[0, i] / vals_trg[0, i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth1():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("thermal_vol_hex_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.eletemp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Elemental", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_mesh", mesh_src)
    sc_map_wf.connect("target_mesh", mesh_trg)
    sc_map_wf.connect("source_data", fc_src[0])

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit_str = fc_trg[0].unit
    assert unit_str == "degC"

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.elemental
    data_sco.ids = [1287, 176]

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    Tvals_trg = rescope_fc.outputs.fields_container()[0].data

    Tcomp = [4.1814, 1.9810]

    for i in range(len(Tcomp)):
        print(Tvals_trg[i])
        assert 1.0 == approx(Tvals_trg[i] / Tcomp[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth2():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
    # map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 1
    is_conservative = True

    mesh_path_trg = test_utils.getPathToTestFile("thermal_surf_tet_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("thermal_surf_tet_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("thermal_surf_tet_1.temp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.source_mesh.connect(mesh_src)
    map_builder.inputs.target_mesh.connect(mesh_trg)
    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Nodal")
    map_builder.inputs.dimensionality.connect(dimensionality)
    # data_tree1 = dpf.DataTree()
    # data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    # data_tree2 = dpf.DataTree()
    # data_tree2.add(conservative=is_conservative, name="mapping_options")
    # my_options_data_tree = dpf.DataTree()
    # my_options_data_tree.data_definition = data_tree1
    # my_options_data_tree.mapping_options = data_tree2

    # map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [7409, 809]

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    vals_trg = rescope_fc.outputs.fields_container()[0].data

    Tcomp = [3.1639e-1, 8.8269e-1]

    for i in range(len(Tcomp)):
        assert 1.0 == approx(vals_trg[i] / Tcomp[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth3():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("thermal_vol_tet_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.nodtemp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.source_mesh.connect(mesh_src)
    map_builder.inputs.target_mesh.connect(mesh_trg)
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [7409, 809, 2200]

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    Tcomp = [5.2836, 4.8361, 4.0660]

    for i in range(len(Tcomp)):
        assert 1.0 == approx(vals_trg[i] / Tcomp[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    sc_map_wf.connect("target_scoping", data_sco)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    for i in range(3):
        T = fc_trg[0].get_entity_data_by_id(data_sco.ids[i])
        assert 1.0 == approx(T[0] / Tcomp[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth4():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_point_cloud_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("thermal_vol_tet_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)
    coords_trg = mesh_trg.nodes.coordinates_field

    mesh_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)
    coords_src = mesh_src.nodes.coordinates_field

    fc_path_src = test_utils.getPathToTestFile("thermal_vol_tet_1.nodtemp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()

    Tcomp = [5.1389, 4.8361, 4.0660]
    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [7409, 809, 2200]

    sc_map_wf.connect("source_data", fc_src)
    sc_map_wf.connect("source_mesh", coords_src)
    sc_map_wf.connect("target_mesh", coords_trg)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    for i in range(len(Tcomp)):
        assert 1.0 == approx(vals_trg[i] / Tcomp[i], rel=test_utils.RELTOL)

    sc_map_wf.connect("target_scoping", data_sco)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    Tcomp = [5.2837, 4.8215, 4.0296]
    for i in range(3):
        T = fc_trg[0].get_entity_data_by_id(data_sco.ids[i])
        assert 1.0 == approx(T[0] / Tcomp[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_WebPyr():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 3

    mesh_path_trg = test_utils.getPathToTestFile("wedpyr_vol.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("wedpyr_vol.disp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.source_mesh.connect(mesh)
    map_builder.inputs.target_mesh.connect(mesh.deep_copy())
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=True, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [55, 38000, 6969]

    import time

    start = time.time()
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    stop = time.time()
    duration = stop - start
    print(f"Mapping time for conservative (extensive) : {duration} s. \n")

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)
    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)
    ucomp = [
        3.5839e-08,
        -1.5970e-03,
        6.2010e-05,
        -3.2069e-07,
        -5.6099e-04,
        3.9058e-05,
        3.7233e-07,
        -1.4063e-03,
        1.0923e-04,
    ]

    length = int(len(ucomp) / dimensionality)
    for i in range(length):
        for j in range(dimensionality):
            assert 1.0 == approx(
                float(vals_trg[i][j]) / float(ucomp[i * dimensionality + j]),
                rel=test_utils.RELTOL,
                abs=test_utils.ABSTOL,
            )

    data_tree2.conservative = False
    map_builder.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    start = time.time()
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    stop = time.time()
    duration = stop - start
    print(f"Mapping time for non-conservative (intensive) : {duration} s. \n")

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)
    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)
    rescope_fc.inputs.fields_container.connect(fc_src)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)
    vals_src = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    for i in range(len(data_sco.ids)):
        for j in range(dimensionality):
            assert 1.0 == approx(
                float(vals_trg[i][j]) / float(vals_src[i][j]),
                rel=test_utils.RELTOL,
                abs=test_utils.ABSTOL,
            )


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_Mc1():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()

    dimensionality = 3
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("shell.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh = deserializer.get_output(1, dpf.types.meshes_container)
    mesh1 = deserializer.get_output(1, dpf.types.meshes_container)

    fc_path_src = test_utils.getPathToTestFile("shell.disp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)
    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_mesh", mesh)
    sc_map_wf.connect("target_mesh", mesh1)
    sc_map_wf.connect("source_data", fc_src)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    unit = fc_trg[0].unit

    assert unit == "m"
    assert len(fc_trg) == 24

    nids = [58, 237, 309, 438]
    nfields = [12, 5, 18, 3]
    for i in range(4):
        vals_trg = fc_trg[nfields[i]].get_entity_data_by_id(nids[i])
        vals_src = fc_trg[nfields[i]].get_entity_data_by_id(nids[i])
        print(vals_src)
        assert 1.0 == approx(
            vals_src[0, 1] / vals_trg[0, 1], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )
        assert 1.0 == approx(
            vals_src[0, 1] / vals_trg[0, 1], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )
        assert 1.0 == approx(
            vals_src[0, 2] / vals_trg[0, 2], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )

    sco_cont = dpf.ScopingsContainer()
    sco_cont.add_label("body")

    for i in range(4):
        sco = dpf.Scoping()
        sco.location = dpf.locations.nodal
        sco.ids = [nids[i]]
        sco_cont.add_scoping({"body": i + 1}, sco)

    sc_map_wf.connect("target_scoping", sco_cont)
    for i in range(4):
        vals_trg = fc_trg[nfields[i]].get_entity_data_by_id(nids[i])
        vals_src = fc_trg[nfields[i]].get_entity_data_by_id(nids[i])
        print(vals_src)
        assert 1.0 == approx(
            vals_src[0, 1] / vals_trg[0, 1], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )
        assert 1.0 == approx(
            vals_src[0, 1] / vals_trg[0, 1], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )
        assert 1.0 == approx(
            vals_src[0, 2] / vals_trg[0, 2], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_Mc2():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("mixed.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh = deserializer.get_output(1, dpf.types.meshes_container)
    mesh1 = deserializer.get_output(1, dpf.types.meshes_container)

    fc_path_src = test_utils.getPathToTestFile("mixed.eletemp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Elemental", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_mesh", mesh)
    sc_map_wf.connect("target_mesh", mesh1)
    sc_map_wf.connect("source_data", fc_src)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit = fc_trg[0].unit

    assert unit == "degC"
    assert len(fc_trg) == 3

    assert fc_trg.get_label_space(0)["interface"] == 0
    assert fc_trg.get_label_space(0)["time"] == 0
    assert len(fc_trg[0].data) == 1368

    assert fc_trg.get_label_space(1)["interface"] == 1
    assert fc_trg.get_label_space(1)["time"] == 0
    assert len(fc_trg[1].data) == 114

    assert fc_trg.get_label_space(2)["interface"] == 0
    assert fc_trg.get_label_space(2)["time"] == 1
    assert len(fc_trg[2].data) == 1368


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_Fc1():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_point_cloud_wf()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("mixed.coords")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    coords = deserializer.get_output(1, dpf.types.fields_container)
    coords1 = deserializer.get_output(1, dpf.types.fields_container)

    fc_path_src = test_utils.getPathToTestFile("mixed.nodtemp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.source_mesh.connect(coords)
    map_builder.inputs.target_mesh.connect(coords1)
    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Nodal", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    unit = fc_trg[0].unit

    assert unit == "degC"
    assert len(fc_trg) == 5

    assert fc_trg.get_label_space(0)["interface"] == 0
    assert fc_trg.get_label_space(0)["mylabel"] == 1
    assert len(fc_trg[0].data) == 171

    assert fc_trg.get_label_space(1)["interface"] == 1
    assert fc_trg.get_label_space(1)["mylabel"] == 5
    assert len(fc_trg[1].data) == 2223

    assert fc_trg.get_label_space(2)["interface"] == 0
    assert fc_trg.get_label_space(2)["mylabel"] == 2
    assert len(fc_trg[2].data) == 171

    assert fc_trg.get_label_space(3)["interface"] == 1
    assert fc_trg.get_label_space(3)["mylabel"] == 69
    assert len(fc_trg[3].data) == 2223

    assert fc_trg.get_label_space(4)["interface"] == 0
    assert fc_trg.get_label_space(4)["mylabel"] == 3
    assert len(fc_trg[4].data) == 171

    sco_cont = dpf.ScopingsContainer()
    sco_cont.add_label("interface")

    sco = dpf.Scoping()
    sco.location = dpf.locations.nodal
    sco.ids = [717]
    sco1 = dpf.Scoping()
    sco1.location = dpf.locations.nodal
    sco1.ids = [1719]
    sco_cont.add_scoping({"interface": 0}, sco)
    sco_cont.add_scoping({"interface": 1}, sco1)

    sc_map_wf.connect("target_scoping", sco_cont)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    assert fc_trg.get_label_space(0)["interface"] == 0
    assert fc_trg.get_label_space(0)["mylabel"] == 1
    assert len(fc_trg[0].data) == 1

    assert fc_trg.get_label_space(1)["interface"] == 1
    assert fc_trg.get_label_space(1)["mylabel"] == 5
    assert len(fc_trg[1].data) == 1

    assert fc_trg.get_label_space(2)["interface"] == 0
    assert fc_trg.get_label_space(2)["mylabel"] == 2
    assert len(fc_trg[2].data) == 1

    assert fc_trg.get_label_space(3)["interface"] == 1
    assert fc_trg.get_label_space(3)["mylabel"] == 69
    assert len(fc_trg[3].data) == 1

    assert fc_trg.get_label_space(4)["interface"] == 0
    assert fc_trg.get_label_space(4)["mylabel"] == 3
    assert len(fc_trg[4].data) == 1


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_poly():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.sysc_shape_function_wf()
    rescope = dpf.operators.scoping.rescope()

    dimensionality = 1
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("poly.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh = deserializer.get_output(1, dpf.types.meshes_container)
    mesh1 = deserializer.get_output(1, dpf.types.meshes_container)

    fc_path_src = test_utils.getPathToTestFile("poly.press")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    data_tree1 = dpf.DataTree()
    data_tree1.add(dimensionality=dimensionality, location="Elemental", name="data_definition")
    data_tree2 = dpf.DataTree()
    data_tree2.add(conservative=is_conservative, name="mapping_options")
    my_options_data_tree = dpf.DataTree()
    my_options_data_tree.data_definition = data_tree1
    my_options_data_tree.mapping_options = data_tree2

    map_builder.inputs.options_data_tree.connect(my_options_data_tree)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_mesh", mesh)
    sc_map_wf.connect("target_mesh", mesh1)
    sc_map_wf.connect("source_data", fc_src)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    assert len(fc_trg) == 2
    assert fc_trg[0].elementary_data_count == 11093
    assert fc_trg[1].elementary_data_count == 902

    data_sco_0 = dpf.Scoping()
    data_sco_0.location = dpf.locations.elemental
    data_sco_0.ids = [4679, 174]

    rescope.inputs.fields.connect(fc_src[0])
    rescope.inputs.mesh_scoping.connect(data_sco_0)
    vals_src = copy.deepcopy(rescope.outputs.fields_as_field().data)

    rescope.inputs.fields.connect(fc_trg[0])
    vals_trg = copy.deepcopy(rescope.outputs.fields_as_field().data)

    for i in range(len(data_sco_0)):
        assert 1.0 == approx(
            vals_src[i] / vals_trg[i], rel=test_utils.RELTOL, abs=test_utils.ABSTOL
        )
