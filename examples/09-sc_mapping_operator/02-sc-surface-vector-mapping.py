"""
.. _ref_sc-basic-mapping:

Basic DPF-SYC mapping operator Usage
~~~~~~~~~~~~~~~~~~~~
This example shows how to use systemCoupling mapping operator 
on surface to surface mapping with vector variables and multi
coupling interfaces between source and target meshes_container

First, import the DPF-Core module as ``dpf_core`` and import the
included examples file. 


"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples



###############################################################################
# Then create one deserializer operator to load source mesh container, 
# target mesh container, and source data. Multi coupling interfaces would be 
# created between source and target mesh container. In this example, 
# both source and target mesh container contains four different meshes. Therefore,
# four coupling interfaces are created.

deserializer = dpf.operators.serialization.deserializer()
mesh_path_trg = examples.shell_meshes_container 
deserializer.inputs.file_path.connect(mesh_path_trg)
mesh = deserializer.get_output(1, dpf.types.meshes_container)
# in this example, source and target meshes are the same
mesh1=deserializer.get_output(1, dpf.types.meshes_container)

fc_path_src =examples.shell_meshes_container_field_data 
deserializer.inputs.file_path.connect(fc_path_src)
fc_src = deserializer.get_output(1, dpf.types.fields_container)



###############################################################################
# create a create_sc_mapping_workflow operator and connect inputs.
# in this mapping example, scalar variable is conservative and located in nodes.

map_builder = dpf.operators.mapping.create_sc_mapping_workflow()

dimensionality = 3
is_conservative = False

map_builder.inputs.is_conservative.connect(is_conservative)
map_builder.inputs.location.connect("Nodal")
map_builder.inputs.dimensionality.connect(dimensionality)


###############################################################################
# Then get sc_workflow, connect source field container. Please note that 
# if any input is not connect create_sc_mapping_workflow, it can be connected 
# in the sc mapping workflow as well. And finally evaluate target 
# fields container

sc_map_wf = map_builder.outputs.mapping_workflow()
sc_map_wf.connect("source_mesh", mesh)
sc_map_wf.connect("target_mesh",mesh1) 
sc_map_wf.connect("source_data", fc_src)
fc_trg = sc_map_wf.get_output("target_data", dpf.types.fields_container)

###############################################################################
# Finally visualize source and target mesh results
from ansys.dpf.core.plotter import DpfPlotter
for i in range(len(mesh)):
    p1=DpfPlotter()
    p1.add_field(fc_src[i],mesh[i])

    # Then it is needed to translate target mesh along x axi
    mesh_trg=mesh1[i].deep_copy()
    overall_field = dpf.fields_factory.create_3d_vector_field(1, dpf.locations.overall)
    overall_field.append([1, 0.0, 0.0], 1)
    coordinates_to_update = mesh_trg.nodes.coordinates_field
    add_operator = dpf.operators.math.add(coordinates_to_update, overall_field)
    coordinates_updated = add_operator.outputs.field()
   
    coordinates_to_update.data = coordinates_updated.data 
    p1.add_field(fc_trg[i],mesh_trg)
    p1.show_figure()




