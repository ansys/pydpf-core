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

"""FieldDefinition."""

from __future__ import annotations

import traceback
import warnings

from ansys.dpf.core import server as server_module
from ansys.dpf.core.available_result import Homogeneity
from ansys.dpf.core.check_version import server_meet_version_and_raise, version_requires
from ansys.dpf.core.common import natures, shell_layers
from ansys.dpf.core.dimensionality import Dimensionality
from ansys.dpf.gate import (
    field_definition_capi,
    field_definition_grpcapi,
    integral_types,
)


class FieldDefinition:
    """Contains the physical and mathematical description of the field.

    Parameters
    ----------
    field_definition : optional
        The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use
        the global server.
    """

    def __init__(self, field_definition=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            field_definition._server if isinstance(field_definition, FieldDefinition) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=field_definition_capi.FieldDefinitionCAPI,
            grpcapi=field_definition_grpcapi.FieldDefinitionGRPCAPI,
        )

        # step3: init environment
        self._api.init_field_definition_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if field_definition is not None:
            self._internal_obj = field_definition
        else:
            if self._server.has_client():
                self._internal_obj = self._api.field_definition_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.field_definition_new()

    @property
    def location(self):
        """Field location.

        Returns
        -------
        str
            Location string, such as :class:`ansys.dpf.core.locations.nodal`,
            :class:`ansys.dpf.core.locations.elemental` or
            :class:`ansys.dpf.core.locations.time_freq`.
        """
        location = integral_types.MutableString(256)
        size = integral_types.MutableInt32(0)
        self._api.csfield_definition_fill_location(self, location, size)
        return str(location)

    @property
    @version_requires("4.0")
    def name(self):
        """Field name.

        Returns
        -------
        str
        """
        name = integral_types.MutableString(256)
        size = integral_types.MutableInt32(0)
        self._api.csfield_definition_fill_name(self, name, size)
        return str(name)

    @property
    def unit(self):
        """Units of the field.

        Returns
        -------
        str
            Units of the field.
        """
        unit = integral_types.MutableString(256)
        unused = [
            integral_types.MutableInt32(),
            integral_types.MutableInt32(),
            integral_types.MutableDouble(),
            integral_types.MutableDouble(),
        ]
        self._api.csfield_definition_fill_unit(self, unit, *unused)
        return str(unit)

    @property
    def shell_layers(self):
        """Order of the shell layers.

        Returns
        -------
        shell_layers : shell_layers
            ``LayerIndependent`` is returned for fields unrelated to layers.
        """
        enum_val = self._api.csfield_definition_get_shell_layers(self)
        return shell_layers(
            enum_val.real  # - 1
        )  # +1 is added to the proto enum to have notset as 0

    @property
    def dimensionality(self):
        """Dimensionality.

        Returns
        -------
        dimensionality : Dimensionality
            Nature and size of the elementary data.
        """
        dim = integral_types.MutableListInt32(size=3)
        nature = integral_types.MutableInt32()
        self._api.csfield_definition_fill_dimensionality(self, dim, nature, dim.internal_size)
        return Dimensionality(dim.tolist(), natures(int(nature)))

    @property
    def quantity_types(self):
        """Getter for Quantity Types.

        Returns
        -------
        str
            All quantity types of the elementary data for this FieldDefinition.
        """
        quantity_types = []
        for i in range(self.num_quantity_types()):
            qt = self._api.csfield_definition_get_quantity_type(self, i)
            quantity_types.append(str(qt))

        return quantity_types

    def add_quantity_type(self, quantity_type_to_add):
        """Add a new Quantity Type.

        Parameters
        ----------
        quantity_type_to_add: str
            Quantity type to add
        """
        self._api.csfield_definition_set_quantity_type(self, quantity_type_to_add)

    def num_quantity_types(self):
        """Return number of available quantity types.

        Returns
        -------
        num_quantity_types : int
            Number of quantity types
        """
        num_quantity_types = self._api.csfield_definition_get_num_available_quantity_types(self)
        return num_quantity_types

    def is_of_quantity_type(self, quantity_type):
        """Check if the field definition is of a given quantity type.

        Parameters
        ----------
        quantity_type: str
            Quantity type to check

        Returns
        -------
        is_of_quantity_type : bool
            True if the field definition is of the given quantity type
        """
        is_of_quantity_type = self._api.csfield_definition_is_of_quantity_type(self, quantity_type)
        return is_of_quantity_type

    @unit.setter
    def unit(self, value: str | tuple[Homogeneity, str]):
        """Change the unit for the field definition.

        A single string is interpreted as a known physical unit with an associated homogeneity.

        For DPF 11.0 (2026 R1) and above: A tuple of two strings is interpreted as a homogeneity and a unit name.
            If the homogeneity is :py:attr:`Homogeneity.dimensionless`, then the unit string is kept as a name.
            Otherwise, the homogeneity is ignored, and the unit string interpreted as a known physical unit with an associated homogeneity.

        Parameters
        ----------
        value:
            Units for the field.

        Notes
        -----
        Setting a named dimensionless unit requires DPF 11.0 (2026 R1) or above.

        """
        # setter with explicit homogeneity: homogeneity is taken into account if it is dimensionless
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], Homogeneity)
            and isinstance(value[1], str)
        ):
            server_meet_version_and_raise(
                required_version="11.0",
                server=self._server,
                msg="Setting a named dimensionless unit requires DPF 11.0 (2026 R1) or above.",
            )
            # csfield_definition_set_unit will ignore the homogeneity if it is not dimensionless
            self._api.csfield_definition_set_unit(self, value[1], None, value[0].value, 0, 0)
        # standard unit setter, using string interpreter
        elif isinstance(value, str):
            self._api.csfield_definition_set_unit(self, value, None, 0, 0, 0)
        else:
            raise ValueError("Unit setter supports either string or tuple(Homogeneity, str)")

    @location.setter
    def location(self, value):
        self._api.csfield_definition_set_location(self, value)

    @name.setter
    @version_requires("4.0")
    def name(self, value):
        self._api.csfield_definition_set_name(self, value)

    @shell_layers.setter
    def shell_layers(self, value):
        if hasattr(value, "value"):
            value = value.value
        self._api.csfield_definition_set_shell_layers(self, value)

    @dimensionality.setter
    def dimensionality(self, value: Dimensionality):
        if not isinstance(value, Dimensionality):
            raise TypeError("the dimensionality needs to be of type Dimensionality")
        self._api.csfield_definition_set_dimensionality(
            self, int(value.nature.value), value.dim, len(value.dim)
        )

    def deep_copy(self, server=None):
        """Create a deep copy of the field_definition's data on a given server.

        This can be useful to pass data from one server instance to another.

        Parameters
        ----------
        server : DPFServer, optional

        Returns
        -------
        field_definition_copy : FieldDefinition
        """
        out = FieldDefinition(server=server)
        out.unit = self.unit
        out.location = self.location
        out.dimensionality = self.dimensionality
        out.shell_layers = self.shell_layers
        return out

    def __del__(self):
        """Delete the current instance."""
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
