"""Common dpf methods """
from enum import Enum

import numpy as np
import re


from ansys.grpc.dpf import base_pb2
from ansys.grpc.dpf import field_definition_pb2


def camel_to_snake_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def remove_spaces(name):
    out = name.lower()
    out = out.replace(" ", "_")
    out = out.replace("-", "_")
    return out


def snake_to_camel_case(name):
    return ''.join(word.title() for word in name.split('_'))


class smart_dict_camel(dict):
    def __missing__(self, key):
        return camel_to_snake_case(key)


class smart_dict_unit_system(dict):
    def __missing__(self, key):
        return 'unknown'


names = [m.lower() for m in base_pb2.Type.keys()]
names.append("fields_container")
names.append("scopings_container")
names.append("meshes_container")
types = Enum('types', names)

names = [(m.lower(), num)  for m, num in base_pb2.Nature.items()]
natures = Enum('natures', names)


names = [(m.lower(), num-1)  for m, num in field_definition_pb2.ShellLayers.items()]
shell_layers = Enum('shell_layers', names)


class locations:
    """Contains Python field types"""
    none = "none"

    # data is one per element
    elemental = "Elemental"

    # one per node per element
    elemental_nodal = "ElementalNodal"

    # one per node
    nodal = "Nodal"

    # one per time set
    time_freq = "TimeFreq_sets"

    #applies everywhere
    overall = "overall"
    
    # one per time step
    time_freq_step = "TimeFreq_steps"    
    

class DefinitionLabels:
    """Contains Python definition labels."""
    time = "time"
    complex = "complex"
    

