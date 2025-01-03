# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
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

from pathlib import Path
import conftest
import tempfile
from ansys.dpf import core
from ansys.dpf.core import examples


def get_log_file(log_path, server):
    if not isinstance(server, core.server_types.InProcessServer):
        core.core.download_file(
            log_path,
            str(Path(tempfile.gettempdir()) / "log2.txt"),
            server=server,
        )
        return str(Path(tempfile.gettempdir()) / "log2.txt")
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
        log_path = Path(server_tmp) / "log.txt"
    else:
        log_path = Path(tmpdir) / "log.txt"
        result_file = examples.find_static_rst(server=server_type)

    # download it
    _ = Path(tmpdir) / "my_tmp_dir"
    server_type.session.handle_events_with_file_logger(str(log_path), 2)

    wf = core.Workflow(server=server_type)
    wf.progress_bar = False
    model = core.Model(result_file, server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = Path(get_log_file(str(log_path), server_type))
    assert download_log_path.exists()
    file_size = download_log_path.stat().st_size
    assert file_size > 20
    server_type._del_session()
    download_log_path = Path(get_log_file(str(log_path), server_type))
    file_size = download_log_path.stat().st_size

    wf = core.Workflow(server=server_type)
    wf.progress_bar = False
    model = core.Model(result_file, server=server_type)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = Path(get_log_file(str(log_path), server_type))
    assert file_size == download_log_path.stat().st_size


@conftest.raises_for_servers_version_under("6.1")
def test_logging_remote(tmpdir, server_type_remote_process):
    server_tmp = core.core.make_tmp_dir_server(server=server_type_remote_process)
    result_file = core.upload_file_in_tmp_folder(
        examples.find_multishells_rst(return_local_path=True),
        server=server_type_remote_process,
    )
    log_path = Path(server_tmp) / "log.txt"
    server_type_remote_process.session.handle_events_with_file_logger(str(log_path), 2)
    server_type_remote_process.session.start_emitting_rpc_log()

    wf = core.Workflow(server=server_type_remote_process)
    wf.progress_bar = False
    wf.progress_bar = False
    model = core.Model(result_file, server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = Path(get_log_file(str(log_path), server_type_remote_process))
    assert download_log_path.exists()
    file_size = download_log_path.stat().st_size
    assert file_size > 3000
    server_type_remote_process._del_session()
    download_log_path = Path(get_log_file(str(log_path), server_type_remote_process))
    file_size = download_log_path.stat().st_size

    wf = core.Workflow(server=server_type_remote_process)
    wf.progress_bar = False
    wf.progress_bar = False
    model = core.Model(result_file, server=server_type_remote_process)
    stress = model.results.stress()
    to_nodal = core.operators.averaging.to_nodal_fc(stress, server=server_type_remote_process)
    wf.add_operators([stress, to_nodal])
    wf.set_output_name("out", to_nodal.outputs.fields_container)

    wf.get_output("out", core.types.fields_container)
    download_log_path = Path(get_log_file(str(log_path), server_type_remote_process))
    assert file_size == download_log_path.stat().st_size
