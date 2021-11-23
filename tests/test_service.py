import os
import pathlib

import ansys.grpc.dpf
from ansys import dpf

import pytest
from ansys.dpf.core.check_version import meets_version, get_server_version
SERVER_VERSION_HIGHER_THAN_3_0 = meets_version(get_server_version(dpf.core._global_server()), "3.0")


def test_connect():
    base_service = dpf.core.BaseService(load_operators=False)
    assert isinstance(base_service._stub, ansys.grpc.dpf.base_pb2_grpc.BaseServiceStub)


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


def test_loadplugin():
    loaded = False
    try:
        dpf.core.load_library("libAns.Dpf.Math.so", "math")
        loaded = True
    except Exception as e:
        print(e.args)
        pass
    try:
        dpf.core.load_library("Ans.Dpf.Math.dll", "math")
        loaded = True
    except Exception as e:
        print(e.args)
        pass
    assert loaded


def test_launch_server_not_install():
    ansys_path = os.environ.get(
        "AWP_ROOT" + dpf.core._version.__ansys_version__, dpf.core.misc.find_ansys()
    )
    if os.name == "nt":
        path = os.path.join(ansys_path, "aisol", "bin", "winx64")
    else:
        path = os.path.join(ansys_path, "aisol", "bin", "linx64")

    print("trying to launch on ", path)
    print(os.listdir(path))
    server = dpf.core.start_local_server(as_global=False, ansys_path=path)
    assert "server_port" in server.info


def test_upload_download(allkindofcomplexity, tmpdir):
    file = dpf.core.upload_file_in_tmp_folder(allkindofcomplexity)
    dataSource = dpf.core.DataSources(file)
    op = dpf.core.Operator("S")
    op.connect(4, dataSource)

    fcOut = op.get_output(0, dpf.core.types.fields_container)
    f = fcOut[0]
    fielddef = f.field_definition
    assert fielddef.unit == "Pa"

    dir = os.path.dirname(file)
    vtk_path = os.path.join(dir, "file.vtk")
    vtk = dpf.core.operators.serialization.vtk_export(vtk_path, fields1=fcOut)
    vtk.run()

    dpf.core.download_file(vtk_path, os.path.join(tmpdir, "file.vtk"))
    assert os.path.exists(os.path.join(tmpdir, "file.vtk"))


def test_download_folder(allkindofcomplexity, plate_msup, multishells, tmpdir):
    file = dpf.core.upload_file_in_tmp_folder(allkindofcomplexity)
    file = dpf.core.upload_file_in_tmp_folder(plate_msup)
    file = dpf.core.upload_file_in_tmp_folder(multishells)
    parent_path = os.path.dirname(file)
    dpf.core.download_files_in_folder(parent_path, tmpdir)
    import ntpath

    assert os.path.exists(os.path.join(tmpdir, ntpath.basename(allkindofcomplexity)))
    assert os.path.exists(os.path.join(tmpdir, ntpath.basename(plate_msup)))
    assert os.path.exists(os.path.join(tmpdir, ntpath.basename(multishells)))


def test_download_with_subdir(multishells, tmpdir):
    file = dpf.core.upload_file_in_tmp_folder(multishells)

    base = dpf.core.BaseService()
    separator = base._get_separator(file)

    import ntpath

    filename = ntpath.basename(file)
    parent_path = os.path.dirname(file)
    to_server_path = parent_path + separator + "subdir" + separator + filename
    subdir_filepath = dpf.core.upload_file(file, to_server_path)
    folder = parent_path

    out = dpf.core.download_files_in_folder(folder, tmpdir)
    p1 = os.path.join(tmpdir, filename)
    p2 = os.path.join(tmpdir, "subdir", filename)
    # p1 = tmpdir + "/" + filename
    # p2 = tmpdir + "/subdir/" + filename
    assert os.path.exists(p1)
    assert os.path.exists(p2)


def test_downloadinfolder_uploadinfolder(multishells, tmpdir):
    base = dpf.core.BaseService()
    # create in tmpdir some architecture with subfolder in subfolder
    path1 = os.path.join(tmpdir, os.path.basename(multishells))
    path2 = os.path.join(tmpdir, "subdirA", os.path.basename(multishells))
    path4 = os.path.join(tmpdir, "subdirB", os.path.basename(multishells))
    from shutil import copyfile

    copyfile(multishells, path1)
    os.mkdir(os.path.join(tmpdir, "subdirA"))
    copyfile(multishells, path2)
    os.mkdir(os.path.join(tmpdir, "subdirB"))
    copyfile(multishells, path4)
    # upload it
    TARGET_PATH = base.make_tmp_dir_server()
    dpf.core.upload_files_in_folder(
        to_server_folder_path=TARGET_PATH,
        client_folder_path=tmpdir,
        specific_extension="rst",
    )
    # download it
    new_tmpdir = os.path.join(tmpdir, "my_tmp_dir")
    os.mkdir(new_tmpdir)
    out = dpf.core.download_files_in_folder(TARGET_PATH, new_tmpdir)
    # check if the architecture of the download is ok
    path1_check = os.path.join(new_tmpdir, os.path.basename(multishells))
    path2_check = os.path.join(new_tmpdir, "subdirA", os.path.basename(multishells))
    path4_check = os.path.join(new_tmpdir, "subdirB", os.path.basename(multishells))
    assert os.path.exists(path1_check)
    assert os.path.exists(path2_check)
    assert os.path.exists(path4_check)
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


def test_uploadinfolder_emptyfolder(tmpdir):
    base = dpf.core.BaseService()
    TARGET_PATH = base.make_tmp_dir_server()
    path = base.upload_files_in_folder(
        to_server_folder_path=TARGET_PATH, client_folder_path=tmpdir
    )
    assert len(path) == 0


def test_load_plugin_correctly():
    from ansys.dpf import core as dpf

    base = dpf.BaseService()
    try:
        base.load_library("Ans.Dpf.Math.dll", "math_operators")
    except:
        base.load_library("libAns.Dpf.Math.so", "math_operators")
    actual_path = pathlib.Path(__file__).parent.absolute()
    exists = os.path.exists(
        os.path.join(actual_path, "..", r"ansys/dpf/core/operators/fft_eval.py")
    )
    assert not exists
    num_lines = sum(
        1
        for line in open(
            os.path.join(
                actual_path, "..", r"ansys/dpf/core/operators/math/__init__.py"
            )
        )
    )
    assert num_lines >= 11

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_3_0, reason='Requires server version higher than 3.0')
def test_dpf_join(): 
    core.Operator("U") # start server
    left = "temp"
    right = "file.rst"
    conc = core.path_utilities.join(left, right)
    os_server = core.SERVER.os
    if os_server == 'posix':
        assert conc == "temp/file.rst"
    elif os_server == 'nt':
        assert conc == "temp\\file.rst"
        
if __name__ == "__main__":
    test_dpf_join()