"""
Common
======

.. autoclass:: locations
   :members:

"""
import re
import sys
from enum import Enum

from ansys.dpf.core.misc import module_exists
from ansys.dpf.gate.common import locations, ProgressBarBase  # noqa: F401
from ansys.dpf.gate.dpf_vector import get_size_of_list as _get_size_of_list  # noqa: F401

def _camel_to_snake_case(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _remove_spaces(name):
    out = name.lower()
    out = out.replace(" ", "_")
    out = out.replace("-", "_")
    return out


def _make_as_function_name(name):
    out = name.lower()
    out = out.replace(" ", "_"). \
        replace("-", "_"). \
        replace("/", "_"). \
        replace(".", "_"). \
        replace(":", "_"). \
        replace(";", "_"). \
        replace(",", "_"). \
        replace("(", ""). \
        replace(")", "")
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
    """
    The ``'types'`` enum contains the available types passed through operators
    and workflows to DPF.



    """
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
    fields_container = 23
    scopings_container = 24
    meshes_container = 25


def types_enum_to_types():
    from ansys.dpf.core import (
        cyclic_support,
        data_sources,
        field,
        fields_container,
        collection,
        meshed_region,
        meshes_container,
        property_field,
        string_field,
        result_info,
        scoping,
        scopings_container,
        time_freq_support,
        dpf_operator,
        data_tree,
        workflow,
    )
    from ansys.dpf.gate import dpf_vector
    return {
        types.string: str,
        types.int: int,
        types.double: float,
        types.bool: bool,
        types.collection: collection.Collection,
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
    """The ``'shell_layers'`` enum contains the available order of
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
    """
    element_shape = "elshape"
    element_type = "eltype"
    connectivity = "connectivity"
    material = "mat"
    element_properties = "elprops"
    apdl_element_type = "apdl_element_type"


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
    def __init__(self, text, unit, tot_size=None):
        import tqdm
        super().__init__(text, tot_size)
        bar_format = '{l_bar}{bar}| {n_fmt} {unit}' \
            if self.tot_size is None else '{l_bar}{bar}| {n_fmt}/{total_fmt} {unit}'
        self.bar = tqdm.tqdm(desc=text, total=tot_size, unit=unit, file=sys.stdout,
                             bar_format=bar_format, ncols=100)

    def update(self, current_value):
        if self.tot_size is None:
            self.bar.total = current_value*2
        self.bar.update(current_value-self.current)
        self.current = current_value

    @staticmethod
    def progress_available():
        return module_exists("tqdm")


def _progress_bar_is_available():
    return TqdmProgressBar.progress_available()


def _common_progress_bar(text, unit, tot_size=None):
    return TqdmProgressBar(text, unit, tot_size)


def _common_percentage_progress_bar(text):
    return TqdmProgressBar(text, "%", 100)
