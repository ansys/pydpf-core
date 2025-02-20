# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Faces."""

import numpy as np

from ansys.dpf.core import scoping
from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core.common import face_properties
from ansys.dpf.core.elements import element_types


@version_requires("7.0")
class Face:
    """
    Contains all properties of a face of a mesh.

    The face is created from the
    :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>` class.
    Properties include the face ID, index, type, shape, and connectivity.

    Parameters
    ----------
    mesh : :class:`ansys.dpf.core.meshed_region.MeshedRegion`
        Mesh containing the face.
    faceid : int
        Number (ID) of the face.
    index : int
        Fortran-based (1-based) index of the face in the result.
    nodes : list
        List of DPF nodes belonging to the face.

    Examples
    --------
    Extract a single face from a meshed region.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.fluid_axial_model())
    >>> faces = model.metadata.meshed_region.faces
    >>> face = faces[0]

    List the coordinates belonging to the first node of the face.

    >>> face.nodes[0].coordinates
    [-0.030426240620025163, -0.05908951107677226, -0.034248966723680496]

    Notes
    -----
    Class available with server's version starting at 7.0 (2024 R1 pre0).
    """

    def __init__(self, mesh, faceid, index, nodes):
        self._id = faceid
        self._index = index
        self._nodes = nodes
        self._mesh = mesh

    @property
    def node_ids(self):
        """
        IDs of all nodes in the face.

        Returns
        -------
        list
           List of IDs for all nodes in the face.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> face = faces[0]
        >>> face.node_ids
        [11291, 11416, 11455, 11325]

        """
        return [node.id for node in self._nodes]

    @property
    def id(self) -> int:
        """
        ID of the face.

        Returns
        -------
        int
            ID of the face.

        """
        return self._id

    @property
    def index(self) -> int:
        """
        Index of the face in the result.

        Returns
        -------
        int
            Index of the face in the result. This uses zero-based indexing starting at ``0``.

        """
        return self._index

    @property
    def nodes(self):
        """
        All nodes in the face.

        Returns
        -------
        list
            List of all nodes in the face.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> face = faces[0]
        >>> first_node = face.nodes[0]

        """
        return self._nodes

    @property
    def n_nodes(self) -> int:
        """
        Number of nodes in the face.

        Returns
        -------
        int
            Number of nodes.

        """
        return len(self._nodes)

    def __str__(self):
        """Provide more information in string representation."""
        txt = "DPF Face %d\n" % self.id
        txt += "\tIndex:      %7d\n" % self.index
        txt += "\tNodes:      %7d\n" % self.n_nodes
        txt += f"\tType:       {self.type}\n"
        return txt

    @property
    def type(self) -> int:
        """
        Type of the face.

        Returns
        -------
        int
            Type of the face. For more information, see
            :class:`ansys.dpf.core.elements.element_types`.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> face = faces[0]
        >>> face.type
        <element_types.Quad4: 16>

        """
        return self._get_type()

    def _get_type(self):
        """Retrieve the Ansys element type."""
        return element_types(
            self._mesh.property_field(face_properties.faces_type).get_entity_data(self._index)[0]
        )

    @property
    def connectivity(self):
        """
        Ordered list of node indices of the face.

        Returns
        -------
        list
            Ordered list of node indices.

        """
        list = []
        for node in self._nodes:
            list.append(node.index)
        return list


@version_requires("7.0")
class Faces:
    """
    Contains faces belonging to a meshed region.

    Parameters
    ----------
    mesh : str
        Name of the meshed region.

    Examples
    --------
    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.fluid_axial_model())
    >>> faces = model.metadata.meshed_region.faces
    >>> faces.n_faces
    44242

    Notes
    -----
    Class available with server's version starting at 7.0 (2024 R1 pre0).
    """

    def __init__(self, mesh):
        self._mesh = mesh
        self._server = mesh._server
        self._mapping_id_to_index = None

    def __str__(self):
        """Provide custom string representation."""
        return "DPF Faces object with %d faces" % len(self)

    def __getitem__(self, index):
        """Retrieve face based on an index."""
        return self.face_by_index(index)

    def __len__(self):
        """Retrieve the number of faces."""
        return self.n_faces

    def __iter__(self):
        """Provide for iterating in loops."""
        for i in range(len(self)):
            yield self[i]

    def face_by_id(self, id) -> Face:
        """
        Retrieve a face by face ID.

        Parameters
        ----------
        id : int
            Number (ID) of the face.

        Returns
        -------
        Face
            Face object.

        """
        return self.__get_face(faceid=id)

    def face_by_index(self, index) -> Face:
        """
        Retrieve a face using its index.

        Parameters
        ----------
        index : int
            Zero-based index.

        Returns
        -------
        Face
            Yield face.

        Examples
        --------
        faces.face_by_index(0)

        Notes
        -----
        This is equivalent to ``faces[0]``

        """
        return self.__get_face(faceindex=index)

    def __get_face(self, faceindex=None, faceid=None):
        """
        Retrieve the face by ID or index.

        Parameters
        ----------
        faceid : int, optional
            ID of the face. The default is ``None``.
        faceindex : int, optional
            Index of the face. The default is ``None``.

        Returns
        -------
        face : Face
        """
        if faceindex is None:
            faceindex = self._mesh.property_field(face_properties.faces_type).scoping.index(faceid)
            if faceindex < 0:
                raise ValueError("face not found")
        elif faceid is None:
            faceid = self._mesh.property_field(face_properties.faces_type).scoping.id(faceindex)
            if faceid < 0:
                raise ValueError("face not found")
        nodeIdx = self._mesh.property_field(
            face_properties.faces_nodes_connectivity
        ).get_entity_data(faceindex)
        nodesOut = [self._mesh.nodes.node_by_index(node_index) for node_index in nodeIdx]
        return Face(self._mesh, faceid, faceindex, nodesOut)

    @property
    def scoping(self) -> scoping.Scoping:
        """
        Scoping of the faces.

        Returns
        -------
        :class:`ansys.dpf.core.scoping.Scoping`

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> my_scoping = faces.scoping

        """
        return self._mesh.property_field(face_properties.faces_type).scoping

    @property
    def faces_type_field(self):
        """
        Field of all faces types.

        Returns
        -------
        :class:`ansys.dpf.core.field.Field`
            Field of all faces types.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> field = faces.faces_type_field
        >>> print(field.data)
        [16 16 16 ... 16 16 16]

        """
        return self._mesh.field_of_properties(face_properties.faces_type)

    @property
    def faces_nodes_connectivity_field(self):
        """
        Field containing for each face ID the node indices connected to the face.

        Returns
        -------
        :class:`ansys.dpf.core.field.Field`
            Field containing for each face ID the node indices connected to the face.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> field = faces.faces_nodes_connectivity_field
        >>> field.get_entity_data(1)
        DPFArray([11415, 11347, 11387, 11454])

        """
        return self._mesh.property_field(face_properties.faces_nodes_connectivity)

    @property
    def n_faces(self) -> int:
        """Number of faces."""
        return self._mesh._api.meshed_region_get_num_faces(self._mesh)

    def _build_mapping_id_to_index(self):
        """Retrieve the mapping between the IDs and indices of the entity."""
        return {eid: i for i, eid in enumerate(self.scoping.ids)}

    @property
    def mapping_id_to_index(self) -> dict:
        """
        Mapping between the IDs and indices of the entity.

        This property is useful for mapping scalar results from a field to the meshed region.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> meshed_region = model.metadata.meshed_region
        >>> map = meshed_region.faces.mapping_id_to_index

        """
        if self._mapping_id_to_index is None:
            self._mapping_id_to_index = self._build_mapping_id_to_index()
        return self._mapping_id_to_index

    def map_scoping(self, external_scope):
        """
        Retrieve the indices to map the scoping of these faces to the scoping of a field.

        Parameters
        ----------
        external_scope : :class:`ansys.dpf.core.scoping.Scoping`
            Scoping to map to.

        Returns
        -------
        indices : numpy.ndarray
            List of indices to map from the external scope to the
            scoping of these faces.
        mask : numpy.ndarray
            Members of the external scope that are in the face scoping.

        Examples
        --------
        Return the indices that map a field to a faces collection.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.fluid_axial_model())
        >>> faces = model.metadata.meshed_region.faces
        >>> m = model.results.mass_flow_rate()
        >>> field = m.outputs.fields_container()[0]
        >>> ind, mask = faces.map_scoping(field.scoping)

        """
        if external_scope.location in ["Nodal", "NodalElemental", "Elemental", "ElementalNodal"]:
            raise ValueError('Input scope location must be "Faces"')
        arr = np.array(list(map(self.mapping_id_to_index.get, external_scope.ids)))
        mask = arr != None
        ind = arr[mask].astype(np.int32)
        return ind, mask
