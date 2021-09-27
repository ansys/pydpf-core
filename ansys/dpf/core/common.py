"""
Common
======
"""
import re
from enum import Enum

import progressbar
from ansys.grpc.dpf import base_pb2, field_definition_pb2


def _camel_to_snake_case(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _remove_spaces(name):
    out = name.lower()
    out = out.replace(" ", "_")
    out = out.replace("-", "_")
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
        return progressbar.ProgressBar(
            widgets=widgets, max_value=progressbar.UnknownLength
        )
