"""
.. _ref_create_entities_example:

Create Your Own Entities Use DPF Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can create your field, fields container, or meshed region to use DPF operators
with your own data. The ability to use scripting to create any DPF entity means
that you are not dependent on result files and can connect the DPF environment
with any Python tool.

Import necessary modules:
"""
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops

###############################################################################
# Create a parallel piped mesh made of linear hexa:
length = 0.1
width = 0.05
depth = 0.1
num_nodes_in_length = 10
num_nodes_in_width = 5
num_nodes_in_depth = 10
mesh_iterative = dpf.MeshedRegion()
mesh_from_fields = dpf.MeshedRegion()


def search_sequence_numpy(arr, seq):
    indexes = np.where(np.isclose(arr, seq[0]))
    for index in np.nditer(indexes[0]):
        if index % 3 == 0:
            if np.allclose(arr[index + 1], seq[1]) and np.allclose(
                    arr[index + 2], seq[2]
            ):
                return index
    return -1


###############################################################################
# Add nodes iteratively to the mesh, or create an array of coordinates
node_id = 1
coordinates_array = np.ndarray(shape=(0, 3))
for i, x in enumerate(
        [
            float(i) * length / float(num_nodes_in_length)
            for i in range(0, num_nodes_in_length)
        ]
):
    for j, y in enumerate(
            [
                float(i) * width / float(num_nodes_in_width)
                for i in range(0, num_nodes_in_width)
            ]
    ):
        for k, z in enumerate(
                [
                    float(i) * depth / float(num_nodes_in_depth)
                    for i in range(0, num_nodes_in_depth)
                ]
        ):
            mesh_iterative.nodes.add_node(node_id, [x, y, z])
            np.append(coordinates_array, [x, y, z])

            node_id += 1

###############################################################################
# Get the nodes' coordinates field from the mesh created iteratively:
coordinates = mesh_iterative.nodes.coordinates_field

###############################################################################
# Alternatively, one can set the coordinates field of a mesh,
# triggering creation of the nodes:
coordinates_custom_field = dpf.fields_factory.field_from_array(coordinates_array)
mesh_from_fields.set_coordinates_field(coordinates_custom_field)

###############################################################################
# Set the mesh unit:
mesh_iterative.unit = "mm"

# Get the data from a field
coordinates_data = coordinates.data
flat_coordinates_data = coordinates_data.reshape(coordinates_data.size)
# Get the scoping of a field
coordinates_scoping = coordinates.scoping

###############################################################################
# Add solid elements (linear hexa with eight nodes) iteratively to a mesh,
# or create a connectivity array:
element_id = 1
connectivity_array = []
for i, x in enumerate(
        [
            float(i) * length / float(num_nodes_in_length)
            for i in range(0, num_nodes_in_length - 1)
        ]
):
    for j, y in enumerate(
            [
                float(i) * width / float(num_nodes_in_width)
                for i in range(0, num_nodes_in_width - 1)
            ]
    ):
        for k, z in enumerate(
                [
                    float(i) * depth / float(num_nodes_in_depth)
                    for i in range(0, num_nodes_in_depth - 1)
                ]
        ):
            coord1 = np.array([x, y, z])
            connectivity = []
            for xx in [x, x + length / float(num_nodes_in_length)]:
                for yy in [y, y + width / float(num_nodes_in_width)]:
                    for zz in [z, z + depth / float(num_nodes_in_depth)]:
                        data_index = search_sequence_numpy(
                            flat_coordinates_data, [xx, yy, zz]
                        )
                        scoping_index = int(data_index / 3)  # 3components
                        connectivity.append(scoping_index)
            # rearrange connectivity
            tmp = connectivity[2]
            connectivity[2] = connectivity[3]
            connectivity[3] = tmp
            tmp = connectivity[6]
            connectivity[6] = connectivity[7]
            connectivity[7] = tmp
            mesh_iterative.elements.add_solid_element(element_id, connectivity)
            connectivity_array.extend(connectivity)

            element_id += 1

###############################################################################
# Get the elements' connectivity field from the mesh created iteratively:
connectivity = mesh_iterative.elements.connectivities_field

###############################################################################
# Alternatively, one can set the connectivity, element type, and material
# fields of a mesh, triggering creation of the elements:
connectivity_field = dpf.PropertyField(nentities=len(connectivity_array))
connectivity_field.data = connectivity_array
mesh_from_fields.set_property_field(dpf.common.elemental_properties.connectivity,
                                    connectivity_field)
# Set the element type field of a mesh:
element_type_field = dpf.PropertyField(nentities=element_id)
element_type_field.data = [11]*element_id  # 11 for Hex8 (see dpf.elements.element_types)
mesh_from_fields.set_property_field(dpf.common.elemental_properties.element_type,
                                    element_type_field)

# Set the material field of a mesh:
material_field = dpf.PropertyField(nentities=element_id)
material_field.data = [1]*element_id
mesh_from_fields.set_property_field(dpf.common.elemental_properties.material,
                                    material_field)

###############################################################################
# Plot the resulting meshes, they are identical:
# mesh_iterative.plot()
mesh_from_fields.plot()

###############################################################################
# Create displacement fields over time with three time sets.
# Here the displacement on each node will be the value of its x, y, and
# z coordinates for time 1.
# The displacement on each node will be two times the value of its x, y,
# and z coordinates for time 2.
# The displacement on each node will be three times the value of its x,
# y, and z coordinates for time 3.
num_nodes = mesh_iterative.nodes.n_nodes
time1_array = coordinates_data
time2_array = 2.0 * coordinates_data
time3_array = 3.0 * coordinates_data

time1_field = dpf.fields_factory.create_3d_vector_field(num_nodes)
time2_field = dpf.fields_factory.create_3d_vector_field(num_nodes)
time3_field = dpf.fields_factory.create_3d_vector_field(num_nodes)

time1_field.scoping = coordinates.scoping
time2_field.scoping = coordinates.scoping
time3_field.scoping = coordinates.scoping

time1_field.data = time1_array
time2_field.data = time2_array
time3_field.data = time3_array

time1_field.unit = mesh_iterative.unit
time2_field.unit = mesh_iterative.unit
time3_field.unit = mesh_iterative.unit

###############################################################################
# Create results over times in a fields container with its time frequency support:
fc = dpf.fields_container_factory.over_time_freq_fields_container(
    {0.1: time1_field, 0.2: time2_field, 0.3: time3_field}, "s"
)

###############################################################################
# Check that the time frequency support has been built:
print(fc.time_freq_support)

###############################################################################
# Plot the norm over time of the fields container:
norm = ops.math.norm_fc(fc)
fc_norm = norm.outputs.fields_container()
mesh_iterative.plot(fc_norm.get_field_by_time_complex_ids(1))
mesh_iterative.plot(fc_norm.get_field_by_time_complex_ids(2))
mesh_iterative.plot(fc_norm.get_field_by_time_complex_ids(3))
