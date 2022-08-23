"""
FieldDefinition
================
"""

import traceback
import warnings

from ansys.dpf.core.common import natures, shell_layers
from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core.dimensionality import Dimensionality
from ansys.dpf.core import server as server_module
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
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=field_definition_capi.FieldDefinitionCAPI,
            grpcapi=field_definition_grpcapi.FieldDefinitionGRPCAPI
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
            Location string, such as ``"Nodal"``, ``"Elemental"``,
            or ``"TimeFreq_sets"``.
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
        unused = [integral_types.MutableInt32(),
                  integral_types.MutableInt32(),
                  integral_types.MutableDouble(),
                  integral_types.MutableDouble()]
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
        """Dimensionality

        Returns
        -------
        dimensionality : Dimensionality
            Nature and size of the elementary data.
        """
        dim = integral_types.MutableListInt32(size=3)
        nature = integral_types.MutableInt32()
        self._api.csfield_definition_fill_dimensionality(self, dim, nature, dim.internal_size)
        return Dimensionality(dim.tolist(), natures(int(nature)))

    @unit.setter
    def unit(self, value):
        self._api.csfield_definition_set_unit(self, value, None, 0, 0, 0)

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
    def dimensionality(self, value):
        if not isinstance(value, Dimensionality):
            raise TypeError("the dimensionality needs to be of type Dimensionality")
        self._api.csfield_definition_set_dimensionality(
            self, int(value.nature.value), value.dim, len(value.dim)
        )

    def deep_copy(self, server=None):
        """Creates a deep copy of the field_definition's data on a given server.
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
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
