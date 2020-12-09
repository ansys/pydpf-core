from ansys import dpf
import ansys.grpc.dpf


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
    assert len(fcOut.get_ids()) == 1


def test_loadmeshoperators(allkindofcomplexity):
    model = dpf.core.Model(allkindofcomplexity)
    mesh = model.metadata.meshed_region
    assert mesh.grid.n_points
    assert mesh.grid.n_cells
