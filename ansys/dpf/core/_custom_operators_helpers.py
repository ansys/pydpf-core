from ansys.dpf.gate import capi, external_operator_capi
from enum import Enum

from ansys.dpf.core import (
    field, property_field, scoping, collection, data_sources, meshed_region, time_freq_support, \
    workflow, data_tree, dpf_operator, fields_container, scopings_container, \
    meshes_container, result_info, string_field
)

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
    (property_field.PropertyField, external_operator_api.external_operator_put_out_property_field),
    (string_field.StringField, external_operator_api.external_operator_put_out_string_field),
    (scoping.Scoping, external_operator_api.external_operator_put_out_scoping),
    (collection.Collection, external_operator_api.external_operator_put_out_collection),
    (data_sources.DataSources, external_operator_api.external_operator_put_out_data_sources),
    (meshed_region.MeshedRegion, external_operator_api.external_operator_put_out_meshed_region),
    (result_info.ResultInfo, external_operator_api.external_operator_put_out_result_info),
    (time_freq_support.TimeFreqSupport, external_operator_api.external_operator_put_out_time_freq),
    # TO DO : (cyclic_support.CyclicSupport, external_operator_api.external_operator_put_out_cy),
    (workflow.Workflow, external_operator_api.external_operator_put_out_workflow),
    (data_tree.DataTree, external_operator_api.external_operator_put_out_data_tree),
    (dpf_operator.Operator, external_operator_api.external_operator_put_out_operator),
]

_type_to_input_method = [
    (bool, external_operator_api.external_operator_get_in_bool),
    (int, external_operator_api.external_operator_get_in_int),
    (str, external_operator_api.external_operator_get_in_string),
    (float, external_operator_api.external_operator_get_in_double),
    (field.Field, external_operator_api.external_operator_get_in_field, "field"),
    (property_field.PropertyField, external_operator_api.external_operator_get_in_property_field,
     "property_field"),
    (string_field.StringField, external_operator_api.external_operator_get_in_string_field,
     "string_field"),
    (scoping.Scoping, external_operator_api.external_operator_get_in_scoping,
     "scoping"),
    (fields_container.FieldsContainer,
     external_operator_api.external_operator_get_in_fields_container,
     "fields_container"),
    (scopings_container.ScopingsContainer,
     external_operator_api.external_operator_get_in_scopings_container,
     "scopings_container"),
    (meshes_container.MeshesContainer,
     external_operator_api.external_operator_get_in_meshes_container,
     "meshes_container"),
    (data_sources.DataSources, external_operator_api.external_operator_get_in_data_sources,
     "data_sources"),
    (meshed_region.MeshedRegion, external_operator_api.external_operator_get_in_meshed_region,
     "mesh"),
    # TO DO : (result_info.ResultInfo, external_operator_api.external_operator_get_in_re),
    (time_freq_support.TimeFreqSupport, external_operator_api.external_operator_get_in_time_freq,
     "time_freq_support"),
    # TO DO : (cyclic_support.CyclicSupport, external_operator_api.external_operator_get_in_cy),
    (workflow.Workflow, external_operator_api.external_operator_get_in_workflow,
     "workflow"),
    (data_tree.DataTree, external_operator_api.external_operator_get_in_data_tree,
     "data_tree"),
    # TO DO : (dpf_operator.Operator, external_operator_api.external_operator_get_in_operator,
    # "operator"),
]
