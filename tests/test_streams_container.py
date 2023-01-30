import os
import shutil

from ansys import dpf


def test_create_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    assert hasattr(sc, "release_handles")


def test_release_handles(server_in_process, simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0] + "copy" + split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path, server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    sc.release_handles()
    os.remove(copy_path)


def test_release_streams_model(server_in_process, simple_bar):
    split = os.path.splitext(simple_bar)
    copy_path = split[0] + "copy2" + split[1]
    shutil.copyfile(simple_bar, copy_path)
    model = dpf.core.Model(copy_path, server=server_in_process)
    # Evaluate something from the rst
    _ = model.metadata.meshed_region
    model.metadata.release_streams()
    os.remove(copy_path)


def test_release_streams_model_empty(server_in_process):
    model = dpf.core.Model(server=server_in_process)
    model.metadata.release_streams()


def test_create_from_streams_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    dpf.core.streams_container.StreamsContainer(streams_container=sc, server=server_in_process)
