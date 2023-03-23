import os
import conftest
import tempfile
from ansys.dpf import core
from ansys.dpf.core import examples


def get_log_file(log_path, server):
    if not isinstance(server, core.server_types.InProcessServer):
        core.core.download_file(
            log_path,
            os.path.join(tempfile.gettempdir(), "log2.txt"),
            server=server,
        )
        return os.path.join(tempfile.gettempdir(), "log2.txt")
    else:
        return log_path


@conftest.raises_for_servers_version_under("6.1")
def test_logging(tmpdir, server_type):
    if not isinstance(server_type, core.server_types.InProcessServer):
        server_tmp = core.core.make_tmp_dir_server(server=server_type)
        result_file = core.upload_file_in_tmp_folder(
            examples.find_static_rst(return_local_path=True, server=server_type),
            server=server_type,
        )
        log_path = os.path.join(server_tmp, "log.txt")
    else:
        log_path = os.path.join(tmpdir, "log.txt")
        result_file = examples.find_static_rst(server=server_type)

    # download it
    new_tmpdir = os.path.join(tmpdir, "my_tmp_dir")
    server_type.session.handle_events_with_file_logger(log_path, 2)

    wf = core.Workflow(server=server_type)
    model = core.Model(result_file, server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = get_log_file(log_path, server_type)
    assert os.path.exists(download_log_path)
    file_size = os.path.getsize(download_log_path)
    assert file_size > 20
    server_type._del_session()
    download_log_path = get_log_file(log_path, server_type)
    file_size = os.path.getsize(download_log_path)

    wf = core.Workflow(server=server_type)
    model = core.Model(result_file, server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = get_log_file(log_path, server_type)
    assert file_size == os.path.getsize(download_log_path)


@conftest.raises_for_servers_version_under("6.1")
def test_logging_remote(tmpdir, server_type_remote_process):
    server_tmp = core.core.make_tmp_dir_server(server=server_type_remote_process)
    result_file = core.upload_file_in_tmp_folder(
        examples.find_multishells_rst(return_local_path=True),
        server=server_type_remote_process,
    )
    log_path = os.path.join(server_tmp, "log.txt")
    server_type_remote_process.session.handle_events_with_file_logger(log_path, 2)
    server_type_remote_process.session.start_emitting_rpc_log()

    wf = core.Workflow(server=server_type_remote_process)
    model = core.Model(result_file, server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = get_log_file(log_path, server_type_remote_process)
    assert os.path.exists(download_log_path)
    file_size = os.path.getsize(download_log_path)
    assert file_size > 3000
    server_type_remote_process._del_session()
    download_log_path = get_log_file(log_path, server_type_remote_process)
    file_size = os.path.getsize(download_log_path)

    wf = core.Workflow(server=server_type_remote_process)
    model = core.Model(result_file, server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = get_log_file(log_path, server_type_remote_process)
    assert file_size == os.path.getsize(download_log_path)
