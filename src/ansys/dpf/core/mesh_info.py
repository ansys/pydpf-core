"""
MeshInfo
==========
"""
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

    """

    def __init__(
        self,
        generic_data_container=None,
        mesh_info=None,
        server=None,
    ):
        """Initialize with a MeshInfo message"""
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

    def __str__(self):
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
        """GenericDataContainer wrapped into the MeshInfo
        that contains all the relative information of the derived class.

        Returns
        -------
        :class:`ansys.dpf.core.generic_data_container.GenericDataContainer`

        """

        return self._generic_data_container

    @generic_data_container.setter
    def generic_data_container(self, value: GenericDataContainer):
        """GenericDataContainer wrapped into the MeshInfo
        that contains all the relative information of the derived class.
        """

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
        """
        Returns
        -------
        number_nodes : int
            Number of nodes of the mesh.
        """

        return self.generic_data_container.get_property("num_nodes")

    @property
    def number_elements(self):
        """
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
        """
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
        """
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
        """
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
    def part_scoping(self):
        """
        Returns
        -------
        part_scoping : Scoping
            part Scoping of the mesh (if it can be split by parts)
        """

        if "part_scoping" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("part_scoping")
        else:
            return None

    @property
    def body_names(self):
        """
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
        """
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
    def zone_names(self):
        """
        Returns
        -------
        zone_names : StringField
            zone_names of the mesh (if it can be split by zones)
        """

        if "zone_names" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("zone_names")
        else:
            return None

    @property
    def zone_scoping(self):
        """
        Returns
        -------
        zone_scoping : Scoping
            zone Scoping of the mesh (if it can be split by zone)
        """

        if "zone_scoping" in self._generic_data_container.get_property_description():
            return self.generic_data_container.get_property("zone_scoping")
        else:
            return None

    @number_nodes.setter
    def number_nodes(self, value):
        """Set the number of nodes in the mesh"""

        self.generic_data_container.set_property("num_nodes", value)

    @number_elements.setter
    def number_elements(self, value):
        """Set the number of elements in the mesh"""

        self.generic_data_container.set_property("num_elements", value)

    @splittable_by.setter
    def splittable_by(self, value):
        """Set name of the properties according to which the mesh can be split by"""

        self.generic_data_container.set_property("splittable_by", value)

    @available_elem_types.setter
    def available_elem_types(self, value):
        """Set the available element types"""

        self.generic_data_container.set_property("avalaible_elem_type", value)
