"""
MeshedRegion
============
"""
import numpy as np

from ansys import dpf
from ansys.grpc.dpf import meshed_region_pb2, meshed_region_pb2_grpc, base_pb2
from ansys.dpf.core import scoping, field
from ansys.dpf.core.common import locations
from ansys.dpf.core.plotter import Plotter as _DpfPlotter
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.core import BaseService
from ansys.dpf.core.vtk_helper import dpf_mesh_to_vtk

   
class MeshedRegion:
    """A class used to represent a Mesh from DPF.

    Parameters
    ----------
    num_nodes : int
        number of nodes to reserve for mesh creation
    
    num_elements : int
        number of elements to reserve for mesh creation
        
    mesh : ansys.grpc.dpf.meshed_region_pb2.MeshedRegion
    
    server : DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

    Attributes
    ----------
    nodes : ansys.dpf.core.meshed_region.Nodes
        Entity containing all the nodal properties

    elements : ansys.dpf.core.meshed_region.Elements
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
            node.id = i+1
            node.coordinates = [float(i), float(i), 0.0]
            i=i+1
    >>> i=0
    >>> for element in meshed_region.elements.add_elements(3):
            element.id=i+1
            element.connectivity = [i, i+1]
            element.is_beam=True #or is_solid, is_beam, is_point
            i=i+1
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
            self._message.id = mesh.id
        

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
        """Returns elements collection containing all elements
        belonging to this meshed region.

        Returns
        -------
        Elements
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
        """Returns nodes collection.

        Returns
        -------
        Nodes
            Nodes collection contains all the nodal properties of the
            nodes belonging to this mesh region.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = meshed_region.nodes
        >>>print(nodes)
        DPF Node collection with 81 nodes
        """
        if self._nodes is None:
            self._nodes = Nodes(self)
        return self._nodes
    
    @property
    def unit(self):
        """Unit type"""
        return self._get_unit()

    def _get_unit(self):
        """Returns the unit type

        Returns
        -------
        unit : str
        """
        return self._stub.List(self._message).unit

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
        return BaseService(self._server)._description(self._message)
    
    @property
    def available_named_selections(self):
        """Returns a list of available named selections
        
        Returns
        -------
        named_selections : list str
        """
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
        named_selection : dpf.core.Scoping
        """
        request = meshed_region_pb2.GetScopingRequest(mesh=self._message)
        request.named_selection = named_selection
        out = self._stub.GetScoping(request)
        return scoping.Scoping(scoping=out, server=self._server)
        
        

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
        >>> grid = meshed_region.grid
        >>> grid
        UnstructuredGrid (0x7f9a64b41910)
          N Cells:	24982
          N Points:	71987
          X Bounds:	-7.297e-01, 3.703e+00
          Y Bounds:	-1.299e+00, 1.331e+00
          Z Bounds:	-6.268e-02, 7.495e+00
          N Arrays:	3

        Plot this grid directly

        >>> grid.plot()

        Extract the surface mesh of this grid

        >>> mesh = grid.extract_surface()
        >>> mesh
        PolyData (0x7f9a5d150b40)
          N Cells:	11190
          N Points:	8855
          X Bounds:	-7.273e-01, 3.700e+00
          Y Bounds:	-1.299e+00, 1.329e+00
          Z Bounds:	-6.087e-02, 7.495e+00
          N Arrays:	5

        Access the corresponding node and element IDs of the surface mesh

        >>> mesh.point_arrays
        pyvista DataSetAttributes
        Association: POINT
        Contains keys:
                node_ids
                vtkOriginalPointIds

        >>> mesh.point_arrays['node_ids']
            pyvista_ndarray([    1,   179, 65561, ..., 72150, 72145, 72144])
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
        """
        pl = _DpfPlotter(self)
        if field_or_fields_container is not None:
            return pl.plot_contour(field_or_fields_container, notebook, shell_layers,
                                   off_screen, show_axes, **kwargs)

        # otherwise, simply plot self
        kwargs['notebook'] = notebook
        return pl.plot_mesh(**kwargs)
    
    @protect_grpc
    def __send_init_request(self, num_nodes=0, num_elements=0):
        request = meshed_region_pb2.CreateRequest()
        if num_nodes:
            request.num_nodes_reserved = num_nodes
        if num_elements:
            request.num_elements_reserved = num_elements
        self._message = self._stub.Create(request)


class Node:
    """A DPF Node

    Created from an element or a meshed region.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> nodes = model.metadata.meshed_region.nodes

    Initialize a node from a nodes collection

    >>> node = nodes[0]
    >>> print(node)
    DPF Node  63631
    Index:    63247
    Location: [-0.72324787407068, 0.80845567299105, 1.2400404500674]

    Initialize a node from an element

    >>> element = model.metadata.meshed_region.elements[0]
    >>> node = element.nodes[0]
    """

    def __init__(self, mesh, nodeid, index, coordinates):
        self._id = nodeid
        self._index = index
        self._coordinates = coordinates
        self._mesh = mesh

    @property
    def index(self) -> int:
        """Fortran index of the node in the model"""
        return self._index

    @property
    def id(self) -> int:
        """Node number"""
        return self._id

    @property
    def coordinates(self):
        """Cartesian coordinates of the node.

        Examples
        --------
        >>> node.coordinates
        [-0.72324787407068, 0.80845567299105, 1.2400404500674]
        """
        return self._coordinates

    def __str__(self):
        txt = 'DPF Node     %7d\n' % self.id
        txt += 'Index:      %7d\n' % self.index
        txt += f'Location: {self.coordinates}\n'
        return txt


class Element:
    """A DPF element.

    Created from a ``MeshedRegion``.

    Parameters
    ----------
    mesh : MeshedRegion
        ``MeshedRegion`` containing this element.

    elementid : int
        Element ID.  This is the element number corresponding to the element.

    index : int
        Index of the element.  Fortran based index of the element in
        the result.

    nodes : list[Node]
        List of DPF nodes belonging to the element.

    Examples
    --------
    Extract a single element from a meshed region

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> elements = model.metadata.meshed_region.elements
    >>> element = elements[0]
    >>> print(element)
    DPF Element 29502
            Index:            1
            Nodes:           10
            Type:             0
            Shape:        Solid

    List the coordinates belonging to the first node of the element

    >>> element.nodes[0].coordinates
    [-0.72324787407068, 0.80845567299105, 1.2400404500674]
    """

    def __init__(self, mesh, elementid, index, nodes):
        self._id = elementid
        self._index = index
        self._nodes = nodes
        self._mesh = mesh

    @property
    def node_ids(self):
        """IDs of all the nodes in this element

        Returns
        --------
        list
            IDs of all the nodes in this element

        Examples
        --------
        >>> element.node_ids
        [1, 2, 3, 4, 5, 6, 7, 8]
        """
        return [node.id for node in self._nodes]

    @property
    def id(self) -> int:
        """Element number"""
        return self._id

    @property
    def index(self) -> int:
        """Fortran based index of the element in the result"""
        return self._index

    @property
    def nodes(self):
        """List of Nodes

        Examples
        --------
        >>> print(element.nodes[1])
        DPF Node  63631
        Index:    63247
        Location: [-0.72324787407068, 0.80845567299105, 1.2400404500674]
        """
        return self._nodes

    @property
    def n_nodes(self) -> int:
        """Number of nodes"""
        return len(self._nodes)

    def __str__(self):
        txt = 'DPF Element %d\n' % self.id
        txt += '\tIndex:      %7d\n' % self.index
        txt += '\tNodes:      %7d\n' % self.n_nodes
        txt += '\tType:       %7d\n' % self.type
        txt += '\tShape:      %7s\n' % self.shape.capitalize()
        return txt

    @property
    def type(self) -> int:
        """Element type of this element.

        Examples
        --------
        >>> element.type
        6
        """
        return self._get_type()

    @protect_grpc
    def _get_type(self):
        """Return the Ansys element type"""
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        request.property = meshed_region_pb2.ELEMENT_TYPE
        return self._mesh._stub.GetElementalProperty(request).prop

    @property
    def shape(self) -> str:
        """Element shape.

        Can be ``'shell'``, ``'solid'``, ``'beam'``, or ``'unknown_shape'``.

        Examples
        --------
        >>> element.shape
        'solid'
        """
        return self._get_shape()

    @protect_grpc
    def _get_shape(self):
        """Return the element shape"""
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        request.property = meshed_region_pb2.ELEMENT_SHAPE
        prop = self._mesh._stub.GetElementalProperty(request).prop
        return meshed_region_pb2.ElementShape.Name(prop).lower()
    
    @property
    def connectivity(self):
        """Return the ordered list of node indexes of the element
        
        Returns
        --------
        connectivity : list of int
        """
        list=[]
        for node in self._nodes:
            list.append(node.index)
        return list
        


class Nodes():
    """Collection of DPF Nodes.

    Created from a MeshedRegion

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> meshed_region = model.meshed_region
    >>> nodes = model.metadata.meshed_region.nodes
    >>> print(nodes)
    DPF Nodes object with 71987 nodes
    """

    def __init__(self, mesh):
        self._mesh = mesh
        self._mapping_id_to_index = None

    def __str__(self):
        return f'DPF Node collection with {len(self)} nodes\n'

    def __getitem__(self, index):
        """Returns node based on index"""
        return self.node_by_index(index)

    def __len__(self):
        return self.n_nodes

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def node_by_id(self, id):
        """Array of node coordinates ordered by index"""
        return self.__get_node(nodeid=id)

    def node_by_index(self, index):
        """Array of node coordinates ordered by index"""
        return self.__get_node(nodeindex=index)

    @protect_grpc
    def __get_node(self, nodeindex=None, nodeid=None):
        """Returns the node by its id or its index

        Parameters
        ----------
        nodeid : int
            id of the requested node

        nodeindex : int
            index of the requested node

        Returns
        -------
        node : ansys.dpf.core.meshed_region.Node
            Requested node
        """
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(self._mesh._message)
        if nodeindex is None:
            request.id = nodeid
        else:
            request.index = nodeindex
        nodeOut = self._mesh._stub.GetNode(request)
        return Node(self._mesh, nodeOut.id, nodeOut.index, nodeOut.coordinates)

    @property
    def scoping(self):
        """Return the scoping of the Nodes

        Returns
        -------
        scoping.Scoping
            Scoping of the Nodes

        Examples
        --------
        Get the ids of all the nodes in this collection

        >>> nodes.scoping.ids
        [1,
         2,
         3,
         4,
        ...]
        """
        return self._mesh._get_scoping(loc=dpf.core.locations.nodal)

    @property
    def n_nodes(self):
        """Number of nodes"""
        return self._mesh._stub.List(self._mesh._message).num_nodes

    @property
    def coordinates_field(self):
        """Coordinates field

        Returns
        -------
        coordinates_field : Field
            field of all the nodes coordinates

        Examples
        --------
        >>> print(nodes.coordinates_field)
        DPF  Field
                Location: Nodal
                71987 id(s)
                Shape: (71987, 3)

        Extract the array of coordinates the coordinates field
        
        >>> nodes.coordinates_field.data
        array([[ 3.40556124, -0.24838723,  0.69582925],
               [ 3.49706859, -0.151947  ,  0.6686485 ],
               [ 3.43478821, -0.24973448,  0.69217843],
               ...,
               [ 3.44598692, -0.10708114,  0.64389383],
               [ 3.453663  , -0.14285579,  0.61316773],
               [ 3.39599888, -0.22926613,  0.66507732]])
        """
        return self._get_coordinates_field()

    @protect_grpc
    def _get_coordinates_field(self):
        """Return the coordinates field"""
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.nodal_property = meshed_region_pb2.NodalPropertyType.COORDINATES
        request.nodal_property = meshed_region_pb2.COORDINATES
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._server.channel, field=fieldOut)

    def _build_mapping_id_to_index(self):
        """Return a mapping between ids and indices of the entity."""
        return {eid: i for i, eid in enumerate(self.scoping.ids)}

    @property
    def mapping_id_to_index(self):
        if self._mapping_id_to_index is None:
            self._mapping_id_to_index = self._build_mapping_id_to_index()
        return self._mapping_id_to_index

    def map_scoping(self, external_scope):
        """Return the indices to map the scoping of these elements to
        the scoping of a field.

        Parameters
        ----------
        external_scope : scoping.Scoping
            Scoping to map to.

        Returns
        -------
        indices : numpy.ndarray
            List of indices to map from the external scope to the
            scoping of these nodes.

        mask : numpy.ndarray
            Members of the external scope that are in the node scoping.

        Examples
        --------
        Return the indices that map a field to a nodes collection.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> nodes = model.metadata.meshed_region.nodes
        >>> disp = model.results.displacements()
        >>> field = disp.outputs.field_containers()[0]
        >>> ind, mask = nodes.map_scoping(field.scoping)
        >>> ind, mask
        array([ 508,  509,  909, ..., 3472, 3471, 3469])
        array([True, True, True, ..., True, True, True])

        These indices can then be used to remap ``nodes.coordinates`` to
        match the order of the field data.  That way the field data matches the
        order of the nodes in the ``meshed_region``

        >>> mapped_nodes = nodes.coordinates[ind]

        """
        if external_scope.location in ['Elemental', 'NodalElemental']:
            raise ValueError('Input scope location must be "Nodal"')
        arr = np.array(list(map(self.mapping_id_to_index.get, external_scope.ids)))
        mask = arr != None
        ind = arr[mask].astype(np.int)
        return ind, mask
    
    def add_node(self, id, coordinates):
        """Appends a new node in the mesh
        
        Parameters
        ----------
        id : int
            new node's id
        
        coordinates : list of doubles
            x, y, z coordinates of the node
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        node_request = meshed_region_pb2.NodeRequest(id=id)
        node_request.coordinates.extend(coordinates)
        request.nodes.append(node_request)
        self._mesh._stub.Add(request)
        
    def add_nodes(self, num):   
        """Add num new nodes in the mesh. 
        add_nodes yields num nodes that the user can fill
        
        Parameters
        ----------
        num : int
            number of nodes to add
        
        Returns
        -------
        yield node : _NodeAdder
            node to add
        
        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=3)
        >>> for i, node in enumerate(meshed_region.nodes.add_nodes(4)):
        ...     node.id = i+1
        ...     node.coordinates = [float(i), float(i), 0.0]
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        for i in range(0, num):
            add = _NodeAdder()
            yield add
            node_request = meshed_region_pb2.NodeRequest(id=add.id)
            node_request.coordinates.extend(add.coordinates)
            request.nodes.append(node_request)
        self._mesh._stub.Add(request)
        

class Elements():
    """Elements belonging to a ``meshed_region``.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> elements = model.metadata.meshed_region.elements
    >>> print(elements)
    DPF Elements object with 24982 elements
    """

    def __init__(self, mesh):
        self._mesh = mesh
        self._mapping_id_to_index = None

    def __str__(self):
        return 'DPF Elements object with %d elements' % len(self)

    def __getitem__(self, index):
        """Returns element based on index"""
        return self.element_by_index(index)

    def __len__(self):
        return self.n_elements

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def element_by_id(self, id) -> Element:
        """Return an element using its element number (id).

        Parameters
        ----------
        id : int
            Element number.

        Returns
        -------
        Element
            DPF Element

        """
        return self.__get_element(elementid=id)

    def element_by_index(self, index) -> Element:
        """Return an element using its index.

        Parameters
        ----------
        index : int
            Zero-based index.

        Returns
        -------
        Element
            DPF Element.

        Examples
        --------
        elements.element_by_index(0)

        Notes
        -----
        This is equivalent to ``elements[0]``

        """
        return self.__get_element(elementindex=index)  
        
    def add_elements(self, num):     
        """Add num new elements in the mesh. 
        add_elements yields num element that the user can fill
        
        Parameters
        ----------
        num : int
            number of elements to add
        
        Returns
        -------
        yield element : _ElementAdder
            element to add
        
        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=3)
        >>> i=0
        >>> for node in meshed_region.nodes.add_nodes(4):
                node.id = i+1
                node.coordinates = [float(i), float(i), 0.0]
                i=i+1
        >>> i=0
        >>> for element in meshed_region.elements.add_elements(3):
                element.id=i+1
                element.connectivity = [i, i+1]
                element.is_beam=True #or is_solid, is_beam, is_point
                i=i+1
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        for i in range(0, num):
            add = _ElementAdder()
            yield add
            element_request = meshed_region_pb2.ElementRequest(id=add.id)
            element_request.connectivity.extend(add.connectivity)          
            element_request.shape =meshed_region_pb2.ElementShape.Value(add.shape.upper())
            request.elements.append(element_request)  
        self._mesh._stub.Add(request)
    
    def add_solid_element(self, id, connectivity):
        """Appends a new solid 3D element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indexes connected to the the element
        """
        self.add_element(id,"solid",connectivity)

    def add_shell_element(self, id, connectivity):
        """Appends a new shell 2D element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indexes connected to the the element
        """
        self.add_element(id, "shell",connectivity)   
        
    def add_beam_element(self, id, connectivity):
        """Appends a new beam 1D element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indexes connected to the the element
        """
        self.add_element(id, "beam",connectivity)   
        
    def add_point_element(self, id, connectivity):
        """Appends a new point element (1 node connectivity) in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indexes connected to the the element
        """
        if not isinstance(connectivity, list):
            connectivity = [connectivity]
        self.add_element(id, "unknown_shape",connectivity)
    
    def add_element(self, id, shape, connectivity):
        """Appends a new element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
            
        shape : str
            shape of the element, expected are "solid", "shell", "beam" or "unknown_shape"
        
        connectivity : list of int
            list of node indexes connected to the the element
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        element_request = meshed_region_pb2.ElementRequest(id=id)
        element_request.connectivity.extend(connectivity)
        element_request.shape = meshed_region_pb2.ElementShape.Value(shape.upper())
        request.elements.extend([element_request])
        self._mesh._stub.Add(request)
    
    @protect_grpc
    def __get_element(self, elementindex=None, elementid=None):
        """Returns the element by its id or its index

        Parameters
        ----------
        elementid : int
            id of the requested element
        elementindex : int
            index of the requested element

        Returns
        -------
        element : Element
        """
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(self._mesh._message)
        if elementindex is None:
            request.id = elementid
        else:
            request.index = elementindex

        elementOut = self._mesh._stub.GetElement(request)
        nodesOut = []
        for node in elementOut.nodes:
            nodesOut.append(Node(self._mesh, node.id, node.index, node.coordinates))
        return Element(self._mesh, elementOut.id, elementOut.index, nodesOut)

    @property
    def scoping(self) -> scoping.Scoping:
        """The Scoping of the elements.

        Examples
        --------
        >>> print(elements.scoping)
        DPF Scoping Object
        Size: 24982
        Location: Elemental
        """
        return self._mesh._get_scoping(loc=locations.elemental)

    @property
    def element_types_field(self):
        """Element types field

        Returns
        -------
        element_types_field : core.Field
            Field of all the element types.

        Examples
        --------
        >>> field = elements.element_types_field
        >>> field.data
        array([0, 0, 0, ..., 0, 0, 0], dtype=int32)
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.ELEMENT_TYPE
        request.elemental_property = meshed_region_pb2.ELEMENT_TYPE
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._server.channel, field=fieldOut)

    @property
    @protect_grpc
    def materials_field(self):
        """Materials field

        Returns
        -------
        materials_field : core.Field
            Field of all the materials ids.

        Examples
        --------
        Extract the material ids from the materials_field

        >>> elements.materials_field.data
        array([1, 1, 1, ..., 1, 1, 1], dtype=int32)
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.MATERIAL
        request.elemental_property = meshed_region_pb2.MATERIAL
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._server.channel, field=fieldOut)

    @property
    def connectivities_field(self):
        """Connectivity field

        Returns
        -------
        connectivities_field : core.Field
            Field of the node indices associated to each element.

        Examples
        --------
        >>> field = elements.connectivities_field
        >>> field.data
        array([ 523,  532,  531, ..., 2734, 2732, 2736], dtype=int32)
        """
        return self._get_connectivities_field()

    @protect_grpc
    def _get_connectivities_field(self):
        """Return the connectivities field"""
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.CONNECTIVITY
        request.elemental_property = meshed_region_pb2.CONNECTIVITY
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._server.channel, field=fieldOut)

    @property
    def n_elements(self) -> int:
        """Number of elements"""
        return self._mesh._stub.List(self._mesh._message).num_element

    def _build_mapping_id_to_index(self):
        """Return a mapping between ids and indices of the entity."""
        return {eid: i for i, eid in enumerate(self.scoping.ids)}

    @property
    def mapping_id_to_index(self) -> dict:
        """Mapping between the ids and indices of the entity.

        Useful for mapping scalar results from a field to this meshed region.

        Examples
        --------
        >>> meshed_region.mapping_id_to_index
        {28947: 0,
         29502: 1,
         29101: 2,
         28563: 3,
         29503: 4,
        ...
        }

        """
        if self._mapping_id_to_index is None:
            self._mapping_id_to_index = self._build_mapping_id_to_index()
        return self._mapping_id_to_index

    def map_scoping(self, external_scope):
        """Return the indices to map the scoping of these elements to
        the scoping of a field.

        Parameters
        ----------
        external_scope : scoping.Scoping
            Scoping to map to.

        Returns
        -------
        indices : numpy.ndarray
            List of indices to map from the external scope to the
            scoping of these elements.

        mask : numpy.ndarray
            Members of the external scope that are in the element scoping.

        Examples
        --------
        Return the indices that map a field to an elements collection.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> elements = model.metadata.meshed_region.elements
        >>> vol = model.results.volume()
        >>> field = vol.outputs.field_containers()[0]
        >>> ind, mask = elements.map_scoping(field.scoping)
        >>> ind
        [66039
         11284,
         26474,
         11286,
         27090,
         26656,
         11287,
         ...]

        These indices can then be used to remap ``field.data`` to
        match the order of the elements.  That way the field data matches the
        order of the elements in the ``meshed_region``

        >>> mapped_data = field.data[ind]

        """
        if external_scope.location in ['Nodal', 'NodalElemental']:
            raise ValueError('Input scope location must be "Nodal"')
        arr = np.array(list(map(self.mapping_id_to_index.get, external_scope.ids)))
        mask = arr != None
        ind = arr[mask].astype(np.int)
        return ind, mask
    
    @property
    def has_shell_elements(self) -> bool:
        """Returns true if at list one element is a 2D element (shell)"""
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_shell_elements
   
    @property
    def has_solid_elements(self) -> bool:
        """Returns true if at list one element is a 3D element (solid)"""
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_solid_elements
    
    @property
    def has_beam_elements(self) -> bool:
        """Returns true if at list one element is a 1D beam element"""
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_beam_elements
    
    @property
    def has_point_elements(self) -> bool:
        """Returns true if at list one element is a point element"""
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_point_elements
    
    

class _NodeAdder:
    """A class used to add new nodes into a meshed region
    
    Attributes
    ----------
    id : int
    
    coordinates : list of doubles
        x, y, z coordinates
    
    Examples
    --------
    Create a meshed region from scratch
    
    >>> import ansys.dpf.core as dpf
    >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=1)
    >>> i=0
    >>> for node in meshed_region.nodes.add_nodes(4):
            node.id = i+1
            node.coordinates = [float(i), float(i), 0.0]       
            i=i+1 
    """
    def __init__(self):
        self.id=0
        self.coordinates=[0.0,0.0,0.0]
        
class _ElementAdder:
    """A class used to add new elements into a meshed region
    
    Attributes
    ----------
    id : int
    
    connectivity : list of int
        ordered list of node indexes of the element
        
    shape : str
        "solid", "shell", "beam" or "unknown_shape"
    
    Examples
    --------
    Create a meshed region from scratch
    
    >>> import ansys.dpf.core as dpf
    >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=1)
    >>> i=0
    >>> for node in meshed_region.nodes.add_nodes(4):
            node.id = i+1
            node.coordinates = [float(i), float(i), 0.0]
            i=i+1
    >>> for element in meshed_region.elements.add_elements(1):
            element.id=1
            element.connectivity = range(0,4)
            element.is_shell=True #or is_solid, is_beam, is_point
    """
    def __init__(self):
        self.id=0
        self.connectivity=[0]
        self._shape_info={"solid":True, "shell":False, "beam":False,"point":False}
    
    @property
    def is_solid(self) ->bool :
        return self._shape_info["solid"]
    
    @is_solid.setter
    def is_solid(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["solid"]=True
    
    @property
    def is_shell(self) ->bool :
        return self._shape_info["shell"]
    
    @is_shell.setter
    def is_shell(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["shell"]=True
    
    @property
    def is_beam(self) ->bool :
        return self._shape_info["beam"]
    
    @is_beam.setter
    def is_beam(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["beam"]=True
    
    @property
    def is_point(self) ->bool :
        return self._shape_info["point"]
    
    @is_point.setter
    def is_point(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["point"]=True
     
    @property
    def shape(self) ->str:
        """Gives the element shape
        
        Returns
        --------
        shape : str
            "solid", "shell", "beam" or "unknown_shape"
        """
        if self.is_solid:
            return "solid"
        elif self.is_shell:            
            return "shell"
        elif self.is_beam:    
            return "beam"        
        else:   
            return "unknown_shape"  
    
    @shape.setter
    def shape(self, value):
        """Set the element shape
        
        Parameters
        --------
        shape : str
            "solid", "shell", "beam" or "unknown_shape"
        """
        if value == "solid":
            self.is_solid=True 
        elif value =="shell":            
            self.is_shell =True
        elif value =="beam":    
            self.is_beam=True     
        else:   
            self.is_point=True
        
    
     