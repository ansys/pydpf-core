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
    n_nodes = num_nodes_in_length * num_nodes_in_width
    n_elems = (num_nodes_in_length - 1) * (num_nodes_in_width - 1)
    mesh = dpf.MeshedRegion(num_nodes=n_nodes, num_elements=n_elems)
    mesh.unit = "mm"
    n_id = 1
    for i, x in enumerate(
        [float(i) * length / float(num_nodes_in_length) for i in range(0, num_nodes_in_length)]
    ):
        for j, y in enumerate(
            [float(i) * width / float(num_nodes_in_width) for i in range(0, num_nodes_in_width)]
        ):
            mesh.nodes.add_node(n_id, [x, y, 0.0])
            n_id += 1

    e_id = 1
    for i in range(0, num_nodes_in_length - 1):
        for j in range(0, num_nodes_in_width - 1):
            e_ind = e_id - 1
            a = e_ind + i
            b = e_ind + i + 1
            c = j + num_nodes_in_length * (i + 1)
            d = j + num_nodes_in_length * (i + 1) + 1
            connectivity = [a, b, d, c]
            mesh.elements.add_shell_element(e_id, connectivity)
            e_id += 1

    return mesh


def create_volume_mesh(
    length, width, depth, num_nodes_in_length, num_nodes_in_width, num_nodes_in_depth
):
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
    n_nodes = num_nodes_in_length * num_nodes_in_width * num_nodes_in_depth
    n_elems = (num_nodes_in_length - 1) * (num_nodes_in_width - 1) * (num_nodes_in_depth - 1)
    mesh = dpf.MeshedRegion(num_nodes=n_nodes, num_elements=n_elems)
    mesh.unit = "mm"
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

    e_id = 1
    for k in range(0, num_nodes_in_depth - 1):
        for j in range(0, num_nodes_in_width - 1):
            for i in range(0, num_nodes_in_length - 1):
                a = k * num_nodes_in_length * num_nodes_in_width + j * num_nodes_in_length + i
                b = k * num_nodes_in_length * num_nodes_in_width + j * num_nodes_in_length + i + 1
                c = k * num_nodes_in_length * num_nodes_in_width + (j + 1) * num_nodes_in_length + i
                d = (
                    k * num_nodes_in_length * num_nodes_in_width
                    + (j + 1) * num_nodes_in_length
                    + i
                    + 1
                )
                e = (k + 1) * num_nodes_in_length * num_nodes_in_width + j * num_nodes_in_length + i
                f = (
                    (k + 1) * num_nodes_in_length * num_nodes_in_width
                    + j * num_nodes_in_length
                    + i
                    + 1
                )
                g = (
                    (k + 1) * num_nodes_in_length * num_nodes_in_width
                    + (j + 1) * num_nodes_in_length
                    + i
                )
                h = (
                    (k + 1) * num_nodes_in_length * num_nodes_in_width
                    + (j + 1) * num_nodes_in_length
                    + i
                    + 1
                )
                connectivity = [a, b, d, c, e, f, h, g]
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
    elem_nod_field = dpf.Field(nature=nat, location=dpf.locations.elemental_nodal)
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
def averaging_using_max_value(elemental_nodal_field, b_use_absolute_value=False):
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
    b_use_absolute_value: bool
        Default is False. If set to True, considers the absolute value
        to check the maximum for averaging.

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
    # start compute
    elems_scoping_in = elemental_nodal_field.scoping.ids
    elems_scoping_base = mesh.elements.scoping
    nodes_scoping = mesh.nodes.scoping.ids
    elems_connectivity = mesh.elements.connectivities_field  # list of nodes per elements
    already_computed = {}  # { nod_id : val }
    for el_ind_in, el_id_in in enumerate(elems_scoping_in):
        mesh_el_ind = elems_scoping_base.index(el_id_in)
        el_connectivity = elems_connectivity.get_entity_data(mesh_el_ind)
        el_data = elemental_nodal_field.get_entity_data(el_ind_in)
        ldata = len(el_data)
        for nod_ind_in, nod_ind_mesh in enumerate(el_connectivity):
            if nod_ind_in >= ldata:
                break
            # get nod id for res scoping
            nod_id = nodes_scoping[nod_ind_mesh]
            # get nod data
            nod_data = el_data[nod_ind_in]
            # check if nod_data is already defined
            val_to_check = already_computed.get(nod_id)
            if val_to_check is not None:
                # - if defined, then check max value and append
                if b_use_absolute_value:
                    val_max = max(abs(val_to_check), abs(nod_data))
                else:
                    val_max = max(val_to_check, nod_data)
                already_computed[nod_id] = val_max
            else:
                # - if not defined, then insert
                if b_use_absolute_value:
                    already_computed[nod_id] = abs(nod_data)
                else:
                    already_computed[nod_id] = nod_data
    for key, val in already_computed.items():
        output_field.append(val, key)

    return output_field


###############################################################################
# Create surface mesh and compute maximum value averaging
# -------------------------------------------------------
l = 1
n_l = 3
###############################################################################
# Define the geometry:
cust_length = l
cust_width = l
cust_num_nodes_in_length = n_l
cust_num_nodes_in_width = n_l
mesh = create_surface_mesh(
    cust_length, cust_width, cust_num_nodes_in_length, cust_num_nodes_in_width
)

###############################################################################
# Create the mesh and compute the specific averaging:
stress_field_surf = create_elemental_nodal_field(mesh, 1)
output_field_surf = averaging_using_max_value(stress_field_surf, True)
mesh.plot(output_field_surf)

###############################################################################
# Compare with averaged values:
fc_surf = dpf.fields_container_factory.over_time_freq_fields_container(
    {0.1: stress_field_surf}, "s"
)
field_averaged_surf = ops.averaging.to_nodal_fc(
    fields_container=fc_surf, mesh=mesh
).outputs.fields_container()
mesh.plot(field_averaged_surf[0])

###############################################################################
# Create volume mesh and compute maximum value averaging
# -------------------------------------------------------
# Define the geometry:
cust_depth = l
cust_num_nodes_in_depth = n_l
mesh = create_volume_mesh(
    cust_length,
    cust_width,
    cust_depth,
    cust_num_nodes_in_length,
    cust_num_nodes_in_width,
    cust_num_nodes_in_depth,
)

###############################################################################
# Create the mesh and compute the specific averaging:
stress_field_vol = create_elemental_nodal_field(mesh, 1)
output_field_vol = averaging_using_max_value(stress_field_vol)
mesh.plot(output_field_vol)

###############################################################################
# Compare with averaged values:
fc_vol = dpf.fields_container_factory.over_time_freq_fields_container({0.1: stress_field_vol}, "s")
field_averaged_vol = ops.averaging.to_nodal_fc(
    fields_container=fc_vol, mesh=mesh
).outputs.fields_container()
mesh.plot(field_averaged_vol[0])
