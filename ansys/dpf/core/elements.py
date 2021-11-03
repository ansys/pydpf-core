"""
Elements
========
"""

import numpy as np
from enum import Enum


from ansys import dpf
from ansys.dpf.core import scoping, field, property_field
from ansys.grpc.dpf import meshed_region_pb2
from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.common import locations, elemental_properties
from ansys.dpf.core import nodes
from ansys.dpf.core.common import __write_enum_doc__

class Element:
    """An element of the mesh. Encapsulates all the properties of an element: 
        its id, index, element type, element shape, connectivity...

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
    

    List the coordinates belonging to the first node of the element

    >>> element.nodes[0].coordinates
    [0.015, 0.045, 0.015]
    
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
        node_ids : list[int]
            IDs of all the nodes in this element

        Examples
        --------
        >>> element.node_ids
        [1, 26, 14, 12, 2, 27, 15, 13, 33, 64, 59, 30, 37, 65, 61, 34, 28, 81, 63, 58]
        
        """
        return [node.id for node in self._nodes]

    @property
    def id(self) -> int:
        """Element number"""
        return self._id

    @property
    def index(self) -> int:
        """Index of the element in the result (int starting at 0)"""
        return self._index

    @property
    def nodes(self):
        """List of Nodes
        
        Returns
        --------
        nodes : list[Node]

        Examples
        --------
        >>> first_node = element.nodes[0]
        
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
        txt += f'\tType:       {self.type}\n'  
        txt += '\tShape:      %7s\n' % self.shape.capitalize()
        return txt

    @property
    def type(self) -> int:
        """Element type of this element.
        
        Returns
        -------
        element_type : element_types

        Examples
        --------
        >>> element.type
        <element_types.Hex20: 1>
        
        """
        return self._get_type()

    def _get_type(self):
        """Return the Ansys element type"""
        prop = self._get_single_property(elemental_properties.element_type)
        return element_types(prop)

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

    def _get_shape(self):
        """Return the element shape"""
        prop = self._get_single_property(elemental_properties.element_shape)
        return meshed_region_pb2.ElementShape.Name(prop).lower()

    @protect_grpc
    def _get_single_property(self, property_name):
        """Return the element shape"""
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        if hasattr(request, "property_name"):
            request.property_name.property_name = property_name
        elif property_name in elemental_properties._elemental_property_type_dict:
            request.property = meshed_region_pb2.ElementalPropertyType.Value(
                elemental_properties._elemental_property_type_dict[property_name]
            )
        else:
            raise ValueError(property_name + " property is not supported")

        return self._mesh._stub.GetElementalProperty(request).prop

    @property
    def connectivity(self):
        """Return the ordered list of node indices of the element
        
        Returns
        --------
        connectivity : list[int]
        """
        list=[]
        for node in self._nodes:
            list.append(node.index)
        return list
        

class Elements():
    """Elements belonging to a ``meshed_region``.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> elements = model.metadata.meshed_region.elements
    >>> elements.n_elements
    8
     
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
        element : Element.

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
        yield element : ElementAdder
            element to add
        
        Examples
        --------
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
                
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        for i in range(0, num):
            add = ElementAdder()
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
            list of node indices connected to the the element
        """
        self.add_element(id,"solid",connectivity)

    def add_shell_element(self, id, connectivity):
        """Appends a new shell 2D element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indices connected to the the element
        """
        self.add_element(id, "shell",connectivity)   
        
    def add_beam_element(self, id, connectivity):
        """Appends a new beam 1D element in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indices connected to the the element
        """
        self.add_element(id, "beam",connectivity)   
        
    def add_point_element(self, id, connectivity):
        """Appends a new point element (1 node connectivity) in the mesh
        
        Parameters
        ----------
        id : int
            new element's id
        
        connectivity : list of int
            list of node indices connected to the the element
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
            list of node indices connected to the the element
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
            nodesOut.append(nodes.Node(self._mesh, node.id, node.index, node.coordinates))
        return Element(self._mesh, elementOut.id, elementOut.index, nodesOut)

    @property
    def scoping(self) -> scoping.Scoping:
        """The Scoping of the elements.

        Examples
        --------
        >>> my_scoping = elements.scoping
        
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
        array([1, 1, 1, 1, 1, 1, 1, 1])
        
        """
        return self._mesh.field_of_properties(elemental_properties.element_type)

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
        array([1, 1, 1, 1, 1, 1, 1, 1])
        
        """
        return self._mesh.field_of_properties(elemental_properties.material)

    @property
    def connectivities_field(self):
        """Connectivity field : field containing for each element id
        the nodes indices connected to the given element

        Returns
        -------
        connectivities_field : Field
            Field of the node indices associated to each element.

        Examples
        --------
        >>> field = elements.connectivities_field
        >>> field.get_entity_data(1)
        array([ 0, 11, 13, 25,  2,  9,  8,  3, 29, 58, 63, 32, 40, 52, 42, 37, 28,
               55, 53, 43])

        """
        return self._get_connectivities_field()

    @protect_grpc
    def _get_connectivities_field(self):
        """Return the connectivities field"""
        return self._mesh.field_of_properties(elemental_properties.connectivity)

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
        >>> meshed_region.nodes.mapping_id_to_index
        {1: 0, 2: 1, 3: 2, 4: 3}

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
        >>> vol = model.results.elemental_volume()
        >>> field = vol.outputs.fields_container()[0]
        >>> ind, mask = elements.map_scoping(field.scoping)
        >>> ind
        array([0, 1, 2, 3, 4, 5, 6, 7])
        
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
    

class ElementAdder:
    """A class used to add new elements into a meshed region
    
    Attributes
    ----------
    id : int
    
    connectivity : list of int
        ordered list of node indices of the element
        
    shape : str
        "solid", "shell", "beam" or "unknown_shape"
    
    Examples
    --------
    Create a meshed region from scratch
    
    >>> import ansys.dpf.core as dpf
    >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=1)
    >>> i=0
    >>> for node in meshed_region.nodes.add_nodes(4):
    ...     node.id = i+1
    ...     node.coordinates = [float(i), float(i), 0.0]
    ...     i=i+1
    >>> for element in meshed_region.elements.add_elements(1):
    ...     element.id=1
    ...     element.connectivity = range(0,4)
    ...     element.is_shell=True #or is_solid, is_beam, is_point
    
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
        self._shape_info={"solid":False, "shell":False, "beam":False,"point":False}
        if value == "solid":
            self.is_solid=True 
        elif value =="shell":            
            self.is_shell =True
        elif value =="beam":    
            self.is_beam=True     
        else:   
            self.is_point=True
        
class element_types(Enum):
    General = -2
    All = -1
    Tet10 = 0
    Hex20 = 1
    Wedge15 = 2
    Pyramid13 = 3
    Tri6 = 4
    TriShell6 = 5
    Quad8 = 6
    QuadShell8 = 7
    Line3 = 8
    Point1 = 9
    Tet4 = 10
    Hex8 = 11
    Wedge6 = 12
    Pyramid5 = 13
    Tri3 = 14
    TriShell3 = 15
    Quad4 = 16
    QuadShell4 = 17
    Line2 = 18
    NumElementTypes = 19
    Unknown = 20
    EMagLine = 21
    EMagArc = 22
    EMagCircle = 23
    Surface3 = 24
    Surface4 = 25
    Surface6 = 26
    Surface8 = 27
    Edge2 = 28
    Edge3 = 29
    Beam3 = 30
    Beam4 = 31
    GeneralPlaceholder = 32
    Polygon = 33
    Polyhedron=34
    
    @staticmethod
    def _shapes():
        return { element_types.Tet10 : "solid",
                element_types.Hex20 : "solid",
                element_types.Wedge15 : "solid",
                element_types.Pyramid13 : "solid",
                element_types.Tri6 : "shell",
                element_types.TriShell6 :  "shell",
                element_types.Quad8 : "shell",
                element_types.QuadShell8 : "shell",
                element_types.Line3 : "beam",
                element_types.Tet4 : "solid",
                element_types.Hex8 : "solid",
                element_types.Wedge6 : "solid",
                element_types.Pyramid5 : "solid",
                element_types.Tri3 : "shell",
                element_types.TriShell3 : "shell",
                element_types.Quad4 : "shell",
                element_types.QuadShell4 : "shell",
                element_types.Line2 : "beam",
                element_types.EMagLine : "beam",
                element_types.EMagArc: "beam",
                element_types.EMagCircle : "shell",
                element_types.Surface3 : "shell",
                element_types.Surface4 : "shell",
                element_types.Surface6 : "shell",
                element_types.Surface8 : "shell",
                element_types.Edge2 : "beam",
                element_types.Edge3 : "beam",
                element_types.Beam3 : "beam",
                element_types.Beam4 : "beam",
                element_types.Polygon : "shell",
                element_types.Polyhedron : "solid"}
    
    @staticmethod
    def shape(element_type):
        if isinstance(element_type,(int, np.int32)):
            element_type = element_types(element_type)
        return element_types._shapes().get(element_type, "unknown_shape")
        

element_types.__doc__=__write_enum_doc__(element_types,"Types of elements available in a dpf's mesh.")
