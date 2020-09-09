import tempfile
import os

import pytest

from ansys import dpf
import ansys.grpc.dpf

if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

# start local server if necessary
if not dpf.has_local_server():
    dpf.start_local_server()

TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'allKindOfComplexity.rst')


def test_connect():
    base_service = dpf.BaseService(load_operators=False)
    assert isinstance(base_service._stub, ansys.grpc.dpf.base_pb2_grpc.BaseServiceStub)


def test_loadmapdloperators():
    dpf.BaseService(load_operators=True)
    dataSource = dpf.DataSources()
    dataSource.set_result_file_path(TEST_FILE_PATH)
    op = dpf.Operator("U")
    op.connect(4, dataSource)
    fcOut = op.get_output(0, dpf.types.fields_container)
    assert len(fcOut.get_ids()) == 1


def test_loadmeshoperators():
    model = dpf.Model(TEST_FILE_PATH)
    mesh = model.metadata.meshed_region
    assert mesh.grid.n_points
    assert mesh.grid.n_cells
