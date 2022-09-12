from ast import operator
import os

import pytest

from ansys.dpf import core as dpf
from pytest import approx

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
def test_sc_mapping1(source_region,target_region,source_data):

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
def test_sc_mapping2(source_region,target_region,source_data):

    dimensionality = 1
    op = dpf.operators.mapping.create_sc_mapping_workflow()
    op.inputs.source_mesh.connect(source_region)
    op.inputs.is_conservative.connect(False)
    op.inputs.is_pointcloud.connect(True)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_coords",target_region.nodes.coordinates_field)
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
def test_sc_mapping3(source_region,target_region,source_data):

    dimensionality = 1
    #first operator
    op = dpf.operators.mapping.create_sc_mapping_workflow()
    op.inputs.source_mesh.connect(source_region)
    op.inputs.is_conservative.connect(False)
    sc_map_wf = op.outputs.mapping_workflow()
    sc_map_wf.connect("target_mesh",target_region)
    sc_map_wf.connect("location","Nodal")
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
    sc_map_wf2=op.outputs.mapping_workflow()
    sc_map_wf2.connect("location","Nodal")
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
    sc_map_wf.connect("target_mesh",source_region)
    out_fc=sc_map_wf.get_output("target_data", dpf.types.fields_container)
    target_data=out_fc[0].data
    assert target_data[0] == approx(0.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[1] == approx(1.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[2] == approx(4.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[3] == approx(-40.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[4] == approx(25.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[5] == approx(10.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert target_data[8] == approx(-3.0, rel=test_utils.RELTOL, abs=test_utils.ABSTOL)
    assert len(target_data) == 9
    
    #Back to the second operator and change src data -> throws
    source_data.unit="MPa"
    sc_map_wf2.connect("source_data",source_data)
    with pytest.raises(Exception):
        out_fc2=sc_map_wf2.get_output("target_data", dpf.types.fields_container)
    
    