import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

model = dpf.Model(examples.find_static_rst())
nid_1 = 6
nid_2 = 17

mesh = model.metadata.meshed_region
n1 = mesh.nodes.node_by_id(nid_1)
n2 = mesh.nodes.node_by_id(nid_2)


x_0 = n1.coordinates[0]
y_0 = n1.coordinates[1]
z_0 = n1.coordinates[2]

x_1 = n2.coordinates[0]
y_1 = n2.coordinates[1]
z_1 = n2.coordinates[2]

path_length = ((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2 + (z_1 - z_0) ** 2) ** 0.5

n_points = 49  # A linearized stress has fixed a number of 48 points.
delta = path_length / (n_points - 1)

line_unit_vector = [(x_1 - x_0) / path_length, (y_1 - y_0) / path_length, (z_1 - z_0) / path_length]

# Line equation
fx = lambda t: x_0 + line_unit_vector[0] * t
fy = lambda t: y_0 + line_unit_vector[1] * t
fz = lambda t: z_0 + line_unit_vector[2] * t

coordinates = [[fx(t * delta), fy(t * delta), fz(t * delta)] for t in range(n_points)]
flat_coordinates = [entry for data in coordinates for entry in data]

field_coord = dpf.fields_factory.create_3d_vector_field(n_points)
field_coord.data = flat_coordinates
field_coord.scoping.ids = list(range(1, n_points + 1))

# SX
s = model.operator("SX")
s.inputs.requested_location.connect("Nodal")
s_f = s.outputs.fields_container.get_data()

mapping_operator = dpf.operators.mapping.on_coordinates(
    fields_container=s_f,
    coordinates=field_coord,
    create_support=True,
    mesh=mesh
)
fields_mapped = mapping_operator.outputs.fields_container.get_data()

ls = list(fields_mapped[0].data)
# Membrane Stress
membrane_stress = (ls[0] / 2 + ls[-1] / 2 + sum(ls[1:-1])) / (n_points - 1)

# Bending stress
path_1 = -1 * path_length / 2
path_n = path_length / 2
path_range = [path_1 + delta * i for i in range(n_points)]
path_range_field = dpf.fields_factory.create_scalar_field(n_points, location=dpf.locations.nodal)
path_range_field.data = path_range
path_range_field.scoping.ids = range(1, 50)

# Function to be integrated
stress_scaled = dpf.operators.math.scale_by_field(fieldA=fields_mapped[0], fieldB=path_range_field)
stress_scaled_data = list(stress_scaled.outputs.field.get_data().data)

# Use extended Simpson's rule for Numerical Integration of `stress_scaled_data`
stress_scaled_integral = (17 * stress_scaled_data[0] + 59 * stress_scaled_data[1] + 43 * stress_scaled_data[2] + 49 *
                          stress_scaled_data[3] + 48 * sum(stress_scaled_data[4:-4]) + 49 * stress_scaled_data[
                              n_points - 4] + 43 * stress_scaled_data[n_points - 3] + 59 * stress_scaled_data[
                              n_points - 2] + 17 * stress_scaled_data[n_points - 1]) / 48.0

b1 = stress_scaled_integral * (-6.0 / path_length) / 48.0
b2 = (-1.0) * b1
slope_bending = (b2 - b1) / (path_length)
fb = lambda t: b1 + slope_bending * t
bending_stress = [fb(t * delta) for t in range(n_points)]

bend_f = dpf.fields_factory.create_scalar_field(49, location=dpf.locations.nodal)
bend_f.data = bending_stress
bend_f.scoping.ids = list(range(1, n_points + 1))

# Add Membrane and Bending Stress
bend_mem_f = dpf.operators.math.add_constant(field=bend_f, ponderation=[membrane_stress])
bend_mem_f_neg = dpf.operators.math.scale(field=bend_mem_f, ponderation=-1.0)

# Peak stress
ps = dpf.operators.math.add(fieldA=fields_mapped[0], fieldB=bend_mem_f_neg)
ps_data = ps.outputs.field.get_data().data

plt.plot(path_range, ps_data, "b", label="Peak Stress")
plt.plot(path_range, bending_stress, "r", label="Bending Stress")
plt.plot(path_range, [membrane_stress] * n_points, "y", label="Membrane Stress")
plt.xlabel("Path (m)")
plt.ylabel("Stress (Pa)")
plt.legend()
plt.show()