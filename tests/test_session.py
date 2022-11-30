import os
import conftest
from ansys.dpf import core
from ansys.dpf.core import examples


@conftest.raises_for_servers_version_under("6.1")
def test_logging(tmpdir, server_type):
    server_type.session.handle_events_with_file_logger(os.path.join(tmpdir, "log.txt"), 2)

    wf = core.Workflow(server=server_type)
    model = core.Model(examples.download_pontoon(server=server_type), server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    assert os.path.exists(os.path.join(tmpdir, "log.txt"))
    file_size = os.path.getsize(os.path.join(tmpdir, "log.txt"))
    assert file_size > 20
    server_type._del_session()
    file_size = os.path.getsize(os.path.join(tmpdir, "log.txt"))

    wf = core.Workflow(server=server_type)
    model = core.Model(examples.download_pontoon(server=server_type), server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    assert file_size == os.path.getsize(os.path.join(tmpdir, "log.txt"))


@conftest.raises_for_servers_version_under("6.1")
def test_logging_remote(tmpdir, server_type_remote_process):
    server_type_remote_process.session.handle_events_with_file_logger(
        os.path.join(tmpdir, "log.txt"), 2
    )
    server_type_remote_process.session.start_emitting_rpc_log()

    wf = core.Workflow(server=server_type_remote_process)
    model = core.Model(examples.download_pontoon(server=server_type_remote_process),
                       server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    assert os.path.exists(os.path.join(tmpdir, "log.txt"))
    file_size = os.path.getsize(os.path.join(tmpdir, "log.txt"))
    assert file_size > 3000
    server_type_remote_process._del_session()
    file_size = os.path.getsize(os.path.join(tmpdir, "log.txt"))

    wf = core.Workflow(server=server_type_remote_process)
    model = core.Model(examples.download_pontoon(server=server_type_remote_process),
                       server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    assert file_size == os.path.getsize(os.path.join(tmpdir, "log.txt"))
