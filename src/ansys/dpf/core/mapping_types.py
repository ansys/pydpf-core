import sys
import inspect

## to do : change that one the module is done
from ansys.dpf.core.meshed_region import *  # noqa: F401, F403
from ansys.dpf.core.available_result import *  # noqa: F401, F403
from ansys.dpf.core.data_sources import *  # noqa: F401, F403
from ansys.dpf.core.field import *  # noqa: F401, F403
from ansys.dpf.core.fields_container import *  # noqa: F401, F403
from ansys.dpf.core.scoping import *  # noqa: F401, F403
from ansys.dpf.core.time_freq_support import *  # noqa: F401, F403
from ansys.dpf.core.common import (
    _smart_dict_camel,
    _camel_to_snake_case,
    _snake_to_camel_case,
    _smart_dict_unit_system,
)


map_types_to_cpp = _smart_dict_camel()
for classes in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    map_types_to_cpp[classes[0]] = _camel_to_snake_case(classes[0])
map_types_to_cpp["str"] = "string"
map_types_to_cpp["MeshedRegion"] = "abstract_meshed_region"
map_types_to_cpp["DataTree"] = "abstract_data_tree"
map_types_to_cpp["DPFVectorDouble"] = "vector<double>"
map_types_to_cpp["DPFVectorInt"] = "vector<int32>"
map_types_to_cpp["list"] = "vector<int32>"
map_types_to_cpp["bool"] = "bool"
map_types_to_cpp["int"] = "int32"
map_types_to_cpp["double"] = "double"
map_types_to_cpp["float"] = "double"


class _smart_dict_snake(dict):
    def __missing__(self, key):
        return _snake_to_camel_case(key)


map_types_to_python = _smart_dict_snake()
for k, v in map_types_to_cpp.items():
    map_types_to_python[v] = k
map_types_to_python["vector<double>"] = "list"
map_types_to_python["b"] = "bool"

map_unit_system = _smart_dict_unit_system()
map_unit_system[5] = "Metric (cm, g, dyne, s, V, A)"
map_unit_system[6] = "Metric (mm, Kg, N, s, mV, mA)"
map_unit_system[7] = "U.S Customary (ft, lbm, lbf, F, s, V, A)"
map_unit_system[8] = "U.S Customary (in, lbm, lbf, F, s, V, A)"
map_unit_system[10] = "Metric (um, t, uN, s, V, mA)"
map_unit_system[11] = "Metric (m, kg, N, s, V, A)"
