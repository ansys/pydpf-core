# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from ansys.dpf import core as dpf
# from ansys.dpf.core.check_version import server_meet_version


# def test_unit_mesh_cache(simple_bar):
#     model = dpf.Model(simple_bar)
#     mesh = model.metadata.meshed_region
#     initunit = mesh.unit
#     assert len(mesh._cache.cached) == 1
#     assert mesh.unit == initunit
#     mesh.unit = "cm"
#     assert len(mesh._cache.cached) == 0
#     assert mesh.unit == "cm"
#     assert len(mesh._cache.cached) == 1


# def test_named_selections_mesh_cache(simple_bar):
#     model = dpf.Model(simple_bar)
#     mesh = model.metadata.meshed_region
#     init = mesh.available_named_selections
#     assert len(mesh._cache.cached) == 1
#     assert mesh.available_named_selections == init
#     assert len(mesh._cache.cached) == 1
#     ns = mesh.named_selection(init[0])
#     assert len(mesh._cache.cached) == 2


# def test_mismatch_instances_cache(simple_bar):
#     model = dpf.Model(simple_bar)
#     model2 = dpf.Model(simple_bar)
#     mesh = model.metadata.meshed_region
#     mesh2 = model2.metadata.meshed_region
#     initunit = mesh.unit
#     assert len(mesh._cache.cached) == 1
#     assert len(mesh2._cache.cached) == 0
#     assert mesh.unit == initunit
#     mesh.unit = "cm"
#     assert len(mesh._cache.cached) == 0
#     mesh2.unit
#     assert len(mesh2._cache.cached) == 1


# def test_available_results_cache(simple_bar):
#     model = dpf.Model(simple_bar)
#     res_info = model.metadata.result_info
#     for res in res_info:
#         pass
#     assert len(res_info._cache.cached) == len(res_info) + 1


# def test_physics_type_cache(simple_bar):
#     ds = dpf.DataSources(simple_bar)
#     provider = dpf.operators.metadata.result_info_provider(data_sources=ds)
#     res_info = provider.outputs.result_info()
#     assert len(res_info._cache.cached) == 0
#     res_info.unit_system
#     assert len(res_info._cache.cached) == 1
#     res_info.physics_type
#     assert len(res_info._cache.cached) == 2
