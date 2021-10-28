"""
Nodes
=====
"""

import numpy as np


from ansys import dpf
from ansys.dpf.core import field, property_field
from ansys.grpc.dpf import meshed_region_pb2
from ansys.dpf.core.errors import protect_grpc


class Node:
    """Encapsulates all properties of a node in the mesh.

    A node is created from the :class:`ansys.dpf.core.elements` or
    :class:`ansys.dpf.core.meshed_region` class.

    Parameters
    ----------
    mesh : :class:`ansys.dpf.core.meshed_region` class
        Mesh region that the node is contained in.
    nodeid : int
        ID of the node.
    nodeindex : int
        Index of the node.
    coordinates : list
        List of ``[x, y, z]`` coordinates for the node.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> nodes = model.metadata.meshed_region.nodes

    >>> # Initialize a node from a nodes collection
    >>> node = nodes[0]

    Initialize a node from an element.

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
        """Index of the node. The index starts at 0."""
        return self._index

    @property
    def id(self) -> int:
        """ID of the node."""
        return self._id

    @property
    def coordinates(self):
        """Cartesian coordinates of the node.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> node = model.metadata.meshed_region.nodes[0]
        >>> node.coordinates
        [0.015, 0.045, 0.015]

        """
        return self._coordinates

    @property
    def nodal_connectivity(self):
        """Elements indices connected to the node.

        Returns
        -------
        nodal_connectivity : numpy.array
        """
        return self._mesh.nodes.nodal_connectivity_field.get_entity_data(self.index)

    def __str__(self):
        txt = "DPF Node     %7d\n" % self.id
        txt += "Index:      %7d\n" % self.index
        txt += f"Location: {self.coordinates}\n"
        return txt


class Nodes:
    """Provides a collection of DPF nodes.

    Parameters
    ----------
    mesh : :class:`ansys.dpf.core.meshed_region` class
       Mesh region that the collection is created from.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.static_rst)
    >>> meshed_region = model.metadata.meshed_region
    >>> nodes = model.metadata.meshed_region.nodes
    >>> nodes.n_nodes
    81

    """

    def __init__(self, mesh):
        self._mesh = mesh
        self._mapping_id_to_index = None

    def __str__(self):
        return f"DPF Node collection with {len(self)} nodes\n"

    def __getitem__(self, index):
        """Returns node based on index"""
        return self.node_by_index(index)

    def __len__(self):
        return self.n_nodes

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def node_by_id(self, id):
        """Array of node coordinates ordered by ID."""
        return self.__get_node(nodeid=id)

    def node_by_index(self, index):
        """Array of node coordinates ordered by index"""
        return self.__get_node(nodeindex=index)

    @protect_grpc
    def __get_node(self, nodeindex=None, nodeid=None):
        """Retrieves the node by its ID or index.

        Parameters
        ----------
        nodeid : int
            ID of the node. The default is ``None``.
        nodeindex : int
            Index of the node. The default is ``None``.

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
        """Scoping of the nodes.

        Returns
        -------
        scoping : Scoping
            Scoping of the nodes.

        Examples
        --------
        Get the IDs of all nodes in this collection.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = model.metadata.meshed_region.nodes
        >>> nodes.scoping.ids[2]
        3

        """
        return self._mesh._get_scoping(loc=dpf.core.locations.nodal)

    @property
    def n_nodes(self):
        """Number of nodes."""
        return self._mesh._stub.List(self._mesh._message).num_nodes

    @property
    def coordinates_field(self):
        """Coordinates field.

        Returns
        -------
        coordinates_field : Field
            Field with all the coordinates for the nodes.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = model.metadata.meshed_region.nodes
        >>> coordinates = nodes.coordinates_field

        >>> # Extract the array of coordinates the coordinates field
        >>> nodes.coordinates_field.data[2]
        array([0.015, 0.045, 0.03 ])

        """
        return self._get_coordinates_field()

    @property
    def nodal_connectivity_field(self):
        """Nodal connectivity field

        Field containing each node ID for the elements indices
        connected to the given node.

        Returns
        -------
        nodal_connectivity_field : PropertyField
            Field of the element indices associated with each node.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = model.metadata.meshed_region.nodes
        >>> field = nodes.nodal_connectivity_field
        >>> field.get_entity_data(1)
        array([0, 2, 4, 6])

        """
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        request.nodal_property = meshed_region_pb2.NODAL_CONNECTIVITY
        fieldOut = self._mesh._stub.ListProperty(request)
        return property_field.PropertyField(
            server=self._mesh._server, property_field=fieldOut
        )

    @protect_grpc
    def _get_coordinates_field(self):
        """Retrieve the coordinates field."""
        request = meshed_region_pb2.ListPropertyRequest()
        request.mesh.CopyFrom(self._mesh._message)
        # request.nodal_property = meshed_region_pb2.NodalPropertyType.COORDINATES
        request.nodal_property = meshed_region_pb2.COORDINATES
        fieldOut = self._mesh._stub.ListProperty(request)
        return field.Field(server=self._mesh._server, field=fieldOut)

    def _build_mapping_id_to_index(self):
        """Retrieve a mapping between IDs and indices of the entity."""
        return {eid: i for i, eid in enumerate(self.scoping.ids)}

    @property
    def mapping_id_to_index(self):
        if self._mapping_id_to_index is None:
            self._mapping_id_to_index = self._build_mapping_id_to_index()
        return self._mapping_id_to_index

    def map_scoping(self, external_scope):
        """Retrieve the indices to map the scoping of these elements to the scoping of a field.

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
        Retrieve the indices that map a field to a nodes collection.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> nodes = model.metadata.meshed_region.nodes
        >>> disp = model.results.displacement()
        >>> field = disp.outputs.fields_container()[0]
        >>> ind, mask = nodes.map_scoping(field.scoping)

        These indices can then be used to remap the coordinates of the nodes to
        match the order of the field data. This way, the field data matches the
        order of the nodes in the :class:`ansys.dpf.core.meshed_region` class.

        >>> mapped_nodes = nodes.coordinates_field.data[ind]

        """
        if external_scope.location in ["Elemental", "NodalElemental"]:
            raise ValueError('Input scope location must be "Nodal"')
        arr = np.array(list(map(self.mapping_id_to_index.get, external_scope.ids)))
        mask = arr != None
        ind = arr[mask].astype(np.int)
        return ind, mask

    def add_node(self, id, coordinates):
        """Add a node in the mesh.

        Parameters
        ----------
        id : int
            ID for the new node.

        coordinates : list[float]
            List of ``[x, y, z]`` coordinates for the node.
        """
        request = meshed_region_pb2.AddRequest(mesh=self._mesh._message)
        node_request = meshed_region_pb2.NodeRequest(id=id)
        node_request.coordinates.extend(coordinates)
        request.nodes.append(node_request)
        self._mesh._stub.Add(request)

    def add_nodes(self, num):
        """Add a number of nodes in the mesh.

        This method yields a number of nodes that you can define.

        Parameters
        ----------
        num : int
            Number of nodes to add.

        Yields
        ------
        yield node : NodeAdder
            Node to add

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
            add = NodeAdder()
            yield add
            node_request = meshed_region_pb2.NodeRequest(id=add.id)
            node_request.coordinates.extend(add.coordinates)
            request.nodes.append(node_request)
        self._mesh._stub.Add(request)


class NodeAdder:
    """Adds a new node to a meshed region.

    Attributes
    ----------
    id : int

    coordinates : list of doubles
        List of ``[x, y, z]'' coordinates.

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

    """

    def __init__(self):
        self._id = 0
        self._coordinates = [0.0, 0.0, 0.0]

    @property
    def id(self):
        """ID of the node."""
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def coordinates(self):
        """Coordinates of the node."""
        return self._coordinates

    @coordinates.setter
    def coordinates(self, xyz):
        if isinstance(xyz, (np.ndarray, np.generic)):
            self._coordinates = xyz.flatten().tolist()
        else:
            self._coordinates = xyz
