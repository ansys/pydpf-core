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
"""Provide utility functions for downloading and locating DPF example files."""

from .examples import get_example_required_minimum_dpf_version, find_files, fluid_axial_model
from .downloads import (
    delete_downloads,
    download_transient_result,
    download_all_kinds_of_complexity,
    download_all_kinds_of_complexity_modal,
    download_pontoon,
    download_multi_harmonic_result,
    download_multi_stage_cyclic_result,
    download_sub_file,
    download_msup_files_to_dict,
    download_average_filter_plugin,
    download_distributed_files,
    download_fluent_multi_species,
    download_fluent_multi_phase,
    download_extrapolation_3d_result,
    download_extrapolation_2d_result,
    download_easy_statistics,
    download_gltf_plugin,
    download_hemisphere,
    download_example_asme_result,
    download_crankshaft,
    download_piston_rod,
    download_d3plot_beam,
    download_binout_matsum,
    download_binout_glstat,
    download_cycles_to_failure,
    download_modal_frame,
    download_harmonic_clamped_pipe,
    download_modal_cyclic,
    download_fluent_axial_comp,
    download_fluent_mixing_elbow_steady_state,
    download_fluent_mixing_elbow_transient,
    download_cfx_heating_coil,
    download_cfx_mixing_elbow,
    find_simple_bar,
    find_static_rst,
    find_complex_rst,
    find_multishells_rst,
    find_electric_therm,
    find_steady_therm,
    find_transient_therm,
    find_msup_transient,
    find_simple_cyclic,
    find_distributed_msup_folder,
)


# called if module.<name> fails
def __getattr__(name):
    if name == "simple_bar":
        global simple_bar
        simple_bar = find_simple_bar()
        return simple_bar
    elif name == "static_rst":
        global static_rst
        static_rst = find_static_rst()
        return static_rst
    elif name == "complex_rst":
        global complex_rst
        complex_rst = find_complex_rst()
        return complex_rst
    elif name == "multishells_rst":
        global multishells_rst
        multishells_rst = find_multishells_rst()
        return multishells_rst
    elif name == "electric_therm":
        global electric_therm
        electric_therm = find_electric_therm()
        return electric_therm
    elif name == "steady_therm":
        global steady_therm
        steady_therm = find_steady_therm()
        return steady_therm
    elif name == "transient_therm":
        global transient_therm
        transient_therm = find_transient_therm()
        return transient_therm
    elif name == "msup_transient":
        global msup_transient
        msup_transient = find_msup_transient()
        return msup_transient
    elif name == "simple_cyclic":
        global simple_cyclic
        simple_cyclic = find_simple_cyclic()
        return simple_cyclic
    elif name == "distributed_msup_folder":
        global distributed_msup_folder
        distributed_msup_folder = find_distributed_msup_folder()
        return distributed_msup_folder
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "download_all_kinds_of_complexity",
    "download_all_kinds_of_complexity_modal",
    "get_example_required_minimum_dpf_version",
    "find_files",
    "fluid_axial_model",
    "download_all_kinds_of_complexity",
    "download_modal_frame",
    "download_transient_result",
    "download_multi_stage_cyclic_result",
    "download_fluent_mixing_elbow_steady_state",
    "download_fluent_multi_species",
    "download_harmonic_clamped_pipe",
    "download_binout_glstat",
    "download_fluent_axial_comp",
    "download_d3plot_beam",
    "download_multi_harmonic_result",
    "find_simple_bar",
    "find_static_rst",
    "find_complex_rst",
    "find_multishells_rst",
    "find_electric_therm",
    "find_steady_therm",
    "find_transient_therm",
    "find_msup_transient",
    "find_simple_cyclic",
    "find_distributed_msup_folder",
    "download_average_filter_plugin",
    "delete_downloads",
    "download_cfx_mixing_elbow",
    "download_cfx_heating_coil",
    "download_modal_cyclic",
    "download_crankshaft",
    "download_example_asme_result",
    "download_piston_rod",
    "download_fluent_mixing_elbow_transient",
    "download_easy_statistics",
    "download_gltf_plugin",
    "download_fluent_multi_phase",
    "download_pontoon",
    "download_binout_matsum",
    "download_cycles_to_failure",
    "download_distributed_files",
    "download_hemisphere",
    "download_sub_file",
    "download_extrapolation_3d_result",
    "download_extrapolation_2d_result",
    "download_msup_files_to_dict",
]
