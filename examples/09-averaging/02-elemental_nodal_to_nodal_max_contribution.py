"""
.. _averaging_elem_nod_with_max_contribution:

Elemental nodal to nodal computing maximum stress value at the nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows you how to get the maximum stress values at the nodes
instead of the averaged values, for a conversion from elemental nodal
location to nodal location.

It defines methods to create a surface mesh, a volume mesh, and
an elemental nodal field with one component.

"""

###############################################################################
# Elemental nodal to nodal computing maximum stress value at the nodes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# Define computation methods
# --------------------------
# Import modules:
import numpy as np
from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops


###############################################################################
# Define methods to create MeshedRegion:
def create_surface_mesh(length, width, num_nodes_in_length, num_nodes_in_width):
    """Creates surface MeshedRegion from geometry information.

    Parameters
    ----------
    length: float
        Total length of the surface to compute.
    width: float
        Total width of the surface to compute.
    num_nodes_in_length: int
    num_nodes_in_width: int

    Returns
    -------
    mesh: MeshedRegion
        Computed surface mesh.

    """
    mesh = dpf.MeshedRegion()
    n_id = 1
    for i, x in enumerate(
            [float(i) * length / float(num_nodes_in_length) for i in range(0, num_nodes_in_length)]
    ):
        for j, y in enumerate(
                [float(i) * width / float(num_nodes_in_width) for i in range(0, num_nodes_in_width)]
        ):
            mesh.nodes.add_node(n_id, [x, y, 0.0])
            n_id += 1

    coordinates = mesh.nodes.coordinates_field
    mesh.unit = "mm"
    coordinates_data = coordinates.data
    flat_coordinates_data = coordinates_data.reshape(coordinates_data.size)

    e_id = 1
    for i, x in enumerate(
            [float(i) * length / float(num_nodes_in_length) for i in range(num_nodes_in_length - 1)]
    ):
        for j, y in enumerate(
                [float(i) * width / float(num_nodes_in_width) for i in range(num_nodes_in_width - 1)]
        ):
            connectivity = []
            for xx in [x, x + length / float(num_nodes_in_length)]:
                for yy in [y, y + width / float(num_nodes_in_width)]:
                    data_index = search_sequence_numpy(flat_coordinates_data, [xx, yy, 0.0])
                    scoping_index = int(data_index / 3)  # 3components
                    connectivity.append(scoping_index)
            # rearrange connectivity
            # a = 2
            # b = 1
            # tmp = connectivity[a]
            # connectivity[a] = connectivity[b]
            # connectivity[b] = tmp
            mesh.elements.add_solid_element(e_id, connectivity)
            e_id += 1

    return mesh


def create_volume_mesh(length, width, depth, num_nodes_in_length, num_nodes_in_width, num_nodes_in_depth):
    """Creates surface MeshedRegion from geometry information.

    Parameters
    ----------
    length: float
        Total length of the surface to compute.
    width: float
        Total width of the surface to compute.
    depth: float
        Total depth of the surface to compute.
    num_nodes_in_length: int
    num_nodes_in_width: int
    num_nodes_in_depth: int

    Returns
    -------
    mesh: MeshedRegion
        Computed volume mesh.

    """
    mesh = dpf.MeshedRegion()
    n_id = 1
    for i, x in enumerate(
            [float(i) * length / float(num_nodes_in_length) for i in range(0, num_nodes_in_length)]
    ):
        for j, y in enumerate(
                [float(i) * width / float(num_nodes_in_width) for i in range(0, num_nodes_in_width)]
        ):
            for k, z in enumerate(
                    [float(i) * depth / float(num_nodes_in_depth) for i in range(0, num_nodes_in_depth)]
            ):
                mesh.nodes.add_node(n_id, [x, y, z])
                n_id += 1

    coordinates = mesh.nodes.coordinates_field
    mesh.unit = "mm"
    coordinates_data = coordinates.data
    flat_coordinates_data = coordinates_data.reshape(coordinates_data.size)

    e_id = 1
    for i, x in enumerate(
            [float(i) * length / float(num_nodes_in_length) for i in range(num_nodes_in_length - 1)]
    ):
        for j, y in enumerate(
                [float(i) * width / float(num_nodes_in_width) for i in range(num_nodes_in_width - 1)]
        ):
            for k, z in enumerate(
                    [float(i) * depth / float(num_nodes_in_depth) for i in range(num_nodes_in_depth - 1)]
            ):
                connectivity = []
                for xx in [x, x + length / float(num_nodes_in_length)]:
                    for yy in [y, y + width / float(num_nodes_in_width)]:
                        for zz in [z, z + depth / float(num_nodes_in_depth)]:
                            data_index = search_sequence_numpy(flat_coordinates_data, [xx, yy, zz])
                            scoping_index = int(data_index / 3)  # 3components
                            connectivity.append(scoping_index)
                # rearrange connectivity
                tmp = connectivity[2]
                connectivity[2] = connectivity[3]
                connectivity[3] = tmp
                tmp = connectivity[6]
                connectivity[6] = connectivity[7]
                connectivity[7] = tmp
                mesh.elements.add_solid_element(e_id, connectivity)
                e_id += 1

    return mesh


###############################################################################
# Define methods to create an ElementalNodal field:
def create_elemental_nodal_field(meshed_region, number_of_components=6):
    """Computes elemental nodal field from a MeshedRegion.
    Takes all the elements of the MeshedRegion, and associate a value
    for each node of this element corresponding to 20 * element_indice
    value.

    Parameters
    ----------
    meshed_region: MeshedRegion
    number_of_components: int
        Number of components the output field contains.
        Default is 6 (e.g. stress field).

    Returns
    -------
    elemental_nodal_field: Field

    """
    if number_of_components == 1:
        nat = dpf.natures.scalar
    elif number_of_components == 3:
        nat = dpf.natures.vector
    elif number_of_components == 6:
        nat = dpf.natures.symmatrix
    else:
        raise Exception(f"{number_of_components} number of components not supported")
    elem_nod_field = dpf.Field(
        nature=nat,
        location=dpf.locations.elemental_nodal
    )
    field_def = elem_nod_field.field_definition
    field_def.name = "stress"
    elems_scop = meshed_region.elements.scoping
    connectivity_field = meshed_region.elements.connectivities_field
    for el_id in elems_scop.ids:
        ele_ind = elems_scop.index(el_id)
        el_connectivity = connectivity_field.get_entity_data(ele_ind)
        field_val = []
        for nod_ind in el_connectivity:
            i = 0
            while i < number_of_components:
                field_val.append(20.0 * ele_ind)
                i += 1
        if len(field_val) > 0:
            elem_nod_field.append(field_val, el_id)

    return elem_nod_field


###############################################################################
# Define averaging method:
def averaging_using_max_value(elemental_nodal_field, b_compute_max=True):
    """Computes an averaging based on the highest value for a specific node.
    For elemental nodal field, each node has several contributions (one per element).
    The averaged field is nodal and for each node, the taken value is the maximum of
    the contributions.
    For example, node 1 is connected to elements 1,2,3 and 4. The maximum nodal
    stress value at node 1 among all the element's contributions (maximum of
    stress at node 1 among elements 1,2,3 and 4) is the contribution of element
    3. So the elemental nodal value for element 3, node 1 is taken and placed in
    the nodal averaged field. If b_compute_max is set to False, then minimum value
    is taken.

    This algorithm is made for solid or surface elements (shell are not supported).
    Results are mid side nodes are not taken into account.
    Only elemental nodal fields with one component (e.g. von mises
    stress, sxx) are handled.

    Parameters
    ----------
    elemental_nodal_field: Field
        Elemental nodal field the averaging must be applied on.
    b_compute_max: bool
        Default is True. If set to True, considers the maximum value
        for averaging. If set to False, considers the minimum value
        for averaging.

    Returns
    -------
    averaged_field: Field

    """
    # initial checks
    ncomp = elemental_nodal_field.component_count
    if ncomp != 1:
        raise Exception("input field must only have one component")
    # set output
    output_field = dpf.Field(nature=dpf.natures.scalar, location=dpf.locations.nodal)
    field_def = output_field.field_definition
    field_def.name = elemental_nodal_field.field_definition.name
    elem_property_field = dpf.PropertyField(nature=dpf.natures.scalar, location=dpf.locations.nodal)
    # start compute
    elems_scoping_in = elemental_nodal_field.scoping.ids
    elems_scoping_base = mesh.elements.scoping
    nodes_scoping = mesh.nodes.scoping.ids
    elems_connectivity = mesh.elements.connectivities_field # list of nodes per elements
    nodes_connectivity = mesh.nodes.nodal_connectivity_field # list of elements per nodes
    for el_id in elems_scoping_in:
        mesh_el_ind = elems_scoping_base.index(el_id)
        el_connectivity = elems_connectivity.get_entity_data(mesh_el_ind)
        for nod_ind in el_connectivity:
            # get nod id for res scoping
            nod_id = nodes_scoping[nod_ind]
            is_already_defined = output_field.scoping.index(nod_id)
            if is_already_defined != -1:
                continue
            # get reverse connectivity for this node
            connected_elems_ind = nodes_connectivity.get_entity_data(nod_ind)
            # loop over connected elements
            connected_elems_data = []
            connected_elems_nodes_connectivities = []
            size_tot_connect = 0
            connected_elems_ids = []
            for conn_elem_ind in connected_elems_ind:
                # get data by index for each element
                elem_data = elemental_nodal_field.get_entity_data(conn_elem_ind)
                if len(elem_data) != 0:
                    for val in elem_data:
                        connected_elems_data.append(val)
                    # get elem id
                    connected_elems_ids.append(elems_scoping_base[conn_elem_ind])
                    # get list of nodes for each element
                    elem_conn = elems_connectivity.get_entity_data(conn_elem_ind)
                    connected_elems_nodes_connectivities.append(elem_conn)
                    size_tot_connect += len(elem_conn)
            # check the maximum value
            # -----------------------
            # - create mask with wanted node ind
            mask = np.full((size_tot_connect), True, dtype=bool)
            offset = 0
            for i_ind, i_val in enumerate(connected_elems_nodes_connectivities):
                for j_ind, j_val in enumerate(i_val):
                    if j_val == nod_ind:
                        mask[offset] = True
                    else:
                        mask[offset] = False
                    offset += 1
            vals = np.array(connected_elems_data, dtype=float)
            vals_for_nod_ind = vals[mask]
            # - apply max on data
            if b_compute_max:
                compute_val = np.max(vals_for_nod_ind)
            else:
                compute_val = np.min(vals_for_nod_ind)
            # - get max ind (= elem ind in connected_elems_ids)
            max_ind = np.where(vals_for_nod_ind == compute_val)[0][0]
            # - get element id from connected_elems_ids using max ind
            max_elem_id = connected_elems_ids[max_ind]
            # - in res field, append(data_val, nod_id)
            output_field.append(compute_val, nod_id)
            # - in elem_prop_field, append(elem_id, nod_id)
            elem_property_field.append(max_elem_id, nod_id)

    return output_field

###############################################################################
# Define utilities:
def search_sequence_numpy(arr, seq):
    """Find a sequence in an array and return its index."""
    indexes = np.where(np.isclose(arr, seq[0]))
    for index in np.nditer(indexes[0]):
        if index % 3 == 0:
            if np.allclose(arr[index + 1], seq[1]) and np.allclose(arr[index + 2], seq[2]):
                return index
    return -1



###############################################################################
# Create surface mesh and compute maximum value averaging
# -------------------------------------------------------
# Define the geometry:
import time
text_time = "Time report \n"
text_time += "==============="

l = 1
n_l = 20

cust_length = l
cust_width = l
cust_num_nodes_in_length = n_l
cust_num_nodes_in_width = n_l
text_time += "\n------------- \n"
text_time += "Create surf mesh duration \n"
text_time += "------------- \n"
prev_time = time.time()
mesh = create_surface_mesh(
    cust_length,
    cust_width,
    cust_num_nodes_in_length,
    cust_num_nodes_in_width
)
text_time += str(time.time() - prev_time) + " s \n"
text_time += "\n------------- \n"
text_time += "Surf mesh statistics \n"
text_time += "------------- \n"
text_time += str(mesh)

# Create the mesh and compute the specific averaging:
text_time += "\n------------- \n"
text_time += "Create elem nodal field duration \n"
text_time += "------------- \n"
prev_time = time.time()
stress_field_surf = create_elemental_nodal_field(mesh, 1)
text_time += str(time.time() - prev_time) + " s \n"

text_time += "\n------------- \n"
text_time += "Average \n"
text_time += "------------- \n"
prev_time = time.time()
output_field_surf = averaging_using_max_value(stress_field_surf, True)
text_time += str(time.time() - prev_time) + " s \n"
mesh.plot(output_field_surf)

# Compare with averaged values:
# fc_surf = dpf.fields_container_factory.over_time_freq_fields_container({0.1: stress_field_surf}, "s")
# field_averaged_surf = ops.averaging.to_nodal_fc(
#     fields_container=fc_surf, mesh=mesh
# ).outputs.fields_container()
# mesh.plot(field_averaged_surf[0])

# Create volume mesh and compute maximum value averaging
# -------------------------------------------------------
# Define the geometry:
cust_depth = l
cust_num_nodes_in_depth = n_l
text_time += "\n------------- \n"
text_time += "Create vol mesh duration \n"
text_time += "------------- \n"
prev_time = time.time()
mesh = create_volume_mesh(
    cust_length,
    cust_width, cust_depth,
    cust_num_nodes_in_length,
    cust_num_nodes_in_width,
    cust_num_nodes_in_depth
)
text_time += str(time.time() - prev_time) + " s \n"
text_time += "\n------------- \n"
text_time += "Vol mesh statistics \n"
text_time += "------------- \n"
text_time += str(mesh)

# Create the mesh and compute the specific averaging:
# Create the mesh and compute the specific averaging:
text_time += "\n------------- \n"
text_time += "Create elem nodal field duration \n"
text_time += "------------- \n"
prev_time = time.time()
stress_field_vol = create_elemental_nodal_field(mesh, 1)
text_time += str(time.time() - prev_time) + " s \n"

text_time += "\n------------- \n"
text_time += "Average \n"
text_time += "------------- \n"
prev_time = time.time()
output_field_vol = averaging_using_max_value(stress_field_vol, True)
text_time += str(time.time() - prev_time) + " s \n"
mesh.plot(output_field_vol)

# Compare with averaged values:
# fc_vol = dpf.fields_container_factory.over_time_freq_fields_container({0.1: stress_field_vol}, "s")
# field_averaged_vol = ops.averaging.to_nodal_fc(
#     fields_container=fc_vol, mesh=mesh
# ).outputs.fields_container()
# mesh.plot(field_averaged_vol[0])

print(text_time)