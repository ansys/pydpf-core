import os

import pytest
import conftest
import pkgutil
import datetime

from ansys import dpf
from ansys.dpf.core import path_utilities
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


def transfer_to_local_path(path):
    return os.path.normpath(
        path.replace(
            path_utilities.downloaded_example_path(),
            dpf.core.LOCAL_DOWNLOADED_EXAMPLES_PATH,
        )
    )


def test_upload_download(allkindofcomplexity, tmp_path, server_type_remote_process):
    tmp_path = str(tmp_path)
    file = dpf.core.upload_file_in_tmp_folder(
        transfer_to_local_path(allkindofcomplexity),
        server = server_type_remote_process
    )
    dataSource = dpf.core.DataSources(file, server=server_type_remote_process)
    op = dpf.core.Operator("S", server=server_type_remote_process)
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    fielddef = f.field_definition
    assert fielddef.unit == "Pa"

    dir = os.path.dirname(file)
    vtk_path = os.path.join(dir, "file.vtk")
    vtk = dpf.core.operators.serialization.vtk_export(file_path=vtk_path, fields1=fcOut,
                                                      server=server_type_remote_process)
    vtk.run()

    dpf.core.download_file(vtk_path, os.path.join(tmp_path, "file.vtk"),
                           server=server_type_remote_process)
    assert os.path.exists(os.path.join(tmp_path, "file.vtk"))


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_download_folder(
    allkindofcomplexity, plate_msup, multishells, tmp_path, server_type_remote_process
):
    tmp_path = str(tmp_path)
    file = dpf.core.upload_file_in_tmp_folder(
        allkindofcomplexity, server=server_type_remote_process
    )
    file = dpf.core.upload_file_in_tmp_folder(
        plate_msup, server=server_type_remote_process
    )
    file = dpf.core.upload_file_in_tmp_folder(
        multishells, server=server_type_remote_process
    )
    parent_path = os.path.dirname(file)
    dpf.core.download_files_in_folder(
        parent_path, tmp_path, server=server_type_remote_process
    )
    import ntpath

    assert os.path.exists(os.path.join(tmp_path, ntpath.basename(allkindofcomplexity)))
    assert os.path.exists(os.path.join(tmp_path, ntpath.basename(plate_msup)))
    assert os.path.exists(os.path.join(tmp_path, ntpath.basename(multishells)))


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_download_with_subdir(multishells, tmp_path, server_type_remote_process):
    tmp_path = str(tmp_path)
    file = dpf.core.upload_file_in_tmp_folder(
        multishells, server=server_type_remote_process
    )

    base = dpf.core.BaseService(server=server_type_remote_process)
    separator = base._get_separator(file)

    import ntpath

    filename = ntpath.basename(file)
    parent_path = os.path.dirname(file)
    to_server_path = parent_path + separator + "subdir" + separator + filename
    subdir_filepath = dpf.core.upload_file(
        file, to_server_path, server=server_type_remote_process
    )
    folder = parent_path

    out = dpf.core.download_files_in_folder(
        folder, tmp_path, server=server_type_remote_process
    )
    p1 = os.path.join(tmp_path, filename)
    p2 = os.path.join(tmp_path, "subdir", filename)
    # p1 = tmp_path + "/" + filename
    # p2 = tmp_path + "/subdir/" + filename
    assert os.path.exists(p1)
    assert os.path.exists(p2)


@pytest.mark.skipif(running_docker, reason="Path hidden within docker container")
def test_downloadinfolder_uploadinfolder(
    multishells, tmp_path, server_type_remote_process
):
    tmp_path = str(tmp_path)
    base = dpf.core.BaseService(server=server_type_remote_process)
    # create in tmp_path some architecture with subfolder in subfolder
    path1 = os.path.join(tmp_path, os.path.basename(multishells))
    path2 = os.path.join(tmp_path, "subdirA", os.path.basename(multishells))
    path4 = os.path.join(tmp_path, "subdirB", os.path.basename(multishells))
    from shutil import copyfile

    copyfile(multishells, path1)
    os.mkdir(os.path.join(tmp_path, "subdirA"))
    copyfile(multishells, path2)
    os.mkdir(os.path.join(tmp_path, "subdirB"))
    copyfile(multishells, path4)
    # upload it
    TARGET_PATH = base.make_tmp_dir_server()
    dpf.core.upload_files_in_folder(
        to_server_folder_path=TARGET_PATH,
        client_folder_path=tmp_path,
        specific_extension="rst",
        server=server_type_remote_process,
    )
    # download it
    new_tmp_path = os.path.join(tmp_path, "my_tmp_dir")
    os.mkdir(new_tmp_path)
    out = dpf.core.download_files_in_folder(
        TARGET_PATH, new_tmp_path, server=server_type_remote_process
    )
    # check if the architecture of the download is ok
    path1_check = os.path.join(new_tmp_path, os.path.basename(multishells))
    path2_check = os.path.join(new_tmp_path, "subdirA", os.path.basename(multishells))
    path4_check = os.path.join(new_tmp_path, "subdirB", os.path.basename(multishells))
    assert os.path.exists(path1_check)
    assert os.path.exists(path2_check)
    assert os.path.exists(path4_check)
    # clean
    # os.remove(os.path.join(tmp_path, "tmp_path"))
    # os.remove(os.path.join(tmp_path, "subdirA"))
    # os.remove(os.path.join(tmp_path, "subdirB"))


# def test_downloadinfolder_uploadinfolder_subsubdir(multishells, tmp_path):
#     base = dpf.core.BaseService()
#     # create in tmp_path some architecture with subfolder in subfolder
#     path1 = os.path.join(tmp_path, os.path.basename(multishells))
#     path2 = os.path.join(tmp_path, "subdirA", os.path.basename(multishells))
#     path3 = os.path.join(tmp_path, "subdirA", "subdir1", os.path.basename(multishells))
#     path4 = os.path.join(tmp_path, "subdirB", os.path.basename(multishells))
#     from shutil import copyfile
#     copyfile(multishells, path1)
#     os.mkdir(os.path.join(tmp_path, "subdirA"))
#     copyfile(multishells, path2)
#     os.mkdir(os.path.join(tmp_path, "subdirA", "subdir1"))
#     copyfile(multishells, path3)
#     os.mkdir(os.path.join(tmp_path, "subdirB"))
#     copyfile(multishells, path4)
#     # upload it
#     TARGET_PATH = base.make_tmp_dir_server()
#     base.upload_files_in_folder(
#         to_server_folder_path = TARGET_PATH,
#         client_folder_path = tmp_path,
#         specific_extension = "rst"
#     )
#     # download it
#     new_tmp_path = os.path.join(tmp_path, "tmp_path")
#     os.mkdir(new_tmp_path)
#     out = dpf.core.download_files_in_folder(TARGET_PATH, new_tmp_path)
#     # check if the architecture of the download is ok
#     path1_check = os.path.join(new_tmp_path, os.path.basename(multishells))
#     path2_check = os.path.join(new_tmp_path, "subdirA", os.path.basename(multishells))
#     path3_check = os.path.join(new_tmp_path, "subdirA", "subdir1", os.path.basename(multishells))
#     path4_check = os.path.join(new_tmp_path, "subdirB", os.path.basename(multishells))
#     assert os.path.exists(path1_check)
#     assert os.path.exists(path2_check)
#     assert os.path.exists(path3_check)
#     assert os.path.exists(path4_check)
#     # clean
#     # os.remove(os.path.join(tmp_path, "tmp_path"))
#     # os.remove(os.path.join(tmp_path, "subdirA"))
#     # os.remove(os.path.join(tmp_path, "subdirA", "subdir1"))
#     # os.remove(os.path.join(tmp_path, "subdirB"))


def test_uploadinfolder_emptyfolder(tmp_path, server_type_remote_process):
    tmp_path = str(tmp_path)
    base = dpf.core.BaseService(server=server_type_remote_process)
    TARGET_PATH = base.make_tmp_dir_server()
    path = base.upload_files_in_folder(
        to_server_folder_path=TARGET_PATH, client_folder_path=tmp_path
    )
    assert len(path) == 0


def test_load_plugin_correctly(server_type):
    from ansys.dpf import core as dpf
    actual_path = os.path.dirname(pkgutil.get_loader("ansys.dpf.core").path)

    base = dpf.BaseService(server=server_type)
    if os.name == "nt":
        base.load_library("Ans.Dpf.Math.dll", "math_operators", generate_operators=True)
        t = os.path.getmtime(os.path.join(actual_path, r"operators/math/fft_eval.py"))
        assert datetime.datetime.fromtimestamp(t).date() == datetime.datetime.today().date()
    else:
        base.load_library("libAns.Dpf.Math.so", "math_operators")
    exists = os.path.exists(os.path.join(actual_path, r"operators/fft_eval.py"))
    assert not exists
    num_lines = sum(
        1 for line in open(os.path.join(actual_path, r"operators/math/__init__.py"))
    )
    assert num_lines >= 11


@conftest.raises_for_servers_version_under("4.0")
def test_load_plugin_correctly_remote():
    from ansys.dpf import core as dpf
    server = dpf.start_local_server(config=dpf.AvailableServerConfigs.GrpcServer, as_global=False)
    server_connected = dpf.connect_to_server(server.ip, server.port, as_global=False)

    actual_path = os.path.dirname(pkgutil.get_loader("ansys.dpf.core").path)

    if os.name == "posix":
        dpf.load_library("libAns.Dpf.Math.so", "math_operators", server=server_connected)
    else:
        dpf.load_library("Ans.Dpf.Math.dll", "math_operators", server=server_connected)
        t = os.path.getmtime(os.path.join(actual_path, r"operators/math/fft_eval.py"))
        assert datetime.datetime.fromtimestamp(t).date() == datetime.datetime.today().date()

    actual_path = os.path.dirname(pkgutil.get_loader("ansys.dpf.core").path)

    assert os.path.exists(os.path.join(actual_path, r"operators/math/fft_eval.py"))


def test_dpf_join(server_type):
    dpf.core.DataSources("bla", server=server_type)  # start server
    left = "temp"
    right = "file.rst"
    conc = dpf.core.path_utilities.join(left, right)
    os_server = dpf.core.SERVER.os
    if os_server == "posix":
        assert conc == "temp/file.rst"
    elif os_server == "nt":
        assert conc == "temp\\file.rst"


@pytest.mark.skipif(
    not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed"
)
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
    del os.environ[awp_root_name]

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    serv = dpf.core.connect_to_server(
        config=conf, as_global=False, ip=loc_serv.ip, port=loc_serv.port
    )

    assert serv._client_api_path is not None
    assert serv._grpc_client_path is not None
    dpf_inner_path = os.path.join("ansys", "dpf", "gatebin")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


@pytest.mark.skipif(
    not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed"
)
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
    dpf_inner_path = os.path.join("ansys", "dpf", "gatebin")
    assert dpf_inner_path in serv_2._client_api_path
    assert dpf_inner_path in serv_2._grpc_client_path


@pytest.mark.skipif(
    not conftest.IS_USING_GATEBIN, reason="This test must have gatebin installed"
)
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
        config=conf, as_global=False, ip=loc_serv.ip, port=loc_serv.port
    )

    assert serv._client_api_path is not None
    assert serv._grpc_client_path is not None
    dpf_inner_path = os.path.join("ansys", "dpf", "gatebin")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


@pytest.mark.skipif(
    conftest.IS_USING_GATEBIN, reason="This test must not have gatebin installed"
)
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
    del os.environ[awp_root_name]

    # start CServer
    conf = ServerConfig(protocol=CommunicationProtocols.gRPC, legacy=False)
    with pytest.warns(UserWarning, match="Could not connect to remote server as ansys-dpf--gatebin "
                                         "is missing. Trying again using LegacyGrpcServer.\n"):
        serv = dpf.core.connect_to_server(
            config=conf, as_global=False, ip=loc_serv.ip, port=loc_serv.port
        )


@pytest.mark.skipif(
    conftest.IS_USING_GATEBIN, reason="This test must no have gatebin installed"
)
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
        dpf_inner_path = os.path.join("aisol", "bin", "winx64")
    else:
        dpf_inner_path = os.path.join("aisol", "dll", "linx64")
    assert dpf_inner_path in serv_2._client_api_path
    assert dpf_inner_path in serv_2._grpc_client_path


@pytest.mark.skipif(
    conftest.IS_USING_GATEBIN, reason="This test must not have gatebin installed"
)
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
        dpf_inner_path = os.path.join("aisol", "bin", "winx64")
    else:
        dpf_inner_path = os.path.join("aisol", "dll", "linx64")
    assert dpf_inner_path in serv._client_api_path
    assert dpf_inner_path in serv._grpc_client_path


if __name__ == "__main__":
    test_load_api_with_awp_root()
