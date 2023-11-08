"""
.. _ref_sc-basic-mapping:

Basic DPF-SYC mapping operator Usage
~~~~~~~~~~~~~~~~~~~~
This example shows how to use systemCoupling mapping operator 
on simple surface.

First, import the DPF-Core module as ``dpf_core`` 


"""

from ansys.dpf import core as dpf

###############################################################################
# Next, define a function to create simple square mesh region for later mapping
# process. Input arguments are number of nodes for mesh region length and height,
# and distance between nodes


def get_sq_mesh(NX: int, NY: int, Ax: float):
    EX = NX-1
    EY = NY-1
    numNode = NX*NY
    numElem = EX*EY
    ref_mesh = dpf.MeshedRegion(num_nodes=numNode, num_elements=numElem)
    for j in range(NY):
        for i in range(NX):
            ref_mesh.nodes.add_node(NX*j+i+1, [Ax*i, Ax*j, 0.0])

    for j in range(EY):
        for i in range(EX):
            ref_mesh.elements.add_shell_element(EY*j+i+1, [NX * j + i, NX * j + (i + 1),
                            NX * (j + 1) + (i + 1), NX * (j + 1) + i])
    return ref_mesh

###############################################################################
# Here is example to create a mesh region using above function

surfaceMesh = get_sq_mesh(3, 3, 0.1)


###############################################################################
# Then create a field to store the source data on the node for the above 
# surfaceMesh with 9 nodes and set unit of the field as "K"

def source_data():
    source_data = dpf.Field(9, dpf.natures.scalar, "Nodal")
    source_data.append([0.0], scopingid=1)
    source_data.append([1.0], scopingid=2)
    source_data.append([4.0], scopingid=3)
    source_data.append([-40.0], scopingid=4)
    source_data.append([25.0], scopingid=5)
    source_data.append([10.0], scopingid=6)
    source_data.append([4.5], scopingid=7)
    source_data.append([7.0], scopingid=8)
    source_data.append([-3.0], scopingid=9)
    source_data.unit = "K"

    return source_data


###############################################################################
# Next step is to create create_sc_mapping_workflow and set up the inputs, 
# which are "source_mesh","target_mesh", "is_conservative"( mapping variable 
# is extensive or intensive), "location"(Nodal or Elemental), "dimensional",
# "is_pointcloud", "target_scoping". These inputs are optional.


source_region = get_sq_mesh(3, 3, 0.1)
target_region = get_sq_mesh(5, 5, 0.05)
dimensionality = 1
op = dpf.operators.mapping.create_sc_mapping_workflow()
op.inputs.source_mesh.connect(source_region)
op.inputs.target_mesh.connect(target_region)
op.inputs.is_conservative.connect(False)
op.inputs.location.connect("Nodal")
op.inputs.dimensionality.connect(dimensionality)
source_data=source_data()


###############################################################################
# Then a system coupling mapping workflow can be obtained from 
# create_sc_mapping_workflow operator

sc_map_wf = op.outputs.mapping_workflow()


###############################################################################
# connect "source_data" to system coupling mapping workflow

sc_map_wf.connect("source_data", source_data)


###############################################################################
# finally, the target_data is obtained from system coupling mapping workflow

out_fc = sc_map_wf.get_output("target_data", dpf.types.fields_container)

target_data = out_fc[0].data

###############################################################################
source_region.plot(source_data)
target_region.plot(out_fc)


