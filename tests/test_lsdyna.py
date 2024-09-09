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

import numpy as np
import pytest
import conftest
from ansys.dpf import core as dpf
from ansys.dpf.core.check_version import server_meet_version


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1,
    reason="LS-DYNA source operators where not supported before 6.0,"
    " and unit systems where not supported before 6.1.",
)
def test_lsdyna_generic(d3plot_files):
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_files[0], "d3plot")
    ds.add_file_path(d3plot_files[1], "actunits")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([3])
    model = dpf.Model(ds)

    # ------------------------------------------------- Stress Von Mises

    von_mises_op = dpf.operators.result.stress_von_mises()
    von_mises_op.inputs.time_scoping.connect(time_sco)
    von_mises_op.inputs.data_sources.connect(ds)
    von_mises_fc = von_mises_op.outputs.fields_container()

    von_mises_model = model.results.stress_von_mises(time_scoping=time_sco).eval()

    assert np.allclose(von_mises_fc[0].data, von_mises_model[0].data)
    assert von_mises_fc[0].unit == "MPa"
    assert von_mises_model[0].unit == "MPa"

    # ------------------------------------------------- Global Kinetic energy

    kinetic_energy_op = dpf.operators.result.global_kinetic_energy()
    kinetic_energy_op.inputs.data_sources.connect(ds)
    kinetic_energy_fc = kinetic_energy_op.outputs.fields_container()

    kinetic_energy_model = model.results.global_kinetic_energy().eval()

    assert np.allclose(kinetic_energy_fc[0].data, kinetic_energy_model[0].data)
    assert kinetic_energy_fc[0].unit == "mJ"
    assert kinetic_energy_model[0].unit == "mJ"

    # ------------------------------------------------- Global Internal energy

    internal_energy_op = dpf.operators.result.global_internal_energy()
    internal_energy_op.inputs.data_sources.connect(ds)
    internal_energy_fc = internal_energy_op.outputs.fields_container()

    internal_energy_model = model.results.global_internal_energy().eval()

    assert np.allclose(internal_energy_fc[0].data[0], internal_energy_model[0].data[0])
    assert internal_energy_fc[0].unit == "mJ"
    assert internal_energy_model[0].unit == "mJ"

    # ------------------------------------------------- Global Total energy

    total_energy_op = dpf.operators.result.global_total_energy()
    total_energy_op.inputs.data_sources.connect(ds)
    total_energy_fc = total_energy_op.outputs.fields_container()

    total_energy_model = model.results.global_total_energy().eval()

    assert np.allclose(total_energy_fc[0].data[0], total_energy_model[0].data[0])

    # ------------------------------------------------- Global velocity

    global_velocity_op = dpf.operators.result.global_velocity()
    global_velocity_op.inputs.data_sources.connect(ds)
    global_velocity_fc = global_velocity_op.outputs.fields_container()

    global_velocity_model = model.results.global_velocity().eval()

    assert np.allclose(global_velocity_fc[0].data[0], global_velocity_model[0].data[0])
    if server_meet_version("7.1", global_velocity_op._server):
        assert global_velocity_fc[0].unit == "mm/s"
        assert global_velocity_model[0].unit == "mm/s"
    else:
        assert global_velocity_fc[0].unit == "mm*Hz"
        assert global_velocity_model[0].unit == "mm*Hz"

    # ------------------------------------------------- Initial Coordinates

    initial_coordinates_op = dpf.operators.result.initial_coordinates()
    initial_coordinates_op.inputs.time_scoping.connect(time_sco)
    initial_coordinates_op.inputs.data_sources.connect(ds)
    initial_coordinates_fc = initial_coordinates_op.outputs.fields_container()

    initial_coordinates_model = model.results.initial_coordinates(time_scoping=time_sco).eval()

    assert np.allclose(initial_coordinates_fc[0].data, initial_coordinates_model[0].data)
    assert initial_coordinates_fc[0].unit == "mm"
    assert initial_coordinates_model[0].unit == "mm"

    # ------------------------------------------------- Coordinates

    coordinates_op = dpf.operators.result.coordinates()
    coordinates_op.inputs.time_scoping.connect(time_sco)
    coordinates_op.inputs.data_sources.connect(ds)
    coordinates_fc = coordinates_op.outputs.fields_container()

    coordinates_model = model.results.coordinates(time_scoping=time_sco).eval()

    assert np.allclose(coordinates_fc[0].data, coordinates_model[0].data)

    # ------------------------------------------------- Node Velocity

    velocity_op = dpf.operators.result.velocity()
    velocity_op.inputs.time_scoping.connect(time_sco)
    velocity_op.inputs.data_sources.connect(ds)
    velocity_fc = velocity_op.outputs.fields_container()

    velocity_model = model.results.velocity(time_scoping=time_sco).eval()

    assert np.allclose(velocity_fc[0].data, velocity_model[0].data)

    # ------------------------------------------------- Node Acceleration

    acceleration_op = dpf.operators.result.acceleration()
    acceleration_op.inputs.time_scoping.connect(time_sco)
    acceleration_op.inputs.data_sources.connect(ds)
    acceleration_fc = acceleration_op.outputs.fields_container()

    acceleration_model = model.results.acceleration(time_scoping=time_sco).eval()

    assert np.allclose(acceleration_fc[0].data, acceleration_model[0].data)
    assert acceleration_fc[0].unit == "mm/s^2"
    assert acceleration_model[0].unit == "mm/s^2"

    # ------------------------------------------------- Effective Plastic Strain

    equivalent_plastic_strain_op = dpf.operators.result.plastic_strain_eqv()
    equivalent_plastic_strain_op.inputs.time_scoping.connect(time_sco)
    equivalent_plastic_strain_op.inputs.data_sources.connect(ds)
    equivalent_plastic_strain_fc = equivalent_plastic_strain_op.outputs.fields_container()

    equivalent_plastic_strain_model = model.results.plastic_strain_eqv(time_scoping=time_sco).eval()

    assert np.allclose(
        equivalent_plastic_strain_fc[0].data, equivalent_plastic_strain_model[0].data
    )
    assert equivalent_plastic_strain_fc[0].unit == ""
    assert equivalent_plastic_strain_model[0].unit == ""


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1,
    reason="LS-DYNA source operators where not supported before 6.0,"
    " and unit systems where not supported before 6.1.",
)
def test_lsdyna_beam(d3plot_beam):
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_beam, "d3plot")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([5])
    model = dpf.Model(ds)

    # Create a custom unit system to scope the units of the results
    my_units = dpf.UnitSystem("my_us", unit_names="mm;kg;s;K;C;deg")

    # ------------------------------------------------- Axial Force

    beam_axial_force_op = dpf.operators.result.beam_axial_force()
    beam_axial_force_op.inputs.time_scoping.connect(time_sco)
    beam_axial_force_op.inputs.data_sources.connect(ds)
    beam_axial_force_op.inputs.unit_system.connect(my_units)
    beam_axial_force_fc = beam_axial_force_op.outputs.fields_container()

    # As the model employs a streams_container under the hood, if we set it
    # up once, we are going to get it covered
    beam_axial_force_model_op = model.results.beam_axial_force(time_scoping=time_sco)
    beam_axial_force_model_op.inputs.unit_system.connect(my_units)
    beam_axial_force_model = beam_axial_force_model_op.outputs.fields_container()

    beam_axial_force_model = model.results.beam_axial_force(time_scoping=time_sco).eval()
    assert beam_axial_force_fc[0].unit == "mN"
    assert beam_axial_force_model[0].unit == "mN"

    # ------------------------------------------------- S Shear Force

    beam_s_shear_force_op = dpf.operators.result.beam_s_shear_force()
    beam_s_shear_force_op.inputs.time_scoping.connect(time_sco)
    beam_s_shear_force_op.inputs.data_sources.connect(ds)
    beam_s_shear_force_op.connect(50, my_units)
    t1_fc = beam_s_shear_force_op.outputs.fields_container()

    t1_mod = model.results.beam_s_shear_force(time_scoping=time_sco).eval()

    assert np.allclose(t1_fc[0].data, t1_mod[0].data)
    assert t1_fc[0].unit == "mN"
    assert t1_mod[0].unit == "mN"

    # ------------------------------------------------- T Shear Force

    beam_t_shear_force_op = dpf.operators.result.beam_t_shear_force()
    beam_t_shear_force_op.inputs.time_scoping.connect(time_sco)
    beam_t_shear_force_op.inputs.data_sources.connect(ds)
    beam_t_shear_force_op.inputs.unit_system.connect(my_units)
    t2_fc = beam_t_shear_force_op.outputs.fields_container()

    t2_mod = model.results.beam_t_shear_force(time_scoping=time_sco).eval()

    assert np.allclose(t2_fc[0].data, t2_mod[0].data)
    assert t2_fc[0].unit == "mN"
    assert t2_mod[0].unit == "mN"

    # ------------------------------------------------- Bending S Moment

    beam_s_bending_moment_op = dpf.operators.result.beam_s_bending_moment()
    beam_s_bending_moment_op.inputs.time_scoping.connect(time_sco)
    beam_s_bending_moment_op.inputs.data_sources.connect(ds)
    beam_s_bending_moment_op.inputs.unit_system.connect(my_units)
    m1_fc = beam_s_bending_moment_op.outputs.fields_container()

    m1_mod = model.results.beam_s_bending_moment(time_scoping=time_sco).eval()

    assert np.allclose(m1_fc[0].data, m1_mod[0].data)
    assert m1_fc[0].unit == "uJ"
    assert m1_mod[0].unit == "uJ"

    # ------------------------------------------------- Bending T Moment

    beam_t_bending_moment_op = dpf.operators.result.beam_t_bending_moment()
    beam_t_bending_moment_op.inputs.time_scoping.connect(time_sco)
    beam_t_bending_moment_op.inputs.data_sources.connect(ds)
    beam_t_bending_moment_op.inputs.unit_system.connect(my_units)
    m2_fc = beam_t_bending_moment_op.outputs.fields_container()

    m2_mod = model.results.beam_t_bending_moment(time_scoping=time_sco).eval()

    assert np.allclose(m2_fc[0].data, m2_mod[0].data)
    assert m2_fc[0].unit == "uJ"
    assert m2_mod[0].unit == "uJ"

    # ------------------------------------------------- Torsional Moment

    beam_torsional_moment_op = dpf.operators.result.beam_torsional_moment()
    beam_torsional_moment_op.inputs.time_scoping.connect(time_sco)
    beam_torsional_moment_op.inputs.data_sources.connect(ds)
    beam_torsional_moment_op.inputs.unit_system.connect(my_units)
    mt_fc = beam_torsional_moment_op.outputs.fields_container()

    mt_mod = model.results.beam_torsional_moment(time_scoping=time_sco).eval()

    assert np.allclose(mt_fc[0].data, mt_mod[0].data)
    assert mt_fc[0].unit == "uJ"
    assert mt_mod[0].unit == "uJ"

    # ------------------------------------------------- Axial stress

    beam_axial_stress_op = dpf.operators.result.beam_axial_stress()
    beam_axial_stress_op.inputs.time_scoping.connect(time_sco)
    beam_axial_stress_op.inputs.data_sources.connect(ds)
    beam_axial_stress_op.inputs.unit_system.connect(my_units)
    sn_fc = beam_axial_stress_op.outputs.fields_container()

    sn_mod = model.results.beam_axial_stress(time_scoping=time_sco).eval()

    assert np.allclose(sn_fc[0].data, sn_mod[0].data)
    assert sn_fc[0].unit == "kPa"
    assert sn_mod[0].unit == "kPa"

    # ------------------------------------------------- Shear RS Stress

    beam_rs_shear_stress_op = dpf.operators.result.beam_rs_shear_stress()
    beam_rs_shear_stress_op.inputs.time_scoping.connect(time_sco)
    beam_rs_shear_stress_op.inputs.data_sources.connect(ds)
    beam_rs_shear_stress_op.inputs.unit_system.connect(my_units)
    st1_fc = beam_rs_shear_stress_op.outputs.fields_container()

    st1_mod = model.results.beam_rs_shear_stress(time_scoping=time_sco).eval()

    assert np.allclose(st1_fc[0].data, st1_mod[0].data)
    assert st1_fc[0].unit == "kPa"
    assert st1_mod[0].unit == "kPa"

    # ------------------------------------------------- Shear TR Stress

    beam_tr_shear_stress_op = dpf.operators.result.beam_tr_shear_stress()
    beam_tr_shear_stress_op.inputs.time_scoping.connect(time_sco)
    beam_tr_shear_stress_op.inputs.data_sources.connect(ds)
    beam_tr_shear_stress_op.inputs.unit_system.connect(my_units)
    st2_fc = beam_tr_shear_stress_op.outputs.fields_container()

    st2_mod = model.results.beam_tr_shear_stress(time_scoping=time_sco).eval()

    assert np.allclose(st2_fc[0].data, st2_mod[0].data)
    assert st2_fc[0].unit == "kPa"
    assert st2_mod[0].unit == "kPa"

    # ------------------------------------------------- Axial Plastic Strain

    beam_axial_plastic_strain_op = dpf.operators.result.beam_axial_plastic_strain()
    beam_axial_plastic_strain_op.inputs.time_scoping.connect(time_sco)
    beam_axial_plastic_strain_op.inputs.data_sources.connect(ds)
    beam_axial_plastic_strain_op.inputs.unit_system.connect(my_units)
    bel_fc = beam_axial_plastic_strain_op.outputs.fields_container()

    bel_mod = model.results.beam_axial_plastic_strain(time_scoping=time_sco).eval()

    assert np.allclose(bel_fc[0].data, bel_mod[0].data)
    assert bel_fc[0].unit == ""
    assert bel_mod[0].unit == ""

    # ------------------------------------------------- Axial Total Strain

    beam_axial_total_strain_op = dpf.operators.result.beam_axial_total_strain()
    beam_axial_total_strain_op.inputs.time_scoping.connect(time_sco)
    beam_axial_total_strain_op.inputs.data_sources.connect(ds)
    beam_axial_total_strain_op.inputs.unit_system.connect(my_units)
    beam_axial_total_strain_fc = beam_axial_total_strain_op.outputs.fields_container()

    beam_axial_total_strain_model = model.results.beam_axial_total_strain(
        time_scoping=time_sco
    ).eval()

    assert np.allclose(beam_axial_total_strain_fc[0].data, beam_axial_total_strain_model[0].data)
    assert beam_axial_total_strain_fc[0].unit == ""
    assert beam_axial_total_strain_model[0].unit == ""


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_1,
    reason="LS-DYNA source operators where not supported before 6.0,"
    " and unit systems where not supported before 6.1.",
)
def test_lsdyna_matsum_rcforc(binout_matsum):
    ds = dpf.DataSources()
    ds.set_result_file_path(binout_matsum, "binout")
    part_sco = dpf.Scoping()
    part_sco.ids = [50]
    part_sco.location = "part"

    model = dpf.Model(ds)

    # ------------------------------------------------- Kinetic Energy

    kinetic_energy_op = dpf.operators.result.part_kinetic_energy()
    kinetic_energy_op.inputs.data_sources.connect(ds)
    kinetic_energy_op.inputs.entity_scoping.connect(part_sco)
    kinetic_energy_op.connect(50, dpf.unit_systems.solver_bft)
    ke_fc = kinetic_energy_op.outputs.fields_container()

    kinetic_energy_op_2 = model.results.part_kinetic_energy()
    kinetic_energy_op_2.inputs.entity_scoping.connect(part_sco)
    kinetic_energy_op_2.inputs.unit_system.connect(dpf.unit_systems.solver_bft)  # just once
    ke_mod = kinetic_energy_op_2.eval()

    assert np.allclose(ke_fc[0].data[39], ke_mod[0].data[39])
    assert ke_fc[0].unit == "ft^2*slug*s^-2"
    assert ke_mod[0].unit == "ft^2*slug*s^-2"

    # ------------------------------------------------- Eroded Kinetic Energy

    part_eroded_kinetic_energy_op = dpf.operators.result.part_eroded_kinetic_energy()
    part_eroded_kinetic_energy_op.inputs.data_sources.connect(ds)
    part_eroded_kinetic_energy_op.inputs.entity_scoping.connect(part_sco)
    part_eroded_kinetic_energy_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    part_eroded_kinetic_energy_fc = part_eroded_kinetic_energy_op.outputs.fields_container()

    part_eroded_kinetic_energy_op_2 = model.results.part_eroded_kinetic_energy()
    part_eroded_kinetic_energy_op_2.inputs.entity_scoping.connect(part_sco)
    part_eroded_kinetic_energy_model = part_eroded_kinetic_energy_op_2.eval()

    assert np.allclose(
        part_eroded_kinetic_energy_fc[0].data[39],
        part_eroded_kinetic_energy_model[0].data[39],
    )
    assert part_eroded_kinetic_energy_fc[0].unit == "ft^2*slug*s^-2"
    assert part_eroded_kinetic_energy_model[0].unit == "ft^2*slug*s^-2"

    # ------------------------------------------------- Internal Energy

    internal_energy_op = dpf.operators.result.part_internal_energy()
    internal_energy_op.inputs.data_sources.connect(ds)
    internal_energy_op.inputs.entity_scoping.connect(part_sco)
    internal_energy_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    ie_fc = internal_energy_op.outputs.fields_container()

    internal_energy_op_2 = model.results.part_internal_energy()
    internal_energy_op_2.inputs.entity_scoping.connect(part_sco)
    ie_mod = internal_energy_op_2.eval()

    assert np.allclose(ie_fc[0].data[39], ie_mod[0].data[39])
    assert ie_fc[0].unit == "ft^2*slug*s^-2"
    assert ie_mod[0].unit == "ft^2*slug*s^-2"

    # ------------------------------------------------- Eroded Internal Energy

    part_eroded_internal_energy_op = dpf.operators.result.part_eroded_internal_energy()
    part_eroded_internal_energy_op.inputs.data_sources.connect(ds)
    part_eroded_internal_energy_op.inputs.entity_scoping.connect(part_sco)
    part_eroded_internal_energy_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    erie_fc = part_eroded_internal_energy_op.outputs.fields_container()

    part_eroded_internal_energy_op_2 = model.results.part_eroded_internal_energy()
    part_eroded_internal_energy_op_2.inputs.entity_scoping.connect(part_sco)
    erie_mod = part_eroded_internal_energy_op_2.eval()

    assert np.allclose(erie_fc[0].data[39], erie_mod[0].data[39])
    assert erie_fc[0].unit == "ft^2*slug*s^-2"
    assert erie_mod[0].unit == "ft^2*slug*s^-2"

    # ------------------------------------------------- Added Mass

    part_added_mass_op = dpf.operators.result.part_added_mass()
    part_added_mass_op.inputs.data_sources.connect(ds)
    part_added_mass_op.inputs.entity_scoping.connect(part_sco)
    part_added_mass_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    am_fc = part_added_mass_op.outputs.fields_container()

    part_added_mass_op_2 = model.results.part_added_mass()
    part_added_mass_op_2.inputs.entity_scoping.connect(part_sco)
    am_mod = part_added_mass_op_2.eval()

    assert np.allclose(am_fc[0].data[39], am_mod[0].data[39])
    assert am_fc[0].unit == "slug"
    assert am_mod[0].unit == "slug"

    # ------------------------------------------------- Momentum

    part_momentum_op = dpf.operators.result.part_momentum()
    part_momentum_op.inputs.data_sources.connect(ds)
    part_momentum_op.inputs.entity_scoping.connect(part_sco)
    part_momentum_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    mv_fc = part_momentum_op.outputs.fields_container()

    part_momentum_op_2 = model.results.part_momentum()
    part_momentum_op_2.inputs.entity_scoping.connect(part_sco)
    mv_mod = part_momentum_op_2.eval()

    assert np.allclose(mv_fc[0].data[39], mv_mod[0].data[39])
    assert mv_fc[0].unit == "ft*slug*Hz"
    assert mv_mod[0].unit == "ft*slug*Hz"

    # ------------------------------------------------- RB Velocity

    part_rigid_body_velocity_op = dpf.operators.result.part_rigid_body_velocity()
    part_rigid_body_velocity_op.inputs.data_sources.connect(ds)
    part_rigid_body_velocity_op.inputs.entity_scoping.connect(part_sco)
    part_rigid_body_velocity_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    rbv_fc = part_rigid_body_velocity_op.outputs.fields_container()

    part_rigid_body_velocity_op_2 = model.results.part_rigid_body_velocity()
    part_rigid_body_velocity_op_2.inputs.entity_scoping.connect(part_sco)
    rbv_mod = part_rigid_body_velocity_op_2.eval()

    assert np.allclose(rbv_fc[0].data[39], rbv_mod[0].data[39])
    assert rbv_fc[0].unit == "ft*Hz"
    assert rbv_mod[0].unit == "ft*Hz"

    # RCFORC RESULTS
    interface_sco = dpf.Scoping()
    interface_sco.ids = [19]
    interface_sco.location = "interface"

    # ------------------------------------------------- Contact Force

    interface_contact_force_op = dpf.operators.result.interface_contact_force()
    interface_contact_force_op.inputs.data_sources.connect(ds)
    interface_contact_force_op.inputs.entity_scoping.connect(interface_sco)
    interface_contact_force_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    cf_fc = interface_contact_force_op.outputs.fields_container()

    interface_contact_force_op_2 = model.results.interface_contact_force()
    interface_contact_force_op_2.inputs.entity_scoping.connect(interface_sco)
    cf_mod = interface_contact_force_op_2.eval()

    assert np.allclose(cf_fc[0].data[0], cf_mod[0].data[0])
    assert cf_fc[0].unit == "ft*slug*s^-2"
    assert cf_mod[0].unit == "ft*slug*s^-2"

    # ------------------------------------------------- Contact Mass

    interface_contact_mass_op = dpf.operators.result.interface_contact_mass()
    interface_contact_mass_op.inputs.data_sources.connect(ds)
    interface_contact_mass_op.inputs.entity_scoping.connect(interface_sco)
    interface_contact_mass_op.inputs.unit_system.connect(dpf.unit_systems.solver_bft)
    cm_fc = interface_contact_mass_op.outputs.fields_container()

    interface_contact_mass_op_2 = model.results.interface_contact_mass()
    interface_contact_mass_op_2.inputs.entity_scoping.connect(interface_sco)
    cm_mod = interface_contact_mass_op_2.eval()

    assert np.allclose(cm_fc[0].data[2], cm_mod[0].data[2])
    assert cm_fc[0].unit == "slug"
    assert cm_mod[0].unit == "slug"


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
    reason="LS-DYNA source operators where not supported before 6.0",
)
def test_lsdyna_glstat(binout_glstat):
    ds = dpf.DataSources()
    ds.set_result_file_path(binout_glstat, "binout")
    model = dpf.Model(ds)

    # ------------------------------------------------- Global Time Step

    global_time_step_op = dpf.operators.result.global_time_step()
    global_time_step_op.inputs.data_sources.connect(ds)
    dt_fc = global_time_step_op.outputs.fields_container()

    dt_mod = model.results.global_time_step().eval()

    assert np.allclose(dt_fc[0].data, dt_mod[0].data)
    assert dt_fc[0].unit == ""
    assert dt_mod[0].unit == ""

    # ------------------------------------------------- Global Kinetic Energy

    global_kinetic_energy_op = dpf.operators.result.global_kinetic_energy()
    global_kinetic_energy_op.inputs.data_sources.connect(ds)
    ke_fc = global_kinetic_energy_op.outputs.fields_container()

    ke_mod = model.results.global_kinetic_energy().eval()

    assert np.allclose(ke_fc[0].data, ke_mod[0].data)
    assert ke_fc[0].unit == ""
    assert ke_mod[0].unit == ""

    # ------------------------------------------------- Global Internal Energy

    global_internal_energy_op = dpf.operators.result.global_internal_energy()
    global_internal_energy_op.inputs.data_sources.connect(ds)
    ie_fc = global_internal_energy_op.outputs.fields_container()

    ie_mod = model.results.global_internal_energy().eval()

    assert np.allclose(ie_fc[0].data, ie_mod[0].data)
    assert ie_fc[0].unit == ""
    assert ie_mod[0].unit == ""

    # ------------------------------------------------- Global Spring and Damper Energy

    global_spring_damper_energy_op = dpf.operators.result.global_spring_damper_energy()
    global_spring_damper_energy_op.inputs.data_sources.connect(ds)
    kde_fc = global_spring_damper_energy_op.outputs.fields_container()

    kde_mod = model.results.global_spring_damper_energy().eval()

    assert np.allclose(kde_fc[0].data, kde_mod[0].data)
    assert kde_fc[0].unit == ""
    assert kde_mod[0].unit == ""

    # ------------------------------------------------- Global System Damping Energy

    global_system_damping_energy_op = dpf.operators.result.global_system_damping_energy()
    global_system_damping_energy_op.inputs.data_sources.connect(ds)
    sde_fc = global_system_damping_energy_op.outputs.fields_container()

    sde_mod = model.results.global_system_damping_energy().eval()

    assert np.allclose(sde_fc[0].data, sde_mod[0].data)
    assert sde_fc[0].unit == ""
    assert sde_mod[0].unit == ""

    # ------------------------------------------------- Global Sliding Interface Energy

    glob_slid_int_energy_op = dpf.operators.result.global_sliding_interface_energy()
    glob_slid_int_energy_op.inputs.data_sources.connect(ds)
    glob_slid_int_energy_fc = glob_slid_int_energy_op.outputs.fields_container()

    glob_slid_int_energy_mod = model.results.global_sliding_interface_energy().eval()

    assert np.allclose(glob_slid_int_energy_fc[0].data, glob_slid_int_energy_mod[0].data)
    assert glob_slid_int_energy_fc[0].unit == ""
    assert glob_slid_int_energy_mod[0].unit == ""

    # ------------------------------------------------- Global External Work

    global_external_work_op = dpf.operators.result.global_external_work()
    global_external_work_op.inputs.data_sources.connect(ds)
    ew_fc = global_external_work_op.outputs.fields_container()

    ew_mod = model.results.global_external_work().eval()

    assert np.allclose(ew_fc[0].data, ew_mod[0].data)
    assert ew_fc[0].unit == ""
    assert ew_mod[0].unit == ""

    # ------------------------------------------------- Global Eroded Kinetic Energy

    global_eroded_kinetic_energy_op = dpf.operators.result.global_eroded_kinetic_energy()
    global_eroded_kinetic_energy_op.inputs.data_sources.connect(ds)
    global_eroded_kinetic_energy_fc = global_eroded_kinetic_energy_op.outputs.fields_container()

    global_eroded_kinetic_energy_model = model.results.global_eroded_kinetic_energy().eval()

    assert np.allclose(
        global_eroded_kinetic_energy_fc[0].data,
        global_eroded_kinetic_energy_model[0].data,
    )
    assert global_eroded_kinetic_energy_fc[0].unit == ""
    assert global_eroded_kinetic_energy_model[0].unit == ""

    # ------------------------------------------------- Global Eroded Internal Energy

    global_eroded_internal_energy_op = dpf.operators.result.global_eroded_internal_energy()
    global_eroded_internal_energy_op.inputs.data_sources.connect(ds)
    erie_fc = global_eroded_internal_energy_op.outputs.fields_container()

    erie_mod = model.results.global_eroded_internal_energy().eval()

    assert np.allclose(erie_fc[0].data, erie_mod[0].data)
    assert erie_fc[0].unit == ""
    assert erie_mod[0].unit == ""

    # ------------------------------------------------- Global Eroded Hourglass Energy

    global_eroded_hourglass_energy_op = dpf.operators.result.global_eroded_hourglass_energy()
    global_eroded_hourglass_energy_op.inputs.data_sources.connect(ds)
    global_eroded_hourglass_energy_fc = global_eroded_hourglass_energy_op.outputs.fields_container()

    global_eroded_hourglass_energy_mod = model.results.global_eroded_hourglass_energy().eval()

    assert np.allclose(
        global_eroded_hourglass_energy_fc[0].data,
        global_eroded_hourglass_energy_mod[0].data,
    )
    assert global_eroded_hourglass_energy_fc[0].unit == ""
    assert global_eroded_hourglass_energy_mod[0].unit == ""

    # ------------------------------------------------- Global Total Energy

    total_energy_op = dpf.operators.result.global_total_energy()
    total_energy_op.inputs.data_sources.connect(ds)
    total_energy_fc = total_energy_op.outputs.fields_container()

    total_energy_mod = model.results.global_total_energy().eval()

    assert np.allclose(total_energy_fc[0].data, total_energy_mod[0].data)
    assert total_energy_fc[0].unit == ""
    assert total_energy_mod[0].unit == ""

    # ------------------------------------------------- Global Energy Ratio

    global_energy_ratio_op = dpf.operators.result.global_energy_ratio()
    global_energy_ratio_op.inputs.data_sources.connect(ds)
    er_fc = global_energy_ratio_op.outputs.fields_container()

    er_mod = model.results.global_energy_ratio().eval()

    assert np.allclose(er_fc[0].data, er_mod[0].data)
    assert er_fc[0].unit == ""
    assert er_mod[0].unit == ""

    # ------------------------------------------------- Global Energy Ratio without Eroded Energy

    global_energy_ratio_wo_eroded_op = dpf.operators.result.global_energy_ratio_wo_eroded()
    global_energy_ratio_wo_eroded_op.inputs.data_sources.connect(ds)
    global_energy_ratio_wo_eroded_fc = global_energy_ratio_wo_eroded_op.outputs.fields_container()

    global_energy_ratio_wo_eroded_mod = model.results.global_energy_ratio_wo_eroded().eval()

    assert np.allclose(
        global_energy_ratio_wo_eroded_fc[0].data,
        global_energy_ratio_wo_eroded_mod[0].data,
    )
    assert global_energy_ratio_wo_eroded_fc[0].unit == ""
    assert global_energy_ratio_wo_eroded_mod[0].unit == ""

    # ------------------------------------------------- Global Velocity

    global_velocity_op = dpf.operators.result.global_velocity()
    global_velocity_op.inputs.data_sources.connect(ds)
    v_fc = global_velocity_op.outputs.fields_container()

    v_mod = model.results.global_velocity().eval()

    assert np.allclose(v_fc[0].data, v_mod[0].data)
    assert v_fc[0].unit == ""
    assert v_mod[0].unit == ""
