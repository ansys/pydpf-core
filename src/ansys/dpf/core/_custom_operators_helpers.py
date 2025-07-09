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

from enum import Enum

from ansys.dpf.core import (
    collection,
    custom_type_field,
    data_sources,
    data_tree,
    dpf_operator,
    field,
    fields_container,
    generic_data_container,
    meshed_region,
    meshes_container,
    property_field,
    result_info,
    scoping,
    scopings_container,
    string_field,
    time_freq_support,
    workflow,
)
from ansys.dpf.gate import capi, external_operator_capi

external_operator_api = external_operator_capi.ExternalOperatorCAPI

functions_registry = []


@capi.OperatorCallBack
def __operator_main__(operator_functor, data):
    capi.OperatorMainCallback(operator_functor)(data)


_type_to_output_method = [
    (bool, external_operator_api.external_operator_put_out_bool),  # always before int
    ((int, Enum), external_operator_api.external_operator_put_out_int),
    (str, external_operator_api.external_operator_put_out_string),
    (float, external_operator_api.external_operator_put_out_double),
    (field.Field, external_operator_api.external_operator_put_out_field),
    (
        property_field.PropertyField,
        external_operator_api.external_operator_put_out_property_field,
    ),
    (
        string_field.StringField,
        external_operator_api.external_operator_put_out_string_field,
    ),
    (scoping.Scoping, external_operator_api.external_operator_put_out_scoping),
    (collection.CollectionBase, external_operator_api.external_operator_put_out_collection),
    (
        data_sources.DataSources,
        external_operator_api.external_operator_put_out_data_sources,
    ),
    (
        meshed_region.MeshedRegion,
        external_operator_api.external_operator_put_out_meshed_region,
    ),
    (
        result_info.ResultInfo,
        external_operator_api.external_operator_put_out_result_info,
    ),
    (
        time_freq_support.TimeFreqSupport,
        external_operator_api.external_operator_put_out_time_freq,
    ),
    # TO DO : (cyclic_support.CyclicSupport, external_operator_api.external_operator_put_out_cy),
    (workflow.Workflow, external_operator_api.external_operator_put_out_workflow),
    (data_tree.DataTree, external_operator_api.external_operator_put_out_data_tree),
    (dpf_operator.Operator, external_operator_api.external_operator_put_out_operator),
    (
        custom_type_field.CustomTypeField,
        external_operator_api.external_operator_put_out_custom_type_field,
    ),
    (
        generic_data_container.GenericDataContainer,
        external_operator_api.external_operator_put_out_generic_data_container,
    ),
]

_type_to_input_method = [
    (bool, external_operator_api.external_operator_get_in_bool),
    (int, external_operator_api.external_operator_get_in_int),
    (str, external_operator_api.external_operator_get_in_string),
    (float, external_operator_api.external_operator_get_in_double),
    (field.Field, external_operator_api.external_operator_get_in_field, "field"),
    (
        property_field.PropertyField,
        external_operator_api.external_operator_get_in_property_field,
        "property_field",
    ),
    (
        string_field.StringField,
        external_operator_api.external_operator_get_in_string_field,
        "string_field",
    ),
    (
        custom_type_field.CustomTypeField,
        external_operator_api.external_operator_get_in_custom_type_field,
        "field",
    ),
    (
        scoping.Scoping,
        external_operator_api.external_operator_get_in_scoping,
        "scoping",
    ),
    (
        fields_container.FieldsContainer,
        external_operator_api.external_operator_get_in_fields_container,
        "fields_container",
    ),
    (
        scopings_container.ScopingsContainer,
        external_operator_api.external_operator_get_in_scopings_container,
        "scopings_container",
    ),
    (
        meshes_container.MeshesContainer,
        external_operator_api.external_operator_get_in_meshes_container,
        "meshes_container",
    ),
    (
        data_sources.DataSources,
        external_operator_api.external_operator_get_in_data_sources,
        "data_sources",
    ),
    (
        meshed_region.MeshedRegion,
        external_operator_api.external_operator_get_in_meshed_region,
        "mesh",
    ),
    # TO DO : (result_info.ResultInfo, external_operator_api.external_operator_get_in_re),
    (
        time_freq_support.TimeFreqSupport,
        external_operator_api.external_operator_get_in_time_freq,
        "time_freq_support",
    ),
    # TO DO : (cyclic_support.CyclicSupport, external_operator_api.external_operator_get_in_cy),
    (
        workflow.Workflow,
        external_operator_api.external_operator_get_in_workflow,
        "workflow",
    ),
    (
        data_tree.DataTree,
        external_operator_api.external_operator_get_in_data_tree,
        "data_tree",
    ),
    (
        generic_data_container.GenericDataContainer,
        external_operator_api.external_operator_get_in_generic_data_container,
        "generic_data_container",
    ),
    # TO DO : (dpf_operator.Operator, external_operator_api.external_operator_get_in_operator,
    # "operator"),
]
