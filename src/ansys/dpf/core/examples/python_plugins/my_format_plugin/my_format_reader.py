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

"""Utility module to parse files in the MyFormat ASCII format (.myf)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class MyFormatResult:
    """Data for one result quantity across all frequencies.

    Parameters
    ----------
    name : str
        Result name (e.g., ``"displacement"``, ``"temperature"``).
    location : str
        ``"NODAL"`` or ``"ELEMENTAL"``.
    num_components : int
        Number of components per entity (e.g., 3 for displacement, 1 for temperature).
    data : dict
        Mapping ``{freq_id: {entity_id: [v1, v2, ...]}}``
    """

    name: str
    location: str
    num_components: int
    data: Dict[int, Dict[int, List[float]]] = field(default_factory=dict)


@dataclass
class MyFormatModel:
    """In-memory representation of a parsed ``.myf`` file.

    Parameters
    ----------
    analysis_type : str
        Analysis type string read from the ``ANALYSIS_TYPE`` section.
    unit_system : str
        Unit system string read from the ``UNIT_SYSTEM`` section.
    frequencies : dict
        Mapping ``{freq_id: frequency_value}`` for each frequency set.
    node_coords : dict
        Mapping ``{node_id: [x, y, z]}`` for each node.
    elements : dict
        Mapping ``{elem_id: {"type": str, "connectivity": [node_ids]}}``.
    results : list
        :class:`MyFormatResult` objects, one per ``RESULT`` block in the file.
    """

    analysis_type: str
    unit_system: str
    frequencies: Dict[int, float]
    node_coords: Dict[int, List[float]]
    elements: Dict[int, dict]
    results: List[MyFormatResult]


def read(file_path: str | Path) -> MyFormatModel:
    """Parse a ``.myf`` file and return a :class:`MyFormatModel`.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the ``.myf`` file to read.

    Returns
    -------
    MyFormatModel
        In-memory representation of the file contents.

    Raises
    ------
    FileNotFoundError
        If *file_path* does not point to an existing file.
    ValueError
        If the file is malformed.
    """
    path = Path(file_path)
    lines = path.read_text(encoding="utf-8").splitlines()

    def _tokens(line: str) -> List[str]:
        return line.strip().split()

    analysis_type = "unknown"
    unit_system = "m_kg_s"
    frequencies: Dict[int, float] = {}
    node_coords: Dict[int, List[float]] = {}
    elements: Dict[int, dict] = {}
    results: List[MyFormatResult] = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip comments and blank lines.
        if not line or line.startswith("#"):
            i += 1
            continue

        tokens = _tokens(line)
        keyword = tokens[0].upper()

        if keyword == "ANALYSIS_TYPE":
            analysis_type = tokens[1]

        elif keyword == "UNIT_SYSTEM":
            unit_system = tokens[1]

        elif keyword == "FREQUENCIES":
            # Next non-blank/non-comment line: NUM_FREQS N
            i += 1
            while lines[i].strip().startswith("#") or not lines[i].strip():
                i += 1
            num_freqs = int(_tokens(lines[i])[1])
            for _ in range(num_freqs):
                i += 1
                parts = _tokens(lines[i])
                frequencies[int(parts[0])] = float(parts[1])

        elif keyword == "NODES":
            i += 1
            while lines[i].strip().startswith("#") or not lines[i].strip():
                i += 1
            num_nodes = int(_tokens(lines[i])[1])
            for _ in range(num_nodes):
                i += 1
                parts = _tokens(lines[i])
                node_coords[int(parts[0])] = [float(parts[1]), float(parts[2]), float(parts[3])]

        elif keyword == "ELEMENTS":
            i += 1
            while lines[i].strip().startswith("#") or not lines[i].strip():
                i += 1
            num_elems = int(_tokens(lines[i])[1])
            for _ in range(num_elems):
                i += 1
                parts = _tokens(lines[i])
                elem_id = int(parts[0])
                elem_type = parts[1]
                connectivity = [int(n) for n in parts[2:]]
                elements[elem_id] = {"type": elem_type, "connectivity": connectivity}

        elif keyword == "RESULT":
            result_name = None
            location = None
            num_components = None
            result_data: Dict[int, Dict[int, List[float]]] = {}
            current_freq_id = None

            while True:
                i += 1
                if i >= len(lines):
                    break
                inner = lines[i].strip()
                if not inner or inner.startswith("#"):
                    continue

                inner_tokens = _tokens(inner)
                inner_key = inner_tokens[0].upper()

                if inner_key == "NAME":
                    result_name = inner_tokens[1]
                elif inner_key == "LOCATION":
                    location = inner_tokens[1].upper()
                elif inner_key == "NUM_COMPONENTS":
                    num_components = int(inner_tokens[1])
                elif inner_key == "FREQ_ID":
                    current_freq_id = int(inner_tokens[1])
                    result_data[current_freq_id] = {}
                elif inner_key in {
                    "RESULT",
                    "NODES",
                    "ELEMENTS",
                    "FREQUENCIES",
                    "ANALYSIS_TYPE",
                    "UNIT_SYSTEM",
                }:
                    # A new top-level block starts; step back so the outer loop
                    # processes this line.
                    i -= 1
                    break
                else:
                    # Entity value line: id  v1 [v2 v3 ...]
                    if current_freq_id is not None:
                        entity_id = int(inner_tokens[0])
                        values = [float(v) for v in inner_tokens[1:]]
                        result_data[current_freq_id][entity_id] = values

            results.append(
                MyFormatResult(
                    name=result_name,
                    location=location,
                    num_components=num_components,
                    data=result_data,
                )
            )

        i += 1

    return MyFormatModel(
        analysis_type=analysis_type,
        unit_system=unit_system,
        frequencies=frequencies,
        node_coords=node_coords,
        elements=elements,
        results=results,
    )
