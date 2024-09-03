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

def test_retrieve_ip(server_in_process):
    start_server = dpf.core.Operator("grpc::stream_provider", server=server_in_process)
    in_thread = 1
    should_start_server = 3

    start_server.connect(2, in_thread)
    start_server.connect(3, should_start_server)

    streams = start_server.get_output(0, dpf.core.types.streams_container)
    ds = streams.datasources()

    # look for ip
    assert len(ds.result_files) == 1
    assert ds.result_key == "grpc"

    addr = ds.result_files[0]
    import re
    # can match 999.999.999.999:99999, 0.0.0.0:0
    # but not 0.0.0:0, 9999.999.999.999:999, 0.0.0.0
    ip_addr_regex = r"([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}"
    assert re.match(ip_addr_regex, addr) != None 