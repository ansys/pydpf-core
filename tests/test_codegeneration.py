# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
import copy
import os
import tempfile

import numpy as np

from ansys.dpf import core
from ansys.dpf.core import examples
import ansys.dpf.core.operators as op
import ansys.grpc.dpf


def test_workflowwithgeneratedcode(allkindofcomplexity):
    disp = core.operators.result.displacement()
    ds = core.DataSources(allkindofcomplexity)
    nodes = [1]
    scop = core.Scoping()
    scop.ids = nodes
    scop.location = "Nodal"
    disp.inputs.data_sources.connect(ds)
    disp.inputs.mesh_scoping.connect(scop)
    a = disp.outputs.fields_container.get_data()
    assert a[0].data[0][0] == 7.120546307743541e-07
    assert len(a[0].data[0]) == 3
    assert len(a[0].data) == 1
    norm = core.operators.math.norm()
    norm.inputs.field.connect(disp.outputs.fields_container)
    b = norm.outputs.field()
    assert b.data[0] == 1.26387078548793e-06
    filt = core.operators.filter.scoping_high_pass()
    filt.inputs.field.connect(norm.outputs.field)
    filt.inputs.threshold.connect(1e-05)
    pow_op = core.operators.math.pow()
    pow_op.inputs.factor.connect(3.0)
    pow_op.inputs.field.connect(norm.outputs.field)
    d = pow_op.outputs.field.get_data()
    assert d.data[0] == 2.0188684707833254e-18


def test_calloperators(allkindofcomplexity):
    my_data_sources = core.DataSources(allkindofcomplexity)
    my_model = core.Model(my_data_sources)
    displacement_op = my_model.results.displacement()
    assert isinstance(displacement_op, ansys.dpf.core.dpf_operator.Operator)
    norm_op = my_model.operator("norm_fc")
    assert isinstance(norm_op, ansys.dpf.core.dpf_operator.Operator)
    square_op = core.operators.math.sqr()
    assert isinstance(square_op, ansys.dpf.core.operators.math.sqr)


def test_makeconnections(allkindofcomplexity):
    my_data_sources = core.DataSources(allkindofcomplexity)
    my_model = core.Model(my_data_sources)
    displacement_op = my_model.results.displacement()
    norm_op = my_model.operator("norm")
    square_op = core.operators.math.sqr()
    assert len(displacement_op.inputs._connected_inputs) == 2
    assert len(norm_op.inputs._connected_inputs) == 0
    # assert len(square_op.inputs._connected_inputs)==0
    norm_op.inputs.connect(displacement_op.outputs)
    square_op.inputs.field.connect(norm_op.outputs.field)
    assert len(displacement_op.inputs._connected_inputs) == 2
    assert len(norm_op.inputs._connected_inputs) == 1
    assert len(square_op.inputs._connected_inputs) == 1
    square_op.inputs.connect(norm_op.outputs.field)
    assert len(square_op.inputs._connected_inputs) == 1
    square_op.inputs.field.connect(norm_op.outputs)
    assert len(square_op.inputs._connected_inputs) == 1
    # assert len(square_op.inputs._connected_inputs)==1


def test_get_result(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.data_sources.connect(ds)
    stress.inputs.requested_location.connect("Nodal")
    avg = core.operators.averaging.to_elemental_fc()
    avg.inputs.fields_container.connect(stress.outputs.fields_container)
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert out[0].location == core.locations.elemental


def test_operator_inheritance(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.connect(4, ds)
    stress.inputs.requested_location.connect("Nodal")
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert out[0].location == core.locations.elemental


def test_operator_inheritance_2(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.data_sources.connect(ds)
    stress.inputs.requested_location.connect("Nodal")
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert out[0].location == core.locations.elemental


def test_inputs_inheritance(allkindofcomplexity):
    stress = core.operators.result.stress_X()
    ds = core.DataSources(allkindofcomplexity)
    stress.inputs.connect(ds)
    stress.inputs.requested_location.connect("Nodal")
    avg = core.operators.averaging.to_elemental_fc()
    avg.connect(0, stress)
    avg.run()
    out = avg.outputs.fields_container()
    assert len(out) == 2
    assert out[0].location == core.locations.elemental


def test_operator_any_input(allkindofcomplexity):
    serialization = core.operators.serialization.serializer()
    model = core.Model(allkindofcomplexity)
    u = model.results.displacement()

    serialization.inputs.any_input1.connect(u.outputs)
    serialization.inputs.any_input2.connect(u.outputs.fields_container)
    serialization.inputs.any_input3.connect(u.outputs)

    # create a temporary file at the default temp directory
    path = os.path.join(tempfile.gettempdir(), "dpf_temp_ser.txt")
    if not core.SERVER.local_server:
        core.upload_file_in_tmp_folder(examples.find_static_rst(return_local_path=True))
        path = core.path_utilities.join(core.make_tmp_dir_server(), "dpf_temp_ser.txt")
    serialization.inputs.file_path(path)
    serialization.run()

    deser = core.operators.serialization.deserializer()
    deser.inputs.connect(path)
    fc = deser.get_output(1, core.types.fields_container)
    assert len(fc) == 1
    fc = deser.get_output(2, core.types.fields_container)
    assert len(fc) == 1
    fc = deser.get_output(2, core.types.fields_container)
    assert len(fc) == 1

    assert hasattr(fc, "outputs") == False

    if os.path.exists(path):
        os.remove(path)


def test_create_op_with_inputs(plate_msup):
    ds = core.DataSources(plate_msup)
    u = core.operators.result.displacement(time_scoping=0.015, data_sources=ds)
    norm = core.operators.math.norm_fc(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [0.00036435444541115566])
    u = core.operators.result.displacement(time_scoping=0.025, data_sources=ds)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [1.50367127e-13, 8.96539310e-04, 1.62125644e-05])
    u = core.operators.result.displacement(time_scoping=[0.015, 0.025], data_sources=ds)
    fc = u.outputs.fields_container()
    assert len(fc) == 2
    assert np.allclose(fc[0].data[0], [5.12304110e-14, 3.64308310e-04, 5.79805917e-06])
    assert np.allclose(fc[1].data[0], [1.50367127e-13, 8.96539310e-04, 1.62125644e-05])
    u = core.operators.result.displacement(time_scoping=1, data_sources=ds)
    fc = u.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [1.62364553e-14, 1.47628321e-04, 1.96440004e-06])


def test_create_op_in_chain(plate_msup):
    ds = core.DataSources(plate_msup)
    s = op.result.stress(time_scoping=0.015, data_sources=ds)
    eqv1 = op.invariant.von_mises_eqv_fc(op.averaging.to_nodal_fc(s))
    fc1 = eqv1.outputs.fields_container()
    eqv2 = op.invariant.von_mises_eqv_fc(
        op.result.stress(
            time_scoping=0.015, data_sources=ds, requested_location=core.locations.nodal
        )
    )
    fc2 = eqv2.outputs.fields_container()
    identical = op.logic.identical_fc(fc1, fc2)
    out = identical.outputs.boolean()
    assert out == True
    identical = op.logic.identical_fc(eqv2, eqv1)
    out = identical.outputs.boolean()
    assert out == True
    identical = op.logic.identical_fc(eqv2.outputs, eqv1.outputs)
    out = identical.outputs.boolean()
    assert out == True
    identical = op.logic.identical_fc(eqv2.outputs.fields_container, eqv1.outputs.fields_container)
    out = identical.outputs.boolean()
    assert out == True


def test_create_op_with_input_model(plate_msup):
    model = core.Model(plate_msup)
    u = core.operators.result.displacement(time_scoping=0.015, data_sources=model)
    norm = core.operators.math.norm_fc(u)
    fc = norm.outputs.fields_container()
    assert len(fc) == 1
    assert np.allclose(fc[0].data[0], [0.00036435444541115566])


def test_connect_output_to_inputs(plate_msup):
    my_model = core.Model(plate_msup)
    s = my_model.results.stress()

    to_elemental = op.averaging.to_elemental_fc()
    to_elemental.inputs.connect(s.outputs)

    comp = op.logic.component_selector_fc()
    comp.inputs.component_number.connect(2)
    comp.inputs.connect(to_elemental.outputs)

    min_max = op.min_max.min_max_over_label_fc()
    min_max.inputs.connect(comp.outputs)
    min_max.inputs.label.connect("time")

    scale = op.math.scale(min_max.outputs.field_max, 0.5)

    high_pass = op.filter.field_high_pass_fc(comp, scale)

    fields = high_pass.outputs.fields_container()
    assert len(fields) == 1


def test_generated_operator_several_output_types(plate_msup):
    inpt = core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    uc = op.math.unit_convert()
    uc.inputs.entity_to_convert(inpt)
    uc.inputs.unit_name("mm")
    f = uc.outputs.converted_entity_as_field()
    assert f.unit == "mm"
    assert np.allclose(f.data.flatten("C"), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) * 1000)

    model = core.Model(plate_msup)
    din = copy.deepcopy(model.metadata.meshed_region.nodes.coordinates_field.data)

    assert model.metadata.meshed_region.nodes.coordinates_field.unit == "m"

    uc.inputs.entity_to_convert(model.metadata.meshed_region)
    uc.inputs.unit_name("mm")
    m = uc.outputs.converted_entity_as_meshed_region()

    assert m.nodes.coordinates_field.unit == "mm"
    assert np.allclose(m.nodes.coordinates_field.data, np.array(din) * 1000)


def test_generated_operator_several_output_types2():
    inpt = core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"
    uc = op.scoping.rescope(inpt, core.Scoping(ids=[1, 2]))
    f = uc.outputs.fields_as_field()
    assert np.allclose(f.data.flatten("C"), [1, 2, 3, 4, 5, 6])

    fc = core.FieldsContainer()
    fc.labels = ["time"]
    fc.add_field({"time": 1}, inpt)
    uc = op.scoping.rescope(fc, core.Scoping(ids=[1, 2]))
    fc2 = uc.outputs.fields_as_fields_container()
    assert np.allclose(fc2[0].data.flatten("C"), [1, 2, 3, 4, 5, 6])


def test_generated_operator_set_config():
    inpt = core.Field(nentities=3)
    inpt.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt.scoping.ids = [1, 2, 3]
    inpt.unit = "m"

    inpt2 = core.Field(nentities=3)
    inpt2.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inpt2.scoping.ids = [3, 4, 5]
    inpt2.unit = "m"

    conf = op.math.add.default_config()
    # print(conf)
    conf.set_work_by_index_option(True)
    op1 = op.math.add(config=conf)
    op1.inputs.fieldA.connect(inpt)
    op1.inputs.fieldB.connect(inpt2)
    out = op1.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2, 3]) or np.allclose(out.scoping.ids, [3, 4, 5])
    assert np.allclose(out.data, np.array([[2.0, 4.0, 6.0], [8.0, 10.0, 12.0], [14.0, 16.0, 18.0]]))

    conf.set_work_by_index_option(False)
    op1 = op.math.add(config=conf)
    op1.inputs.fieldA.connect(inpt)
    op1.inputs.fieldB.connect(inpt2)
    out = op1.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2, 3, 4, 5])
    assert np.allclose(
        out.data,
        np.array(
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [8.0, 10.0, 12.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0],
            ]
        ),
    )

    inpt2.unit = "Pa"
    conf = op.math.add.default_config()
    conf.set_permissive_option(True)
    op1.config = conf
    op1.inputs.fieldB.connect(inpt2)
    out = op1.outputs.field()
    assert np.allclose(out.scoping.ids, [1, 2, 3, 4, 5])
    assert np.allclose(
        out.data,
        np.array(
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [8.0, 10.0, 12.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0],
            ]
        ),
    )

    assert conf.get_mutex_option() == "false"
    assert conf.config_option_default_value("mutex") == "false"
    assert conf.config_option_accepted_types("mutex") == ["bool"]
    assert conf.options["mutex"] == "false"
    assert "multiple threads" in conf.config_option_documentation("mutex")
