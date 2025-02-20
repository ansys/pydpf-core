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
"""Provides utilities for mapping and transforming data types between Python and C++ representations."""

from enum import Enum  # noqa: F401  # pylint: disable=W0611
import inspect
from pathlib import Path  # noqa: F401  # pylint: disable=W0611
import sys

# Import types to map to cpp (camel case to snake case)
from ansys.dpf.core.available_result import (  # noqa: F401  # pylint: disable=W0611
    AvailableResult,
    Homogeneity,
)
from ansys.dpf.core.collection_base import CollectionBase  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.common import (
    _camel_to_snake_case,
    _smart_dict_camel,
    _snake_to_camel_case,
)
from ansys.dpf.core.data_sources import DataSources  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.dpf_array import DPFArray  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.field import Field, FieldDefinition  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.fields_container import FieldsContainer  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.meshed_region import MeshedRegion  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.scoping import Scoping  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.support import Support  # noqa: F401  # pylint: disable=W0611
from ansys.dpf.core.time_freq_support import TimeFreqSupport  # noqa: F401  # pylint: disable=W0611

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
map_types_to_cpp["UnitSystem"] = "class dataProcessing::unit::CUnitSystem"
map_types_to_cpp["dict"] = "label_space"


class _smart_dict_snake(dict):
    def __missing__(self, key):
        return _snake_to_camel_case(key)


map_types_to_python = _smart_dict_snake()
for k, v in map_types_to_cpp.items():
    map_types_to_python[v] = k
map_types_to_python["vector<double>"] = "list"
map_types_to_python["b"] = "bool"
