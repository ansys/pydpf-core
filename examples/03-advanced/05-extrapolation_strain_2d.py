"""
.. _extrapolation_test_strain_2Delement:

Extrapolation method for strain result of a 2D element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to compute the nodal component elastic strain
from Gaussian points (integration points) for a 2D element by using the
extrapolation method.

Extrapolate results available at Gaussian or quadrature points to nodal
points for a field or fields container. The available elements are:

* Linear quadrangle
* Parabolic quadrangle
* Linear hexagonal
* Quadratic hexagonal
* Linear tetrahedral
* Quadratic tetrahedral

Here are the steps for extrapolation:

#. Get the data source's solution from the integration points. (This
   result file was generated with the Ansys Mechanical APDL (MAPDL)
   option ``EREXS, NO``).
#. Use the extrapolation operator to compute the nodal elastic strain.
#. Get the result for nodal elastic strain from the data source.
   The analysis was computed by MAPDL.
#. Compare the result for nodal elastic strain from the data source
   and the nodal elastic strain computed by the extrapolation method.


"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Get the data source's analyse of integration points and data source's analyse reference
datafile = examples.download_extrapolation_2d_result()

# integration points (Gaussian points)
data_integration_points = datafile["file_integrated"]
data_sources_integration_points = dpf.DataSources(data_integration_points)

# reference
dataSourceref = datafile["file_ref"]
data_sources_ref = dpf.DataSources(dataSourceref)

# get the mesh
model = dpf.Model(data_integration_points)
mesh = model.metadata.meshed_region

###############################################################################
# Extrapolate from integration points for elastic strain result
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This example uses the ``gauss_to_node_fc`` operator to compute nodal component
# elastic strain results from the elastic strain at the integration points.

# Create elastic strain operator to get strain result of integration points
strainop = dpf.operators.result.elastic_strain()
strainop.inputs.data_sources.connect(data_sources_integration_points)
strain = strainop.outputs.fields_container()

###############################################################################
# Nodal elastic strain result of integration points:
###############################################################################
# The command ``ERESX,NO`` in MAPDL is used to copy directly the
# Gaussian (integration) points results to the nodes, instead of the results
# at nodes or elements (which are an interpolation of results at a few
# Gaussian points).
#
# The following plot shows the nodal values that are the averaged values
# of elastic strain at each node. The value shown at the node is the
# average of the elastic strains from the Gaussian points of each element
# that it belongs to.

# plot
strain_nodal_op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
strain_nodal_op.inputs.fields_container.connect(strain)
mesh.plot(strain_nodal_op.outputs.fields_container())

###############################################################################
# Create the ``gauss_to_node_fc`` operator and compute nodal component
# elastic strain by applying the extrapolation method.

ex_strain = dpf.operators.averaging.gauss_to_node_fc()
# connect mesh
ex_strain.inputs.mesh.connect(mesh)
# connect fields container elastic strain
ex_strain.inputs.fields_container.connect(strain)
# get output
fex = ex_strain.outputs.fields_container()

###############################################################################
# Elastic strain result of reference Ansys Workbench
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Strain from file dataSourceref
strainop_ref = dpf.operators.result.elastic_strain()
strainop_ref.inputs.data_sources.connect(data_sources_ref)
strain_ref = strainop_ref.outputs.fields_container()

###############################################################################
# Plot
# ~~~~
# Show plots of extrapolation's elastic strain result and reference's elastic strain result

# extrapolation
fex_nodal_op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
fex_nodal_op.inputs.fields_container.connect(fex)
mesh.plot(fex_nodal_op.outputs.fields_container())
# reference
strain_ref_nodal_op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
strain_ref_nodal_op.inputs.fields_container.connect(strain_ref)
mesh.plot(strain_ref_nodal_op.outputs.fields_container())

###############################################################################
# Comparison
# ~~~~~~~~~~~~
# Compare the elastic strain result computed by extrapolation and reference's result.
# Check if the two fields containers are identical.
# The maximum tolerance gap between two compared values is 1e-3.
# The smallest value that is to be considered during the comparison
# step : all the ``abs(values)`` in the field less than 1e-14 are considered null.

# operator AreFieldsIdentical_fc
op = dpf.operators.logic.identical_fc()
op.inputs.fields_containerA.connect(fex)
op.inputs.fields_containerB.connect(strain_ref)
op.inputs.tolerance.connect(1.0e-14)
op.inputs.small_value.connect(0.001)
op.outputs.boolean()
