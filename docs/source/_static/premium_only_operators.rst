List of Premium-only operators
==============================
Generated using ``dpf.core.operators.premium_operators``.

averaging
~~~~~~~~~
elemental_difference
^^^^^^^^^^^^^^^^^^^^
Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the computed result for all nodes in this element. Result is computed on a given element scoping.

elemental_difference_fc
^^^^^^^^^^^^^^^^^^^^^^^
Transform ElementalNodal or Nodal field into Elemental field. Each elemental value is the maximum difference between the unaveraged or averaged (depending on the input fields) computed result for all nodes in this element. Result is computed on a given element scoping. If the input fields are mixed shell/solid and the shells layers are not asked to be collapsed, then the fields are split by element shape and the output fields container has elshape label.

elemental_fraction_fc
^^^^^^^^^^^^^^^^^^^^^
Transform ElementalNodal fields into Elemental fields. Each elemental value is the fraction between the elemental difference and the entity average. Result is computed on a given elements scoping.

extend_to_mid_nodes
^^^^^^^^^^^^^^^^^^^
Extends an ElementalNodal or Nodal field defined on corner nodes to a field defined also on the mid nodes.

extend_to_mid_nodes_fc
^^^^^^^^^^^^^^^^^^^^^^
Extends ElementalNodal or Nodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.

gauss_to_node_fc
^^^^^^^^^^^^^^^^
Extrapolating results available at Gauss or quadrature points to nodal points for a field container. The available elements are : Linear quadrangle , parabolique quadrangle,Linear Hexagonal, quadratic hexagonal , linear tetrahedral, quadratic tetrahedral 

nodal_difference
^^^^^^^^^^^^^^^^
Transform ElementalNodal field into Nodal field. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping.

nodal_difference_fc
^^^^^^^^^^^^^^^^^^^
Transform ElementalNodal fields into Nodal fields. Each nodal value is the maximum difference between the unaveraged computed result for all elements that share this particular node. Result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are split by element shape and the output fields container has elshape label.

nodal_fraction_fc
^^^^^^^^^^^^^^^^^
Transform ElementalNodal fields into Nodal fields. Each nodal value is the fraction between the nodal difference and the nodal average. Result is computed on a given node scoping.

filter
~~~~~~
field_band_pass
^^^^^^^^^^^^^^^
The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.

field_band_pass_fc
^^^^^^^^^^^^^^^^^^
The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.

field_high_pass
^^^^^^^^^^^^^^^
The high pass filter returns all the values strictly superior to the threshold value in input.

field_high_pass_fc
^^^^^^^^^^^^^^^^^^
The high pass filter returns all the values strictly superior to the threshold value in input.

field_low_pass
^^^^^^^^^^^^^^
The low pass filter returns all the values strictly inferior to the threshold value in input.

field_low_pass_fc
^^^^^^^^^^^^^^^^^
The low pass filter returns all the values strictly inferior to the threshold value in input.

field_signed_high_pass
^^^^^^^^^^^^^^^^^^^^^^
The high pass filter returns all the values superior or equal in absolute value to the threshold value in input.

scoping_band_pass
^^^^^^^^^^^^^^^^^
The band pass filter returns all the values strictly superior to the min threshold value and strictly inferior to the max threshold value in input.

scoping_high_pass
^^^^^^^^^^^^^^^^^
The high pass filter returns all the values strictly superior to the threshold value in input.

scoping_low_pass
^^^^^^^^^^^^^^^^
The low pass filter returns all the values strictly inferior to the threshold value in input.

signed_scoping_high_pass
^^^^^^^^^^^^^^^^^^^^^^^^
The high pass filter returns all the values superior or equal in absolute value to the threshold value in input.

geo
~~~
element_nodal_contribution
^^^^^^^^^^^^^^^^^^^^^^^^^^
Compute the fraction of volume attributed to each node of each element.

elements_facets_surfaces_over_time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Calculation of the surface of each element's facet over time of a mesh for each specified time step. Moreover, it gives as output a new mesh made with only surface elements.

elements_volume
^^^^^^^^^^^^^^^
Compute the volume of each element of a mesh, using default shape functions.

elements_volumes_over_time
^^^^^^^^^^^^^^^^^^^^^^^^^^
Calculation of the volume of each element over time of a mesh for each specified time step.

gauss_to_node
^^^^^^^^^^^^^
Extrapolating results available at Gauss or quadrature points to nodal points for one field. The available elements are : Linear quadrangle , parabolique quadrangle,Linear Hexagonal, quadratic hexagonal , linear tetrahedral, quadratic tetrahedral 

integrate_over_elements
^^^^^^^^^^^^^^^^^^^^^^^
Integration of an input field over mesh.

normals
^^^^^^^
compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)

normals_provider_nl
^^^^^^^^^^^^^^^^^^^
Compute the normals on nodes/elements based on integration points(more accurate for non-linear elements), on a skin mesh

rotate
^^^^^^
Apply a transformation (rotation) matrix on field.

rotate_fc
^^^^^^^^^
Apply a transformation (rotation) matrix on all the fields of a fields container.

rotate_in_cylindrical_cs
^^^^^^^^^^^^^^^^^^^^^^^^
Rotate a field to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

rotate_in_cylindrical_cs_fc
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Rotate all the fields of a fields container (not defined with a cynlindrical coordinate system) to its corresponding values into the specified cylindrical coordinate system (corresponding to the field position). If no coordinate system is set in the coordinate_system pin, field is rotated on each node following the local polar coordinate system.

to_polar_coordinates
^^^^^^^^^^^^^^^^^^^^
Find r, theta (rad), z coordinates of a coordinates (nodal) field in cartesian coordinates system with respoect to the input coordinate system defining the rotation axis and the origin.

invariant
~~~~~~~~~
segalman_von_mises_eqv
^^^^^^^^^^^^^^^^^^^^^^
Computes the element-wise Segalman Von-Mises criteria on a tensor field.

segalman_von_mises_eqv_fc
^^^^^^^^^^^^^^^^^^^^^^^^^
Computes the element-wise Segalman Von-Mises criteria on all the tensor fields of a fields container.

logic
~~~~~
ascending_sort
^^^^^^^^^^^^^^
Sort a field (in 0) in ascending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.

ascending_sort_fc
^^^^^^^^^^^^^^^^^
Sort a field (in 0) in ascending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.

descending_sort
^^^^^^^^^^^^^^^
Sort a field (in 0) in descending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.

descending_sort_fc
^^^^^^^^^^^^^^^^^^
Sort a field (in 0) in descending order, with an optional component priority table or a boolean to enable sort by scoping (in 1). This operator doesn't support multiple elementary data per entity.

enrich_materials
^^^^^^^^^^^^^^^^
Take a MaterialContainer and a stream and enrich the MaterialContainer using stream data.

identical_fc
^^^^^^^^^^^^
Check if two fields container are identical.

identical_fields
^^^^^^^^^^^^^^^^
Check if two fields are identical.

identical_meshes
^^^^^^^^^^^^^^^^
Take two meshes and compare them. Note: When comparing mesh properties the current behaviour is to verify that the properties in the first mesh (pin 0) are included in the second mesh (pin 1).

identical_property_fields
^^^^^^^^^^^^^^^^^^^^^^^^^
Take two property fields and compare them.

included_fields
^^^^^^^^^^^^^^^
Check if one field belongs to another.

mapping
~~~~~~~
find_reduced_coordinates
^^^^^^^^^^^^^^^^^^^^^^^^
Find the elements corresponding to the given coordinates in input and compute their reduced coordinates in those elements.

on_coordinates
^^^^^^^^^^^^^^
Evaluates a result on specified coordinates (interpolates results inside elements with shape functions).

on_reduced_coordinates
^^^^^^^^^^^^^^^^^^^^^^
Evaluates a result on specified reduced coordinates of given elements (interpolates results inside elements with shape functions).

prepare_mapping_workflow
^^^^^^^^^^^^^^^^^^^^^^^^
Generate a workflow that can map results from a support to another one.

scoping_on_coordinates
^^^^^^^^^^^^^^^^^^^^^^
Finds the Elemental scoping of a set of coordinates.

solid_to_skin
^^^^^^^^^^^^^
Maps a field defined on solid elements to a field defined on skin elements.

math
~~~~
correlation
^^^^^^^^^^^
take two fields and a weighting and compute their correlation: aMb/(||aMa||.||bMb||)

fft_approx
^^^^^^^^^^
Computes the fitting curve using FFT filtering and cubic fitting in space (node i: x=time, y=data), with possibility to compute the first and the second derivatives of the curve.


fft_eval
^^^^^^^^
Evaluate the fast fourier transforms at a given set of fields.

fft_gradient_eval
^^^^^^^^^^^^^^^^^
Evaluate min max based on the fast fourier transform at a given field, using gradient method for adaptative time step.

fft_multi_harmonic_minmax
^^^^^^^^^^^^^^^^^^^^^^^^^
Evaluate min max fields on multi harmonic solution. min and max fields are calculated based on evaluating a fft wrt rpms and using the gradient method for adaptive time steping

matrix_inverse
^^^^^^^^^^^^^^
computes the complex matrix inverse at a given fields container.

modal_superposition
^^^^^^^^^^^^^^^^^^^
Compute the solution in the time/frequency space from a modal solution by multiplying a modal basis (in 0) by the solution in this modal space (coefficients for each mode for each time/frequency) (in 1).

qr_solve
^^^^^^^^
computes the solution using QR factorization.

svd
^^^
computes the complex matrix svd at a given fields container.

mesh
~~~~
change_cs
^^^^^^^^^
Apply a transformation (rotation and displacement) matrix on a mesh or meshes container.

combine_levelset
^^^^^^^^^^^^^^^^
Takes two levelsets and compute their binary union.

decimate_mesh
^^^^^^^^^^^^^
Decimate a surface meshed region with triangle elements

exclude_levelset
^^^^^^^^^^^^^^^^
Take a leveset and exclude the second one from it.

external_layer
^^^^^^^^^^^^^^
Extracts the external layer (thick skin) of the mesh (3D elements) in a new meshed region

from_scoping
^^^^^^^^^^^^
Extracts a meshed region from an other meshed region base on a scoping

make_plane_levelset
^^^^^^^^^^^^^^^^^^^
Compute the levelset for a plane using coordinates.

make_sphere_levelset
^^^^^^^^^^^^^^^^^^^^
Compute the levelset for a sphere using coordinates.

mesh_clip
^^^^^^^^^
Clip a volume mesh along an iso value x, and construct the volume mesh defined by v < x.

mesh_cut
^^^^^^^^
Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

mesh_plan_clip
^^^^^^^^^^^^^^
Clip a volume mesh along a plane, and keep one side.

mesh_to_graphics
^^^^^^^^^^^^^^^^
Generate tessellation for input mesh

mesh_to_graphics_edges
^^^^^^^^^^^^^^^^^^^^^^
Generate edges of surface elements for input mesh

points_from_coordinates
^^^^^^^^^^^^^^^^^^^^^^^
Extract a mesh made of points elements. This mesh is made from input meshes coordinates on the input scopings.

skin
^^^^
Extracts a skin of the mesh (2D elements) in a new meshed region. Material id of initial elements are propagated to their facets.

split_fields
^^^^^^^^^^^^
Split the input field or fields container based on the input mesh regions 

split_mesh
^^^^^^^^^^
Split the input mesh into several meshes based on a given property (material property be default)

stl_export
^^^^^^^^^^
export a mesh into a stl file.

tri_mesh_skin
^^^^^^^^^^^^^
Extracts a skin of the mesh in triangles (2D elements) in a new meshed region

min_max
~~~~~~~
max_over_phase
^^^^^^^^^^^^^^
Returns, for each entity, the maximum value of (real value * cos(theta) - imaginary value * sin(theta)) for theta in [0, 360]degrees with the increment in input.

min_max_fc_inc
^^^^^^^^^^^^^^
Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.

min_max_inc
^^^^^^^^^^^
Compute the component-wise minimum (out 0) and maximum (out 1) over coming fields.

phase_of_max
^^^^^^^^^^^^
Evaluates phase of maximum.

time_of_max_by_entity
^^^^^^^^^^^^^^^^^^^^^
Evaluates time/frequency of maximum.

time_of_min_by_entity
^^^^^^^^^^^^^^^^^^^^^
Evaluates time/frequency of minimum.

result
~~~~~~
cgns::cgns::Pressure
^^^^^^^^^^^^^^^^^^^^
Read/compute names result from result streams.

cgns::cgns::result_provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read/compute names result from result streams.

cgns::cgns::zone_pressure_spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read/compute names result from result streams.

compute_stress
^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.

compute_stress_1
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the 1st principal component.

compute_stress_2
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the 2nd principal component.

compute_stress_3
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the 3rd principal component.

compute_stress_X
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the XX normal component (00 component).

compute_stress_XY
^^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the XY shear component (01 component).

compute_stress_XZ
^^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the XZ shear component (02 component).

compute_stress_Y
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the YY normal component (11 component).

compute_stress_YZ
^^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the YZ shear component (12 component).

compute_stress_Z
^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the ZZ normal component (22 component).

compute_stress_von_mises
^^^^^^^^^^^^^^^^^^^^^^^^
Computes the stress from an elastic strain field.Only some 3-D elements (only hexa, tetra, pyramid and wedge) and integration schemes are supported.
Only isotropic materials are supported. Material nonlinearity is not supported.
Only constant materials are supported.
All coordinates are global coordinates.
All units need to be consistent.Get the Von Mises equivalent stress.

compute_total_strain
^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.


compute_total_strain_1
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the 1st principal component.

compute_total_strain_2
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the 2nd principal component.

compute_total_strain_3
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the 3rd principal component.

compute_total_strain_X
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the XX normal component (00 component).

compute_total_strain_XY
^^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the XY shear component (01 component).

compute_total_strain_XZ
^^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the XZ shear component (02 component).

compute_total_strain_Y
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the YY normal component (11 component).

compute_total_strain_YZ
^^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the YZ shear component (12 component).

compute_total_strain_Z
^^^^^^^^^^^^^^^^^^^^^^
Computes the strain from a displacement field.
Only some 3-D elements and integration schemes are supported (only hexa, tetra, pyramid and wedge).
Layered elements are not supported.
All coordinates are global coordinates.
Not all strain formulations are supported.
Get the ZZ normal component (22 component).

equivalent_radiated_power
^^^^^^^^^^^^^^^^^^^^^^^^^
Compute the Equivalent Radiated Power (ERP)

erp_accumulate_results
^^^^^^^^^^^^^^^^^^^^^^
Compute the Equivalent Radiated Power (ERP) by panels and sum over the panels

erp_radiation_efficiency
^^^^^^^^^^^^^^^^^^^^^^^^
Compute the radiation efficiency (enhanced erp divided by classical erp)

euler_load_buckling
^^^^^^^^^^^^^^^^^^^
Computing Euler's Critical Load. Formula: Ncr = n*E*I*pi*pi /(L*L) 

members_in_bending_not_certified
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This operator is a non-certified example of buckling resistance verification for the bending members. It is only provided as an example if you want to develop your own compute norm operator. The results computed by this beta operator have not been certified by ANSYS. ANSYS declines all responsibility for the use of this operator. HATS Beam and irregular beams (unequal I-Beam, not-square Channel-Beam, not-square Angle L-beam, unequal hollow rectangular beam) not supported.

members_in_compression_not_certified
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This operator is a non-certified example of buckling resistance verification for the compression members for Class I, 2 and 3 cross-sections. It is only provided as an example if you want to develop your own compute norm operator. The results computed by this beta operator have not been certified by ANSYS. ANSYS declines all responsibility for the use of this operator.

members_in_linear_compression_bending_not_certified
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This operator is a non-certified example of buckling resistance verification for the compression and bending members for Class I, 2 and 3 cross-sections. It is only provided as an example if you want to develop your own compute norm operator. This norm is linear summation of the utilization ratios of compression members and bending members. The results computed by this beta operator have not been certified by ANSYS. ANSYS declines all responsibility for the use of this operator.

migrate_to_h5dpf
^^^^^^^^^^^^^^^^
Read mesh properties from the results files contained in the streams or data sources and make those properties available through a mesh selection manager in output.

poynting_vector
^^^^^^^^^^^^^^^
Compute the Poynting Vector

poynting_vector_surface
^^^^^^^^^^^^^^^^^^^^^^^
Compute the Poynting Vector surface integral

torque
^^^^^^
Compute torque of a force based on a 3D point.

transient_rayleigh_integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Computes the transient Rayleigh integral

serialization
~~~~~~~~~~~~~
csv_to_field
^^^^^^^^^^^^
transform csv file to a field or fields container

data_tree_to_json
^^^^^^^^^^^^^^^^^
Writes a json file or string from a DataTree

data_tree_to_txt
^^^^^^^^^^^^^^^^
Writes a txt file or string from a DataTree

export_symbolic_workflow
^^^^^^^^^^^^^^^^^^^^^^^^
Transforms a Workflow into a symbolic Workflow and writes it to a file (if a path is set in input) or string

field_to_csv
^^^^^^^^^^^^
Exports a field or a fields container into a csv file

import_symbolic_workflow
^^^^^^^^^^^^^^^^^^^^^^^^
Reads a file or string holding a Symbolic Workflow and instantiate a WorkFlow with its data.

json_to_data_tree
^^^^^^^^^^^^^^^^^
Reads a json file or string to a DataTree

mechanical_csv_to_field
^^^^^^^^^^^^^^^^^^^^^^^
Reads mechanical exported csv file

migrate_file_to_vtk
^^^^^^^^^^^^^^^^^^^
Take an input data sources or streams and convert as much data as possible to vtk.

migrate_to_vtu
^^^^^^^^^^^^^^
Extract all results from a datasources and exports them into vtu format. All the connected inputs are forwarded to the result providers operators.

serialize_to_hdf5
^^^^^^^^^^^^^^^^^
Serialize the inputs in an hdf5 format.

txt_to_data_tree
^^^^^^^^^^^^^^^^
Reads a txt file or string to a DataTree

vtk_export
^^^^^^^^^^
Write the input field and fields container into a given vtk path

vtk_to_fields
^^^^^^^^^^^^^
Write a field based on a vtk file.

vtu_export
^^^^^^^^^^
Export DPF data into vtu format.

utility
~~~~~~~
hdf5dpf_custom_read
^^^^^^^^^^^^^^^^^^^
Extract a custom result from an hdf5dpf file.

strain_from_voigt
^^^^^^^^^^^^^^^^^
Put strain field from Voigt notation to standard format.

