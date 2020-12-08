import os
import numpy as np

from ansys import dpf
from ansys.dpf.core import Model, Operator
from ansys.dpf.core import locations
from ansys.dpf.core.rescoper import Rescoper

    

def test_rescoper_init(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    assert rescoper.location == disp[0].location
    assert rescoper.mesh_scoping.location == locations.nodal
    stress_op = model.results.stress()
    stress_op.inputs.requested_location.connect(locations.elemental)
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress_op.outputs.fields_container)
    stress = avg_op.outputs.fields_container()
    assert len(stress) == 2
    rescoper = Rescoper(model.metadata.meshed_region, stress[0].location, stress[0].component_count)
    assert rescoper.location == stress[0].location
    assert rescoper.mesh_scoping.location == locations.elemental
    

def test_rescoper_nanfield(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper1 = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    assert len(rescoper1.nan_field) == 15129
    assert len(rescoper1.nan_field[10]) == 3
    assert np.isnan(rescoper1.nan_field).all()
    stress_op = model.results.stress()
    stress_op.inputs.requested_location.connect(locations.elemental)
    avg_op = Operator("to_elemental_fc")
    avg_op.inputs.fields_container.connect(stress_op.outputs.fields_container)
    stress = avg_op.outputs.fields_container()
    assert len(stress) == 2
    rescoper2 = Rescoper(model.metadata.meshed_region, stress[0].location, stress[0].component_count)
    assert len(rescoper2.nan_field) == 10292
    assert len(rescoper2.nan_field[10]) == 6
    assert np.isnan(rescoper2.nan_field).all()
    

def test_rescoper_rescope(allkindofcomplexity):
    model = Model(allkindofcomplexity)
    disp_op = model.results.displacement()
    disp = disp_op.outputs.fields_container()
    assert len(disp) == 1
    rescoper = Rescoper(model.metadata.meshed_region, disp[0].location, disp[0].component_count)
    field = rescoper.rescope(disp[0])
    assert len(field) == 15129
    assert len(field[0]) == 3
    assert field[20][2] == -1.0882665178147842e-07
    assert field[103][0] == 1.334345300352076e-07
    assert field[12][1] == 4.343049969079495e-07
