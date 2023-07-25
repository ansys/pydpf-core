import os

import numpy as np
import pytest

from ansys.dpf import core
from ansys.dpf.core import examples
from ansys.dpf.core.errors import ServerTypeError
from ansys.dpf.core import operators as ops
from conftest import local_servers, running_docker
import conftest


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_simple_remote_workflow(simple_bar, local_server):
    data_sources1 = core.DataSources(simple_bar)
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement(data_sources=data_sources1)
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_output_name("out", average.outputs.fields_container)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    min_max = ops.min_max.min_max_fc()
    local_wf.add_operator(min_max)
    local_wf.set_input_name("in", min_max.inputs.fields_container)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    grpc_stream_provider = ops.metadata.streams_provider()
    grpc_data_sources = core.DataSources()
    grpc_data_sources.set_result_file_path(local_server.ip + ":" + str(local_server.port), "grpc")
    grpc_stream_provider.inputs.data_sources(grpc_data_sources)

    remote_workflow_prov = core.Operator("remote_workflow_instantiate")
    remote_workflow_prov.connect(3, grpc_stream_provider, 0)
    remote_workflow_prov.connect(0, wf)

    remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

    local_wf.connect_with(remote_workflow, ("out", "in"))
    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [2.52368345e-05])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_remote_workflow():
    files = examples.download_distributed_files()
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i])
        wf = core.Workflow()
        wf.progress_bar = False
        op = ops.result.displacement(data_sources=data_sources1)
        average = core.operators.math.norm_fc(op)

        wf.add_operators([op, average])
        wf.set_output_name("distrib" + str(i), average.outputs.fields_container)

        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator("remote_workflow_instantiate")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)

        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

        workflows.append(remote_workflow)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf)

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_connect_remote_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.set_output_name("distrib", average.outputs.fields_container)
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i])

        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator("remote_workflow_instantiate")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)

        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)
        remote_workflow.connect("data_sources", data_sources1)
        workflows.append(remote_workflow)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_connect_operator_remote_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.set_output_name("distrib", average.outputs.fields_container)
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i])

        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator("remote_workflow_instantiate")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)

        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)
        forward = ops.utility.forward(data_sources1)
        remote_workflow.connect("data_sources", forward, 0)
        workflows.append(remote_workflow)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_getoutput_remote_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.set_output_name("distrib", average.outputs.fields_container)
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i])

        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator("remote_workflow_instantiate")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)
        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

        remote_workflow.connect("data_sources", data_sources1)
        workflows.append(remote_workflow)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        tmp = wf.get_output("distrib", core.types.fields_container)
        local_wf.connect("distrib" + str(i), tmp)

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_chain_remote_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.set_output_name("distrib", average.outputs.fields_container)
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i])

        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator("remote_workflow_instantiate")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)
        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

        remote_workflow.connect("data_sources", data_sources1)
        workflows.append(remote_workflow)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)
    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
    grpc_stream_provider = ops.metadata.streams_provider()
    grpc_data_sources = core.DataSources()
    grpc_data_sources.set_result_file_path(
        local_servers[2].ip + ":" + str(local_servers[2].port), "grpc"
    )
    grpc_stream_provider.inputs.data_sources(grpc_data_sources)

    remote_workflow_prov = core.Operator("remote_workflow_instantiate")
    remote_workflow_prov.connect(3, grpc_stream_provider, 0)
    remote_workflow_prov.connect(0, local_wf)
    remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

    for i, wf in enumerate(workflows):
        remote_workflow.connect_with(wf, ("distrib", "distrib" + str(i)))

    max_field = remote_workflow.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_remote_workflow_info(local_server):
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_input_name("data_sources", op.inputs.data_sources)
    wf.set_output_name("distrib", average.outputs.fields_container)
    grpc_stream_provider = ops.metadata.streams_provider()
    grpc_data_sources = core.DataSources()
    grpc_data_sources.set_result_file_path(local_server.ip + ":" + str(local_server.port), "grpc")
    grpc_stream_provider.inputs.data_sources(grpc_data_sources)
    remote_workflow_prov = core.Operator("remote_workflow_instantiate")
    remote_workflow_prov.connect(3, grpc_stream_provider, 0)
    remote_workflow_prov.connect(0, wf)
    remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)
    assert "data_sources" in remote_workflow.input_names
    assert "distrib" in remote_workflow.output_names


@pytest.mark.slow
@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_local_remote_local_remote_workflow(server_type_remote_process):
    files = examples.download_distributed_files()

    wf = core.Workflow(server=server_type_remote_process)
    wf.progress_bar = False
    average = core.operators.math.norm_fc(server=server_type_remote_process)

    wf.add_operators([average])
    wf.set_input_name("u", average.inputs.fields_container)
    wf.set_output_name("distrib", average.outputs.fields_container)
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i], server=server_type_remote_process)

        grpc_stream_provider = ops.metadata.streams_provider(server=server_type_remote_process)
        grpc_data_sources = core.DataSources(server=server_type_remote_process)
        grpc_data_sources.set_result_file_path(
            local_servers[i].ip + ":" + str(local_servers[i].port), "grpc"
        )
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)

        remote_workflow_prov = core.Operator(
            "remote_workflow_instantiate", server=server_type_remote_process
        )
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)
        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)

        first_wf = core.Workflow(server=server_type_remote_process)
        first_wf.progress_bar = False
        op = ops.result.displacement(server=server_type_remote_process)
        first_wf.add_operator(op)
        first_wf.set_input_name("data_sources", op.inputs.data_sources)
        first_wf.set_output_name("u", op.outputs.fields_container)

        first_wf.connect("data_sources", data_sources1)
        remote_workflow.connect_with(first_wf)

        workflows.append(remote_workflow)

    local_wf = core.Workflow(server=server_type_remote_process)
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers(server=server_type_remote_process)
    min_max = ops.min_max.min_max_fc(merge, server=server_type_remote_process)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
def test_multi_process_transparent_api_remote_workflow():
    files = examples.download_distributed_files()
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i], server=local_servers[i])
        wf = core.Workflow(server=local_servers[i])
        wf.progress_bar = False
        op = ops.result.displacement(data_sources=data_sources1, server=local_servers[i])
        average = core.operators.math.norm_fc(op, server=local_servers[i])

        wf.add_operators([op, average])
        wf.set_output_name("distrib" + str(i), average.outputs.fields_container)

        workflows.append(wf)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf)

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
def test_multi_process_with_names_transparent_api_remote_workflow():
    files = examples.download_distributed_files()
    workflows = []
    for i in files:
        data_sources1 = core.DataSources(files[i], server=local_servers[i])
        wf = core.Workflow(server=local_servers[i])
        wf.progress_bar = False
        op = ops.result.displacement(data_sources=data_sources1, server=local_servers[i])
        average = core.operators.math.norm_fc(op, server=local_servers[i])

        wf.add_operators([op, average])
        wf.set_output_name("distrib", average.outputs.fields_container)

        workflows.append(wf)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_transparent_api_connect_local_datasources_remote_workflow():
    files = examples.download_distributed_files()
    workflows = []
    for i in files:
        wf = core.Workflow(server=local_servers[i])
        wf.progress_bar = False
        op = ops.result.displacement(server=local_servers[i])
        average = core.operators.math.norm_fc(op, server=local_servers[i])

        wf.add_operators([op, average])
        wf.set_output_name("distrib" + str(i), average.outputs.fields_container)
        wf.set_input_name("ds", op.inputs.data_sources)
        workflows.append(wf)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        data_sources1 = core.DataSources(files[i])
        wf.connect("ds", data_sources1)
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf)

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(reason="Unstable test")
@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_transparent_api_connect_local_op_remote_workflow():
    files = examples.download_distributed_files()
    workflows = []
    for i in files:
        wf = core.Workflow(server=local_servers[i])
        wf.progress_bar = False
        op = ops.result.displacement(server=local_servers[i])
        average = core.operators.math.norm_fc(op, server=local_servers[i])

        wf.add_operators([op, average])
        wf.set_output_name("distrib" + str(i), average.outputs.fields_container)
        wf.set_input_name("ds", op.inputs.data_sources)
        workflows.append(wf)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i, wf in enumerate(workflows):
        data_sources1 = core.DataSources(files[i])
        forward = ops.utility.forward(data_sources1)
        wf.connect("ds", forward, 0)
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(wf)

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@pytest.mark.skipif(
    (not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0 and os.name == "posix")
    and not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_3_0,
    reason="Connecting data from different servers is " "supported starting server version 3.0",
)
def test_multi_process_transparent_api_create_on_local_remote_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_output_name("distrib", average.outputs.fields_container)
    wf.set_input_name("ds", op.inputs.data_sources)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i in files:
        data_sources1 = core.DataSources(files[i])
        remote_wf = wf.create_on_other_server(server=local_servers[i])
        remote_wf.connect("ds", data_sources1)
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(remote_wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.xfail(raises=ServerTypeError)
@conftest.raises_for_servers_version_under("3.0")
def test_multi_process_transparent_api_create_on_local_remote_ith_address_workflow():
    files = examples.download_distributed_files()
    wf = core.Workflow()
    wf.progress_bar = False
    op = ops.result.displacement()
    average = core.operators.math.norm_fc(op)

    wf.add_operators([op, average])
    wf.set_output_name("distrib", average.outputs.fields_container)
    wf.set_input_name("ds", op.inputs.data_sources)

    local_wf = core.Workflow()
    local_wf.progress_bar = False
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)

    for i in files:
        data_sources1 = core.DataSources(files[i])
        remote_wf = wf.create_on_other_server(ip=local_servers[i].ip, port=local_servers[i].port)
        remote_wf.connect("ds", data_sources1)
        local_wf.set_input_name("distrib" + str(i), merge, i)
        local_wf.connect_with(remote_wf, ("distrib", "distrib" + str(i)))

    max_field = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max_field.data, [10.03242272])


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="Requires server version higher than 4.0",
)
def test_distributed_workflows_integral_types():
    data_types = [
        {"value": True, "type": core.types.bool},
        {"value": 123.0, "type": core.types.double},
        {"value": 123, "type": core.types.int},
        {"value": "hello", "type": core.types.string},
        {"value": [123.0, 456.0, 789.0], "type": core.types.vec_double},
        {"value": [123, 456, 789], "type": core.types.vec_int},
    ]

    server1 = local_servers[0]
    server2 = local_servers[1]

    for data in data_types:
        fwd1 = core.operators.utility.forward(server=server1)
        fwd1.inputs.connect(data["value"])

        fwd2 = core.operators.utility.forward(server=server2)
        fwd2.inputs.connect(fwd1.outputs)

        fwd2.get_output(0, data["type"])
