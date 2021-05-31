from ansys import dpf
import ansys.grpc.dpf
import os


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
    ansys_path = dpf.core.misc.find_ansys()
    server = dpf.core.start_local_server(as_global=False, ansys_path = ansys_path, load_operators=False)
    base = dpf.core.BaseService(server=server,load_operators= False)
    loaded = False
    try:
        base.load_library('libAns.Dpf.Math.so', "math")
        loaded=True
    except:
        pass
    try:
        base.load_library('Ans.Dpf.Math.dll', "math")
        loaded=True
    except:
        pass
    server.shutdown()
    assert loaded
    

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
    vtk_path = os.path.join(dir,"file.vtk")
    vtk = dpf.core.operators.serialization.vtk_export(vtk_path, fields1=fcOut )
    vtk.run()
    
    dpf.core.download_file(vtk_path, os.path.join(tmpdir,"file.vtk"))
    assert os.path.exists(os.path.join(tmpdir,"file.vtk"))
    
    
def test_download_folder(allkindofcomplexity, plate_msup,multishells,tmpdir):
    file = dpf.core.upload_file_in_tmp_folder(allkindofcomplexity)
    file = dpf.core.upload_file_in_tmp_folder(plate_msup)
    file = dpf.core.upload_file_in_tmp_folder(multishells)
    parent_path = os.path.dirname(file)
    dpf.core.download_files_in_folder(parent_path, tmpdir)
    import ntpath
    assert os.path.exists(os.path.join(tmpdir,ntpath.basename(allkindofcomplexity)))
    assert os.path.exists(os.path.join(tmpdir,ntpath.basename(plate_msup)))
    assert os.path.exists(os.path.join(tmpdir,ntpath.basename(multishells)))

    
    
    
    
