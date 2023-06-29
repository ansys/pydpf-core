"""
MeshInfo
==========
"""
import ansys.dpf.core as dpf
from ansys.dpf.core import server as server_module
from ansys.dpf.core.generic_data_container import GenericDataContainer


class MeshInfo:
    """Represents the mesh information.

    This class describes the available mesh information.

    Parameters
    ----------
     server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Explore the mesh info from the model

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> fluent = examples.fluid_axial_model()
    >>> model = dpf.Model(fluent)
    >>> mesh_info = model.metadata.mesh_info_provider # printable mesh_info

    """

    def __init__(self, generic_data_container: GenericDataContainer = None, mesh_info=None, server=None):
        """Initialize with a MeshInfo message"""
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        try:
            if generic_data_container is None and mesh_info is None:
                self._generic_data_container = dpf.generic_data_container.GenericDataContainer()
            elif generic_data_container is not None and mesh_info is None:
                self._generic_data_container = generic_data_container
            elif generic_data_container is None and MeshInfo is not None:
                self._generic_data_container = mesh_info._generic_data_container
        except ValueError:
            print("Both generic data container and mesh info can't be filled")

    def __call__(self):
        return self

    @property
    def generic_data_container(self) -> GenericDataContainer:
        """GenericDataContainer wrapped into the MeshInfo that contains all the relative information of
        the derived class.

        Returns
        -------
        :class:`ansys.dpf.core.generic_data_container.GenericDataContainer`

        """

        return self._generic_data_container

    @generic_data_container.setter
    def generic_data_container(self, value: GenericDataContainer):
        if type(value) is not GenericDataContainer:
            raise ValueError("Input value must be a GenericDataContainer.")
        self._generic_data_container = value

    def deep_copy(self, server=None):
        """Create a deep copy of the scoping's data on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        scoping_copy : Scoping
        """
        mesh_info = MeshInfo(server=server)
        mesh_info._generic_data_container = self.generic_data_container
        return mesh_info

    def get_property(self, property_name, output_type):
        """Get property with given name.

        Parameters
        ----------
        property_name : str
            Property name.
        output_type :  :class:`ansys.dpf.core.common.types`

        Returns
        -------
        type
            Property object instance.
        """
        return self.generic_data_container.get_property(property_name, output_type)

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

    def get_number_nodes(self):
        """
        Returns
        -------
        number_nodes : int
            Number of nodes of the mesh.
        """

        return self.generic_data_container.get_property("num_nodes", int)

    def get_number_elements(self):
        """
        Returns
        -------
        number_elements : int
            Number of elements of the mesh.
        """

        return self.generic_data_container.get_property("num_elements", int)

    def get_splittable_by(self):
        """
        Returns
        -------
        splittable by which entity : StringField
                Name of mesh subdivisions.
        """

        return self.generic_data_container.get_property("splittable_by", dpf.StringField)

    def get_available_elem_types(self):
        """
        Returns
        -------
        available element types : Scoping
            element type available for the mesh.
        """

        return self.generic_data_container.get_property("avalaible_elem_type", dpf.Scoping)

    def set_number_nodes(self, number_of_nodes):
        """Set the number of nodes in the mesh"""

        return self.generic_data_container.set_property("num_nodes", number_of_nodes)

    def set_number_elements(self, number_of_elements):
        """Set the number of elements in the mesh"""

        return self.generic_data_container.set_property("num_elements", number_of_elements)

    def set_splittable_by(self, split):
        """Set name subdivision stringfield of the mesh"""

        return self.generic_data_container.set_property("splittable_by", split)

    def set_available_elem_types(self, available_elem_types):
        """Set the available element types"""

        return self.generic_data_container.set_property("avalaible_elem_type", available_elem_types)
