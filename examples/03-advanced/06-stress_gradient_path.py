from ansys.dpf import core as dpf
from ansys.dpf.core import operators as ops
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core import examples

node_id = 1928
depth = 10

model = dpf.Model(examples.hemisphere)
mesh = model.metadata.meshed_region
stress_fc = model.results.stress().eqv().outputs.fields_container()

nodal_scoping = dpf.Scoping(location="Nodal")
nodal_scoping.ids = [node_id]

skin_mesh = ops.mesh.skin(mesh=mesh)
skin_meshed_region = skin_mesh.outputs.mesh.get_data()

normal = dpf.operators.geo.normals()
normal.inputs.mesh.connect(skin_meshed_region)
normal.inputs.mesh_scoping.connect(nodal_scoping)
normal_vec_out_field = normal.outputs.field.get_data()
normal_vec_in_field = dpf.operators.math.scale(field=normal_vec_out_field,
                                               ponderation=-1.0)
normal_vec_in = normal_vec_in_field.outputs.field.get_data().data[0]

# Line base point
node = mesh.nodes.node_by_id(node_id)
line_fp = node.coordinates

# 3D line equation
fx = lambda t: line_fp[0] + normal_vec_in[0] * t
fy = lambda t: line_fp[1] + normal_vec_in[1] * t
fz = lambda t: line_fp[2] + normal_vec_in[2] * t

coordinates = [[fx(t / 10.0), fy(t / 10.0), fz(t / 10.0)] for t in
               range(int(depth
                         * 10))]
flat_coordinates = [entry for data in coordinates for entry in data]

field_coord = dpf.fields_factory.create_3d_vector_field(len(coordinates))
field_coord.data = flat_coordinates
field_coord.scoping.ids = list(range(1, len(coordinates) + 1))

mapping_operator = ops.mapping.on_coordinates(
    fields_container=stress_fc,
    coordinates=field_coord,
    create_support=True,
    mesh=mesh)
fields_mapped = mapping_operator.outputs.fields_container()

field_m = fields_mapped[0]
mesh_m = field_m.meshed_region

pl = DpfPlotter()

pl.add_field(field_m, mesh_m, show_max=True)
pl.add_mesh(mesh, style="surface", show_edges=True,
            color="w", opacity=0.3)

pl.show_figure(show_axes=True)
