# -*- coding: utf-8 -*-
"""
MeshesContainer
===============
Contains classes associated to the DPF MeshesContainer
"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types


class MeshesContainer(Collection):
    """A class used to represent a MeshesContainer which contains
    meshes splitted on a given space

    Parameters
    ----------
    meshes_container : ansys.grpc.dpf.collection_pb2.Collection or ansys.dpf.core.MeshesContainer, optional
        Create a meshes container from a Collection message or create a copy from an existing meshes container

    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    """

    def __init__(self, meshes_container=None, server=None):
        """Initialize the scoping with either optional scoping message,
        or by connecting to a stub.
        """
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()
        
        Collection.__init__(self, types.meshed_region,  
                            collection=meshes_container, server=self._server)

    def get_meshes(self, label_space_or_index):
        """Returns the meshes at a requested index or label space

        Parameters
        ----------
        label_space_or_index (optional) : dict(string:int) or int
            Meshes correponding to the filter (label space) in input, for example:
            ``{"elshape":1, "body":12}``
            or Index of the mesh.

        Returns
        -------
        meshes : list of MeshedRegion or MeshedRegion (if only one)
            meshes corresponding to the request
        """
        return super()._get_entries(label_space_or_index)

    def __getitem__(self, key):
        """Returns the mesh at a requested index

        Parameters
        ----------
        key : int
            the index

        Returns
        -------
        mesh : MeshedRegion
            mesh corresponding to the request
        """
        return super().__getitem__(key)

    def add_mesh(self, label_space, mesh):
        """Update or add the scoping at a requested label space.

        Parameters
        ----------
        label_space : dict(string:int)
            label_space of the requested meshes, ex : {"elshape":1, "body":12}

        mesh : MeshedRegion
            DPF mesh to add.
        """
        return super()._add_entry(label_space, mesh)

    def __str__(self):
        txt = 'DPF Meshes Container with\n'
        txt += "\t%d mesh(es)\n" % len(self)
        txt += f"\tdefined on labels {self.labels} \n\n"
        return txt

    
