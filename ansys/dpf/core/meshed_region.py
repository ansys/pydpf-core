from ansys import dpf
from ansys.grpc.dpf import meshed_region_pb2, meshed_region_pb2_grpc
from ansys.dpf.core import scoping, field
from ansys.dpf.core.common import locations
from ansys.dpf.core.plotter import Plotter as _DpfPlotter


class MeshedRegion:
    """A class used to represent a Mesh"""

    def __init__(self, mesh, channel=None):
        """
        Intialize the mesh with MeshedRegion message

        Parameters
        ----------
        mesh : ansys.grpc.dpf.meshed_region_pb2.MeshedRegion
        
        Attributes
        ----------
        nodes : ansys.dpf.core.meshed_region.Nodes
            Entity containing all the nodal properties
        
        elements : ansys.dpf.core.meshed_region.Elements
            Entity containing all the elemental properties
        """
        
        if channel is None:
            channel = dpf.core._global_channel()       
        
        
        if isinstance(mesh, MeshedRegion):
            self._message = mesh._mesh
        elif isinstance(mesh, meshed_region_pb2.MeshedRegion):
            self._message = mesh
        else:
            self._message=meshed_region_pb2.MeshedRegion()
            self._message.id = mesh.id
                
        self._channel = channel
        self._stub = self._connect()
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
        request = meshed_region_pb2.LocationRequest(mesh=self._message)
        request.loc.location =loc
        out = self._stub.List(request)
        return scoping.Scoping(scoping=out,channel=self._channel)

    
    @property
    def elements(self):
        """ returns instance of Elements which contains all the elemental properties"""
        if self._elements == None:
            self._elements= Elements(self)
        return self._elements

    @property
    def nodes(self):
        """ returns instance of Nodes which contains all the nodal properties"""
        if self._nodes == None:
            self._nodes= Nodes(self)
        return self._nodes
    
    

    @property
    def unit(self):
        """Unit type"""
        return self._get_unit()

    # TODO: Depreciate in favor of unit property
    def _get_unit(self):
        """Returns the unit type

        Returns
        -------
        unit : str
        """
        request = meshed_region_pb2.GetRequest()
        request.mesh.CopyFrom(self._message)
        return self._stub.Get(request).unit

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass

    def _connect(self):
        """Connect to the grpc service containing the reader"""
        return meshed_region_pb2_grpc.MeshedRegionServiceStub(self._channel)


    def __str__(self):
        txt = 'Meshed Region\n'
        txt += '\t%d nodes\n' % self.nodes.n_nodes
        txt += '\t%d elements\n' % self.elements.n_elements
        txt += '\tUnit: %s \n' % self.unit
        return txt

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
    #     return MeshedRegion(self._channel, skin, self._model, name)

    def _as_vtk(self, as_linear=True):
        """Convert DPF mesh to a pyvista unstructured grid"""
        from ansys.dpf.core.vtk_helper import dpf_mesh_to_vtk
        nodes = self.nodes.coordinates_field.data
        etypes = self.elements.element_types_field.data
        conn = self.elements.connectivities_field.data
        grid = dpf_mesh_to_vtk(nodes, etypes, conn, as_linear)
        grid['node_ids'] = self.nodes.scoping.ids
        grid['element_ids'] = self.elements.scoping.ids
        return grid

    @property
    def grid(self):
        """Return full grid by default"""
        if self._full_grid is None:
            self._full_grid = self._as_vtk()
        return self._full_grid
    
    def plot(self, field_or_fields_container=None, is3dplotting=False):
        """Plot the field/fields container on mesh.
        
        Parameters
        ----------
        field_or_fields_container
            dpf.core.Field or dpf.core.FieldsContainer
            
        is3dplotting (default: False)
            bool, that specifies if the plotting is 3D or not
        """
        pl = _DpfPlotter(self)
        if isinstance(field_or_fields_container, dpf.core.Field) or isinstance(field_or_fields_container, dpf.core.FieldsContainer):
            fields_container = None
            if isinstance(field_or_fields_container, dpf.core.Field):
                fields_container = dpf.core.FieldsContainer()
                fields_container.add_label('time')
                fields_container.add_field({'time':1}, field_or_fields_container)
            elif isinstance(field_or_fields_container, dpf.core.FieldsContainer):
                fields_container = field_or_fields_container
            pl.plot_contour(fields_container, not is3dplotting)
        elif(field_or_fields_container is None):
            pl.plot_mesh(not is3dplotting)



class Node:
    """A class used to represent a Node"""
    def __init__(self, mesh, nodeid, index, coordinates):
        self._id = nodeid
        self._index = index
        self._coordinates = coordinates
        self._mesh = mesh
        
    @property
    def index(self):
        return self._index

    @property
    def id(self):
        return self._id

    @property
    def coordinates(self):
        return self._coordinates

    def __str__(self):
        txt = 'DPF Node %d\n' % self.id
        txt += 'Index: %d\n' % self.index
        txt += f'{self.coordinates}\n'
        return txt
    
    


class Element:
    """A class used to represent an Element"""
    def __init__(self, mesh, elementid, index, nodes):
        self._id = elementid
        self._index = index
        self._nodes = nodes
        self._mesh = mesh

    @property
    def node_ids(self):
        node_ids=[]
        for node in self._nodes:
            node_ids.append(node.id)
        return node_ids

    @property
    def id(self):
        return self._id

    @property
    def index(self):
        return self._index

    @property
    def nodes(self):
        return self._nodes

    @property
    def n_nodes(self):
        return len(self._nodes)

    def __str__(self):
        txt = 'DPF Element %d\n' % self.id
        txt += '\tIndex: %d\n' % self.index
        txt += '\tNumber of nodes: %d\n' % self.n_nodes
        return txt
    
    @property
    def element_type(self):
        return self._get_element_type()
    
    @property
    def element_shape(self):
        return self._get_element_shape()
    
    def _get_element_type(self):
        """Returns the element type of the element
       
        Returns
        -------
        element_type : int
        """
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        # request.property = meshed_region_pb2.ElementalPropertyType.ELEMENT_TYPE
        request.property = meshed_region_pb2.ELEMENT_TYPE
        return self._mesh._stub.GetElementalProperty(request).prop

    def _get_element_shape(self):
        """Returns the element shape (beam, shell or solid) of the element 

        Returns
        -------
        element_shape : str
        """
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        request.property = meshed_region_pb2.ELEMENT_SHAPE
        prop = self._mesh._stub.GetElementalProperty(request).prop
        return meshed_region_pb2.ElementShape.Name(prop).lower()


class Nodes():
    """Class to encapsulate mesh nodes"""

    def __init__(self, mesh):
        self._mesh = mesh

    def __str__(self):
        return 'DPF Nodes object with %d nodes\n' % len(self)

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
        request.loc.location = dpf.core.locations.nodal
        if nodeindex is None:
            request.id = nodeid
        else:
            request.index = nodeindex
        nodeOut = self._mesh._stub.Get(request).node
        return Node(self._mesh, nodeOut.id, nodeOut.index, nodeOut.coordinates)
    
    @property
    def scoping(self):
        return self._mesh._get_scoping(loc=dpf.core.locations.nodal)
    
    @property
    def n_nodes(self):
        """Number of nodes"""
        return self.scoping.size
    
    @property
    def coordinates_field(self):
        """Coordinates field

        Returns
        -------
        coordinates_field : Field
            field of all the nodes coordinates
        """
        return self._get_coordinates_field()

    def _get_coordinates_field(self):
        """
        Returns
        -------
        coordinates_field : Field
            field of all the nodes coordinates
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.nodal_property = meshed_region_pb2.NodalPropertyType.COORDINATES
        request.nodal_property = meshed_region_pb2.COORDINATES
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._channel, field=fieldOut)


class Elements():
    """Class to encapsulate mesh elements"""

    def __init__(self, mesh):
        self._mesh = mesh

    def __str__(self):
        return 'DPF Elements object with %d elements' % len(self)

    def __getitem__(self, index):
        """Returns element based on index"""
        return self._mesh.element_by_index(index)

    def __len__(self):
        return self.n_elements

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]   

    def element_by_id(self, id):
        return self.__get_element(elementid=id)

    def element_by_index(self, index):
        return self.__get_element(elementindex=index)

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
        request.loc.location = dpf.core.locations.elemental
        if elementindex is None:
            request.id = elementid
        else:
            request.index = elementindex

        elementOut = self._mesh._stub.Get(request).element
        nodesOut = []
        for node in elementOut.nodes:
            nodesOut.append(Node(self._mesh, node.id, node.index, node.coordinates))
        return Element(self._mesh, elementOut.id, elementOut.index, nodesOut)
    
    @property
    def scoping(self):
        return self._mesh._get_scoping(loc=locations.elemental)

    @property
    def element_types_field(self):
        """Element types field
        
        Returns
        -------
        element_types_field : Field
            field of all the element types
        """
        return self._get_element_types_field()

    def _get_element_types_field(self):
        """
        Returns
        -------
        element_types_field : Field
            field of all the element types
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.ELEMENT_TYPE
        request.elemental_property = meshed_region_pb2.ELEMENT_TYPE
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._channel, field=fieldOut)

    @property
    def materials_field(self):
        """Materials field
        
        Returns
        -------
        materials_field : Field
            field of all the materials ids
        """
        return self._get_materials_field()

    def _get_materials_field(self):
        """
        Returns
        -------
        materials_field : Field
            field of all the materials ids
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.MATERIAL
        request.elemental_property = meshed_region_pb2.MATERIAL
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._channel, field=fieldOut)

    @property
    def connectivities_field(self):
        """Connectivity field
        
        Returns
        -------
        connectivities_field : Field
            Field of all the connectivities (nodes indices associated to an element)
        """
        return self._get_connectivities_field()

    def _get_connectivities_field(self):
        """
        Returns
        -------
        connectivities_field : Field
            Field of all the connectivities (nodes indices associated to an element)
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.CONNECTIVITY
        request.elemental_property = meshed_region_pb2.CONNECTIVITY
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(self._mesh._channel, field=fieldOut)
    

    @property
    def n_elements(self):
        """Number of elements"""
        return self.scoping.size

