# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""result_info_provider operator for MyFormat files.

Returns a :class:`~ansys.dpf.core.result_info.ResultInfo` describing the
available result quantities (name, location, nature, homogeneity) and the
analysis type.
"""

import my_format_reader as reader

from ansys.dpf import core as dpf
from ansys.dpf.core.available_result import Homogeneity
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)
from ansys.dpf.core.result_info import analysis_types, physics_types

# Map MyFormat location strings to DPF location constants.
_LOCATION_MAP = {
    "NODAL": dpf.locations.nodal,
    "ELEMENTAL": dpf.locations.elemental,
}

# Map number of components to DPF natures.
_NATURE_MAP = {
    1: dpf.natures.scalar,
    3: dpf.natures.vector,
    6: dpf.natures.symmatrix,
}

# Map result names to DPF Homogeneity values.
_HOMOGENEITY_MAP = {
    "displacement": Homogeneity.displacement,
    "temperature": Homogeneity.temperature,
}


class result_info_provider(CustomOperatorBase):
    """Return a :class:`~ansys.dpf.core.result_info.ResultInfo` for a MyFormat file.

    Inputs
    ------
    pin 3 : StreamsContainer, optional
        Streams container returned by the streams_provider.
    pin 4 : DataSources
        DataSources with a path to a ``.myf`` file (used when pin 3 is absent).

    Outputs
    -------
    pin 0 : ResultInfo
        Metadata describing the available result quantities.
    """

    def run(self):
        """Run the operator."""
        file_path = _get_file_path(self)

        model = reader.read(file_path)
        result_info = _build_result_info(model)

        self.set_output(0, result_info)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification("Reads result metadata from a MyFormat (.myf) result file.")
        spec.inputs = {
            3: PinSpecification(
                name="streams_container",
                type_names=dpf.StreamsContainer,
                optional=True,
                document="Streams container (optional); takes priority over pin 4.",
            ),
            4: PinSpecification(
                name="data_sources",
                type_names=dpf.DataSources,
                optional=True,
                document="DataSources with a path to a .myf file.",
            ),
        }
        spec.outputs = {
            0: PinSpecification(
                name="result_info",
                type_names=dpf.ResultInfo,
                optional=False,
                document="ResultInfo describing available results.",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="MyFormat result info provider", category="myformat"
        )
        return spec

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::myformat::result_info_provider"


# ---------------------------------------------------------------------------
# Helpers shared across operator modules
# ---------------------------------------------------------------------------


def _get_file_path(operator: CustomOperatorBase) -> str:
    """Return the result file path from pin 3 (StreamsContainer) or pin 4 (DataSources)."""
    try:
        sc: dpf.StreamsContainer = operator.get_input(3, dpf.StreamsContainer)
        result_files = sc.datasources.result_files
        if result_files:
            return result_files[0]
    except Exception:
        pass
    ds: dpf.DataSources = operator.get_input(4, dpf.DataSources)
    return ds.result_files[0]


def _build_result_info(model: reader.MyFormatModel) -> dpf.ResultInfo:
    """Build a :class:`~ansys.dpf.core.result_info.ResultInfo` from a parsed model."""
    analysis_type_map = {
        "static": analysis_types.static,
        "harmonic": analysis_types.harmonic,
        "transient": analysis_types.transient,
        "modal": analysis_types.modal,
    }
    a_type = analysis_type_map.get(model.analysis_type.lower(), analysis_types.static)

    result_info = dpf.ResultInfo(
        analysis_type=a_type,
        physics_type=physics_types.mechanical,
    )

    for res in model.results:
        homogeneity = _HOMOGENEITY_MAP.get(res.name.lower(), Homogeneity.dimensionless)
        location = _LOCATION_MAP.get(res.location, dpf.locations.nodal)
        nature = _NATURE_MAP.get(res.num_components, dpf.natures.scalar)

        result_info.add_result(
            operator_name=f"myformat::myformat::{res.name}",
            scripting_name=res.name,
            homogeneity=homogeneity,
            location=location,
            nature=nature,
            dimensions=[res.num_components],
            description=f"MyFormat result: {res.name}",
        )

    return result_info
