import numpy as np
from conftest import local_server,local_servers
from ansys.dpf import core
from ansys.dpf.core import operators as ops
from ansys.dpf.core import examples

def test_simple_remote_workflow(simple_bar):
    data_sources1 = core.DataSources(simple_bar)    
    wf = core.Workflow()
    op = ops.result.displacement(data_sources=data_sources1)
    average = core.operators.math.norm_fc(op)
    
    wf.add_operators([op, average])
    wf.set_output_name("out",average.outputs.fields_container)
    
    
    local_wf = core.Workflow()
    min_max = ops.min_max.min_max_fc()
    local_wf.add_operator(min_max)
    local_wf.set_input_name("in", min_max.inputs.fields_container)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)
    
    grpc_stream_provider = ops.metadata.streams_provider()
    grpc_data_sources = core.DataSources()
    grpc_data_sources.set_result_file_path(local_server.ip+":"+ str(local_server.port),"grpc")
    grpc_stream_provider.inputs.data_sources(grpc_data_sources)
    
    remote_workflow_prov = core.Operator("remote_workflow_provider")
    remote_workflow_prov.connect(3, grpc_stream_provider, 0)
    remote_workflow_prov.connect(0, wf)
    
    remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)
    
    local_wf.connect_with(remote_workflow, ("out", "in"))
    max = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max.data, [2.52368345e-05])
    
    

def test_multi_process_remote_workflow():
    files = examples.download_distributed_files()
    workflows =[]
    for i in files:
        data_sources1 = core.DataSources(files[i])    
        wf = core.Workflow()
        op = ops.result.displacement(data_sources=data_sources1)
        average = core.operators.math.norm_fc(op)
        
        wf.add_operators([op, average])
        wf.set_output_name("distrib"+str(i),average.outputs.fields_container)
        
        grpc_stream_provider = ops.metadata.streams_provider()
        grpc_data_sources = core.DataSources()
        grpc_data_sources.set_result_file_path(local_servers[i].ip+":"+ str(local_servers[i].port),"grpc")
        grpc_stream_provider.inputs.data_sources(grpc_data_sources)
        
        remote_workflow_prov = core.Operator("remote_workflow_provider")
        remote_workflow_prov.connect(3, grpc_stream_provider, 0)
        remote_workflow_prov.connect(0, wf)
        
        remote_workflow = remote_workflow_prov.get_output(0, core.types.workflow)
        
        workflows.append(remote_workflow)
        
    local_wf = core.Workflow()
    merge = ops.utility.merge_fields_containers()
    min_max = ops.min_max.min_max_fc(merge)
    local_wf.add_operator(merge)
    local_wf.add_operator(min_max)
    local_wf.set_output_name("tot_output", min_max.outputs.field_max)
    
    for i,wf in enumerate(workflows):
        local_wf.set_input_name("distrib"+str(i), merge, i)
        local_wf.connect_with(wf)    
        

    max = local_wf.get_output("tot_output", core.types.field)
    assert np.allclose(max.data, [10.03242272])
    