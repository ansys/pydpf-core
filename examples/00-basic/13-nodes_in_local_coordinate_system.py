from ansys.dpf import core as dpf
from ansys.dpf.core import examples

model = dpf.Model(examples.download_hemisphere())

# Global coordinates field
ncoord_f = model.metadata.meshed_region.nodes.coordinates_field

# Get the rotation matrix of the Local Coordinate System
cs = model.operator(r"mapdl::rst::CS")
cs.inputs.cs_id.connect(12)
cs_rot_mat = cs.outputs.field.get_data().data.T[0:9]

# Create rotation matrix field
rot_mat_f = dpf.fields_factory.create_scalar_field(1)
rot_mat_f.data = cs_rot_mat

# Create position vector field
pos_vec = dpf.fields_factory.create_3d_vector_field(1)
pos_vec.data = cs.outputs.field.get_data().data.T[-3:]
# Get rotated position vector
pos_vec_rot = dpf.operators.geo.rotate(field=pos_vec,
                                       field_rotation_matrix=rot_mat_f)

# Get rotated nodal coordinates field
ncoord_rot_f = dpf.operators.geo.rotate(field=ncoord_f,
                                        field_rotation_matrix=rot_mat_f)

# Transform rotated nodal coordinates field along rotated position vector
pos_vec_rot_neg_f = dpf.operators.math.scale(field=pos_vec_rot,
                                             ponderation=-1.0)
pos_vec_rot_neg = pos_vec_rot_neg_f.outputs.field.get_data().data_as_list
nccord_translated = dpf.operators.math.add_constant(field=ncoord_rot_f,
                                                    ponderation=pos_vec_rot_neg)
ncoord_lcs_f = nccord_translated.outputs.field.get_data()

# Coordinates of NID 1 in GCS
print(ncoord_f.get_entity_data_by_id(1))

# Coordinates of NID 1 in LCS
print(ncoord_lcs_f.get_entity_data_by_id(1))
