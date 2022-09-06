import os

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import misc, Workflow

if misc.module_exists("pyvista"):
    HAS_PYVISTA = True
    from ansys.dpf.core.animator import Animator
else:
    HAS_PYVISTA = False


def remove_file(file):
    if os.path.exists(os.path.join(os.getcwd(), file)):
        os.remove(os.path.join(os.getcwd(), file))


def test_animator_animate_no_workflow():
    an = Animator()
    with pytest.raises(ValueError) as e:
        an.animate({})
        assert "self.workflow" in e


def test_animator_set_get_workflow():
    an = Animator()
    wf = Workflow()
    an.workflow = wf
    assert an.workflow == wf


def test_animator_with_workflow():
    wf = Workflow()
    an = Animator(wf)
    assert an.workflow == wf
