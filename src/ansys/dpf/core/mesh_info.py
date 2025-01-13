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

"""MeshInfo."""

from ansys.dpf.core import server as server_module
from ansys.dpf.core.generic_data_container import GenericDataContainer


class MeshInfo:
    """Hold the information relative to a mesh region.

    This class describes the available mesh information.

    Parameters
    ----------
     server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
     generic_data_container : ansys.dpf.core.generic_data_container, optional
        Generic data container that is wrapped into the mesh info.
     mesh_info : optional
        Hold the information of the mesh region into a generic data container.

    Examples
    --------
    Explore the mesh info from the model

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> fluent = examples.fluid_axial_model()
    >>> model = dpf.Model(fluent)
    >>> mesh_info = model.metadata.mesh_info

    Notes
    -----
    Class available with server's version starting at 7.0 (2024 R1 pre0).
    """

    def __init__(
        self,
        generic_data_container=None,
        mesh_info=None,
        server=None,
    ):
        """Initialize with a MeshInfo message."""
        # ############################
        # step 1: get server

        if generic_data_container is None and mesh_info is None:
            self._server = server_module.get_or_create_server(server)
            self._generic_data_container = GenericDataContainer(server=self._server)
        elif generic_data_container is not None and mesh_info is None:
            self._server = generic_data_container._server
            self._generic_data_container = generic_data_container
        elif generic_data_container is None and MeshInfo is not None:
            self._server = mesh_info.generic_data_container._server
            self._generic_data_container = mesh_info.generic_data_container
        else:
            raise ValueError(
                "Arguments generic_data_container and mesh_info are mutually exclusive."
            )
        self._part_map = None
        self._zone_map = None
        self._cell_zone_map = None
        self._face_zone_map = None
        self._bodies_map = None

    def __str__(self):
        """
        Return a string representation of the MeshInfo instance.

        Returns
        -------
        str
            A string representation of the information about a mesh space.
        """
        txt = "DPF MeshInfo\n"
        txt += "-" * 30 + "\n"
        txt += "with properties:\n"
        txt += "\n".join(
            "  {:20s}\t{:s}".format(k, v)
            for k, v in self._generic_data_container.get_property_description().items()
        )
        return txt

    @property
    def generic_data_container(self) -> GenericDataContainer:
        """GenericDataContainer wrapped into the MeshInfo that contains all the relative information of the derived class.

        Returns
        -------
        :class:`ansys.dpf.core.generic_data_container.GenericDataContainer`

        """
        return self._generic_data_container

    @generic_data_container.setter
    def generic_data_container(self, value: GenericDataContainer):
        """GenericDataContainer wrapped into the MeshInfo that contains all the relative information of the derived class."""
        if not isinstance(value, GenericDataContainer):
            raise ValueError("Input value must be a GenericDataContainer.")
        self._generic_data_container = value
        self._server = self._generic_data_container._server

    def deep_copy(self, server=None):
        """Create a deep copy of the mesh_info's data on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        mesh_info_copy : MeshInfo
        """
        mesh_info = MeshInfo(server=server)
        mesh_info.generic_data_container = self._generic_data_container.deep_copy(server)
        return mesh_info

    def get_property(self, property_name):
        """Get property with given name.

        Parameters
        ----------
        property_name : str
            Property name.

        Returns
        -------
        Property object instance.
        """
        return self.generic_data_container.get_property(property_name)

    def set_property(self, property_name, prop):
        """Register given property with the given name.

        Parameters
        ----------
        property_name : str
            Property name.
        prop : Int, String, Float, Field, StringField, GenericDataContainer, Scoping
            object instance.
        """
        return self.generic_data_container.set_property(property_name, prop)

    @property
    def number_nodes(self):
        """Returns number of nodes in the mesh.

        Returns
        -------
        number_nodes : int
            Number of nodes of the mesh.
        """
        return self.generic_data_container.get_property("num_nodes")

    @property
    def number_faces(self):
        """Returns number of faces in the mesh.

        Returns
        -------
        number_faces : int
            Number of faces of the mesh.
        """
        if "num_faces" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("num_faces")
        else:
            return 0

    @property
    def number_elements(self):
        """Returns number of elements in the mesh.

        Returns
        -------
        number_elements : int
            Number of elements of the mesh.
        """
        if "num_cells" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("num_cells")
        else:
            return self.generic_data_container.get_property("num_elements")

    @property
    def splittable_by(self):
        """Return name of properties according to which the mesh can be split by.

        Returns
        -------
        splittable by which entity : StringField
            Name of the properties according to which the mesh can be split by.
        """
        if "splittable_by" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("splittable_by")
        else:
            return None

    @property
    def available_elem_types(self):
        """Returns available mesh element types.

        Returns
        -------
        available element types : Scoping
            element type available for the mesh.
        """
        if "available_elem_types" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("available_elem_types")
        else:
            return None

    @property
    def part_names(self):
        """Return part names of the mesh.

        Returns
        -------
        part_names : StringField
            part names of the mesh (if it can be split by parts)
        """
        if "part_names" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("part_names")
        else:
            return None

    @property
    def parts(self) -> dict:
        """Dictionary of available part IDs to part names.

        Returns
        -------
        parts:
            Map of part IDs to part names.

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if self._part_map:
            return self._part_map
        part_names = self.part_names
        part_map = {}
        if part_names:
            names = part_names.data
            for i, key in enumerate(part_names.scoping.ids):
                part_map[str(key)] = names[i]
        self._part_map = part_map
        return self._part_map

    @property
    def part_scoping(self):
        """Return part scoping of the mesh.

        Returns
        -------
        part_scoping : Scoping
            part Scoping of the mesh (if it can be split by parts)

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if "part_scoping" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("part_scoping")
        else:
            return None

    @property
    def body_names(self):
        """Return body names of the mesh.

        Returns
        -------
        body_names : StringField
            body names of the mesh (if it can be split by bodies)
        """
        if "body_names" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("body_names")
        else:
            return None

    @property
    def body_scoping(self):
        """Return body scoping of the mesh.

        Returns
        -------
        body_scoping : Scoping
            body Scoping of the mesh (if it can be split by bodies)
        """
        if "body_scoping" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("body_scoping")
        else:
            return None

    @property
    def bodies(self) -> dict:
        """Dictionary of available body IDs to body names.

        Returns
        -------
        bodies:
            Map of body IDs to body names.

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if self._bodies_map:
            return self._bodies_map
        body_names = self.body_names
        bodies_map = {}
        if body_names:
            names = body_names.data
            for i, key in enumerate(body_names.scoping.ids):
                bodies_map[str(key)] = names[i]
        self._bodies_map = bodies_map
        return self._bodies_map

    @property
    def zone_names(self):
        """Return zone names of the mesh.

        Returns
        -------
        zone_names : StringField
            zone_names of the mesh (if it can be split by zones)

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if "zone_names" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("zone_names")
        else:
            return None

    @property
    def zones(self) -> dict:
        """Dictionary of available zone IDs to zone names.

        Returns
        -------
        zones:
            Map of zone IDs to zone names.

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if self._zone_map:
            return self._zone_map
        zone_names = self.zone_names
        zone_map = {}
        if zone_names:
            names = zone_names.data
            for i, key in enumerate(zone_names.scoping.ids):
                zone_map[str(key)] = names[i]
        self._zone_map = zone_map
        return self._zone_map

    @property
    def face_zones(self) -> dict:
        """Dictionary of available face zone IDs to face zone names.

        Returns
        -------
        face_zones:
            Map of face zone IDs to face zone names.

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if self._face_zone_map:
            return self._face_zone_map
        if "zone_names" in self._generic_data_container.get_property_description():
            zone_names = self.generic_data_container.get_property("face_zone_names")
        else:
            zone_names = None
        zone_map = {}
        if zone_names:
            names = zone_names.data
            for i, key in enumerate(zone_names.scoping.ids):
                zone_map[str(key)] = names[i]
        self._face_zone_map = zone_map
        return self._face_zone_map

    @property
    def cell_zones(self) -> dict:
        """Dictionary of available cell zone IDs to cell zone names.

        Returns
        -------
        cell_zones:
            Map of cell zone IDs to cell zone names.

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if self._cell_zone_map:
            return self._cell_zone_map
        if "zone_names" in self._generic_data_container.get_property_description():
            zone_names = self.generic_data_container.get_property("cell_zone_names")
        else:
            zone_names = None
        zone_map = {}
        if zone_names:
            names = zone_names.data
            for i, key in enumerate(zone_names.scoping.ids):
                zone_map[str(key)] = names[i]
        self._cell_zone_map = zone_map
        return self._cell_zone_map

    @property
    def zone_scoping(self):
        """Return zone scoping of the mesh.

        Returns
        -------
        zone_scoping : Scoping
            zone Scoping of the mesh (if it can be split by zone)

        .. warning:
            Currently unavailable for LegacyGrpc servers.
        """
        if "zone_scoping" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("zone_scoping")
        else:
            return None

    @number_nodes.setter
    def number_nodes(self, value):
        """Set the number of nodes in the mesh."""
        self.generic_data_container.set_property("num_nodes", value)

    @number_elements.setter
    def number_elements(self, value):
        """Set the number of elements in the mesh."""
        self.generic_data_container.set_property("num_elements", value)

    @splittable_by.setter
    def splittable_by(self, value):
        """Set name of the properties according to which the mesh can be split by."""
        self.generic_data_container.set_property("splittable_by", value)

    @available_elem_types.setter
    def available_elem_types(self, value):
        """Set the available element types."""
        self.generic_data_container.set_property("available_elem_types", value)
