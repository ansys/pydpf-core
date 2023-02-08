import numpy as np
import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import examples, server, server_types
from ansys.dpf.core.errors import ServerTypeError
from ansys.dpf.core.server_factory import CommunicationProtocols, ServerConfig
import conftest

if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
    dpf.set_default_server_context(dpf.AvailableServerContexts.entry)


@pytest.fixture(
    scope="module",
    params=[ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)]
    if (isinstance(server._global_server(), server_types.InProcessServer))
    else conftest.remove_none_available_config(
        [
            ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False),
            ServerConfig(protocol=CommunicationProtocols.InProcess, legacy=False),
        ],
        ["gRPC", "inProcess"],
    )[0]
    if isinstance(server._global_server(), server_types.GrpcServer)
    else [ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)],
)
def other_remote_server(request):
    server = dpf.start_local_server(config=request.param, as_global=False)
    if request.param == ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False):
        dpf.settings.get_runtime_client_config(server).cache_enabled = False
    return server


if conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0:
    dpf.server.shutdown_all_session_servers()
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)


@pytest.fixture()
def static_models(local_server, other_remote_server):
    try:
        upload = dpf.upload_file_in_tmp_folder(examples.static_rst, server=other_remote_server)
    except ServerTypeError:
        upload = examples.static_rst
    return (
        dpf.Model(upload, server=other_remote_server),
        dpf.Model(examples.find_static_rst(server=local_server), server=local_server),
    )


@pytest.fixture()
def transient_models(local_server, other_remote_server):
    try:
        upload = dpf.upload_file_in_tmp_folder(examples.msup_transient, server=other_remote_server)
    except ServerTypeError:
        upload = examples.msup_transient
    return (
        dpf.Model(upload, server=other_remote_server),
        dpf.Model(examples.find_msup_transient(server=local_server), server=local_server),
    )


@pytest.fixture()
def cyc_models(local_server, other_remote_server):
    try:
        upload = dpf.upload_file_in_tmp_folder(examples.simple_cyclic, server=other_remote_server)
    except ServerTypeError:
        upload = examples.simple_cyclic
    return (
        dpf.Model(upload, server=other_remote_server),
        dpf.Model(examples.find_simple_cyclic(server=local_server), server=local_server),
    )


def test_different_multi_server(static_models):
    assert static_models[0]._server != static_models[1]._server
    assert not static_models[0]._server == static_models[1]._server
    assert static_models[0]._server.info != static_models[1]._server.info


def test_model_time_freq_multi_server(static_models):
    tf = static_models[0].metadata.time_freq_support
    tf2 = static_models[1].metadata.time_freq_support
    assert tf.time_frequencies.shape == tf2.time_frequencies.shape
    assert tf.time_frequencies.size == tf2.time_frequencies.size
    assert np.allclose(tf.time_frequencies.data, tf2.time_frequencies.data)
    assert np.allclose(tf.time_frequencies.scoping.ids, tf2.time_frequencies.scoping.ids)
    assert tf.n_sets == tf2.n_sets
    assert tf.get_frequency(0, 0) == tf2.get_frequency(0, 0)
    assert tf.get_cumulative_index(0, 0) == tf2.get_cumulative_index(0, 0)


# make sure that after starting a first local server we are still using
# 2 different servers
def test_different_multi_server2(static_models):
    assert static_models[0]._server != static_models[1]._server
    assert not static_models[0]._server == static_models[1]._server
    assert static_models[0]._server.info != static_models[1]._server.info


def test_model_mesh_multi_server(static_models):
    mesh = static_models[0].metadata.meshed_region
    mesh2 = static_models[1].metadata.meshed_region
    assert mesh.unit == mesh2.unit
    assert mesh.available_named_selections == mesh2.available_named_selections
    assert np.allclose(
        mesh.named_selection(mesh.available_named_selections[0]).ids,
        mesh2.named_selection(mesh2.available_named_selections[0]).ids,
    )

    elements = mesh.elements
    elements2 = mesh2.elements
    assert np.allclose(elements.scoping.ids, elements2.scoping.ids)
    assert np.allclose(elements.element_types_field.data, elements2.element_types_field.data)
    assert np.allclose(elements.connectivities_field.data, elements2.connectivities_field.data)
    assert np.allclose(elements.materials_field.data, elements2.materials_field.data)
    assert elements.n_elements == elements2.n_elements
    assert elements.has_shell_elements == elements2.has_shell_elements
    assert elements.has_solid_elements == elements2.has_solid_elements
    assert elements.has_beam_elements == elements2.has_beam_elements
    assert elements.has_point_elements == elements2.has_point_elements

    nodes = mesh.nodes
    nodes2 = mesh2.nodes
    assert np.allclose(nodes.scoping.ids, nodes2.scoping.ids)


def test_model_result_info_multi_server(static_models):
    result_info = static_models[0].metadata.result_info
    result_info2 = static_models[1].metadata.result_info
    assert result_info.analysis_type == result_info2.analysis_type
    assert result_info.physics_type == result_info2.physics_type
    assert result_info.unit_system == result_info2.unit_system
    assert result_info.cyclic_symmetry_type == result_info2.cyclic_symmetry_type
    assert result_info.has_cyclic == result_info2.has_cyclic
    available_results = result_info.available_results
    available_results2 = result_info2.available_results
    for i, res in enumerate(available_results):
        assert res.name == available_results2[i].name
        assert res.n_components == available_results2[i].n_components
        assert res.dimensionality == available_results2[i].dimensionality
        assert res.homogeneity == available_results2[i].homogeneity
        assert res.unit == available_results2[i].unit
        assert res.operator_name == available_results2[i].operator_name
        assert res.sub_results == available_results2[i].sub_results


def test_model_cyc_support_multi_server(cyc_models):
    result_info = cyc_models[0].metadata.result_info
    result_info2 = cyc_models[1].metadata.result_info
    assert result_info.has_cyclic == result_info2.has_cyclic
    assert result_info.cyclic_symmetry_type == result_info2.cyclic_symmetry_type
    cyc_support = result_info.cyclic_support
    cyc_support2 = result_info2.cyclic_support
    assert cyc_support.num_stages == cyc_support2.num_stages
    assert cyc_support.num_sectors() == cyc_support2.num_sectors()
    assert np.allclose(cyc_support.base_nodes_scoping().ids, cyc_support2.base_nodes_scoping().ids)
    assert np.allclose(
        cyc_support.base_elements_scoping().ids,
        cyc_support2.base_elements_scoping().ids,
    )
    assert np.allclose(
        cyc_support.sectors_set_for_expansion().ids,
        cyc_support2.sectors_set_for_expansion().ids,
    )
    assert np.allclose(cyc_support.expand_node_id(1).ids, cyc_support2.expand_node_id(1).ids)
    assert np.allclose(cyc_support.expand_element_id(1).ids, cyc_support2.expand_element_id(1).ids)
    assert np.allclose(
        cyc_support.expand_node_id(1, cyc_support.sectors_set_for_expansion()).ids,
        cyc_support2.expand_node_id(1, cyc_support2.sectors_set_for_expansion()).ids,
    )
    assert np.allclose(
        cyc_support.expand_element_id(1, cyc_support.sectors_set_for_expansion()).ids,
        cyc_support2.expand_element_id(1, cyc_support2.sectors_set_for_expansion()).ids,
    )


def test_model_displacement_multi_server(transient_models):
    tf = transient_models[0].metadata.time_freq_support
    time_scoping = range(1, 3)
    disp = transient_models[0].results.displacement()
    disp.inputs.time_scoping(time_scoping)
    disp2 = transient_models[1].results.displacement()
    disp2.inputs.time_scoping(time_scoping)
    fc = disp.outputs.fields_container()
    fc2 = disp2.outputs.fields_container()
    for i, f in enumerate(fc):
        assert fc.get_label_space(i) == fc2.get_label_space(i)
        ftocheck = fc2[i].deep_copy(server=f._server)
        iden = dpf.operators.logic.identical_fields(f, ftocheck, server=f._server)
        assert iden.outputs.boolean()
        assert np.allclose(f.data, fc2[i].data)
        assert np.allclose(f.scoping.ids, fc2[i].scoping.ids)
        assert np.allclose(f.data, ftocheck.data)
        assert np.allclose(f.scoping.ids, ftocheck.scoping.ids)


def check_fc(fc, fc2):
    for i, f in enumerate(fc):
        assert fc.get_label_space(i) == fc2.get_label_space(i)
        ftocheck = fc2[i].deep_copy(server=f._server)
        iden = dpf.operators.logic.identical_fields(f, ftocheck, server=f._server)
        assert iden.outputs.boolean()
        assert np.allclose(f.data, fc2[i].data)
        assert np.allclose(f.scoping.ids, fc2[i].scoping.ids)
        assert np.allclose(f.data, ftocheck.data)
        assert np.allclose(f.scoping.ids, ftocheck.scoping.ids)
    idenfc = dpf.operators.logic.identical_fc(fc, fc2.deep_copy(server=f._server), server=f._server)
    assert idenfc.outputs.boolean()


def test_model_stress_multi_server(transient_models):
    tf = transient_models[0].metadata.time_freq_support
    time_scoping = range(1, 3)
    disp = transient_models[0].results.stress()
    disp.inputs.time_scoping(time_scoping)
    disp2 = transient_models[1].results.stress()
    disp2.inputs.time_scoping(time_scoping)
    fc = disp.outputs.fields_container()
    fc2 = disp2.outputs.fields_container()
    check_fc(fc, fc2)
    idenfc = dpf.operators.logic.identical_fc(fc.deep_copy(fc2._server), fc2, server=fc2._server)
    assert idenfc.outputs.boolean()
