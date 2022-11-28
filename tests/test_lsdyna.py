import numpy as np
import pytest
import conftest
from ansys.dpf import core as dpf

@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='LS-DYNA source operators where not supported before 0.6')
def test_lsdyna_generic(d3plot):
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot, "d3plot")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([3])
    model = dpf.Model(ds)

    # ------------------------------------------------- Stress Von Mises

    VM = dpf.operators.result.stress_von_mises()
    VM.inputs.time_scoping.connect(time_sco)
    VM.inputs.data_sources.connect(ds)
    vm_op = VM.outputs.fields_container()

    vm_mod = model.results.stress_von_mises(time_scoping=time_sco).eval()

    assert np.allclose(vm_op[0].data, vm_mod[0].data)

    # ------------------------------------------------- Global Kinetic energy

    KE = dpf.operators.result.global_kinetic_energy()
    KE.inputs.data_sources.connect(ds)
    ke_op = KE.outputs.fields_container()

    ke_mod = model.results.global_kinetic_energy().eval()

    assert np.allclose(ke_op[0].data, ke_mod[0].data)

    # ------------------------------------------------- Global Internal energy

    IE = dpf.operators.result.global_internal_energy()
    IE.inputs.data_sources.connect(ds)
    ie_op = IE.outputs.fields_container()

    ie_mod = model.results.global_internal_energy().eval()

    assert np.allclose(ie_op[0].data[0], ie_mod[0].data[0])

    # ------------------------------------------------- Global Total energy

    TE = dpf.operators.result.global_total_energy()
    TE.inputs.data_sources.connect(ds)
    te_op = TE.outputs.fields_container()

    te_mod = model.results.global_total_energy().eval()

    assert np.allclose(te_op[0].data[0], te_mod[0].data[0])

    # ------------------------------------------------- Global velocity

    GV = dpf.operators.result.global_velocity()
    GV.inputs.data_sources.connect(ds)
    gv_op = GV.outputs.fields_container()

    gv_mod = model.results.global_velocity().eval()

    assert np.allclose(gv_op[0].data[0], gv_mod[0].data[0])

    # ------------------------------------------------- Initial Coordinates

    XI = dpf.operators.result.initial_coordinates()
    XI.inputs.time_scoping.connect(time_sco)
    XI.inputs.data_sources.connect(ds)
    xi_op = XI.outputs.fields_container()

    xi_mod = model.results.initial_coordinates(time_scoping=time_sco).eval()

    assert np.allclose(xi_op[0].data, xi_mod[0].data)

    # ------------------------------------------------- Coordinates

    X = dpf.operators.result.coordinates()
    X.inputs.time_scoping.connect(time_sco)
    X.inputs.data_sources.connect(ds)
    x_op = X.outputs.fields_container()

    x_mod = model.results.coordinates(time_scoping=time_sco).eval()

    assert np.allclose(x_op[0].data, x_mod[0].data)
    # ------------------------------------------------- Node Velocity

    V = dpf.operators.result.velocity()
    V.inputs.time_scoping.connect(time_sco)
    V.inputs.data_sources.connect(ds)
    v_op = V.outputs.fields_container()

    v_mod = model.results.velocity(time_scoping=time_sco).eval()

    assert np.allclose(v_op[0].data, v_mod[0].data)

    # ------------------------------------------------- Node Acceleration

    A = dpf.operators.result.acceleration()
    A.inputs.time_scoping.connect(time_sco)
    A.inputs.data_sources.connect(ds)
    a_op = A.outputs.fields_container()

    a_mod = model.results.acceleration(time_scoping=time_sco).eval()

    assert np.allclose(a_op[0].data, a_mod[0].data)

    # ------------------------------------------------- Effective Plastic Strain

    EPL = dpf.operators.result.plastic_strain_eqv()
    EPL.inputs.time_scoping.connect(time_sco)
    EPL.inputs.data_sources.connect(ds)
    epl_op = EPL.outputs.fields_container()

    epl_mod = model.results.plastic_strain_eqv(time_scoping=time_sco).eval()

    assert np.allclose(epl_op[0].data, epl_mod[0].data)

@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='LS-DYNA source operators where not supported before 0.6')
def test_lsdyna_beam(d3plot_beam):
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_beam, "d3plot")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([5])
    model = dpf.Model(ds)

    # ------------------------------------------------- Axial Force

    N = dpf.operators.result.beam_axial_force()
    N.inputs.time_scoping.connect(time_sco)
    N.inputs.data_sources.connect(ds)
    n_op = N.outputs.fields_container()

    n_mod = model.results.beam_axial_force(time_scoping=time_sco).eval()

    assert np.allclose(n_op[0].data, n_mod[0].data)

    # ------------------------------------------------- S Shear Force

    T1 = dpf.operators.result.beam_s_shear_force()
    T1.inputs.time_scoping.connect(time_sco)
    T1.inputs.data_sources.connect(ds)
    t1_op = T1.outputs.fields_container()

    t1_mod = model.results.beam_s_shear_force(time_scoping=time_sco).eval()

    assert np.allclose(t1_op[0].data, t1_mod[0].data)

    # ------------------------------------------------- T Shear Force

    T2 = dpf.operators.result.beam_t_shear_force()
    T2.inputs.time_scoping.connect(time_sco)
    T2.inputs.data_sources.connect(ds)
    t2_op = T2.outputs.fields_container()

    t2_mod = model.results.beam_t_shear_force(time_scoping=time_sco).eval()

    assert np.allclose(t2_op[0].data, t2_mod[0].data)

    # ------------------------------------------------- Bending S Moment

    M1 = dpf.operators.result.beam_s_bending_moment()
    M1.inputs.time_scoping.connect(time_sco)
    M1.inputs.data_sources.connect(ds)
    m1_op = M1.outputs.fields_container()

    m1_mod = model.results.beam_s_bending_moment(time_scoping=time_sco).eval()

    assert np.allclose(m1_op[0].data, m1_mod[0].data)

    # ------------------------------------------------- Bending T Moment

    M2 = dpf.operators.result.beam_t_bending_moment()
    M2.inputs.time_scoping.connect(time_sco)
    M2.inputs.data_sources.connect(ds)
    m2_op = M2.outputs.fields_container()

    m2_mod = model.results.beam_t_bending_moment(time_scoping=time_sco).eval()

    assert np.allclose(m2_op[0].data, m2_mod[0].data)

    # ------------------------------------------------- Torsional Moment

    MT = dpf.operators.result.beam_torsional_moment()
    MT.inputs.time_scoping.connect(time_sco)
    MT.inputs.data_sources.connect(ds)
    mt_op = MT.outputs.fields_container()

    mt_mod = model.results.beam_torsional_moment(time_scoping=time_sco).eval()

    assert np.allclose(mt_op[0].data, mt_mod[0].data)
    # ------------------------------------------------- Axial stress

    SN = dpf.operators.result.beam_axial_stress()
    SN.inputs.time_scoping.connect(time_sco)
    SN.inputs.data_sources.connect(ds)
    sn_op = SN.outputs.fields_container()

    sn_mod = model.results.beam_axial_stress(time_scoping=time_sco).eval()

    assert np.allclose(sn_op[0].data, sn_mod[0].data)

    # ------------------------------------------------- Shear RS Stress

    ST1 = dpf.operators.result.beam_rs_shear_stress()
    ST1.inputs.time_scoping.connect(time_sco)
    ST1.inputs.data_sources.connect(ds)
    st1_op = ST1.outputs.fields_container()

    st1_mod = model.results.beam_rs_shear_stress(time_scoping=time_sco).eval()

    assert np.allclose(st1_op[0].data, st1_mod[0].data)

    # ------------------------------------------------- Shear TR Stress

    ST2 = dpf.operators.result.beam_tr_shear_stress()
    ST2.inputs.time_scoping.connect(time_sco)
    ST2.inputs.data_sources.connect(ds)
    st2_op = ST2.outputs.fields_container()

    st2_mod = model.results.beam_tr_shear_stress(time_scoping=time_sco).eval()

    assert np.allclose(st2_op[0].data, st2_mod[0].data)

    # ------------------------------------------------- Axial Plastic Strain

    BEL = dpf.operators.result.beam_axial_plastic_strain()
    BEL.inputs.time_scoping.connect(time_sco)
    BEL.inputs.data_sources.connect(ds)
    bel_op = BEL.outputs.fields_container()

    bel_mod = model.results.beam_axial_plastic_strain(time_scoping=time_sco).eval()

    assert np.allclose(bel_op[0].data, bel_mod[0].data)

    # ------------------------------------------------- Axial Total Strain

    BEPPL = dpf.operators.result.beam_axial_total_strain()
    BEPPL.inputs.time_scoping.connect(time_sco)
    BEPPL.inputs.data_sources.connect(ds)
    beppl_op = BEPPL.outputs.fields_container()

    beppl_mod = model.results.beam_axial_total_strain(time_scoping=time_sco).eval()

    assert np.allclose(beppl_op[0].data, beppl_mod[0].data)

@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='LS-DYNA source operators where not supported before 0.6')
def test_lsdyna_matsum_rcforc(binout_matsum):
    ds = dpf.DataSources()
    ds.set_result_file_path(binout_matsum, "binout")
    part_sco = dpf.Scoping()
    part_sco.ids = [50]
    part_sco.location = "part"

    model = dpf.Model(ds)

    # ------------------------------------------------- Kinetic Energy

    KE = dpf.operators.result.part_kinetic_energy()
    KE.inputs.data_sources.connect(ds)
    KE.inputs.entity_scoping.connect(part_sco)
    ke_op = KE.outputs.fields_container()

    KE2 = model.results.part_kinetic_energy()
    KE2.inputs.entity_scoping.connect(part_sco)
    ke_mod = KE2.eval()

    assert np.allclose(ke_op[0].data[39], ke_mod[0].data[39])

    # ------------------------------------------------- Eroded Kinetic Energy

    ERKE = dpf.operators.result.part_eroded_kinetic_energy()
    ERKE.inputs.data_sources.connect(ds)
    ERKE.inputs.entity_scoping.connect(part_sco)
    erke_op = ERKE.outputs.fields_container()

    ERKE2 = model.results.part_eroded_kinetic_energy()
    ERKE2.inputs.entity_scoping.connect(part_sco)
    erke_mod = ERKE2.eval()

    assert np.allclose(erke_op[0].data[39], erke_mod[0].data[39])

    # ------------------------------------------------- Internal Energy

    IE = dpf.operators.result.part_internal_energy()
    IE.inputs.data_sources.connect(ds)
    IE.inputs.entity_scoping.connect(part_sco)
    ie_op = IE.outputs.fields_container()

    IE2 = model.results.part_internal_energy()
    IE2.inputs.entity_scoping.connect(part_sco)
    ie_mod = IE2.eval()

    assert np.allclose(ie_op[0].data[39], ie_mod[0].data[39])

    # ------------------------------------------------- Eroded Internal Energy

    ERIE = dpf.operators.result.part_eroded_internal_energy()
    ERIE.inputs.data_sources.connect(ds)
    ERIE.inputs.entity_scoping.connect(part_sco)
    erie_op = ERIE.outputs.fields_container()

    ERIE2 = model.results.part_eroded_internal_energy()
    ERIE2.inputs.entity_scoping.connect(part_sco)
    erie_mod = ERIE2.eval()

    assert np.allclose(erie_op[0].data[39], erie_mod[0].data[39])

    # ------------------------------------------------- Added Mass

    AM = dpf.operators.result.part_added_mass()
    AM.inputs.data_sources.connect(ds)
    AM.inputs.entity_scoping.connect(part_sco)
    am_op = AM.outputs.fields_container()

    AM2 = model.results.part_added_mass()
    AM2.inputs.entity_scoping.connect(part_sco)
    am_mod = AM2.eval()

    assert np.allclose(am_op[0].data[39], am_mod[0].data[39])

    # ------------------------------------------------- Hourglassing Energy

    AHO = dpf.operators.result.part_hourglass_energy()
    AHO.inputs.data_sources.connect(ds)
    AHO.inputs.entity_scoping.connect(part_sco)
    aho_op = AHO.outputs.fields_container()

    AHO2 = model.results.part_hourglass_energy()
    AHO2.inputs.entity_scoping.connect(part_sco)
    aho_mod = AHO2.eval()

    assert np.allclose(aho_op[0].data[39], aho_mod[0].data[39])

    # ------------------------------------------------- Momentum

    MV = dpf.operators.result.part_momentum()
    MV.inputs.data_sources.connect(ds)
    MV.inputs.entity_scoping.connect(part_sco)
    mv_op = MV.outputs.fields_container()

    MV2 = model.results.part_momentum()
    MV2.inputs.entity_scoping.connect(part_sco)
    mv_mod = MV2.eval()

    assert np.allclose(mv_op[0].data[39], mv_mod[0].data[39])

    # ------------------------------------------------- RB Velocity

    RBV = dpf.operators.result.part_rigid_body_velocity()
    RBV.inputs.data_sources.connect(ds)
    RBV.inputs.entity_scoping.connect(part_sco)
    rbv_op = RBV.outputs.fields_container()

    RBV2 = model.results.part_rigid_body_velocity()
    RBV2.inputs.entity_scoping.connect(part_sco)
    rbv_mod = RBV2.eval()

    assert np.allclose(rbv_op[0].data[39], rbv_mod[0].data[39])

    # RCFORC RESULTS
    interface_sco = dpf.Scoping()
    interface_sco.ids = [19]
    interface_sco.location = "interface"

    # ------------------------------------------------- Contact Force

    CF = dpf.operators.result.interface_contact_force()
    CF.inputs.data_sources.connect(ds)
    CF.inputs.entity_scoping.connect(interface_sco)
    cf_op = CF.outputs.fields_container()

    CF2 = model.results.interface_contact_force()
    CF2.inputs.entity_scoping.connect(interface_sco)
    cf_mod = CF2.eval()

    assert np.allclose(cf_op[0].data[0], cf_mod[0].data[0])

    # ------------------------------------------------- Contact Mass

    CM = dpf.operators.result.interface_contact_mass()
    CM.inputs.data_sources.connect(ds)
    CM.inputs.entity_scoping.connect(interface_sco)
    cm_op = CM.outputs.fields_container()

    CM2 = model.results.interface_contact_mass()
    CM2.inputs.entity_scoping.connect(interface_sco)
    cm_mod = CM2.eval()

    assert np.allclose(cm_op[0].data[2], cm_mod[0].data[2])

@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0,
                    reason='LS-DYNA source operators where not supported before 0.6')
def test_lsdyna_glstat(binout_glstat):
    ds = dpf.DataSources()
    ds.set_result_file_path(binout_glstat, "binout")
    model = dpf.Model(ds)

    # ------------------------------------------------- Global Time Step

    DT = dpf.operators.result.global_time_step()
    DT.inputs.data_sources.connect(ds)
    dt_op = DT.outputs.fields_container()

    dt_mod = model.results.global_time_step().eval()

    assert np.allclose(dt_op[0].data, dt_mod[0].data)

    # ------------------------------------------------- Global Kinetic Energy

    KE = dpf.operators.result.global_kinetic_energy()
    KE.inputs.data_sources.connect(ds)
    ke_op = KE.outputs.fields_container()

    ke_mod = model.results.global_kinetic_energy().eval()

    assert np.allclose(ke_op[0].data, ke_mod[0].data)

    # ------------------------------------------------- Global Internal Energy

    IE = dpf.operators.result.global_internal_energy()
    IE.inputs.data_sources.connect(ds)
    ie_op = IE.outputs.fields_container()

    ie_mod = model.results.global_internal_energy().eval()

    assert np.allclose(ie_op[0].data, ie_mod[0].data)

    # ------------------------------------------------- Global Spring and Damper Energy

    KDE = dpf.operators.result.global_spring_damper_energy()
    KDE.inputs.data_sources.connect(ds)
    kde_op = KDE.outputs.fields_container()

    kde_mod = model.results.global_spring_damper_energy().eval()

    assert np.allclose(kde_op[0].data, kde_mod[0].data)

    # ------------------------------------------------- Global System Damping Energy

    SDE = dpf.operators.result.global_system_damping_energy()
    SDE.inputs.data_sources.connect(ds)
    sde_op = SDE.outputs.fields_container()

    sde_mod = model.results.global_system_damping_energy().eval()

    assert np.allclose(sde_op[0].data, sde_mod[0].data)

    # ------------------------------------------------- Global Sliding Interface Energy

    SIE = dpf.operators.result.global_sliding_interface_energy()
    SIE.inputs.data_sources.connect(ds)
    sie_op = SIE.outputs.fields_container()

    sie_mod = model.results.global_sliding_interface_energy().eval()

    assert np.allclose(sie_op[0].data, sie_mod[0].data)

    # ------------------------------------------------- Global External Work

    EW = dpf.operators.result.global_external_work()
    EW.inputs.data_sources.connect(ds)
    ew_op = EW.outputs.fields_container()

    ew_mod = model.results.global_external_work().eval()

    assert np.allclose(ew_op[0].data, ew_mod[0].data)

    # ------------------------------------------------- Global Eroded Kinetic Energy

    ERKE = dpf.operators.result.global_eroded_kinetic_energy()
    ERKE.inputs.data_sources.connect(ds)
    erke_op = ERKE.outputs.fields_container()

    erke_mod = model.results.global_eroded_kinetic_energy().eval()

    assert np.allclose(erke_op[0].data, erke_mod[0].data)

    # ------------------------------------------------- Global Eroded Internal Energy

    ERIE = dpf.operators.result.global_eroded_internal_energy()
    ERIE.inputs.data_sources.connect(ds)
    erie_op = ERIE.outputs.fields_container()

    erie_mod = model.results.global_eroded_internal_energy().eval()

    assert np.allclose(erie_op[0].data, erie_mod[0].data)

    # ------------------------------------------------- Global Eroded Hourglass Energy

    ERAHO = dpf.operators.result.global_eroded_hourglass_energy()
    ERAHO.inputs.data_sources.connect(ds)
    eraho_op = ERAHO.outputs.fields_container()

    eraho_mod = model.results.global_eroded_hourglass_energy().eval()

    assert np.allclose(eraho_op[0].data, eraho_mod[0].data)

    # ------------------------------------------------- Global Total Energy

    TE = dpf.operators.result.global_total_energy()
    TE.inputs.data_sources.connect(ds)
    te_op = TE.outputs.fields_container()

    te_mod = model.results.global_total_energy().eval()

    assert np.allclose(te_op[0].data, te_mod[0].data)

    # ------------------------------------------------- Global Energy Ratio

    ER = dpf.operators.result.global_energy_ratio()
    ER.inputs.data_sources.connect(ds)
    er_op = ER.outputs.fields_container()

    er_mod = model.results.global_energy_ratio().eval()

    assert np.allclose(er_op[0].data, er_mod[0].data)

    # ------------------------------------------------- Global Energy Ratio without Eroded Energy

    ERWO = dpf.operators.result.global_energy_ratio_wo_eroded()
    ERWO.inputs.data_sources.connect(ds)
    erwo_op = ERWO.outputs.fields_container()

    erwo_mod = model.results.global_energy_ratio_wo_eroded().eval()

    assert np.allclose(erwo_op[0].data, erwo_mod[0].data)

    # ------------------------------------------------- Global Velocity

    V = dpf.operators.result.global_velocity()
    V.inputs.data_sources.connect(ds)
    v_op = V.outputs.fields_container()

    v_mod = model.results.global_velocity().eval()

    assert np.allclose(v_op[0].data, v_mod[0].data)
