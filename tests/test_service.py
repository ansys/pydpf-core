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

import os
from pathlib import Path

import pytest
import conftest
import pkgutil
import datetime
import platform
from importlib import reload

from ansys import dpf
from ansys.dpf.core import path_utilities
from ansys.dpf.core import examples
from conftest import running_docker


def test_loadmapdloperators(allkindofcomplexity):
    dpf.core.BaseService(load_operators=True)
    dataSource = dpf.core.DataSources(allkindofcomplexity)
    dataSource.set_result_file_path(allkindofcomplexity)
    op = dpf.core.Operator("U")
    op.connect(4, dataSource)
    fcOut = op.get_output(0, dpf.core.types.fields_container)
    assert len(fcOut.get_available_ids_for_label()) == 1


def test_loadmeshoperators(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    assert mesh.grid.n_points
    assert mesh.grid.n_cells


def test_loadplugin(server_type):
    loaded = False
    try:
        dpf.core.load_library("libAns.Dpf.Math.so", "math", server=server_type)
        loaded = True
    except Exception as e:
        print(e.args)
        pass
    try:
        dpf.core.load_library("Ans.Dpf.Math.dll", "math", server=server_type)
        loaded = True
    except Exception as e:
        print(e.args)
        pass
    assert loaded


@pytest.mark.skipif(
    platform.system() == "Windows"
    and (
        platform.python_version().startswith("3.8") or platform.python_version().startswith("3.7")
    ),
    reason="Random SEGFAULT in the GitHub pipeline for 3.7-8 on Windows",
)
def test_upload_download(tmpdir, server_type_remote_process):
    tmpdir = Path(tmpdir)
    file = dpf.core.upload_file_in_tmp_folder(
        examples.download_all_kinds_of_complexity(return_local_path=True),
        server=server_type_remote_process,
    )
    dataSource = dpf.core.DataSources(file, server=server_type_remote_process)
    op = dpf.core.Operator("S", server=server_type_remote_process)
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    fielddef = f.field_definition
    assert fielddef.unit == "Pa"

    vtk_path = Path(file).parent / "file.vtk"
    vtk = dpf.core.operators.serialization.vtk_export(
        file_path=str(vtk_path), fields1=fcOut, server=server_type_remote_process
    )
    vtk.run()

    dpf.core.download_file(vtk_path, str(tmpdir / "file.vtk"), server=server_type_remote_process)
    assert tmpdir.joinpath("file.vtk").exists()


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_download_folder(
    allkindofcomplexity, plate_msup, multishells, tmpdir, server_type_remote_process
):
    tmpdir = str(tmpdir)
    file = dpf.core.upload_file_in_tmp_folder(
        allkindofcomplexity, server=server_type_remote_process
    )
    file = dpf.core.upload_file_in_tmp_folder(plate_msup, server=server_type_remote_process)
    file = dpf.core.upload_file_in_tmp_folder(multishells, server=server_type_remote_process)
    parent_path = str(Path(file).parent)
    dpf.core.download_files_in_folder(parent_path, tmpdir, server=server_type_remote_process)
    import ntpath

    assert Path(tmpdir).joinpath(ntpath.basename(allkindofcomplexity)).exists()
    assert Path(tmpdir).joinpath(ntpath.basename(plate_msup)).exists()
    assert Path(tmpdir).joinpath(ntpath.basename(multishells)).exists()


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_download_with_subdir(multishells, tmpdir, server_type_remote_process):
    tmpdir = Path(tmpdir)
    file = dpf.core.upload_file_in_tmp_folder(multishells, server=server_type_remote_process)

    base = dpf.core.BaseService(server=server_type_remote_process)
    separator = base._get_separator(file)

    import ntpath

    filename = ntpath.basename(file)
    parent_path = str(Path(file).parent)
    to_server_path = parent_path + separator + "subdir" + separator + filename
    dpf.core.upload_file(file, to_server_path, server=server_type_remote_process)
    folder = parent_path

    _ = dpf.core.download_files_in_folder(folder, str(tmpdir), server=server_type_remote_process)
    p1 = tmpdir / filename
    p2 = tmpdir / "subdir" / filename
    # p1 = tmpdir + "/" + filename
    # p2 = tmpdir + "/subdir/" + filename
    assert p1.exists()
    assert p2.exists()


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_downloadinfolder_uploadinfolder(multishells, tmpdir, server_type_remote_process):
    tmpdir = Path(tmpdir)
    base = dpf.core.BaseService(server=server_type_remote_process)
    # create in tmpdir some architecture with subfolder in subfolder
    path1 = tmpdir / Path(multishells).name
    path2 = tmpdir / "subdirA" / Path(multishells).name
    path4 = tmpdir / "subdirB" / Path(multishells).name
    from shutil import copyfile

    copyfile(multishells, path1)
    tmpdir.joinpath("subdirA").mkdir()
    copyfile(multishells, path2)
    tmpdir.joinpath("subdirB").mkdir()
    copyfile(multishells, path4)
    # upload it
    TARGET_PATH = base.make_tmp_dir_server()
    dpf.core.upload_files_in_folder(
        to_server_folder_path=TARGET_PATH,
        client_folder_path=str(tmpdir),
        specific_extension="rst",
        server=server_type_remote_process,
    )
    # download it
    new_tmpdir = tmpdir / "my_tmp_dir"
    new_tmpdir.mkdir()
    _ = dpf.core.download_files_in_folder(
        TARGET_PATH, str(new_tmpdir), server=server_type_remote_process
    )
    # check if the architecture of the download is ok
    path1_check = new_tmpdir / Path(multishells).name
    path2_check = new_tmpdir / "subdirA" / Path(multishells).name
    path4_check = new_tmpdir / "subdirB" / Path(multishells).name
    assert path1_check.exists()
    assert path2_check.exists()
    assert path4_check.exists()
    # clean
    # os.remove(os.path.join(tmpdir, "tmpdir"))
    # os.remove(os.path.join(tmpdir, "subdirA"))
    # os.remove(os.path.join(tmpdir, "subdirB"))


# def test_downloadinfolder_uploadinfolder_subsubdir(multishells, tmpdir):
#     base = dpf.core.BaseService()
#     # create in tmpdir some architecture with subfolder in subfolder
#     path1 = os.path.join(tmpdir, os.path.basename(multishells))
#     path2 = os.path.join(tmpdir, "subdirA", os.path.basename(multishells))
#     path3 = os.path.join(tmpdir, "subdirA", "subdir1", os.path.basename(multishells))
#     path4 = os.path.join(tmpdir, "subdirB", os.path.basename(multishells))
#     from shutil import copyfile
#     copyfile(multishells, path1)
#     os.mkdir(os.path.join(tmpdir, "subdirA"))
#     copyfile(multishells, path2)
#     os.mkdir(os.path.join(tmpdir, "subdirA", "subdir1"))
#     copyfile(multishells, path3)
#     os.mkdir(os.path.join(tmpdir, "subdirB"))
#     copyfile(multishells, path4)
#     # upload it
#     TARGET_PATH = base.make_tmp_dir_server()
#     base.upload_files_in_folder(
#         to_server_folder_path = TARGET_PATH,
#         client_folder_path = tmpdir,
#         specific_extension = "rst"
#     )
#     # download it
#     new_tmpdir = os.path.join(tmpdir, "tmpdir")
#     os.mkdir(new_tmpdir)
#     out = dpf.core.download_files_in_folder(TARGET_PATH, new_tmpdir)
#     # check if the architecture of the download is ok
#     path1_check = os.path.join(new_tmpdir, os.path.basename(multishells))
#     path2_check = os.path.join(new_tmpdir, "subdirA", os.path.basename(multishells))
#     path3_check = os.path.join(new_tmpdir, "subdirA", "subdir1", os.path.basename(multishells))
#     path4_check = os.path.join(new_tmpdir, "subdirB", os.path.basename(multishells))
#     assert os.path.exists(path1_check)
#     assert os.path.exists(path2_check)
#     assert os.path.exists(path3_check)
#     assert os.path.exists(path4_check)
#     # clean
#     # os.remove(os.path.join(tmpdir, "tmpdir"))
#     # os.remove(os.path.join(tmpdir, "subdirA"))
#     # os.remove(os.path.join(tmpdir, "subdirA", "subdir1"))
#     # os.remove(os.path.join(tmpdir, "subdirB"))


def test_uploadinfolder_emptyfolder(tmpdir, server_type_remote_process):
    tmpdir = str(tmpdir)
    base = dpf.core.BaseService(server=server_type_remote_process)
    TARGET_PATH = base.make_tmp_dir_server()
    path = base.upload_files_in_folder(to_server_folder_path=TARGET_PATH, client_folder_path=tmpdir)
    assert len(path) == 0


def test_load_plugin_correctly(server_type):
    from ansys.dpf import core as dpf

    actual_path = Path(pkgutil.get_loader("ansys.dpf.core").path).parent

    base = dpf.BaseService(server=server_type)
    if server_type.os == "nt":
        base.load_library("Ans.Dpf.Math.dll", "math_operators", generate_operators=True)
        t = actual_path.joinpath("operators/math/fft_eval.py").stat().st_mtime
        assert datetime.datetime.fromtimestamp(t).date() == datetime.datetime.today().date()
    else:
        base.load_library("libAns.Dpf.Math.so", "math_operators")
    exists = actual_path.joinpath("operators/fft_eval.py").exists()
    assert not exists
    num_lines = sum(1 for line in actual_path.joinpath("operators/math/__init__.py").open())
    assert num_lines >= 11


@conftest.raises_for_servers_version_under("4.0")
def test_load_plugin_correctly_remote():
    from ansys.dpf import core as dpf

    server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)
    server_connected = dpf.connect_to_server(
        server.external_ip, server.external_port, as_global=False
    )

    actual_path = Path(pkgutil.get_loader("ansys.dpf.core").path).parent

    if server.os == "posix":
        dpf.load_library("libAns.Dpf.Math.so", "math_operators", server=server_connected)
    else:
        dpf.load_library("Ans.Dpf.Math.dll", "math_operators", server=server_connected)
        t = actual_path.joinpath("operators/math/fft_eval.py").stat().st_mtime
        assert datetime.datetime.fromtimestamp(t).date() == datetime.datetime.today().date()

    assert actual_path.joinpath("operators/math/fft_eval.py").exists()


def test_dpf_join(server_type):
    dpf.core.DataSources("bla", server=server_type)  # start server
    left = "temp"
    right = "file.rst"
    conc = path_utilities.join(left, right)
    os_server = dpf.core.SERVER.os
    if os_server == "posix":
        assert conc == "temp/file.rst"
    elif os_server == "nt":
        assert conc == "temp\\file.rst"


@pytest.mark.skipif(not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_without_awp_root(restore_awp_root):
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    legacy_conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    loc_serv = dpf.core.start_local_server(config=legacy_conf, as_global=False)
    ver_to_check = dpf.core._version.server_to_ansys_version[str(loc_serv.version)]
    ver_to_check = ver_to_check[2:4] + ver_to_check[5:6]
    awp_root_name = "AWP_ROOT" + ver_to_check
    # delete awp_root
    os.environ.pop(awp_root_name, None)

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv = dpf.core.connect_to_server(
        config=conf,
        as_global=False,
        ip=loc_serv.external_ip,
        port=loc_serv.external_port,
    )

    assert serv._client_api_path is not None
    assert serv._grpc_client_path is not None
    dpf_inner_path = str(Path("ansys") / "dpf" / "gatebin")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


@pytest.mark.skipif(not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_with_awp_root():
    # with awp_root
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv_2 = dpf.core.start_local_server(config=conf, as_global=False)

    assert serv_2._client_api_path is not None
    assert serv_2._grpc_client_path is not None
    dpf_inner_path = str(Path("ansys") / "dpf" / "gatebin")
    assert dpf_inner_path in serv_2._client_api_path
    assert dpf_inner_path in serv_2._grpc_client_path


@pytest.mark.skipif(not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_with_awp_root_2():
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    legacy_conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    loc_serv = dpf.core.start_local_server(config=legacy_conf, as_global=False)

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv = dpf.core.connect_to_server(
        config=conf,
        as_global=False,
        ip=loc_serv.external_ip,
        port=loc_serv.external_port,
    )

    assert serv._client_api_path is not None
    assert serv._grpc_client_path is not None
    dpf_inner_path = str(Path("ansys") / "dpf" / "gatebin")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


@pytest.mark.skipif(conftest.IS_USING_GATEBIN, reason="This test must not have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_without_awp_root_no_gatebin(restore_awp_root):
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    legacy_conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    loc_serv = dpf.core.start_local_server(config=legacy_conf, as_global=False)

    awp_root_name = "AWP_ROOT" + dpf.core.misc.__ansys_version__
    # delete awp_root
    os.environ.pop(awp_root_name, None)

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    # Cannot test this warning as it only happens if the server is remote,
    # which we cannot test in the CI
    # with pytest.warns(
    #     UserWarning,
    #     match="Could not connect to remote server as ansys.dpf.gatebin "
    #           "is missing. Trying again using LegacyGrpcServer.\n",
    # ):
    # Here it will work as ansys.dpf.gate.load_api._get_api_path_from_installer_or_package
    # will find DPFClientAPI in the server local installation.
    _ = dpf.core.connect_to_server(
        config=conf,
        as_global=False,
        ip=loc_serv.external_ip,
        port=loc_serv.external_port,
    )


@pytest.mark.skipif(conftest.IS_USING_GATEBIN, reason="This test must no have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_with_awp_root_no_gatebin():
    # with awp_root
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv_2 = dpf.core.start_local_server(config=conf, as_global=False)

    assert serv_2._client_api_path is not None
    assert serv_2._grpc_client_path is not None
    ISPOSIX = os.name == "posix"
    if not ISPOSIX:
        dpf_inner_path = str(Path("aisol") / "bin" / "winx64")
    else:
        dpf_inner_path = str(Path("aisol") / "dll" / "linx64")
    assert dpf_inner_path in serv_2._client_api_path
    assert dpf_inner_path in serv_2._grpc_client_path


@pytest.mark.skipif(conftest.IS_USING_GATEBIN, reason="This test must not have gatebin installed")
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
    reason="GrpcServer class is " "supported starting server version 4.0",
)
def test_load_api_with_awp_root_2_no_gatebin():
    from ansys.dpf.core.server_factory import ServerConfig, CommunicationProtocols

    legacy_conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=True)
    loc_serv = dpf.core.start_local_server(config=legacy_conf, as_global=False)

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv = dpf.core.connect_to_server(
        config=conf, as_global=False, ip=loc_serv.ip, port=loc_serv.port
    )

    assert serv._client_api_path is not None
    assert serv._grpc_client_path is not None
    ISPOSIX = os.name == "posix"
    if not ISPOSIX:
        dpf_inner_path = str(Path("aisol") / "bin" / "winx64")
    else:
        dpf_inner_path = str(Path("aisol") / "dll" / "linx64")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


@pytest.fixture(autouse=False, scope="function")
def reset_context_environment_variable(request):
    """Reset ANSYS_DPF_SERVER_CONTEXT."""
    from ansys.dpf.core import server_context as s_c

    key = s_c.DPF_SERVER_CONTEXT_ENV
    init_context = os.environ.get(key, None)

    def revert():
        if init_context:
            os.environ[key] = init_context
        else:
            del os.environ[key]
        reload(s_c)

    request.addfinalizer(revert)


@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="AWP ROOT is not set with Docker",
)
@conftest.raises_for_servers_version_under("6.0")
def test_context_environment_variable(reset_context_environment_variable):
    from ansys.dpf.core import server_context as s_c

    key = s_c.DPF_SERVER_CONTEXT_ENV

    # Test raise on wrong value
    os.environ[key] = "PREM"
    with pytest.warns(
        UserWarning,
        match="which is not recognized as an available " "DPF ServerContext type.",
    ):
        reload(s_c)
    assert s_c.SERVER_CONTEXT == s_c.AvailableServerContexts.premium

    # Test each possible value is correctly understood and sets SERVER_CONTEXT
    for context in s_c.LicensingContextType:
        os.environ[key] = context.name.upper()
        reload(s_c)
        try:
            assert s_c.SERVER_CONTEXT == getattr(s_c.AvailableServerContexts, context.name)
        except AttributeError:
            continue


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_6_0, reason="Failures on Windows 231"
)
def test_server_without_context(remote_config_server_type):
    """Tests starting a server without a no_context given."""
    server = dpf.core.start_local_server(
        as_global=False,
        config=remote_config_server_type,
        context=dpf.core.AvailableServerContexts.no_context,
    )
    none_type = dpf.core.AvailableServerContexts.no_context.licensing_context_type
    assert server.context.licensing_context_type == none_type


@pytest.mark.order("last")
@pytest.mark.skipif(
    running_docker or not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_5_0,
    reason="AWP ROOT is not set with Docker",
)
@conftest.raises_for_servers_version_under("6.0")
def test_release_dpf(server_type):
    dpf.core.Operator("expansion::modal_superposition", server=server_type)
    server_type.release()

    with pytest.raises((KeyError, dpf.core.errors.DPFServerException)):
        dpf.core.Operator("expansion::modal_superposition", server=server_type)


@pytest.mark.skipif(running_docker, reason="BUG: not working on docker")
@conftest.raises_for_servers_version_under("6.1")
def test_license_context_manager_as_context(server_type):
    field = dpf.core.Field(server=server_type)
    field.append([0.0, 0.0, 0.0], 1)
    op = dpf.core.operators.filter.field_high_pass(server=server_type)
    op.inputs.field(field)
    op.inputs.threshold(0.0)
    with dpf.core.LicenseContextManager(server=server_type) as lic:
        op.outputs.field()
        st = lic.status

    assert len(st) != 0
    new_st = lic.status
    assert new_st == ""
    lic = dpf.core.LicenseContextManager(server=server_type)
    op.inputs.field(field)
    op.inputs.threshold(0.0)
    op.outputs.field()
    new_st = lic.status
    assert str(new_st) == str(st)
    lic = None

    op = dpf.core.operators.filter.field_high_pass(server=server_type)
    op.inputs.field(field)
    op.inputs.threshold(0.0)
    with dpf.core.LicenseContextManager(
        increment_name="ansys", license_timeout_in_seconds=1.0, server=server_type
    ) as lic:
        op.outputs.field()
        st = lic.status
        assert "ansys" in st
    st = lic.status
    assert "ansys" not in st


@pytest.mark.skipif(not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_9_1, reason="Bug")
def test_print_non_utf8_string():
    op = dpf.core.Operator("generate_uuid")
    out_str = op.get_output(0, dpf.core.types.string)
    assert len(str(out_str)) > 0


if __name__ == "__main__":
    test_load_api_with_awp_root()
