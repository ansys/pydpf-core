import os

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import misc
from ansys.dpf.core import examples
from ansys.dpf.core import animation


if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
else:
    HAS_PYVISTA = False

gif_name = "test.gif"


@pytest.fixture(autouse=False)
def remove_gifs(request):
    """Remove GIF once finished."""

    def remove_gif():
        if os.path.exists(os.path.join(os.getcwd(), gif_name)):
            os.remove(os.path.join(os.getcwd(), gif_name))

    request.addfinalizer(remove_gif)


@pytest.fixture()
def displacement_fields():
    model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    result = model.results.displacement.on_all_time_freqs.eval()
    return result


def test_animate_mode(displacement_fields):
    animation.animate_mode(displacement_fields, mode_number=10)


def test_animate_mode_full_disp(displacement_fields):
    animation.animate_mode(displacement_fields, mode_number=3, type_mode="full_disp")


def test_animator_animate_mode_fields_container_one_component(displacement_fields):
    animation.animate_mode(displacement_fields.select_component(0), mode_number=10)
