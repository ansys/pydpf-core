"""
.. _ref_matrix-operations:

Matrix Operations
~~~~~~~~~~~~~~~~~

This example shows how to do some matrix operations, including basic mathematical operations (power, add and multiply by
a constant, add field containers and invert) and separating and assembling fields and fields containers.

"""

###############################################################################
# Import the ``ansys.dpf.core`` module, included examples file, and the ``DpfPlotter``
# module.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
import ansys.dpf.core.operators.math as maths

###############################################################################
# Open an example and print the ``Model`` object. Here a result file from a crankshaft
# under load simulation is used.
# The :class:`Model <ansys.dpf.core.model.Model>` class helps to organize access
# methods for the result by keeping track of the operators and data sources
# used by the result file.
#
# Printing the model displays this metadata:
#
# - Analysis type
# - Available results
# - Size of the mesh
# - Number of results
#
my_model = dpf.Model(examples.find_complex_rst())
my_mesh = my_model.metadata.meshed_region
print(my_model)
###############################################################################
# Get the stress tensor and define it's scoping. Here, only three nodes will be take into account to facilitate the
# results visualisation
my_nodes_scoping = dpf.Scoping(ids=[38, 37, 36], location=dpf.locations.elemental)
my_stress = my_model.results.stress(mesh_scoping=my_nodes_scoping).eval()

# Here we need to average the result from 'elemental_nodal' to an 'elemental' location to
# facilitate the visualisation of the plot
my_avg_stress = dpf.operators.averaging.to_elemental_fc(fields_container=my_stress, mesh=my_mesh).eval()
# print(my_avg_stress, my_avg_stress[0])

#########################################################
# Separating tensor by component
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If operations need to be done separetly in each tensor component, the
# :func:'select_component()<ansys.dpf.core.fields_container.FieldsContainer.select_component>'.
# Here, the stress tensor has 6 components by elementary data (symmetrical tensor XX,YY,ZZ,XY,YZ,XZ).

for i in range(0, 6):  # Separating the results in different fields containers for each stress tensor component
    globals()[f'stress_{i + 1}'] = my_avg_stress.select_component(i)

################################################################################
# Mathematical operation on each field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Here we will do some basic mathematical operations on
# Power
# Compute the power operation for each elementary data
stress_1 = maths.pow_fc(fields_container=stress_1, factor=2.0).eval()

# Add constant
# Each component of each field is added by 2
stress_2 = maths.add_constant_fc(fields_container=stress_2, ponderation=2.0).eval()

# Multiply by a constant
# Each component of each field is multiplied by 3
stress_3 = maths.scale_fc(fields_container=stress_3, ponderation=3.0).eval()

# Add fields containers
# Each component of each field is added by the correspondent component of the others fields
stress_4 = maths.add_fc(fields_container1=stress_4, fields_container2=stress_5).eval()
stress_5 = maths.add_fc(fields_container1=stress_5, fields_container2=stress_6).eval()

#Invert
# Compute the invert of each element of each field (1./X)
stress_6 = maths.invert_fc(fields_container=stress_6).eval()

################################################################################
# Reassembling the stress tensor
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# There are different methods to re-assemble the components

# 1) With the class :class:'assemble_scalars_to_matrices_fc <ansys.dpf.core.operators.utility.assemble_scalars_to_matrices_fc.assemble_scalars_to_matrices_fc>'
assemble_1 = dpf.operators.utility.assemble_scalars_to_matrices_fc(xx=stress_1, yy=stress_2, zz=stress_3,
                                                                   xy=stress_4, yz=stress_5, xz=stress_6,
                                                                   symmetrical=True).eval()
print(assemble_1, assemble_1[0])

