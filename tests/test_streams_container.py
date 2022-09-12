import os
import pytest
import shutil

from ansys import dpf
from ansys.dpf.core import errors
from conftest import SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_create_streams_container(simple_bar):
    model = dpf.core.Model(simple_bar)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    assert hasattr(sc, "release_handles")


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_create_streams_container_raise_grpc(server_type_remote_process,
                                             simple_bar):
    model = dpf.core.Model(simple_bar, server=server_type_remote_process)
    streams_provider = model.metadata.streams_provider
    with pytest.raises(ValueError, dpf.gate.errors.DPFServerException):
        _ = streams_provider.outputs.streams_container()


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_release_handles(simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0]+"copy"+split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    sc.release_handles()
    os.remove(copy_path)


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_release_streams_model(simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0]+"copy2"+split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    model.metadata.release_streams()
    os.remove(copy_path)


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_release_streams_model_empty():
    model = dpf.core.Model()
    model.metadata.release_streams()


@pytest.mark.skipif(not SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_4_0,
                    reason='Available only with InProcess')
def test_create_from_streams_container(simple_bar):
    model = dpf.core.Model(simple_bar)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    dpf.core.streams_container.StreamsContainer(streams_container=sc)
