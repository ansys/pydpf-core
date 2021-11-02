"""
MeshedRegion
============
"""
from ansys import dpf
from ansys.grpc.dpf import meshed_region_pb2, meshed_region_pb2_grpc
from ansys.dpf.core import scoping
from ansys.dpf.core.common import locations, types
from ansys.dpf.core.plotter import Plotter as _DpfPlotter
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.nodes import Nodes
from ansys.dpf.core.elements import Elements, element_types
from ansys.dpf.core.check_version import server_meet_version


class MeshedRegion:
    """A class used to represent a Mesh from DPF.

    Parameters
    ----------
    num_nodes : int
        number of nodes to reserve for mesh creation
    
    num_elements : int
        number of elements to reserve for mesh creation
        
    mesh : ansys.grpc.dpf.meshed_region_pb2.MeshedRegion
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Attributes
    ----------
    nodes : Nodes
        Entity containing all the nodal properties

    elements : Elements
        Entity containing all the elemental properties

    Examples
    --------
    Extract a meshed region from a model.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> meshed_region = model.metadata.meshed_region
    
    Create a meshed region from scratch (line with 3 beam elements)
    
    >>> import ansys.dpf.core as dpf
    >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=3)
    >>> i=0
    >>> for node in meshed_region.nodes.add_nodes(4):
    ...     node.id = i+1
    ...     node.coordinates = [float(i), float(i), 0.0]
    ...     i=i+1
    >>> i=0
    >>> for element in meshed_region.elements.add_elements(3):
    ...     element.id=i+1
    ...     element.connectivity = [i, i+1]
    ...     element.is_beam=True #or is_solid, is_beam, is_point
    ...     i=i+1
    >>> meshed_region.elements.add_beam_element(id=4,connectivity=[3,0])
    
    """

    def __init__(self, num_nodes=None, num_elements=None, mesh=None, server=None):

        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()

        if isinstance(mesh, MeshedRegion):
            self._message = mesh._mesh
        elif isinstance(mesh, meshed_region_pb2.MeshedRegion):
            self._message = mesh
        elif mesh==None:
            self.__send_init_request(num_nodes,num_elements)       
        else: #support_pb2.Support
            self._message = meshed_region_pb2.MeshedRegion()
            if isinstance(self._message.id, int):
                self._message.id = mesh.id
            else:
                self._message.id.CopyFrom(mesh.id)
        

        self._full_grid = None
        self._elements = None
        self._nodes = None

    def _get_scoping(self, loc=locations.nodal):
        """
        Parameters
        ----------
        loc : str or ansys.dpf.core.common.locations, optional
            location of the requested scoping ("Nodal", "Elemental"...)

        Returns
        -------
        scoping : Scoping
            ids of the elements or nodes of the mesh
        """
        request = meshed_region_pb2.GetScopingRequest(mesh=self._message)
        request.loc.location = loc
        out = self._stub.GetScoping(request)
        return scoping.Scoping(scoping=out, server=self._server)

    @property
    def elements(self):
        """Gives access to all the elemental properties of the mesh:
            connectivity, element types...

        Returns
        -------
        elements : Elements
            Elements belonging to this meshed region.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> elements = meshed_region.elements
        >>> print(elements)
        DPF Elements object with 8 elements
        
        """
        if self._elements is None:
            self._elements = Elements(self)
        return self._elements

    @property
    def nodes(self):
        """Gives access to all the nodal properties of the mesh:
            nodes coordinates, nodal connectivity...
            
        Returns
        -------
        nodes : Nodes
            Nodes belonging to this meshed region

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = meshed_region.nodes
        >>> nodes.n_nodes
        81
        
        """
        if self._nodes is None:
            self._nodes = Nodes(self)
        return self._nodes
    
    @property
    def unit(self):
        """Unit of the meshed region (same as the unit 
        of the coordinates of the meshed region)
        
        Returns
        -------
        unit : str
        """
        return self._get_unit()
    
    @unit.setter
    def unit(self, value):
        """Unit type
        
        Parameters
        ----------
        unit : str
        """
        return self._set_unit(value)

    def _get_unit(self):
        """Returns the unit type

        Returns
        -------
        unit : str
        """
        return self._stub.List(self._message).unit
    
    def _set_unit(self, unit):
        """Set the unit of the meshed_region.
        
        Parameters
        ----------
        unit: str
        """
        request = meshed_region_pb2.UpdateMeshedRegionRequest()
        request.meshed_region.CopyFrom(self._message)
        request.unit = unit
        return self._stub.UpdateRequest(request)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def _connect(self):
        """Connect to the grpc service containing the reader"""
        return meshed_region_pb2_grpc.MeshedRegionServiceStub(self._server.channel)

    def __str__(self):
        """describe the entity
        
        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description
        return _description(self._message, self._server)
    
    @property
    def available_named_selections(self):
        """Returns a list of available named selections
        
        Returns
        -------
        named_selections : list str
        """
        if hasattr(self._stub, "ListNamedSelections"):
            request = meshed_region_pb2.ListNamedSelectionsRequest()
            request.mesh.CopyFrom(self._message)
            return self._stub.ListNamedSelections(request).named_selections
        else:
            return self._stub.List(self._message).named_selections
    
    def named_selection(self, named_selection):
        """Returns a scoping containing the list of nodes or elements
        in the named selection
        
        Parameters
        ----------
        named_selection : str 
            name of the named selection
            
        Returns
        -------
        named_selection : Scoping
        """
        if server_meet_version("2.1", self._server):
            request = meshed_region_pb2.GetScopingRequest(mesh=self._message)
            request.named_selection = named_selection
            out = self._stub.GetScoping(request)
            return scoping.Scoping(scoping=out, server=self._server)
        else:
            if hasattr(self, "_stream_provider"):
                from ansys.dpf.core.dpf_operator import Operator
                op = Operator("scoping_provider_by_ns", server = self._server)
                op.connect(1,named_selection)
                op.connect(3, self._stream_provider,0)                
                return op.get_output(0, types.scoping)
            else:
                raise Exception("getting a named selection from a meshed region is only implemented for meshed region created from a model for server version 2.0. Please update your server.")
            
    def _set_stream_provider(self, stream_provider):
        self._stream_provider = stream_provider
    # NOTE: kept only for reference as the mesh operator is being moved out of dpf
    # def write_vtk(self, filename, skin_only=True):
    #     """Return a vtk mesh"""
    #     # filename = os.path.join(tempfile.gettempdir(),
    #                             # '%s.vtk' % next(tempfile._get_candidate_names()))

    #     vtk_exp = self._model.operator("vtk_export")
    #     vtk_exp.connect(0, filename)

    #     mesh = self._model.operator("mapdl::rst::MeshProvider")
    #     mesh.connect(4, self._model.data_sources)

    #     if skin_only:
    #         skin = self._model.operator("meshed_skin_sector")
    #         skin.connect(0, mesh, 0)
    #         vtk_exp.connect(1, skin, 0)
    #     else:
    #         vtk_exp.connect(1, mesh, 0)

    #     vtk_exp.run()
    #     if not os.path.isfile(filename):
    #         raise FileNotFoundError('VTK mesh not written to disk')

    # @property
    # def skin(self):
    #     """Surface of the meshed region"""
    #     mesh = self._model.operator("mapdl::rst::MeshProvider")
    #     mesh.connect(4, self._model.data_sources)

        
    #     skin = self._model.operator("meshed_skin_sector")
    #     skin.connect(0, mesh, 0)
    #     # skin.connect(4, self)

    #     skin.get_output(0, types.meshed_region)

    #     name = None
    #     if self._name:
    #         name = 'Skin of %s' % self._name
    #     self._message = skin.get_output(0, types.meshed_region)
    #     return MeshedRegion(self._server.channel, skin, self._model, name)
    
    def _as_vtk(self, as_linear=True, include_ids=False):
        """Convert DPF mesh to a pyvista unstructured grid"""
        nodes = self.nodes.coordinates_field.data
        etypes = self.elements.element_types_field.data
        conn = self.elements.connectivities_field.data
        try:
            from ansys.dpf.core.vtk_helper import dpf_mesh_to_vtk
        except ModuleNotFoundError:
            raise ModuleNotFoundError("to use plotting capabilities, please install pyvista with :\n pip install pyvista>=0.24.0")
       
        grid = dpf_mesh_to_vtk(nodes, etypes, conn, as_linear)

        # consider adding this when scoping request is faster
        if include_ids:
            grid['node_ids'] = self.nodes.scoping.ids
            grid['element_ids'] = self.elements.scoping.ids

        return grid

    @property
    def grid(self):
        """VTK pyvista UnstructuredGrid

        Returns
        -------
        pyvista.UnstructuredGrid
            UnstructuredGrid of the mesh.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> grid = meshed_region.grid

        Plot this grid directly

        >>> grid.plot()
        [(0.0729555495773441, 0.1029555495773441, 0.0729555495773441),
         (0.015, 0.045, 0.015),
         (0.0, 0.0, 1.0)]

        Extract the surface mesh of this grid

        >>> mesh = grid.extract_surface()
            
        """
        if self._full_grid is None:
            self._full_grid = self._as_vtk()
        return self._full_grid

    def plot(self, field_or_fields_container=None, notebook=None,
             shell_layers=None, off_screen=None, show_axes=True, **kwargs):
        """Plot the field/fields container on mesh.

        Parameters
        ----------
        field_or_fields_container
            dpf.core.Field or dpf.core.FieldsContainer

        notebook : bool, optional
            That specifies if the plotting is in the notebook (2D) or not (3D).

        shell_layers : core.shell_layers, optional
            Enum used to set the shell layers if the model to plot
            contains shell elements.

        off_screen : bool, optional
            Renders off screen when ``True``.  Useful for automated screenshots.

        show_axes : bool, optional
            Shows a vtk axes widget.  Enabled by default.

        **kwargs : optional
            Additional keyword arguments for the plotter.  See
            ``help(pyvista.plot)`` for additional keyword arguments.

        Examples
        --------
        Plot the displacement field from an example file

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> disp = model.results.displacement()
        >>> field = disp.outputs.fields_container()[0]
        >>> model.metadata.meshed_region.plot(field)
        [(0.0729555495773441, 0.1029555495773441, 0.0729555495773441),
         (0.015, 0.045, 0.015),
         (0.0, 0.0, 1.0)]
        
        """
        pl = _DpfPlotter(self)
        if field_or_fields_container is not None:
            return pl.plot_contour(field_or_fields_container, notebook, shell_layers,
                                   off_screen, show_axes, **kwargs)

        # otherwise, simply plot self
        kwargs['notebook'] = notebook
        return pl.plot_mesh(**kwargs)
    
    def deep_copy(self,server=None):
        """Creates a deep copy of the meshed region's data on a given server.
        This can be useful to pass data from one server instance to another.
        Warning
        Only nodes scoping and coordinates and elements scoping, connectivity and types 
        are copied. The eventual property field for elemental properties and named selection
        will not be copied.
        
        Parameters
        ----------     
        server : DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the the global server.

        Returns
        -------
        mesh_copy : MeshedRegion
        
        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> other_server = dpf.start_local_server(as_global=False)
        >>> deep_copy = meshed_region.deep_copy(server=other_server)
        
        """
        node_ids = self.nodes.scoping.ids
        element_ids = self.elements.scoping.ids
        mesh = MeshedRegion(num_nodes=len(node_ids), num_elements=len(element_ids),server=server)
        with self.nodes.coordinates_field.as_local_field() as coord:
            for i,node in enumerate(mesh.nodes.add_nodes(len(node_ids))):
                node.id = node_ids[i]
                node.coordinates = coord.get_entity_data(i)
        with self.elements.connectivities_field.as_local_field() as connect :
            with self.elements.element_types_field.as_local_field() as types:
                for i,elem in enumerate(mesh.elements.add_elements(len(element_ids))):
                    elem.id = element_ids[i]
                    elem.connectivity = connect.get_entity_data(i)
                    elem.shape = element_types.shape(types.get_entity_data(i)[0])
        mesh.unit = self.unit
        return mesh
    
    
    def __send_init_request(self, num_nodes=0, num_elements=0):
        request = meshed_region_pb2.CreateRequest()
        if num_nodes:
            request.num_nodes_reserved = num_nodes
        if num_elements:
            request.num_elements_reserved = num_elements
        self._message = self._stub.Create(request)

     