"""
Common
======
"""
from enum import Enum
import re

from ansys.grpc.dpf import base_pb2, field_definition_pb2
import progressbar


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


def __write_enum_doc__(enum, intro=None):
    str = ""
    if intro:
        str = intro + " \n\n"
    str += "    Attributes\n" + "    -----------\n"
    for e in enum:
        str += "    " + e.name + " \n\n"
    return str


names = [m.lower() for m in base_pb2.Type.keys()]
names.append("fields_container")
names.append("scopings_container")
names.append("meshes_container")
types = Enum("types", names)
types.__doc__ = __write_enum_doc__(
    types,
    (
        "The ``'types'`` enum contains the available types passed "
        "through operators and workflows to DPF."
    ),
)

names = [(m.lower(), num) for m, num in base_pb2.Nature.items()]
natures = Enum("natures", names)
natures.__doc__ = __write_enum_doc__(
    natures,
    (
        "The ``'natures'`` enum contains the dimensionality types.\n "
        "It can be used to create a field of a given dimensionality."
    ),
)

names = [(m.lower(), num - 1) for m, num in field_definition_pb2.ShellLayers.items()]
shell_layers = Enum("shell_layers", names)
shell_layers.__doc__ = __write_enum_doc__(
    shell_layers,
    (
        "The ``'shell_layers'`` enum contains the available order of "
        "shell layers (or lack of shell layers) that defines how the "
        "field's data is ordered."
    ),
)


class locations:
    """Contains strings for scoping and field locations.

    Attributes
    -----------
    none = "none"

    elemental = "Elemental"
        data is one per element

    elemental_nodal = "ElementalNodal"
        one per node per element

    nodal = "Nodal"
        one per node

    time_freq = "TimeFreq_sets"
        one per time set

    overall = "overall"
        applies everywhere

    time_freq_step = "TimeFreq_steps"
        one per time step
    """

    none = "none"

    # data is one per element
    elemental = "Elemental"

    # one per node per element
    elemental_nodal = "ElementalNodal"

    # one per node
    nodal = "Nodal"

    # one per time set
    time_freq = "TimeFreq_sets"

    # applies everywhere
    overall = "overall"

    # one per time step
    time_freq_step = "TimeFreq_steps"


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

    _elemental_property_type_dict = {
        element_type: "ELEMENT_TYPE",
        element_shape: "ELEMENT_SHAPE",
        material: "MATERIAL",
        connectivity: "CONNECTIVITY",
    }


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

    _nodal_property_type_dict = {
        coordinates: "COORDINATES",
        nodal_connectivity: "NODAL_CONNECTIVITY",
    }


class DefinitionLabels:
    """Contains Python definition labels."""

    time = "time"
    complex = "complex"


def _common_progress_bar(text, unit, tot_size=None):
    if tot_size:
        widgets = [
            progressbar.FormatLabel(f"{text}: %(value)d of %(max_value)d {unit} "),
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return progressbar.ProgressBar(widgets=widgets, max_value=tot_size)
    else:
        widgets = [
            progressbar.FormatLabel(f"{text}: %(value)d {unit}"),
            progressbar.RotatingMarker(),
        ]
        return progressbar.ProgressBar(widgets=widgets, max_value=progressbar.UnknownLength)


def _common_percentage_progress_bar(text):
    widgets = [progressbar.FormatLabel(f"{text}: %(value)d %%"), progressbar.Bar()]
    return progressbar.ProgressBar(widgets=widgets, max_value=100)
