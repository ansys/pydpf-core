from ast import operator
import os

import pytest

from ansys.dpf import core as dpf
from pytest import approx
import copy


class test_utils:
    ABSTOL = 1e-14
    RELTOL = 1e-2

    @staticmethod
    def get_sq_mesh(NX: int, NY: int, Ax: float):
        EX = NX-1
        EY = NY-1
        numNode = NX*NY
        numElem = EX*EY
        ref_mesh = dpf.MeshedRegion(num_nodes=numNode, num_elements=numElem)
        for j in range(NY):
            for i in range(NX):
                ref_mesh.nodes.add_node(NX*j+i+1, [Ax*i, Ax*j, 0.0])

        for j in range(EY):
            for i in range(EX):
                ref_mesh.elements.add_shell_element(EY*j+i+1, [NX * j + i, NX * j + (i + 1),
                              NX * (j + 1) + (i + 1), NX * (j + 1) + i])
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
    op = dpf.operators.mapping.create_sc_mapping_workflow()
    op.inputs.source_mesh.connect(source_region)
    op.inputs.target_mesh.connect(target_region)
    op.inputs.is_conservative.connect(False)
    op.inputs.location.connect("Nodal")
    op.inputs.dimensionality.connect(dimensionality)
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

    dimensionality = 1
    op = dpf.operators.mapping.create_sc_mapping_workflow()
    op.inputs.source_mesh.connect(source_region)
    op.inputs.is_conservative.connect(False)
    op.inputs.is_pointcloud.connect(True)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_coords", target_region.nodes.coordinates_field)
    sc_map_wf.connect("dimensionality", dimensionality)
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
    #first operator
    op = dpf.operators.mapping.create_sc_mapping_workflow()
    op.inputs.source_mesh.connect(source_region)
    op.inputs.is_conservative.connect(False)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_mesh", target_region)
    sc_map_wf.connect("location", "Nodal")
    sc_map_wf.connect("dimensionality", dimensionality)
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

    #second operator
    op.inputs.target_mesh.connect(source_region)
    sc_map_wf2 = op.outputs.mapping_workflow()
    sc_map_wf2.connect("location", "Nodal")
    sc_map_wf2.connect("dimensionality", dimensionality)
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

    #Back to the first operator and change mesh -> works
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

    #Back to the second operator and change src data -> throws
    source_data.unit = "MPa"
    sc_map_wf2.connect("source_data", source_data)
    with pytest.raises(Exception):
        out_fc2 = sc_map_wf2.get_output("target_data", dpf.types.fields_container)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rst1():

    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
    rescope_fc = dpf.operators.scoping.rescope_fc()

    dimensionality = 3
    is_conservative = False

    mesh_path_trg = test_utils.getPathToTestFile("modal_vol_hex_1.mesh")
    deserializer.inputs.file_path.connect(mesh_path_trg)
    mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

    mesh_path_src = test_utils.getPathToTestFile("modal_vol_hex_2.mesh")
    deserializer.inputs.file_path.connect(mesh_path_src)
    mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

    fc_path_src = test_utils.getPathToTestFile("modal_vol_hex_2.disp")
    deserializer.inputs.file_path.connect(fc_path_src)
    fc_src = deserializer.get_output(1, dpf.types.fields_container)

    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Nodal")
    map_builder.inputs.dimensionality.connect(dimensionality)
    map_builder.inputs.is_pointcloud.connect(False)
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

    UX = [-7.2321E-2, 3.1753E-1, 1.1745E-1, -4.4466E-1, -6.9633E-2, 3.5033E-1]
    UY = [-1.5571E-1, 2.6725E-1, 4.081E-2, -6.4918E-2, 3.0302E-1, -1.0984E-1]
    UZ = [-4.6455E-3, 2.5556E-3, -2.0920E-1, 1.0610E-1,  -7.0386E-3, 1.2782E-2]

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

    vals_src = copy.deepcopy( rescope_fc.outputs.fields_container()[0].data)

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(sco_el_trg)

    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    for i in range(3):
        print(vals_trg[0])
        assert 1.0 == approx(vals_src[0, i]/vals_trg[0, i],
                             rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    # Same comparison, but with target_scoping
    sc_map_wf.connect("target_scoping", sco_el_trg)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    vals_trg = copy.deepcopy(fc_trg[0].data)

    for i in range(3):
        assert 1.0 == approx(vals_src[0, i]/vals_trg[0, i],
                             rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth1():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
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

    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Elemental")
    map_builder.inputs.dimensionality.connect(dimensionality)
    map_builder.inputs.is_pointcloud.connect(False)

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

    Tcomp = [4.1925, 1.9700]

    for i in range(len(Tcomp)):
        assert 1.0 == approx(Tvals_trg[i]/Tcomp[i],
                        rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth2():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
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

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [7409, 809]

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    vals_trg = rescope_fc.outputs.fields_container()[0].data

    Tcomp = [3.1639E-1, 8.8269E-1]

    for i in range(len(Tcomp)):
        assert 1.0 == approx(vals_trg[i]/Tcomp[i],
                        rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth3():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
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
    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Nodal")
    map_builder.inputs.dimensionality.connect(dimensionality)

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
        assert 1.0 == approx(vals_trg[i]/Tcomp[i],
                        rel=test_utils.RELTOL, abs=test_utils.ABSTOL)

    sc_map_wf.connect("target_scoping", data_sco)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    for i in range(3):
        T = fc_trg[0].get_entity_data_by_id(data_sco.ids[i])
        assert 1.0 == approx(T[0]/Tcomp[i],
                rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_rth4():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
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

    map_builder.inputs.is_conservative.connect(is_conservative)
    map_builder.inputs.location.connect("Nodal")
    map_builder.inputs.dimensionality.connect(dimensionality)
    map_builder.inputs.is_pointcloud.connect(True)

    sc_map_wf = map_builder.outputs.mapping_workflow()

    Tcomp = [5.1389, 4.8361, 4.0660]
    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [7409, 809, 2200]

    sc_map_wf.connect("source_data", fc_src)
    sc_map_wf.connect("source_coords", coords_src)
    sc_map_wf.connect("target_coords", coords_trg)

    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)

    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)

    for i in range(len(Tcomp)):
        assert 1.0 == approx(vals_trg[i]/Tcomp[i],
                        rel=test_utils.RELTOL)

    sc_map_wf.connect("target_scoping", data_sco)
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    Tcomp = [5.2837, 4.8215, 4.0296];
    for i in range(3):
        T = fc_trg[0].get_entity_data_by_id(data_sco.ids[i])
        assert 1.0 == approx(T[0]/Tcomp[i],
                rel=test_utils.RELTOL, abs=test_utils.ABSTOL)


@pytest.mark.skipif(
    not try_load_sc_mapping_operators(), reason="Couldn't load sc_mapping operators"
)
def test_sc_WebPyr():
    deserializer = dpf.operators.serialization.deserializer()
    map_builder = dpf.operators.mapping.create_sc_mapping_workflow()
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
    map_builder.inputs.location.connect("Nodal")
    map_builder.inputs.dimensionality.connect(dimensionality)

    sc_map_wf = map_builder.outputs.mapping_workflow()
    sc_map_wf.connect("source_data", fc_src)

    data_sco = dpf.Scoping()
    data_sco.location = dpf.locations.nodal
    data_sco.ids = [55, 38000, 6969]

    sc_map_wf.connect("is_conservative", True)

    import time

    start = time.time()
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    stop = time.time()
    duration = stop-start
    print(f"Mapping time for conservative (extensive) : {duration} s. \n")

    rescope_fc.inputs.fields_container.connect(fc_trg)
    rescope_fc.inputs.mesh_scoping.connect(data_sco)
    vals_trg = copy.deepcopy(rescope_fc.outputs.fields_container()[0].data)
    ucomp = [3.5839e-08,  -1.5970e-03, 6.2010e-05,
        -3.2069e-07, -5.6099e-04, 3.9058e-05,
        3.7233e-07,  -1.4063e-03, 1.0923e-04]

    length=int(len(ucomp)/dimensionality)
    for i in range(length):
        for j in range(dimensionality):
            assert 1.0 == approx(
                float(vals_trg[i][j])/float(ucomp[i*dimensionality+j]),
                rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    
    sc_map_wf.connect("is_conservative", False)


    start = time.time()
    fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)
    stop = time.time()
    duration = stop-start
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
                float(vals_trg[i][j])/float(vals_src[i][j]),
                rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
            
    
