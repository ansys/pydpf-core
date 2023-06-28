"""
MeshInfo
==========
"""
import ansys.dpf.core
from ansys.dpf.core import server as server_module


class MeshInfo:
    """Represents the mesh information.

    This class describes the available mesh information.

    Parameters
    ----------
    mesh_info : ctypes.c_void_p, ansys.grpc.dpf.mesh_info_pb2.MeshInfo message

     server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Explore the mesh info from the model

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> fluent = examples.download_fluent_axial_comp()
    >>> model = dpf.Model(fluent)
    >>> mesh_info = model.metadata.mesh_info_provider # printable mesh_info

    """

    def __init__(self, gdc=None, mesh_info=None, server=None):
        """Initialize with a MeshInfo message"""
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        try:
            if gdc is None and mesh_info is None:
                self._gdc = ansys.dpf.core.generic_data_container.GenericDataContainer()
            elif gdc is not None and mesh_info is None:
                self._gdc = gdc
            elif gdc is None and MeshInfo is not None:
                self._gdc = mesh_info._gdc
        except ValueError:
            print("Both generic data container and mesh info can't be filled")

    def __call__(self):
        return self

    def deep_copy(self, server=None):
        """Create a deep copy of the scoping's data on a given server.

        This method is useful for passiong data from one server instance to another.

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
        mesh_info._gdc = self._gdc
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

        return self._gdc.get_property(property_name, output_type)

    def set_property(self, property_name, prop):
        """Register given property with the given name.

        Parameters
        ----------
        property_name : str
            Property name.
        prop :  type of the property.

        Returns
        -------
        type
            Property object instance.
        """

        return self._gdc.set_property(property_name, prop)

    def get_number_nodes(self):
        """
        Returns
        -------
        number_nodes : int
            Number of nodes of the mesh.
        """

        return self._gdc.get_property("num_nodes", int)

    def get_number_elements(self):
        """
        Returns
        -------
        number_elements : int
            Number of elements of the mesh.
        """

        return self._gdc.get_property("num_elements", int)

    def get_splittable_by(self):
        """
        Returns
        -------
        splittable by which entity : StringField
            Number of elements of the mesh.
        """

        return self._gdc.get_property("splittable_by", ansys.dpf.core.StringField)

    def get_available_elem_types(self):
        """
        Returns
        -------
        available element types : Scoping
            element type available for the mesh.
        """

        return self._gdc.get_property("avalaible_elem_type", ansys.dpf.core.Scoping)

    def set_number_nodes(self, number_of_nodes):
        """Number of nodes"""

        return self._gdc.set_property("num_nodes", number_of_nodes)

    def set_number_elements(self, number_of_elements):
        """Number of elements"""

        return self._gdc.set_property("num_elements", number_of_elements)

    def set_splittable_by(self, split):
        """Splittable by"""

        return self._gdc.set_property("splittable_by", split)

    def set_available_elem_types(self, available_elem_types):
        """Available element types"""

        return self._gdc.set_property("avalaible_elem_type", available_elem_types)
