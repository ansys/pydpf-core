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

"""streams_provider operator for MyFormat files.

The streams_provider is the entry point for DPF's result-file pipeline.
It receives a :class:`~ansys.dpf.core.data_sources.DataSources` and returns a
:class:`~ansys.dpf.core.streams_container.StreamsContainer` that wraps the open
file handle.  Downstream operators (result_info_provider, mesh_provider, etc.)
can receive this container on their pin 3 instead of re-opening the file.

DPF discovers this operator via its namespaced name
``"myformat::stream_provider"``.  When a
:class:`~ansys.dpf.core.data_sources.DataSources` whose result key is
``"myformat"`` is passed to a :class:`~ansys.dpf.core.model.Model`, DPF calls
this operator automatically.
"""

from ansys.dpf import core as dpf
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import (
    CustomSpecification,
    PinSpecification,
    SpecificationProperties,
)
from ansys.dpf.core.streams_container import StreamsContainer


def _make_streams_container(ds: dpf.DataSources) -> StreamsContainer:
    """Create a StreamsContainer from a DataSources.

    Compatible with both the new pydpf-core API (``data_sources`` keyword) and
    the old API found on standalone DPF servers where ``StreamsContainer`` does
    not yet accept a ``data_sources`` argument.
    """
    try:
        return StreamsContainer(data_sources=ds)
    except TypeError:
        # Fallback for older pydpf-core shipped with the DPF server:
        # call streams_new via the low-level C-API and wrap the resulting
        # internal handle in a StreamsContainer.
        from ansys.dpf.gate import streams_capi

        streams_api = ds._server.get_api_for_type(capi=streams_capi.StreamsCAPI, grpcapi=None)
        return StreamsContainer(streams_container=streams_api.streams_new(ds))


class streams_provider(CustomOperatorBase):
    """Create a :class:`~ansys.dpf.core.streams_container.StreamsContainer` from a MyFormat file.

    Inputs
    ------
    pin 4 : DataSources
        DataSources whose first result file points to a ``.myf`` file.

    Outputs
    -------
    pin 0 : StreamsContainer
        An open StreamsContainer wrapping the result file.
    """

    def run(self):
        """Run the operator."""
        ds: dpf.DataSources = self.get_input(4, dpf.DataSources)

        # Build a StreamsContainer that stores the DataSources reference.
        # Downstream operators retrieve the file path via sc.datasources.
        sc = _make_streams_container(ds)

        self.set_output(0, sc)
        self.set_succeeded()

    @property
    def specification(self) -> CustomSpecification:
        """Return the operator specification."""
        spec = CustomSpecification("Creates a StreamsContainer from a MyFormat (.myf) result file.")
        spec.inputs = {
            4: PinSpecification(
                name="data_sources",
                type_names=dpf.DataSources,
                optional=False,
                document="DataSources with a path to a .myf file.",
            ),
        }
        spec.outputs = {
            0: PinSpecification(
                name="streams_container",
                type_names=dpf.StreamsContainer,
                optional=False,
                document="StreamsContainer wrapping the open MyFormat file.",
            ),
        }
        spec.properties = SpecificationProperties(
            user_name="MyFormat streams provider", category="myformat"
        )
        return spec

    @property
    def name(self) -> str:
        """Return the operator scripting name.

        DPF uses the prefix ``myformat::`` to route provider requests for
        DataSources whose result key is ``"myformat"``.
        The suffix ``stream_provider`` (singular) is the name DPF looks up
        internally when constructing a :class:`~ansys.dpf.core.model.Model`.
        """
        return "myformat::stream_provider"
