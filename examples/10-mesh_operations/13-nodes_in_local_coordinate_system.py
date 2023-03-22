# noqa: D400
"""
.. _ref_nodes_in_local_coordinate_system:

Convert nodal coordinates field to local coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, there is no native operator to get nodal coordinates in an Local
Coordinate System (LCS). The operator :class:`rotate <ansys.dpf.core.operators.geo.rotate.rotate>`
rotates the input field in Global Coordinate System (GCS) as per the input rotation matrix.
So, if the LCS is at the same origin as the GCS, only one operation using the
:class:`rotate <ansys.dpf.core.operators.geo.rotate.rotate>` operator give the desired output.
However, if the aim is to obtain the LCS in a case where the LCS origin does not coincide with
the GCS, a transformation is required after the rotation to get the correct coordinates in LCS.

The script below demonstrates the methodology using PyDPF.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.


"""
# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples


###############################################################################
# Create a model object to establish a connection with an example result file:
model = dpf.Model(examples.download_hemisphere())

###############################################################################
# Get the property ``coordinates_field`` from :class:`nodes <ansys.dpf.core.nodes>`:
ncoord_f = model.metadata.meshed_region.nodes.coordinates_field

###############################################################################
# Get the rotation matrix of the LCS ID 12.
# The first 9 values in the ``cs`` output is the rotation matrix.
cs = model.operator(r"mapdl::rst::CS")
cs.inputs.cs_id.connect(12)
cs_rot_mat = cs.outputs.field.get_data().data.T[0:9]

###############################################################################
# Create a 3x3 rotation matrix field ``rot_mat_f``:
rot_mat_f = dpf.fields_factory.create_scalar_field(1)
rot_mat_f.data = cs_rot_mat

###############################################################################
# Create a 3D vector field for the position vector of the LCS's origin and
# rotate the origin as per the rotation matrix of the LCS.
# The last 3 entries of ``cs`` output is the LCS's origin in GCS.
pos_vec = dpf.fields_factory.create_3d_vector_field(1)
pos_vec.data = cs.outputs.field.get_data().data.T[-3:]
pos_vec_rot = dpf.operators.geo.rotate(field=pos_vec, field_rotation_matrix=rot_mat_f)

###############################################################################
# Get rotated nodal coordinates field:
ncoord_rot_f = dpf.operators.geo.rotate(field=ncoord_f, field_rotation_matrix=rot_mat_f)

###############################################################################
# Transform rotated nodal coordinates field along rotated position vector
# ``pos_vec_rot``:
pos_vec_rot_neg_f = dpf.operators.math.scale(field=pos_vec_rot, ponderation=-1.0)
pos_vec_rot_neg = pos_vec_rot_neg_f.outputs.field.get_data().data_as_list
ncoord_translate = dpf.operators.math.add_constant(field=ncoord_rot_f, ponderation=pos_vec_rot_neg)
###############################################################################
# Get the nodal coordinates field ``ncoord_lcs_f`` in LCS:
ncoord_lcs_f = ncoord_translate.outputs.field.get_data()

###############################################################################
# Coordinates of NID 1 in GCS
print(ncoord_f.get_entity_data_by_id(1))

###############################################################################
# Coordinates of NID 1 in LCS
print(ncoord_lcs_f.get_entity_data_by_id(1))
