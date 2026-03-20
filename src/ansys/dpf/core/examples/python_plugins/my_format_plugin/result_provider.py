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

"""Result provider operators for MyFormat files.

Two concrete result operators are provided:

- :class:`displacement_provider` — returns a nodal displacement
  :class:`~ansys.dpf.core.fields_container.FieldsContainer`.
- :class:`temperature_provider` — returns an elemental temperature
  :class:`~ansys.dpf.core.fields_container.FieldsContainer`;

Both inherit from the base :class:`_result_provider` class,  which handles
reading the file and building the FieldsContainer.  Only the ``name`` property
and constructor arguments differ between the two.

Result operators follow the DPF pin convention for result providers:

- Pin 0 : ``time_scoping`` (optional ``int``) — 1-based frequency-set index to
  extract.  When absent all frequency sets are returned.
- Pin 3 : ``streams_container`` (optional) — takes priority over pin 4.
- Pin 4 : ``data_sources`` — fallback when pin 3 is absent.
- Output pin 0 : :class:`~ansys.dpf.core.fields_container.FieldsContainer`.
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
from ansys.dpf.gate.errors import DPFServerException


class _result_provider(CustomOperatorBase):
    """Base class for MyFormat result providers."""

    # Subclasses set this to the result name as it appears in the .myf file.
    _result_name: str = ""

    def run(self):
        """Run the operator."""
        file_path = _get_file_path(self)

        # Optional: restrict to a single frequency set.
        try:
            time_scoping: int = self.get_input(0, int)
        except DPFServerException:
            time_scoping = None

        model = reader.read(file_path)
        fc = _build_fields_container(model, self._result_name, time_scoping)

        self.set_output(0, fc)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification(
            f"Reads the '{self._result_name}' result from a MyFormat (.myf) file."
        )
        spec.inputs = {
            0: PinSpecification(
                name="time_scoping",
                type_names=int,
                optional=True,
                document="1-based index of the frequency set to extract. "
                "All sets are returned when absent.",
            ),
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
                name="fields_container",
                type_names=dpf.FieldsContainer,
                optional=False,
                document="FieldsContainer with one Field per frequency set.",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name=f"MyFormat {self._result_name} provider", category="myformat"
        )
        return spec


class displacement_provider(_result_provider):
    """Return nodal displacement results from a MyFormat file.

    Each field in the output :class:`~ansys.dpf.core.fields_container.FieldsContainer`
    corresponds to one frequency set (label ``"time"``).

    Inputs / Outputs
    ----------------
    See :class:`_result_provider` for the full pin description.
    """

    _result_name = "displacement"

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::displacement"


class temperature_provider(_result_provider):
    """Return elemental temperature results from a MyFormat file.

    Each field in the output :class:`~ansys.dpf.core.fields_container.FieldsContainer`
    corresponds to one frequency set (label ``"time"``).

    Inputs / Outputs
    ----------------
    See :class:`_result_provider` for the full pin description.
    """

    _result_name = "temperature"

    @property
    def name(self) -> str:
        """Return the operator scripting name."""
        return "myformat::temperature"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def _build_fields_container(
    model: reader.MyFormatModel,
    result_name: str,
    time_scoping: int | None,
) -> dpf.FieldsContainer:
    """Build a FieldsContainer for *result_name* from a parsed model.

    Parameters
    ----------
    model : MyFormatModel
        Parsed representation of the .myf file.
    result_name : str
        Result name to extract (e.g., ``"displacement"``).
    time_scoping : int or None
        1-based index of the frequency set to return, or ``None`` for all sets.

    Returns
    -------
    FieldsContainer
        One :class:`~ansys.dpf.core.field.Field` per requested frequency set,
        labelled with ``"time"``.
    """
    # Find the result entry.
    result_entry = next((r for r in model.results if r.name.lower() == result_name.lower()), None)
    if result_entry is None:
        raise ValueError(
            f"Result '{result_name}' not found in the file. "
            f"Available results: {[r.name for r in model.results]}"
        )

    location = dpf.locations.nodal if result_entry.location == "NODAL" else dpf.locations.elemental
    num_comp = result_entry.num_components

    fc = dpf.FieldsContainer()
    fc.add_label("time")

    # Determine which frequency sets to return.
    freq_ids = list(result_entry.data.keys())
    if time_scoping is not None:
        if time_scoping not in freq_ids:
            raise ValueError(
                f"Requested frequency set id {time_scoping} not found. "
                f"Available ids: {freq_ids}"
            )
        freq_ids = [time_scoping]

    for freq_id in freq_ids:
        entity_data = result_entry.data[freq_id]
        entity_ids = list(entity_data.keys())

        scoping = dpf.Scoping(location=location, ids=entity_ids)

        if num_comp == 1:
            field = dpf.Field(
                nature=dpf.natures.scalar, location=location, nentities=len(entity_ids)
            )
        else:
            field = dpf.fields_factory.create_vector_field(
                num_entities=len(entity_ids),
                num_comp=num_comp,
                location=location,
            )

        flat_data = []
        for eid in entity_ids:
            flat_data.extend(entity_data[eid])

        field.scoping = scoping
        field.data = flat_data
        field.name = result_name

        fc.add_field(label_space={"time": freq_id}, field=field)

    return fc
