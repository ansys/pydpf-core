import os
import shutil

from ansys import dpf
from ansys.dpf.core import examples


def test_create_streams_container(simple_bar):
    model = dpf.core.Model(simple_bar)
    streams_provider = model.metadata.streams_provider
    sc = streams_provider.outputs.streams_container()
    assert hasattr(sc, "release_handles")


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
