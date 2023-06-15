"""
MeshInfo
==========
"""
import traceback
import warnings

import ansys.dpf.core
from ansys.dpf.core import server as server_module
from ansys.dpf.core import generic_data_container
from ansys.dpf.core import errors


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

    def __init__(self, mesh_info=None, server=None):
        """Initialize with a MeshInfo message"""
        # ############################
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if not self._server.meet_version("7.0"):
            raise errors.DpfVersionNotSupported("7.0")

        # step 2: we instantiate the mesh_info by forwarding a generic_data_container
        if mesh_info is not None:
            self._internal_obj = mesh_info
        else:
            self._internal_obj = generic_data_container

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

        return self.get_property(self, "avalaible_elem_type", ansys.dpf.core.Scoping)

    def set_number_nodes(self, number_of_nodes):
        """Number of nodes"""

        return self.set_property(self, "num_nodes", number_of_nodes)

    def set_number_elements(self, number_of_elements):
        """Number of elements"""

        return self.set_property(self, "num_elements", number_of_elements)

    def set_splittable_by(self, split):
        """Splittable by"""

        return self.set_property(self, "splittable_by", split)

    def set_available_elem_types(self, available_elem_types):
        """Available element types"""

        return self.set_property(self, "avalaible_elem_type", available_elem_types)

    def __del__(self):
        if self._internal_obj is not None:
            try:
                self._deleter_func[0](self._deleter_func[1](self))
            except Exception as e:
                print(str(e.args), str(self._deleter_func[0]))
                warnings.warn(traceback.format_exc())
