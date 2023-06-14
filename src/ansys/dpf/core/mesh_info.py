"""
MeshInfo
==========
"""
import traceback

import ansys.dpf.core
from ansys.dpf.core import server as server_module
from ansys.dpf.core import generic_data_container


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
    >>> mesh_info = model.metadata.mesh_info # printable mesh_info

    >>> mesh_info._get_num_nodes
    '1345'
    >>> mesh_info.get_num_elements
    '16541'

    """

    def __init__(self, mesh_info, server=None):
        """Initialize with a MeshInfo message"""
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: we instanciate the mesh_info by forwarding a generic_data_container
        if mesh_info is not None:
            self._internal_obj = generic_data_container
        elif mesh_info is None:
            raise Exception("Mesh_info given is None")

    # def __str__(self):
    #     try:
    #         txt = ()
    #     return txt
    #     except Exception as e:
    #         from ansys.dpf.core.core import _description
    #
    #         return _description(self._internal_obj, self._server)

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

        return self.get_property(self, property_name, output_type)


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

        return self.set_property(self, property_name, prop)


    def get_number_nodes(self):
        """
        Returns
        -------
        number_nodes : int
            Number of nodes of the mesh.
        """

        return self.get_property(self, "num_nodes", int)


    def get_number_faces(self):
        """
        Returns
        -------
        number_faces : int
            Number of faces of the mesh.
        """

        return self.get_property(self, "num_faces", int)

    def get_number_elements(self):
        """
        Returns
        -------
        number_elements : int
            Number of elements of the mesh.
        """

        return self.get_property(self, "num_elements", int)


    def get_splittable_by(self):
        """
        Returns
        -------
        splittable by which entity : StringField
            Number of elements of the mesh.
        """

        return self.get_property(self, "splittable_by", ansys.dpf.core.StringField)


    def get_available_elem_type(self):
        """
        Returns
        -------
        available element types : Scoping
            element type available for the mesh.
        """

        return self.get_property(self, "avalaible_et", ansys.dpf.core.Scoping)


    def set_number_nodes(self):
        """Number of nodes"""

        return self.set_property(self, "num_nodes", int)

    def set_number_faces(self):
        """ Number of faces """

        return self.set_property(self, "num_faces", int)

    def set_number_elements(self):
        """ Number of elements """

        return self.set_property(self, "num_elements", int)

    def set_splittable_by(self):
        """ Splittable by """

        return self.set_property(self, "splittable_by", ansys.dpf.core.StringField)

    def set_available_elem_types(self):
        """ Available element types """

        return self.set_property(self, "available_et", ansys.dpf.core.Scoping)
