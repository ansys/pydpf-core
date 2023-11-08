"""
.. _ref_sc-basic-mapping:

DPF-SYC mapping operator Usage
~~~~~~~~~~~~~~~~~~~~
This example shows how to use systemCoupling mapping operator 
on volume to volume mapping with scalar variables and single
coupling interface between one source meshed_region and 
target meshed_region

First, import the DPF-Core module as ``dpf_core`` and import the
included examples file. 


"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples


###############################################################################
# Then create one deserializer operator to load source mesh, target mesh, and
# source field data. In this example, a volume hex source mesh, a volume 
# tet target mesh, and volume tet elemental temperature source fields data
# are read.

deserializer = dpf.operators.serialization.deserializer()
mesh_path_trg =examples.target_vol_hex 
deserializer.inputs.file_path.connect(mesh_path_trg)
mesh_trg = deserializer.get_output(1, dpf.types.meshed_region)

mesh_path_src = examples.source_vol_tet
deserializer.inputs.file_path.connect(mesh_path_src)
mesh_src = deserializer.get_output(1, dpf.types.meshed_region)

fc_path_src = examples.source_vol_tet_field_data
deserializer.inputs.file_path.connect(fc_path_src)
fc_src = deserializer.get_output(1, dpf.types.fields_container)



###############################################################################
# Create a create_sc_mapping_workflow operator and connect inputs.
# In this mapping example, scalar variable is conservative and located in elemental.
# Dimensionality is used to indicate whether variable is scalar or vector.
# is_conservative is used to indicate whether variable is extensive and intensive.
# is_conservative with false value means variables is extensive(e.g. heat flow, force),
# On the contrary, is_conservative with true value is intensive(e.g. heat flux)

map_builder = dpf.operators.mapping.create_sc_mapping_workflow()

dimensionality = 1
is_conservative = False

map_builder.inputs.source_mesh.connect(mesh_src)
map_builder.inputs.target_mesh.connect(mesh_trg)
map_builder.inputs.is_conservative.connect(is_conservative)
map_builder.inputs.location.connect("Elemental")
map_builder.inputs.dimensionality.connect(dimensionality)


###############################################################################
# Then get sc_workflow, connect source field container, and evaluate target 
# fields container

sc_map_wf = map_builder.outputs.mapping_workflow()
sc_map_wf.connect("source_data", fc_src[0])

fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)


###############################################################################
# create scoping operator to get target value of interesting from target 
# fields container for further usage

data_sco = dpf.Scoping()
data_sco.location = dpf.locations.elemental
data_sco.ids = [1287, 176]

rescope_fc = dpf.operators.scoping.rescope_fc()
rescope_fc.inputs.fields_container.connect(fc_trg)
rescope_fc.inputs.mesh_scoping.connect(data_sco)

fields=rescope_fc.outputs.fields_container()

Tvals_trg = rescope_fc.outputs.fields_container()[0].data

###############################################################################
# Finally visualize source and target mesh results
from ansys.dpf.core.plotter import DpfPlotter
p1=DpfPlotter()
p1.add_field(fc_src[0],mesh_src)

# Then it is needed to translate target mesh along x axi
overall_field = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
overall_field.append([0.4, 0.0, 0.0], 1)
coordinates_to_update = mesh_trg.nodes.coordinates_field
add_operator = dpf.operators.math.add(coordinates_to_update, overall_field)
coordinates_updated = add_operator.outputs.field()
coordinates_to_update.data = coordinates_updated.data
p1.add_field(fc_trg[0],mesh_trg)
p1.show_figure()

