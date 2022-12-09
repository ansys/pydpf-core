# -*- coding: utf-8 -*-

import pytest

import conftest
from ansys import dpf
from ansys.dpf.core import MaterialsContainer


def test_create_materials_container(server_in_process, simple_bar):
    model = dpf.core.Model(simple_bar, server=server_in_process)
    materials_provider = dpf.core.operators.metadata.material_provider(
        data_sources=model)
    materials_container = materials_provider.eval()
    print(materials_container)
