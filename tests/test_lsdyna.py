import numpy as np
from ansys.dpf import core as dpf
import pytest

def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNAHGP.dll", "lsdyna")
        return True
    except:
        return False

@pytest.mark.skipif(
    not try_load_lsdyna_operators(), reason="Couldn't load lsdyna operators"
)
def test_lsdyna_generic(d3plot):
    try_load_lsdyna_operators()

    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot, "d3plot")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([3])
    model = dpf.Model(ds)
    print(model)

    # ------------------------------------------------- Stress Von Mises

    VM = dpf.operators.result.stress_von_mises()
    VM.inputs.time_scoping.connect(time_sco)
    VM.inputs.data_sources.connect(ds)
    vm_op = VM.outputs.fields_container()

    vm_mod = model.results.stress_von_mises(time_scoping=time_sco).eval()

    assert np.allclose(vm_op[0].data, vm_mod[0].data)

    # ------------------------------------------------- Global Kinetic energy

    KE = dpf.operators.result.global_kinetic_energy()
    KE.inputs.time_scoping.connect(time_sco)
    KE.inputs.data_sources.connect(ds)
    ke_op = KE.outputs.fields_container()

    ke_mod = model.results.global_kinetic_energy(time_scoping=time_sco).eval()

    assert np.allclose(ke_op[0].data, ke_mod[0].data)

    # ------------------------------------------------- Global Internal energy

    IE = dpf.operators.result.global_internal_energy()
    IE.inputs.time_scoping.connect(time_sco)
    IE.inputs.data_sources.connect(ds)
    ie_op = IE.outputs.fields_container()

    ie_mod = model.results.global_internal_energy(time_scoping=time_sco).eval()

    assert np.allclose(ie_op[0].data[0], ie_mod[0].data[0])

    # ------------------------------------------------- Global Total energy

    TE = dpf.operators.result.global_total_energy()
    TE.inputs.time_scoping.connect(time_sco)
    TE.inputs.data_sources.connect(ds)
    te_op = TE.outputs.fields_container()

    te_mod = model.results.global_total_energy(time_scoping=time_sco).eval()

    assert np.allclose(te_op[0].data[0], te_mod[0].data[0])

    # ------------------------------------------------- Global velocity

    GV = dpf.operators.result.global_velocity()
    GV.inputs.time_scoping.connect(time_sco)
    GV.inputs.data_sources.connect(ds)
    gv_op = GV.outputs.fields_container()

    gv_mod = model.results.global_velocity(time_scoping=time_sco).eval()

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


@pytest.mark.skipif(
    not try_load_lsdyna_operators(), reason="Couldn't load lsdyna operators"
)
def test_lsdyna_beam(d3plot_beam):
    try_load_lsdyna_operators()

    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_beam, "d3plot")
    time_sco = dpf.time_freq_scoping_factory.scoping_by_sets([5])
    model = dpf.Model(ds)
    print(model)

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
