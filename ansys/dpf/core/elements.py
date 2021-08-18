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
from ansys.dpf.core.common import locations
from ansys.dpf.core import nodes
from ansys.dpf.core.common import __write_enum_doc__
from ansys.dpf.core.element_descriptor import ElementDescriptor

class Element:
    """Contains all properties of an element of a mesh. 
    
    The element is created from the :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` class. 
    Properties include the element ID, index, type, shape, and connectivity.

    Parameters
    ----------
    mesh : :class:`ansys.dpf.core.meshed_region.MeshedRegion`
        Mesh containing the element.
    elementid : int
        Number (ID) of the element.
    index : int
        Fortran-based index of the element in the result.
    nodes : list
        List of DPF nodes belonging to the element.

    Examples
    --------
    Extract a single element from a meshed region.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> elements = model.metadata.meshed_region.elements
    >>> element = elements[0]
    
    List the coordinates belonging to the first node of the element.

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
        """IDs of all nodes in the element.

        Returns
        --------
        list
           List of IDs for all nodes in the element.

        Examples
        --------
        >>> element.node_ids
        [1, 26, 14, 12, 2, 27, 15, 13, 33, 64, 59, 30, 37, 65, 61, 34, 28, 81, 63, 58]
        
        """
        return [node.id for node in self._nodes]

    @property
    def id(self) -> int:
        """ID of the element.
        
        Returns
        -------
        int
            ID of the element.
            
        """
        return self._id

    @property
    def index(self) -> int:
        """Index of the element in the result.
        
        Returns
        -------
        int
         Index of the element in the result. The index start at ``0``.
         
        """
        return self._index

    @property
    def nodes(self):
        """All nodes in the element.
            
        Returns
        --------
        list
            List of all nodes in the element.

        Examples
        --------
        >>> first_node = element.nodes[0]
        
        """
        return self._nodes

    @property
    def n_nodes(self) -> int:
        """Number of nodes in the element.
        
        Returns
        -------
        int
            Number of nodes.
            
        """
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
        """Type of the element.
        
        Returns
        -------
        int
            Type of the element. For more information, see :class:`ansys.dpf.core.elements.element_types`.

        Examples
        --------
        >>> element.type
        <element_types.Hex20: 1>
        
        """
        return self._get_type()

    @protect_grpc
    def _get_type(self):
        """Retrieve the Ansys element type."""
        
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        request.property = meshed_region_pb2.ELEMENT_TYPE
        return element_types(self._mesh._stub.GetElementalProperty(request).prop)

    @property
    def shape(self) -> str:
        """Shape of the element.
       
        Returns
        -------
        str
           Shape of the element, which can be ``"shell"``, ``"solid"``, ``"beam"``, 
           or ``"unknown_shape"``.

        Examples
        --------
        >>> element.shape
        'solid'
        
        """
        return self._get_shape()

    @protect_grpc
    def _get_shape(self):
        """Retrieve the element shape."""
        request = meshed_region_pb2.ElementalPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.index = self.index
        request.property = meshed_region_pb2.ELEMENT_SHAPE
        prop = self._mesh._stub.GetElementalProperty(request).prop
        return meshed_region_pb2.ElementShape.Name(prop).lower()
    
    @property
    def connectivity(self):
        """Ordered list of node indices of the element.
        
        Returns
        --------
        list
           Ordered list of node indices. 
           
        """
        list=[]
        for node in self._nodes:
            list.append(node.index)
        return list     

class Elements():
    """Contains elements belonging to a meshed region.
    
    Parameters
    ----------
    mesh : str
        Name of the meshed region.

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
        """Retrieves element based on an index."""
        return self.element_by_index(index)

    def __len__(self):
        return self.n_elements

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def element_by_id(self, id) -> Element:
        """Retrieve an element by element ID.

        Parameters
        ----------
        id : int
            Number (ID) of the element.

        Returns
        -------
        Element
            Element object.

        """
        return self.__get_element(elementid=id)

    def element_by_index(self, index) -> Element:
        """Retrieve an element using its index.

        Parameters
        ----------
        index : int
            Zero-based index.

        Returns
        -------
        Element
            Element object.

        Examples
        --------
        elements.element_by_index(0)

        Notes
        -----
        This is equivalent to ``elements[0]``

        """
        return self.__get_element(elementindex=index)  
        
    def add_elements(self, num):     
        """Add one ore more elements in the mesh. 
                
        Parameters
        ----------
        num : int
            Number of elements to add in the mesh.
        
        Returns
        -------
        :class:`ansys.dpf.core.elements.ElementAdder`
            Elements added to the mesh.
        
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
        """Add a solid 3D element in the mesh.
        
        Parameters
        ----------
        id : int
            ID to assign the new element.
        connectivity : list
            List of the node indices to connect to the new element.
                
        """
        self.add_element(id,"solid",connectivity)

    def add_shell_element(self, id, connectivity):
        """Add a shell 2D element in the mesh.
        
        Parameters
        ----------
        id : int
            ID to assign the new element.
        connectivity : list
            List of the node indices to connect to the new element.
        """
        self.add_element(id, "shell",connectivity)   
        
    def add_beam_element(self, id, connectivity):
        """Add a beam 1D element in the mesh.
        
        Parameters
        ----------
        id : int
            ID to assign the new element.
        connectivity : list
            List of the node indices to connect to the new element.
        
        """
        self.add_element(id, "beam",connectivity)   
        
    def add_point_element(self, id, connectivity):
        """Add a point element (one node connectivity) in the mesh.
        
        Parameters
        ----------
        id : int
            ID to assign the new element.
        connectivity : list
            List of the node indices to connect to the new element.
            
        """
        if not isinstance(connectivity, list):
            connectivity = [connectivity]
        self.add_element(id, "unknown_shape",connectivity)
    
    def add_element(self, id, shape, connectivity):
        """Add an element in the mesh.
        
        Parameters
        ----------
        id : int
            ID to assign the new element.
        shape : str
            Shape of the element. Options are ``"solid"``, ``"shell"``, ``"beam"`` 
            and ``"unknown_shape"``.
        connectivity : list
            List of the node indices to connect to the new element.
                
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        element_request = meshed_region_pb2.ElementRequest(id=id)
        element_request.connectivity.extend(connectivity)
        element_request.shape = meshed_region_pb2.ElementShape.Value(shape.upper())
        request.elements.extend([element_request])
        self._mesh._stub.Add(request)
    
    @protect_grpc
    def __get_element(self, elementindex=None, elementid=None):
        """Retrieve the element by ID or index.

        Parameters
        ----------
        elementid : int, optional
            ID of the element. The default is ``None``.
        elementindex : int, optional
            Index of the element. The default is ``None``.

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
        """Scoping of the elements.

        Returns
        -------
        :class:`ansys.dpf.core.scoping.Scoping`
        
        Examples
        --------
        >>> my_scoping = elements.scoping
        
        """
        return self._mesh._get_scoping(loc=locations.elemental)

    @property
    def element_types_field(self):
        """Field of all element types.

        Returns
        -------
        :class:`ansys.dpf.core.field.Field`
            Field of all element types.

        Examples
        --------
        >>> field = elements.element_types_field
        >>> field.data
        array([1, 1, 1, 1, 1, 1, 1, 1])
        
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.ELEMENT_TYPE
        request.elemental_property = meshed_region_pb2.ELEMENT_TYPE
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(server=self._mesh._server, field=fieldOut)

    @property
    @protect_grpc
    def materials_field(self):
        """Field of all material IDs.

        Returns
        -------
        :class:`ansys.dpf.core.field.Field`
            Field of all materials IDs.

        Examples
        --------
        Extract the material IDs from the materials_field

        >>> elements.materials_field.data
        array([1, 1, 1, 1, 1, 1, 1, 1])
        
        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.MATERIAL
        request.elemental_property = meshed_region_pb2.MATERIAL
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(server=self._mesh._server, field=fieldOut)

    @property
    def connectivities_field(self):
        """Field containing for each element ID the node indices connected to the element.

        Returns
        -------
        :class:`ansys.dpf.core.field.Field`
            Field containing for each element ID the node indices connected to the element.

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
        """Retrieve the connectivities field."""
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.elemental_property = meshed_region_pb2.ElementalPropertyType.CONNECTIVITY
        request.elemental_property = meshed_region_pb2.CONNECTIVITY
        fieldOut = self._mesh._stub.ListProperty(request)
        return property_field.PropertyField(server=self._mesh._server, property_field=fieldOut)

    @property
    def n_elements(self) -> int:
        """Number of elements"""
        return self._mesh._stub.List(self._mesh._message).num_element

    def _build_mapping_id_to_index(self):
        """Retrieve the mapping between the IDs and indices of the entity."""
        return {eid: i for i, eid in enumerate(self.scoping.ids)}

    @property
    def mapping_id_to_index(self) -> dict:
        """Mapping between the IDs and indices of the entity.

        This proprty is useful for mapping scalar results from a field to the meshed region.

        Examples
        --------
        >>> meshed_region.nodes.mapping_id_to_index
        {1: 0, 2: 1, 3: 2, 4: 3}

        """
        if self._mapping_id_to_index is None:
            self._mapping_id_to_index = self._build_mapping_id_to_index()
        return self._mapping_id_to_index

    def map_scoping(self, external_scope):
        """Retrieve the indices to map the scoping of these elements to
        the scoping of a field.

        Parameters
        ----------
        external_scope : :class:`ansys.dpf.core.scoping.Scoping`
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
        """Whether at least one element is a 2D element (shell).
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
        
        """
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_shell_elements
   
    @property
    def has_solid_elements(self) -> bool:
        """Whether at list one element is a 3D element (solid).
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
        
        """
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_solid_elements
    
    @property
    def has_beam_elements(self) -> bool:
        """Whether at least one element is a 1D beam element.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
        
        """
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_beam_elements
    
    @property
    def has_point_elements(self) -> bool:
        """Whether at least one element is a point element.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
             
        """
        return self._mesh._stub.List(self._mesh._message).element_shape_info.has_point_elements
    

class ElementAdder:
    """Provides for adding new elements in a meshed region.
    
    Parameters
    ----------
    id : int
        ID to assign to the new element.
    shape : str
        Shape of the element. Options are ``"solid"``, ``"shell"``, ``"beam"`` 
        and ``"unknown_shape"``.
    connectivity : list
        List of the node indices to connect to the new element.         
    
    Examples
    --------
    Create a meshed region from scratch.
    
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
        """Whether the element is a solid.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
        """
        
        return self._shape_info["solid"]
    
    @is_solid.setter
    def is_solid(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["solid"]=True
    
    @property
    def is_shell(self) ->bool :
        """Whether the element is a shell.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed. 
        """
        
        return self._shape_info["shell"]
    
    @is_shell.setter
    def is_shell(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["shell"]=True
    
    @property
    def is_beam(self) ->bool :
        """Whether the element is a beam.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.  
        """
      
        return self._shape_info["beam"]
    
    @is_beam.setter
    def is_beam(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["beam"]=True
    
    @property
    def is_point(self) ->bool :
        """Whether the element is a point.
        
        Returns
        -------
        bool
             ``True`` when successful, ``False`` when failed.
        """
     
        return self._shape_info["point"]
    
    @is_point.setter
    def is_point(self, value):
        for key in self._shape_info:
            self._shape_info[key]=False
        self._shape_info["point"]=True
     
    @property
    def shape(self) ->str:
        """Shape of the element.
        
        Returns
        --------
        str
           Shape of the element. Options are ``"solid"``, ``"shell"``, ``"beam"`` 
           and ``"unknown_shape"``.
           
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
        """Set the shape of the element.
        
        Parameters
        --------
        value : str
           Shape of the element. Options are ``"solid"``, ``"shell"``, ``"beam"`` 
           and ``"unknown_shape"``.
           
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
    """Contains the types of elements.
    """
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
    Polyhedron = 34
    
    @staticmethod
    def _descriptors():
        return {
                element_types.General : ElementDescriptor(element_types.General, "General", "general"),
                element_types.All : ElementDescriptor(element_types.All, "Unknown", "unknown"),
                element_types.Tet10 : ElementDescriptor(element_types.Tet10, "Quadratic 10-nodes Tetrahedron", "tet10", "solid", 4, 6, 10, True, False, False, True),
                element_types.Hex20 : ElementDescriptor(element_types.Hex20, "Quadratic 20-nodes Hexa", "hex20", "solid", 8, 12, 20, True, False, False, True),
                element_types.Wedge15 : ElementDescriptor(element_types.Wedge15, "Quadratic 15-nodes Wedge", "wedge15", "solid", 6, 9, 15, True, False, False, True),
                element_types.Pyramid13 : ElementDescriptor(element_types.Pyramid13, "Quadratic 13-nodes Pyramid", "pyramid13", "solid", 5, 8, 13, True, False, False, True),
                element_types.Tri6 : ElementDescriptor(element_types.Tri6, "Quadratic 6-nodes Triangle", "tri6", "shell", 3, 3, 6, False, True, False, True),
                element_types.TriShell6 : ElementDescriptor(element_types.TriShell6, "Quadratic 6-nodes Triangle Shell", "triShell6", "shell", 3, 3, 6, False, True, False, True),
                element_types.Quad8 : ElementDescriptor(element_types.Quad8, "Quadratic 8-nodes Quadrangle", "quad8", "shell", 4, 4, 8, False, True, False, True),
                element_types.QuadShell8 : ElementDescriptor(element_types.QuadShell8, "Quadratic 8-nodes Quadrangle Shell", "quadShell8", "shell", 4, 4, 8, False, True, False, True),
                element_types.Line3 : ElementDescriptor(element_types.Line3, "Quadratic 3-nodes Line", "line3", "beam", 2, 1, 3, False, False, True, True),
                element_types.Point1 : ElementDescriptor(element_types.Point1, "Point", "point1", "point", 1, 0, 1, False, False, False, False),
                element_types.Tet4 : ElementDescriptor(element_types.Tet4, "Linear 4-nodes Tetrahedron", "tet4", "solid", 4, 0, 4, True, False, False, False),
                element_types.Hex8 : ElementDescriptor(element_types.Hex8, "Linear 8-nodes Hexa", "hex8", "solid", 8, 0, 8, True, False, False, False),
                element_types.Wedge6 : ElementDescriptor(element_types.Wedge6, "Linear 6-nodes Wedge", "wedge6", "solid", 6, 0, 6, True, False, False, False),
                element_types.Pyramid5 : ElementDescriptor(element_types.Pyramid5, "Linear 5-nodes Pyramid", "pyramid5", "solid", 5, 0, 5, True, False, False, False),
                element_types.Tri3 : ElementDescriptor(element_types.Tri3, "Linear 3-nodes Triangle", "tri3", "shell", 3, 0, 3, False, True, False, False),
                element_types.TriShell3 : ElementDescriptor(element_types.TriShell3, "Linear 3-nodes Triangle Shell", "triShell3", "shell", 3, 0, 3, False, True, False, False),
                element_types.Quad4 : ElementDescriptor(element_types.Quad4, "Linear 4-nodes Quadrangle", "quad4", "shell", 4, 0, 4, False, True, False, False),
                element_types.QuadShell4 : ElementDescriptor(element_types.QuadShell4, "Linear 4-nodes Quadrangle Shell", "quadShell4", "shell", 4, 0, 4, False, True, False, False),
                element_types.Line2 : ElementDescriptor(element_types.Line2, "Linear 2-nodes Line", "line2", "beam", 2, 0, 2, False, False, True, False),
                element_types.NumElementTypes : ElementDescriptor(element_types.NumElementTypes, "NumElementTypes", "numElementTypes"),
                element_types.Unknown : ElementDescriptor(element_types.Unknown, "Unknown", "unknown"),
                element_types.EMagLine : ElementDescriptor(element_types.EMagLine, "EMagLine", "EMagLine", "beam"),
                element_types.EMagArc : ElementDescriptor(element_types.EMagArc, "EMagArc", "EMagArc", "beam"),
                element_types.EMagCircle : ElementDescriptor(element_types.EMagCircle, "EMagCircle", "EMagCircle", "shell"),
                element_types.Surface3 : ElementDescriptor(element_types.Surface3, "Surface3", "surface3", "shell"),
                element_types.Surface4 : ElementDescriptor(element_types.Surface4, "Surface4", "surface4", "shell"),
                element_types.Surface6 : ElementDescriptor(element_types.Surface6, "Surface6", "surface6", "shell"),
                element_types.Surface8 : ElementDescriptor(element_types.Surface8, "Surface8", "surface8", "shell"),
                element_types.Edge2 : ElementDescriptor(element_types.Edge2, "Edge2", "edge2", "beam"),
                element_types.Edge3 : ElementDescriptor(element_types.Edge3, "Edge3", "edge3", "beam"),
                element_types.Beam3 : ElementDescriptor(element_types.Beam3, "Beam3", "beam3", "beam"),
                element_types.Beam4 : ElementDescriptor(element_types.Beam4, "Beam4", "beam4", "beam"),
                element_types.GeneralPlaceholder : ElementDescriptor(element_types.GeneralPlaceholder, "GeneralPlaceholder", "generalPlaceholder"),
                element_types.Polygon : ElementDescriptor(element_types.Polygon, "Polygon", "polygon", "shell", -1, 0, -1, False, True, False),
                element_types.Polyhedron : ElementDescriptor(element_types.Polyhedron, "Polyhedron", "polyhedron", "solid", -1, 0, -1, True, False, False)
            }
    
    @staticmethod
    def shape(element_type):
        """Retrieve the shape of the element.
        
        Returns
        -------
        type
        
        """
        if isinstance(element_type,(int, np.int32)):
            element_type = element_types(element_type)
        el_shape = element_types._descriptors().get(element_type, None).shape
        return el_shape
    
    @staticmethod
    def descriptor(element_type):
        """Retrieve element information.
        
        This method provides access to an instance of the ``ElementDescriptor`` of the requested 
        element to retrieve such information as the number of nodes and shape. 

        Parameters
        ----------
        element_type : int
            Type of the elemment. 

        Returns
        -------
        element_descriptor: ElementDescriptor
            Element descriptor instance that provides element information.
        
        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> elements = model.metadata.meshed_region.elements
        >>> element = elements[0]
        >>> type_of_element = element.type
        >>> type_of_element
        <element_types.Hex20: 1>
        >>> element_descriptor = dpf.element_types.descriptor(type_of_element)
        >>> element_descriptor.name
        'hex20'
        >>> element_descriptor.description
        'Quadratic 20-nodes Hexa'
        
        """
        if isinstance(element_type,(int, np.int32)):
            element_type = element_types(element_type)
        descriptor = element_types._descriptors().get(element_type, None)
        return descriptor
        

element_types.__doc__=__write_enum_doc__(element_types,"Types of elements available in a dpf's mesh.")
