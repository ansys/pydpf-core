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

"""Common."""

from enum import Enum
import re
import sys
from typing import Dict

from ansys.dpf.core.misc import module_exists
from ansys.dpf.gate.common import ProgressBarBase, locations  # noqa: F401
from ansys.dpf.gate.dpf_vector import (  # noqa: F401
    get_size_of_list as _get_size_of_list,
)


def _camel_to_snake_case(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _remove_spaces(name):
    out = name.lower()
    out = out.replace(" ", "_")
    out = out.replace("-", "_")
    return out


def _make_as_function_name(name):
    out = name.lower()
    out = (
        out.replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .replace(".", "_")
        .replace(":", "_")
        .replace(";", "_")
        .replace(",", "_")
        .replace("(", "")
        .replace(")", "")
    )
    return out


def _snake_to_camel_case(name):
    return "".join(word.title() for word in name.split("_"))


class _smart_dict_camel(dict):
    def __missing__(self, key):
        return _camel_to_snake_case(key)


class _smart_dict_unit_system(dict):
    def __missing__(self, key):
        return "unknown"


class types(Enum):
    """The ``'types'`` enum contains the available types passed through operators and workflows to DPF."""

    # Types from grpc proto, do not modify
    string = 0
    int = 1
    double = 2
    bool = 3
    field = 4
    collection = 5
    scoping = 6
    data_sources = 7
    meshed_region = 8
    time_freq_support = 9
    result_info = 10
    cyclic_support = 11
    property_field = 12
    workflow = 13
    run = 14
    any = 15
    vec_int = 16
    vec_double = 17
    support = 18
    operator = 19
    data_tree = 20
    vec_string = 21
    string_field = 22
    custom_type_field = 23
    generic_data_container = 24
    mesh_info = 25
    # Types not from grpc proto, added in Python
    fields_container = -1
    scopings_container = -2
    meshes_container = -3
    streams_container = -4
    bytes = -5


def types_enum_to_types():
    """Return a mapping of enums and corresponding python or dpf types.

    Returns
    -------
    dict
        Mapping of enum to the corresponding type.
    """
    from ansys.dpf.core import (
        Any,
        collection,
        custom_type_field,
        cyclic_support,
        data_sources,
        data_tree,
        dpf_operator,
        field,
        fields_container,
        generic_data_container,
        mesh_info,
        meshed_region,
        meshes_container,
        property_field,
        result_info,
        scoping,
        scopings_container,
        streams_container,
        string_field,
        time_freq_support,
        workflow,
    )
    from ansys.dpf.gate import dpf_vector

    return {
        types.string: str,
        types.int: int,
        types.double: float,
        types.bool: bool,
        types.bytes: bytes,
        types.collection: collection.CollectionBase,
        types.fields_container: fields_container.FieldsContainer,
        types.scopings_container: scopings_container.ScopingsContainer,
        types.meshes_container: meshes_container.MeshesContainer,
        types.field: field.Field,
        types.data_sources: data_sources.DataSources,
        types.cyclic_support: cyclic_support.CyclicSupport,
        types.workflow: workflow.Workflow,
        types.time_freq_support: time_freq_support.TimeFreqSupport,
        types.meshed_region: meshed_region.MeshedRegion,
        types.result_info: result_info.ResultInfo,
        types.property_field: property_field.PropertyField,
        types.data_tree: data_tree.DataTree,
        types.operator: dpf_operator.Operator,
        types.scoping: scoping.Scoping,
        types.vec_int: dpf_vector.DPFVectorInt,
        types.vec_double: dpf_vector.DPFVectorDouble,
        types.string_field: string_field.StringField,
        types.custom_type_field: custom_type_field.CustomTypeField,
        types.streams_container: streams_container.StreamsContainer,
        types.generic_data_container: generic_data_container.GenericDataContainer,
        types.mesh_info: mesh_info.MeshInfo,
        types.any: Any,
    }


class natures(Enum):
    """The ``'natures'`` enum contains the dimensionality types.

    It can be used to create a field of a given dimensionality.
    """

    scalar = 0
    vector = 1
    matrix = 2
    symmatrix = 5


class shell_layers(Enum):
    """Contains data identifying shell layers.

    The ``'shell_layers'`` enum contains the available order of
    shell layers (or lack of shell layers) that defines how the
    field's data is ordered.
    """

    notset = -1
    top = 0
    bottom = 1
    topbottom = 2
    mid = 3
    topbottommid = 4
    nonelayer = 5
    layerindependent = 6


class elemental_properties:
    """Contains strings to define elemental property fields.

    Attributes
    ----------
    element_shape = "elshape"
        element shape property data is provided

    element_type = "eltype"
        element type property data is provided

    connectivity = "connectivity"
        connectivity property data is provided

    material = "mat"
        material property data is provided

    element_properties = "elprops"
        element properties data is provided

    apdl_element_type = "apdl_element_type"
        apdl element type property data is provided

    elements_faces_connectivity = "elements_faces_connectivity"
        element faces connectivity property data is provided
    """

    element_shape = "elshape"
    element_type = "eltype"
    connectivity = "connectivity"
    material = "mat"
    element_properties = "elprops"
    apdl_element_type = "apdl_element_type"
    elements_faces_connectivity = "elements_faces_connectivity"


class nodal_properties:
    """Contains strings to define nodal property fields.

    Attributes
    ----------
    coordinates = "coordinates"
        coordinates data is provided

    nodal_connectivity = "reverse_connectivity"
        nodal connectivity property data is provided
    """

    coordinates = "coordinates"
    nodal_connectivity = "reverse_connectivity"


class face_properties:
    """Contains strings to define face property fields.

    Attributes
    ----------
    faces_type = "faces_type"
        face type property data is provided

    faces_nodes_connectivity = "faces_nodes_connectivity"
        faces connectivity property data is provided
    """

    faces_type = "faces_type"
    faces_nodes_connectivity = "faces_nodes_connectivity"


class config_options:
    """Contains strings to define configuration options.

    Attributes
    ----------
    num_thread = "num_threads"
        number of threads

    use_cache = "use_cache"
        usage of cache if a server with gRPC communication
        protocol is used.
    """

    num_threads = "num_threads"
    use_cache = "use_cache"


class DefinitionLabels:
    """Contains Python definition labels."""

    time = "time"
    complex = "complex"


class TqdmProgressBar(ProgressBarBase):
    """Custom progress bar implementation based on tqdm."""

    def __init__(self, text, unit, tot_size=None):
        import tqdm

        super().__init__(text, tot_size)
        bar_format = (
            "{l_bar}{bar}| {n_fmt} {unit}"
            if self.tot_size is None
            else "{l_bar}{bar}| {n_fmt}/{total_fmt} {unit}"
        )
        self.bar = tqdm.tqdm(
            desc=text,
            total=tot_size,
            unit=unit,
            file=sys.stdout,
            bar_format=bar_format,
            ncols=100,
        )

    def update(self, current_value):
        """Modify how the current value of the progress bar is updated."""
        if self.tot_size is None:
            self.bar.total = current_value * 2
        self.bar.update(current_value - self.current)
        self.current = current_value

    @staticmethod
    def progress_available():
        """Check if the tdqm module exists.

        Returns
        -------
        bool
            True if module exists, else False.
        """
        return module_exists("tqdm")


def _progress_bar_is_available():
    return TqdmProgressBar.progress_available()


def _common_progress_bar(text, unit, tot_size=None):
    return TqdmProgressBar(text, unit, tot_size)


def _common_percentage_progress_bar(text):
    return TqdmProgressBar(text, "%", 100)


class SubClassSmartDict(dict):
    """Return the superclass name for a key if not found initially."""

    def __getitem__(self, item):
        """If found returns the item of key == ìtem`, else returns item with key matching `issubclass(item, key)`."""
        if item in self:
            return super().__getitem__(item)
        else:
            for key, value in self.items():
                if issubclass(item, key):
                    return value
        raise KeyError


_type_to_internal_object_keyword = None


def type_to_internal_object_keyword():
    """Return dpf types mapped to internal object keywords.

    Returns
    -------
    SubClassSmartDict
        Custom dictionary that returns superclass name for a key if not found initially.
    """
    global _type_to_internal_object_keyword
    if _type_to_internal_object_keyword is None:
        from ansys.dpf.core import (
            any,
            collection,
            custom_type_field,
            cyclic_support,
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
            streams_container,
            string_field,
            time_freq_support,
            workflow,
        )

        _type_to_internal_object_keyword = SubClassSmartDict(
            {
                field.Field: "field",
                property_field.PropertyField: "property_field",
                string_field.StringField: "string_field",
                custom_type_field.CustomTypeField: "field",
                scoping.Scoping: "scoping",
                fields_container.FieldsContainer: "fields_container",
                scopings_container.ScopingsContainer: "scopings_container",
                meshes_container.MeshesContainer: "meshes_container",
                streams_container.StreamsContainer: "streams_container",
                data_sources.DataSources: "data_sources",
                cyclic_support.CyclicSupport: "cyclic_support",
                meshed_region.MeshedRegion: "mesh",
                result_info.ResultInfo: "result_info",
                time_freq_support.TimeFreqSupport: "time_freq_support",
                workflow.Workflow: "workflow",
                data_tree.DataTree: "data_tree",
                dpf_operator.Operator: "operator",
                generic_data_container.GenericDataContainer: "generic_data_container",
                any.Any: "any_dpf",
                collection.Collection: "collection",
            }
        )
    return _type_to_internal_object_keyword


_type_to_special_dpf_constructors = None


def type_to_special_dpf_constructors():
    """Return dpf type mapped to special dpf constructors."""
    global _type_to_special_dpf_constructors
    if _type_to_special_dpf_constructors is None:
        from ansys.dpf.core import collection_base
        from ansys.dpf.gate.dpf_vector import DPFVectorInt

        _type_to_special_dpf_constructors = {
            DPFVectorInt: lambda obj, server: collection_base.IntCollection(
                server=server, collection=obj
            ).get_integral_entries()
        }
    return _type_to_special_dpf_constructors


_derived_class_name_to_type = None


def derived_class_name_to_type() -> Dict[str, type]:
    """
    Return a mapping of derived class names to their corresponding Python classes.

    Returns
    -------
    dict[str, type]
        A dictionary mapping derived class names (str) to their corresponding
        Python class objects.
    """
    global _derived_class_name_to_type
    if _derived_class_name_to_type is None:
        from ansys.dpf.core.workflow_topology import WorkflowTopology

        _derived_class_name_to_type = {"WorkflowTopology": WorkflowTopology}
    return _derived_class_name_to_type


def record_derived_class(class_name: str, py_class: type, overwrite: bool = False):
    """
    Record a new derived class in the mapping of class names to their corresponding Python classes.

    This function updates the global dictionary that maps derived class names (str) to their corresponding
    Python class objects (type). If the provided class name already exists in the dictionary, it will either
    overwrite the existing mapping or leave it unchanged based on the `overwrite` flag.

    Parameters
    ----------
    class_name : str
        The name of the derived class to be recorded.
    py_class : type
        The Python class type corresponding to the derived class.
    overwrite : bool, optional
        A flag indicating whether to overwrite an existing entry for the `class_name`.
        If `True`, the entry will be overwritten. If `False` (default), the entry will
        not be overwritten if it already exists.
    """
    recorded_classes = derived_class_name_to_type()
    if overwrite or class_name not in recorded_classes:
        recorded_classes[class_name] = py_class


def create_dpf_instance(type, internal_obj, server):
    """Create a server instance of a given type."""
    spe_constructors = type_to_special_dpf_constructors()
    if type in spe_constructors:
        return spe_constructors[type](internal_obj, server)
    # get current type's constructors' variable keyword for passing the internal_obj
    internal_obj_keyword = type_to_internal_object_keyword()[type]

    # wrap parameters in a dictionary for parameters expansion when calling
    # constructor
    keyword_args = {internal_obj_keyword: internal_obj, "server": server}
    # call constructor
    return type(**keyword_args)
