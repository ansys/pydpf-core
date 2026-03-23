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

"""time_freq_support_provider operator for MyFormat files.

Returns a :class:`~ansys.dpf.core.time_freq_support.TimeFreqSupport` with
the frequency sets read from the ``FREQUENCIES`` block of the file.
"""

import my_format_reader as reader
from result_info_provider import _get_file_path

from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)


class time_freq_support_provider(CustomOperatorBase):
    """Return a :class:`~ansys.dpf.core.time_freq_support.TimeFreqSupport` for a MyFormat file.

    Inputs
    ------
    pin 3 : StreamsContainer, optional
        Streams container returned by the streams_provider.
    pin 4 : DataSources
        DataSources with a path to a ``.myf`` file (used when pin 3 is absent).

    Outputs
    -------
    pin 0 : TimeFreqSupport
        Object describing the frequency sets in the result file.
    """

    def run(self):
        """Run the operator."""
        file_path = _get_file_path(self)

        model = reader.read(file_path)
        tfs = _build_time_freq_support(model)

        self.set_output(0, tfs)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification(
            "Reads the time/frequency information from a MyFormat (.myf) result file."
        )
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
                name="time_freq_support",
                type_names=dpf.TimeFreqSupport,
                optional=False,
                document="TimeFreqSupport with the frequency sets of the result file.",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="MyFormat time/frequency support provider", category="myformat"
        )
        return spec

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::myformat::time_freq_support_provider"


def _build_time_freq_support(model: reader.MyFormatModel) -> dpf.TimeFreqSupport:
    """Build a :class:`~ansys.dpf.core.time_freq_support.TimeFreqSupport` from a parsed model."""
    tfs = dpf.TimeFreqSupport()

    # Group all frequency values into a single step for harmonic analyses.
    freq_values = list(model.frequencies.values())
    tfs.append_step(
        step_id=1,
        step_time_frequencies=freq_values,
    )

    return tfs
