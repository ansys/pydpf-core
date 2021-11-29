# -*- coding: utf-8 -*-
"""
MeshesContainer
===============
Contains classes associated with the DPF MeshesContainer.
"""
from ansys import dpf
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import types
from ansys.dpf.core.plotter import Plotter as _DpfPlotter
from ansys.dpf.core import errors as dpf_errors


class MeshesContainer(Collection):
    """Represents a meshes container, which contains meshes split on a given space.

    Parameters
    ----------
    meshes_container : ansys.grpc.dpf.collection_pb2.Collection or
                       ansys.dpf.core.MeshesContainer, optional
        Create a meshes container from a collection message or create a copy from an
        existing meshes container. The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    """

    def __init__(self, meshes_container=None, server=None):
        """Initialize the scoping with either an optional scoping
        message or by connecting to a stub."""
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()

        Collection.__init__(
            self, types.meshed_region, collection=meshes_container, server=self._server
        )
        

    def plot(self, fields_container=None, **kwargs):
        """
        

        Parameters
        ----------
        fields_container : TYPE, optional
            DESCRIPTION. The default is None.
        **kwargs : TYPE
            DESCRIPTION.
            
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.multishells_rst)
        >>> mesh = model.metadata.meshed_region
        >>> split_mesh_op = dpf.Operator("split_mesh")
        >>> split_mesh_op.connect(7, mesh)
        >>> split_mesh_op.connect(13, "mat")
        >>> meshes_cont = split_mesh_op.outputs.mesh_controller()
        >>> disp_op = dpf.Operator("U")
        >>> disp_op.connect(7, meshes_cont)
        >>> ds = dpf.DataSources(examples.multishells_rst)
        >>> disp_op.connect(4, ds)
        >>> disp_fc = disp_op.outputs.fields_container()
        >>> meshes_cont.plot(disp_fc)
        
        """
        pl = _DpfPlotter()
        
        if fields_container is not None: 
            size = len(fields_container)
            i = 0
            while i < size: 
                label_space = fields_container.get_label_space(i)
                mesh_to_send = self.get_mesh(label_space)
                if mesh_to_send == None:
                    raise dpf_errors.DpfValueError("Meshes container and result fields "
                                                   "container does not have the same scope. "
                                                   "Plotting can not be proceeded. ")
                field = fields_container[i]
                pl.add_field(mesh_to_send, field, **kwargs)
                i += 1
        else:
            for mesh in self:
                pl.add_mesh(mesh, **kwargs)
                
        pl.show_figure(**kwargs)

    def get_meshes(self, label_space):
        """Retrieve the meshes at a label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Meshes corresponding to a filter (label space) in the input. For example:
            ``{"elshape":1, "body":12}``

        Returns
        -------
        meshes : list[MeshedRegion]
            Meshes corresponding to the request.
        """
        return super()._get_entries(label_space)

    def get_mesh(self, label_space_or_index):
        """Retrieve the mesh at a requested index or label space.

        Raises an exception if the request returns more than one mesh.

        Parameters
        ----------
        label_space_or_index : dict[str,int] , int
            Scoping of the requested mesh, such as ``{"time": 1, "complex": 0}``
            or the index of the mesh.

        Returns
        -------
        mesh : MeshedRegion
            Mesh corresponding to the request.
        """
        return super()._get_entry(label_space_or_index)

    def __getitem__(self, key):
        """Retrieves the mesh at a requested index.

        Parameters
        ----------
        key : int
            Index

        Returns
        -------
        mesh : MeshedRegion
            Mesh corresponding to the request.
        """
        return super().__getitem__(key)

    def add_mesh(self, label_space, mesh):
        """Add or update the scoping at a requested label space.

        Parameters
        ----------
        label_space : dict[str,int]
            Label space of the requested meshes. For example, {"elshape":1, "body":12}.

        mesh : MeshedRegion
            DPF mesh to add or update.
        """
        return super()._add_entry(label_space, mesh)

    def __str__(self):
        txt = "DPF Meshes Container with\n"
        txt += "\t%d mesh(es)\n" % len(self)
        txt += f"\tdefined on labels {self.labels} \n\n"
        return txt
