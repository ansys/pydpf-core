"""This module stores the raw html docstrings from DPF

TODO: These should probably be dynamically extracted from DPF when
run, but if the server doesn't have write permission, or is remote,
this html won't be acessable from the python client.  The gRPC server
needs to be able to stream these results to the client.

"""
DPF_HTML_OPERATOR_DOCS = {}

DPF_HTML_OPERATOR_DOCS['mapper'] = """
<li><b>Operator: mapper</b></li>
<ul>
<li>Description:</li>
<ul>Take a field or a field container and apply a Mapping object on it</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  field/fieldsContainer </li>
<li> Pin 1:  Mapping </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0:  field/fieldsContainer </li>
</ol>
</ol>
<ol>
<li>
"""

DPF_HTML_OPERATOR_DOCS['meshed_skin_sector_triangle'] = """
<li><b>Operator: meshed_skin_sector_triangle</b></li>
<ul>
<li>Description:</li>
<ul>Get sector meshed skin in triangles for primary nodes.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  mesh sector </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mesh region </li>
<li> Pin 1: mesh scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['meshed_external_layer_sector'] = """
<li><b>Operator: meshed_external_layer_sector</b></li>
<ul>
<li>Description:</li>
<ul>Get sector meshed skin.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  mesh sector </li>
</ol>
<li>Outputs:</li>
<ol>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['meshCut'] = """
<li><b>Operator: meshCut</b></li>
<ul>
<li>Description:</li>
<ul>Cut a mesh with the field (pin 0) based on the iso value (pin 1), the output mesh can be closed or not based on the parameter in pin 2 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: double scalar, iso value </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mesh </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['vtk::vtk::FieldProvider'] = """
<li><b>Operator: vtk::vtk::FieldProvider</b></li>
<ul>
<li>Description:</li>
<ul>get field requested from vtk file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['sum_contributions'] = """
<li><b>Operator: sum_contributions</b></li>
<ul>
<li>Description:</li>
<ul>Add force contributions.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['time_scoping_manipulation'] = """
<li><b>Operator: time_scoping_manipulation</b></li>
<ul>
<li>Description:</li>
<ul>Test if input value (pin 0) exists, if yes then return it, else return default value (pin 1)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: int </li>
<li> Pin 1: int </li>
<li> Pin 2: TimeFreqSupport </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: value </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_scoping_adapter'] = """
<li><b>Operator: cyclic_scoping_adapter</b></li>
<ul>
<li>Description:</li>
<ul>Adapt a mesh scoping with the correspondind high/low ids.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  mapScopingLowHigh </li>
<li> Pin 1: meshScoping </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: meshScoping </li>
<li> Pin 0: sizeScopingInit </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion_analytic_max_disp'] = """
<li><b>Operator: cyclic_expansion_analytic_max_disp</b></li>
<ul>
<li>Description:</li>
<ul>Expand cyclic results from a stream for a given set and given sector (optionals).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
<li> Pin 7: set to expand vector<dp_int> (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion_mesh'] = """
<li><b>Operator: cyclic_expansion_mesh</b></li>
<ul>
<li>Description:</li>
<ul>Expand a mesh of a sector.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: MeshRegion </li>
<li> Pin 1: number of sectors </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: MeshRegion </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion_field'] = """
<li><b>Operator: cyclic_expansion_field</b></li>
<ul>
<li>Description:</li>
<ul>Expand cyclic results from a stream for a given set and given sector (optionals).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: field a </li>
<li> Pin 1: field b </li>
<li> Pin 2: cyclicSupport </li>
<li> Pin 3: harmonic index int </li>
<li> Pin 4: scoping tot for computation </li>
<li> Pin 5: size scoping out </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['read_high_low_scoping_cyclic'] = """
<li><b>Operator: read_high_low_scoping_cyclic</b></li>
<ul>
<li>Description:</li>
<ul>Read the .dat to get high and low scoping for cyclic symmetry.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: file path </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Scoping_high </li>
<li> Pin 1: Scoping_low </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['PRNS_Reader'] = """
<li><b>Operator: PRNS_Reader</b></li>
<ul>
<li>Description:</li>
<ul>Read the presol of nodal field generated file from mapdl</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: file path </li>
<li> Pin 0: column not taken </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['PRES_Reader'] = """
<li><b>Operator: PRES_Reader</b></li>
<ul>
<li>Description:</li>
<ul>read the presol generated file from mapdl</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: file path </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion'] = """
<li><b>Operator: cyclic_expansion</b></li>
<ul>
<li>Description:</li>
<ul>Expand cyclic results from a stream for a given set, sector and scoping (optionals).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int>(optional) </li>
<li> Pin 1: mesh entities scoping(optional) </li>
<li> Pin 2: phi angle(optional) </li>
<li> Pin 3: vect of sectors to expand(optional) </li>
<li> Pin 4: FCa </li>
<li> Pin 5: FCb </li>
<li> Pin 6: LowHighScopingMap  (optional for ElementalNodal) </li>
<li> Pin 7: sizeScopingOut (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::available_materials'] = """
<li><b>Operator: mapdl::rst::available_materials</b></li>
<ul>
<li>Description:</li>
<ul>Read a result file to get available materials ids and properties.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: Stream </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Materials </li>
<li> Pin 1: scoping of available ids </li>
<li> Pin 1: vector of string if available properties </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::MaterialsProvider'] = """
<li><b>Operator: mapdl::rst::MaterialsProvider</b></li>
<ul>
<li>Description:</li>
<ul>read materials from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: materials </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::SelectionProvider'] = """
<li><b>Operator: mapdl::rst::SelectionProvider</b></li>
<ul>
<li>Description:</li>
<ul>read a mesh from the rst file, default (pin 10) for element is to check and cure degenerated elements
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mapOfSelection </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::MeshSelectionManagerProvider'] = """
<li><b>Operator: mapdl::rst::MeshSelectionManagerProvider</b></li>
<ul>
<li>Description:</li>
<ul>Build selection tool from the rst file, this allows selection operations (ex: create a selection of shell/solid elements, elements of a given material, given type, ...)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Mesh Selection Manager </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::TimeFreqSupportProvider'] = """
<li><b>Operator: mapdl::rst::TimeFreqSupportProvider</b></li>
<ul>
<li>Description:</li>
<ul>read time/freq support from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Time/Freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::MeshProvider'] = """
<li><b>Operator: mapdl::rst::MeshProvider</b></li>
<ul>
<li>Description:</li>
<ul>read a mesh from the rst file, default (pin 10) for element is to check and cure degenerated elements
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
<li> Pin 10: bool </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Mesh Region </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::ResultInfoProvider'] = """
<li><b>Operator: mapdl::rdsp::ResultInfoProvider</b></li>
<ul>
<li>Description:</li>
<ul>read result info from the rdsp file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::ResultInfoProvider'] = """
<li><b>Operator: mapdl::rfrq::ResultInfoProvider</b></li>
<ul>
<li>Description:</li>
<ul>read result info from the rfrq file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::dsub::TimeFreqSupportProvider'] = """
<li><b>Operator: mapdl::dsub::TimeFreqSupportProvider</b></li>
<ul>
<li>Description:</li>
<ul>read time/freq support from the dsub file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Time/Freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::TimeFreqSupportProvider'] = """
<li><b>Operator: mapdl::rdsp::TimeFreqSupportProvider</b></li>
<ul>
<li>Description:</li>
<ul>read time/freq support from the rdsp file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Time/Freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::F'] = """
<li><b>Operator: mapdl::rdsp::F</b></li>
<ul>
<li>Description:</li>
<ul>Compute nodal reaction sum from rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fields container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::F'] = """
<li><b>Operator: mapdl::rfrq::F</b></li>
<ul>
<li>Description:</li>
<ul>Compute nodal reaction sum from rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fields container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::cms::U'] = """
<li><b>Operator: mapdl::cms::U</b></li>
<ul>
<li>Description:</li>
<ul>CMS nodal expansion</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::cms::EPEL'] = """
<li><b>Operator: mapdl::cms::EPEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::cms::S'] = """
<li><b>Operator: mapdl::cms::S</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup stress expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::dsub::U'] = """
<li><b>Operator: mapdl::dsub::U</b></li>
<ul>
<li>Description:</li>
<ul>CMS nodal expansion</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::dsub::EEL'] = """
<li><b>Operator: mapdl::dsub::EEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::dsub::EPEL'] = """
<li><b>Operator: mapdl::dsub::EPEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::dsub::S'] = """
<li><b>Operator: mapdl::dsub::S</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup stress expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::A'] = """
<li><b>Operator: mapdl::rdsp::A</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup displacement expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::EEL'] = """
<li><b>Operator: mapdl::rfrq::EEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::EPEL'] = """
<li><b>Operator: mapdl::rfrq::EPEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::S'] = """
<li><b>Operator: mapdl::rfrq::S</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup stress expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['NMISC'] = """
<li><b>Operator: NMISC</b></li>
<ul>
<li>Description:</li>
<ul>Read NMISC results from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: Element mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fields container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 10: int  index of requested item  </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::TF'] = """
<li><b>Operator: mapdl::rth::TF</b></li>
<ul>
<li>Description:</li>
<ul>Read the elemental-nodal heat flux field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::TG'] = """
<li><b>Operator: mapdl::rth::TG</b></li>
<ul>
<li>Description:</li>
<ul>Read the elemental-nodal temperature gradient field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::EF'] = """
<li><b>Operator: mapdl::rth::EF</b></li>
<ul>
<li>Description:</li>
<ul>Read the elemental-nodal electric field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::VOLT'] = """
<li><b>Operator: mapdl::rth::VOLT</b></li>
<ul>
<li>Description:</li>
<ul>Read the nodal electric potential field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::TEMP'] = """
<li><b>Operator: mapdl::rth::TEMP</b></li>
<ul>
<li>Description:</li>
<ul>Read the nodal temperature field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::rst_corner_node_mapper_provider'] = """
<li><b>Operator: mapdl::rst::rst_corner_node_mapper_provider</b></li>
<ul>
<li>Description:</li>
<ul>Take a rst file/stream and provide a FieldMapping for corner nodes.</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: RstFile/Stream </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldMapping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::MaterialPropertyOfElement'] = """
<li><b>Operator: mapdl::rst::MaterialPropertyOfElement</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::U'] = """
<li><b>Operator: mapdl::rfrq::U</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup displacement expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_KE'] = """
<li><b>Operator: mapdl::rst::ENG_KE</b></li>
<ul>
<li>Description:</li>
<ul>Read kinetic energy form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_AHO'] = """
<li><b>Operator: mapdl::rst::ENG_AHO</b></li>
<ul>
<li>Description:</li>
<ul>Read artificial hourglass energy form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_SE'] = """
<li><b>Operator: mapdl::rst::ENG_SE</b></li>
<ul>
<li>Description:</li>
<ul>Read element energy associated with the stiffness matrix form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_FRES'] = """
<li><b>Operator: mapdl::rst::ECT_FRES</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Actual applied fluid penetration pressure form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_GAP'] = """
<li><b>Operator: mapdl::rst::ECT_GAP</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact gap distance form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['vtk::vtk::ResultInfoProvider'] = """
<li><b>Operator: vtk::vtk::ResultInfoProvider</b></li>
<ul>
<li>Description:</li>
<ul>read result info from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_SLIDE'] = """
<li><b>Operator: mapdl::rst::ECT_SLIDE</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact sliding distance form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_STOT'] = """
<li><b>Operator: mapdl::rst::ECT_STOT</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact total stress (pressure plus friction) form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::boundary_conditions'] = """
<li><b>Operator: mapdl::rst::boundary_conditions</b></li>
<ul>
<li>Description:</li>
<ul>return boundary conditions of a given load step
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
<li> Pin 5: vector<int> selected dofs </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldContainers/Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_SFRIC'] = """
<li><b>Operator: mapdl::rst::ECT_SFRIC</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact friction stress form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_PENE'] = """
<li><b>Operator: mapdl::rst::ECT_PENE</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact penetration form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELYZ'] = """
<li><b>Operator: EPELYZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YZ component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ETH'] = """
<li><b>Operator: mapdl::rst::ETH</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal component thermal strains form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_AHO'] = """
<li><b>Operator: ENG_AHO</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute artificial hourglass energy</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['elemental_to_nodal_fc'] = """
<li><b>Operator: elemental_to_nodal_fc</b></li>
<ul>
<li>Description:</li>
<ul>Transform Elemental fields into Nodal fields using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_VOL'] = """
<li><b>Operator: ENG_VOL</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute element volume</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_CREQ'] = """
<li><b>Operator: ENL_CREQ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal accumulated equivalent creep strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::BFE'] = """
<li><b>Operator: mapdl::rst::BFE</b></li>
<ul>
<li>Description:</li>
<ul>Read Element structural nodal temperatures form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_GAP'] = """
<li><b>Operator: ECT_GAP</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact gap distance</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['sqr'] = """
<li><b>Operator: sqr</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise field1^2.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_KE'] = """
<li><b>Operator: ENG_KE</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute kinetic energy</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['modulus'] = """
<li><b>Operator: modulus</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise modulus of field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['MeshSelectionManagerProvider'] = """
<li><b>Operator: MeshSelectionManagerProvider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and read the mesh selection manager support </ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: time freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_SLIDE'] = """
<li><b>Operator: ECT_SLIDE</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact sliding distance</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['dot_tensor'] = """
<li><b>Operator: dot_tensor</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise dot product between two tensor fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_PRES'] = """
<li><b>Operator: ECT_PRES</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact pressure</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['elemental_nodal_To_nodal'] = """
<li><b>Operator: elemental_nodal_To_nodal</b></li>
<ul>
<li>Description:</li>
<ul>Transform ElementalNodal field into Nodal field using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_PLWK'] = """
<li><b>Operator: ENL_PLWK</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal plastic strain energy density</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_TH'] = """
<li><b>Operator: ENG_TH</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute thermal dissipation energy</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_SEPL'] = """
<li><b>Operator: ENL_SEPL</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal equivalent stress parameter</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPL'] = """
<li><b>Operator: EPPL</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal component plastic  strains</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['kronecker_prod'] = """
<li><b>Operator: kronecker_prod</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise Kronecker product between two tensor fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::EPPL'] = """
<li><b>Operator: mapdl::rst::EPPL</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal component plastic  strains form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_CNOS'] = """
<li><b>Operator: ECT_CNOS</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Total number of contact status changes during substep</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['BFE'] = """
<li><b>Operator: BFE</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element structural nodal temperatures</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['Average'] = """
<li><b>Operator: Average</b></li>
<ul>
<li>Description:</li>
<ul>Aggregate a field (in 0) by computing its average value
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: ScalarQuantity </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['field_to_csv'] = """
<li><b>Operator: field_to_csv</b></li>
<ul>
<li>Description:</li>
<ul>transform field to a csv file</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: field </li>
<li> Pin 1:  file path </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['multiply'] = """
<li><b>Operator: multiply</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise multiplication between two field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['vtk_export'] = """
<li><b>Operator: vtk_export</b></li>
<ul>
<li>Description:</li>
<ul>write the input fields to a vtk file, it supposes that the mesh support is the same for all the fields 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: string file path </li>
<li> Pin 1: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: can not be linked to a down stream operator </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TimeFreqSupportProvider'] = """
<li><b>Operator: TimeFreqSupportProvider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read The time/freq support </ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: time freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['csv_to_field'] = """
<li><b>Operator: csv_to_field</b></li>
<ul>
<li>Description:</li>
<ul>transform csv file to a field or fields container</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['entity_average_fc'] = """
<li><b>Operator: entity_average_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the average of a multi-entity container of fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['entity_average'] = """
<li><b>Operator: entity_average</b></li>
<ul>
<li>Description:</li>
<ul>Computes the average of a multi-entity fields, (ElementalNodal -> Elemental), (NodalElemental -> Nodal).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['invert'] = """
<li><b>Operator: invert</b></li>
<ul>
<li>Description:</li>
<ul>Compute the element-wise, component-wise, inverse of a field (1./x) 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['UY'] = """
<li><b>Operator: UY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Y  displacements</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['normals_provider'] = """
<li><b>Operator: normals_provider</b></li>
<ul>
<li>Description:</li>
<ul>compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements) 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  mesh Region (optional, if input 2 is a field) </li>
<li> Pin 1:  scoping (optional, if input 2 is a field) </li>
<li> Pin 2:  field (optional, if input 0 and input 1 are connected) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_ELENG'] = """
<li><b>Operator: ENL_ELENG</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal elastic strain energy density</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::EPEL'] = """
<li><b>Operator: mapdl::rdsp::EPEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['DerivableInput'] = """
<li><b>Operator: DerivableInput</b></li>
<ul>
<li>Description:</li>
<ul>Defines an input (in 0) with a symbol (in 1), and its derivatives (in 2). When queried for a derivative, it returns the one corresponding to a given symbol (in 3).</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: String </li>
<li> Pin 2: map<String, Operator>/CField </li>
<li> Pin 3: String </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['strain_from_voigt'] = """
<li><b>Operator: strain_from_voigt</b></li>
<ul>
<li>Description:</li>
<ul>Put strain field from Voigt notation to standard format
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_STOT'] = """
<li><b>Operator: ECT_STOT</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact total stress (pressure plus friction)</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_HPRES'] = """
<li><b>Operator: ENL_HPRES</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal hydrostatic pressure</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::EPEL'] = """
<li><b>Operator: mapdl::rst::EPEL</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal component elastic strains form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['accumulate'] = """
<li><b>Operator: accumulate</b></li>
<ul>
<li>Description:</li>
<ul>Sum all the elementary data of a field to get one elementary data at the end.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field (optional) ponderation </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['vtk::vtk::MeshProvider'] = """
<li><b>Operator: vtk::vtk::MeshProvider</b></li>
<ul>
<li>Description:</li>
<ul>Create vtk streams based on a given data sources 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mesh region </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::U'] = """
<li><b>Operator: mapdl::rdsp::U</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup displacement expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['component_selector_fc'] = """
<li><b>Operator: component_selector_fc</b></li>
<ul>
<li>Description:</li>
<ul>Create a scalar fields based on the selected component
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: index </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_PSV'] = """
<li><b>Operator: mapdl::rst::ENL_PSV</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal plastic state variable form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion_analytic_max_seqv'] = """
<li><b>Operator: cyclic_expansion_analytic_max_seqv</b></li>
<ul>
<li>Description:</li>
<ul>Expand cyclic results from a stream for a given set and given sector (optionals).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
<li> Pin 7: set to expand vector<dp_int> (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_FLUX'] = """
<li><b>Operator: mapdl::rst::ECT_FLUX</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Total heat flux at contact surface form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['default_value'] = """
<li><b>Operator: default_value</b></li>
<ul>
<li>Description:</li>
<ul>Test if input value (pin 0) exists, if yes then return it, else return default value (pin 1)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: value(optional) </li>
<li> Pin 1: default value </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: value </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['norm'] = """
<li><b>Operator: norm</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise L2 norm of the field elementary data.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['InjectToFieldContainer'] = """
<li><b>Operator: InjectToFieldContainer</b></li>
<ul>
<li>Description:</li>
<ul>Create a field container from a field
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['VX'] = """
<li><b>Operator: VX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal X velocities</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::UTOT'] = """
<li><b>Operator: mapdl::rst::UTOT</b></li>
<ul>
<li>Description:</li>
<ul>read the raw U vector from rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cplx_divide'] = """
<li><b>Operator: cplx_divide</b></li>
<ul>
<li>Description:</li>
<ul>Computes division between two field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AreFieldsIdentical'] = """
<li><b>Operator: AreFieldsIdentical</b></li>
<ul>
<li>Description:</li>
<ul>check if two fields are identical
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: double scalar(small value, less then this value is considred as null) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: bool (true if identical...) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::RFTOT'] = """
<li><b>Operator: mapdl::rst::RFTOT</b></li>
<ul>
<li>Description:</li>
<ul>read the raw RF vector from rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['dot'] = """
<li><b>Operator: dot</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise dot product between two vector fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['CplxOp'] = """
<li><b>Operator: CplxOp</b></li>
<ul>
<li>Description:</li>
<ul>Computes aXY + bZ where a,b (in 0, in 3) are scalar and X,Y,Z (in 1,2,4) are complex numbers .
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Double </li>
<li> Pin 1: FieldsContainer </li>
<li> Pin 2: FieldsContainer </li>
<li> Pin 3: Double </li>
<li> Pin 4: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['A'] = """
<li><b>Operator: A</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal accelerations</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_INC'] = """
<li><b>Operator: ENG_INC</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute incremental energy (magnetics)</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_SE'] = """
<li><b>Operator: ENG_SE</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute element energy associated with the stiffness matrix</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::stream_provider'] = """
<li><b>Operator: mapdl::stream_provider</b></li>
<ul>
<li>Description:</li>
<ul>Create mapdl streams based on a given data sources 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Streams </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['VZ'] = """
<li><b>Operator: VZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Z velocities</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::A'] = """
<li><b>Operator: mapdl::rfrq::A</b></li>
<ul>
<li>Description:</li>
<ul>Computes harmonic acceleration
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cos'] = """
<li><b>Operator: cos</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise cos(field1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['sqrt'] = """
<li><b>Operator: sqrt</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise sqrt(field1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['centroid'] = """
<li><b>Operator: centroid</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['RF'] = """
<li><b>Operator: RF</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal reaction forces</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['RegularizedMaximum'] = """
<li><b>Operator: RegularizedMaximum</b></li>
<ul>
<li>Description:</li>
<ul>Aggregate a field (in 0) by computing its regularized maximum value
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: ScalarQuantity </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SumAgg'] = """
<li><b>Operator: SumAgg</b></li>
<ul>
<li>Description:</li>
<ul>Aggregate a field (in 0) by computing its sum
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: ScalarQuantity </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['BindSupport'] = """
<li><b>Operator: BindSupport</b></li>
<ul>
<li>Description:</li>
<ul>Tie a support to a field
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Mesh </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENG_CO'] = """
<li><b>Operator: ENG_CO</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute co-energy (magnetics)</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['unit_convert'] = """
<li><b>Operator: unit_convert</b></li>
<ul>
<li>Description:</li>
<ul>Convert an input field of a given unit to another unit.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: String Unit </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ExtractFromFC'] = """
<li><b>Operator: ExtractFromFC</b></li>
<ul>
<li>Description:</li>
<ul>Extract the fields at the indeces defined in the vector (in 1) form the fields container (in:0) 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['GetSupportFromField'] = """
<li><b>Operator: GetSupportFromField</b></li>
<ul>
<li>Description:</li>
<ul>Extract a field that corresponds to the nodal position of a given input mesh (in 0)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Mesh </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['scoping_provider_by_prop'] = """
<li><b>Operator: scoping_provider_by_prop</b></li>
<ul>
<li>Description:</li>
<ul>provides a scoping at a given location based on a given property name and a property number 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: String location </li>
<li> Pin 1: String property Name </li>
<li> Pin 2: Int scalar property number </li>
<li> Pin 4:  Datasources </li>
<li> Pin 5:  Int inclusive //Optional </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['Buffer'] = """
<li><b>Operator: Buffer</b></li>
<ul>
<li>Description:</li>
<ul>Take a Field (in 0) and a scoping (in 1) and rescope the field on the given scoping. If an id does not exists in the orginal field, default value (in 2) is used if defined.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping </li>
<li> Pin 3: vectorOfDouble (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['elemental_nodal_To_nodal_fc'] = """
<li><b>Operator: elemental_nodal_To_nodal_fc</b></li>
<ul>
<li>Description:</li>
<ul>Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['BindSupportFC'] = """
<li><b>Operator: BindSupportFC</b></li>
<ul>
<li>Description:</li>
<ul>Tie a support to a field
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: Mesh </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_PRES'] = """
<li><b>Operator: mapdl::rst::ECT_PRES</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact pressure form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['RigidTransformationProvider'] = """
<li><b>Operator: RigidTransformationProvider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and rigid transformations</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: streams </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['minus'] = """
<li><b>Operator: minus</b></li>
<ul>
<li>Description:</li>
<ul>Computes the difference of two fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLXZ'] = """
<li><b>Operator: EPPLXZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XZ component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['div'] = """
<li><b>Operator: div</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise division between two fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_CNOS'] = """
<li><b>Operator: mapdl::rst::ECT_CNOS</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Total number of contact status changes during substep form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cplx_dot'] = """
<li><b>Operator: cplx_dot</b></li>
<ul>
<li>Description:</li>
<ul>Computes product between two field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['selector_fc'] = """
<li><b>Operator: selector_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['rotate'] = """
<li><b>Operator: rotate</b></li>
<ul>
<li>Description:</li>
<ul>Apply a transformation matrix (in 1 (3-3 rotation matrix)) on an input vector/tensor field (in 0).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['amplitude'] = """
<li><b>Operator: amplitude</b></li>
<ul>
<li>Description:</li>
<ul>Computes amplitude of a real and an imaginary field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['add'] = """
<li><b>Operator: add</b></li>
<ul>
<li>Description:</li>
<ul>Computes the sum of two fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_CO'] = """
<li><b>Operator: mapdl::rst::ENG_CO</b></li>
<ul>
<li>Description:</li>
<ul>Read co-energy (magnetics) form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['U'] = """
<li><b>Operator: U</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal displacements</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ScopingAdapter'] = """
<li><b>Operator: ScopingAdapter</b></li>
<ul>
<li>Description:</li>
<ul>Convert a standard DPF Scoping to a mapped scoping.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Scoping </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AccumulatorOverDomains'] = """
<li><b>Operator: AccumulatorOverDomains</b></li>
<ul>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SZ'] = """
<li><b>Operator: SZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal ZZ component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['invariants_fc'] = """
<li><b>Operator: invariants_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise princpal stresses of each tensor field of a container, returns in this order: the maximum value, the middle value and the minimum value.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
<li> Pin 2: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_PENE'] = """
<li><b>Operator: ECT_PENE</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact penetration</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['Are_fields_included'] = """
<li><b>Operator: Are_fields_included</b></li>
<ul>
<li>Description:</li>
<ul>check if one field belongs to another.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: double scalar(small value, less then this value is considred as null) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: bool (true if belongs...) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_SRAT'] = """
<li><b>Operator: ENL_SRAT</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal stress ratio</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AreFieldsIdentical_fc'] = """
<li><b>Operator: AreFieldsIdentical_fc</b></li>
<ul>
<li>Description:</li>
<ul>check if two fields container are identical
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FC </li>
<li> Pin 1: FC </li>
<li> Pin 3: double scalar(small value, less then this value is considred as null) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: bool (true if identical...) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['chunk_fc'] = """
<li><b>Operator: chunk_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['acmo_mesh_provider'] = """
<li><b>Operator: acmo_mesh_provider</b></li>
<ul>
<li>Description:</li>
<ul>create a mesh controller (a collection of mesh regions correspending to the bodies)from an acmo mesh 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  assembly mesh </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mesh controller </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['meshed_skin_sector'] = """
<li><b>Operator: meshed_skin_sector</b></li>
<ul>
<li>Description:</li>
<ul>Get sector meshed skin.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0:  mesh sector </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: mesh region </li>
<li> Pin 1: mesh node scoping </li>
<li> Pin 0: map surface to element ids </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['scale'] = """
<li><b>Operator: scale</b></li>
<ul>
<li>Description:</li>
<ul>Scales a field by a constant factor.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Double/Field scoped on overall </li>
<li> Pin 2: bool(optional, default false) if set to true, output of scale is mane dimensionless. </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['Pow'] = """
<li><b>Operator: Pow</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise field1^p.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: double </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cplx_add'] = """
<li><b>Operator: cplx_add</b></li>
<ul>
<li>Description:</li>
<ul>Computes addition between two field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cplx_derive'] = """
<li><b>Operator: cplx_derive</b></li>
<ul>
<li>Description:</li>
<ul>Derive field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TF'] = """
<li><b>Operator: TF</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Heat flux</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['unit_convert_fc'] = """
<li><b>Operator: unit_convert_fc</b></li>
<ul>
<li>Description:</li>
<ul>Convert an input fields container of a given unit to another unit.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: String Unit </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['min_max_fc'] = """
<li><b>Operator: min_max_fc</b></li>
<ul>
<li>Description:</li>
<ul>Compute the component-wise minimum (out 0) and maximum (out 1) over a fields container.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field (min) </li>
<li> Pin 1: Field (max) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['sweeping_phase'] = """
<li><b>Operator: sweeping_phase</b></li>
<ul>
<li>Description:</li>
<ul>Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fie	lds container containing only one field </li>
<li> Pin 2: Double </li>
<li> Pin 3: String Unit </li>
<li> Pin 4: Boolean Absolute </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['make_unit'] = """
<li><b>Operator: make_unit</b></li>
<ul>
<li>Description:</li>
<ul>Take a field and returns its unit equivalent
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['generalized_inner_product'] = """
<li><b>Operator: generalized_inner_product</b></li>
<ul>
<li>Description:</li>
<ul>Computes a general notion of inner product between two fields of possibly different dimensionality.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['norm_fc'] = """
<li><b>Operator: norm_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise L2 norm of  the fields elementary data.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::available_results'] = """
<li><b>Operator: mapdl::rst::available_results</b></li>
<ul>
<li>Description:</li>
<ul>Read a result file to get the result infos with the available operators.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: Stream </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: ResultInfo </li>
<li> Pin 1: vector of available operators </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['VolumeForce'] = """
<li><b>Operator: VolumeForce</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mechanical_csv_to_field'] = """
<li><b>Operator: mechanical_csv_to_field</b></li>
<ul>
<li>Description:</li>
<ul>transform csv file to a field</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: unit </li>
<li> Pin 1: mesh </li>
<li> Pin 4: dataSources </li>
<li> Pin 9: location </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['scale_by_field'] = """
<li><b>Operator: scale_by_field</b></li>
<ul>
<li>Description:</li>
<ul>Scales a field (in 0) by a scalar field (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
<li> Pin 1: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENF'] = """
<li><b>Operator: ENF</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal forces form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['GetElementScopingFromMesh'] = """
<li><b>Operator: GetElementScopingFromMesh</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::V'] = """
<li><b>Operator: mapdl::rfrq::V</b></li>
<ul>
<li>Description:</li>
<ul>Computes harmonic velocity
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ResultInfoProvider'] = """
<li><b>Operator: ResultInfoProvider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and get result infos</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['fieldify'] = """
<li><b>Operator: fieldify</b></li>
<ul>
<li>Description:</li>
<ul>take a double or a vector of double and transform it in a field
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: double/vector<double> </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_PSV'] = """
<li><b>Operator: ENL_PSV</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal plastic state variable</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::cms::EEL'] = """
<li><b>Operator: mapdl::cms::EEL</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup strain expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_FRES'] = """
<li><b>Operator: ECT_FRES</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Actual applied fluid penetration pressure</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['img_part'] = """
<li><b>Operator: img_part</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise imaginary part of field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['Rescope'] = """
<li><b>Operator: Rescope</b></li>
<ul>
<li>Description:</li>
<ul>Take a Field (in 0) and a scoping (in 1) and rescope the field on the given scoping. If an id does not exists in the orginal field, default value (in 2) is used if defined.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping </li>
<li> Pin 3: vectorOfDouble (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['V'] = """
<li><b>Operator: V</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal velocities</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPEL'] = """
<li><b>Operator: EPEL</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal component elastic strains</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['UX'] = """
<li><b>Operator: UX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal X displacements</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ECT_STAT'] = """
<li><b>Operator: mapdl::rst::ECT_STAT</b></li>
<ul>
<li>Description:</li>
<ul>Read Element Contact status form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ETH'] = """
<li><b>Operator: ETH</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal component thermal strains</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['UZ'] = """
<li><b>Operator: UZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Z displacements</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['VY'] = """
<li><b>Operator: VY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Y  velocities</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_VOL'] = """
<li><b>Operator: mapdl::rst::ENG_VOL</b></li>
<ul>
<li>Description:</li>
<ul>Read element volume form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AX'] = """
<li><b>Operator: AX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal X acceleration</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['realP_part'] = """
<li><b>Operator: realP_part</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise real part of field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::RF'] = """
<li><b>Operator: mapdl::rst::RF</b></li>
<ul>
<li>Description:</li>
<ul>Read nodal reaction forces from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TFX'] = """
<li><b>Operator: TFX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute elemental nodal X heat flux</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SY'] = """
<li><b>Operator: SY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YY component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TFY'] = """
<li><b>Operator: TFY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute elemental nodal Y  heat flux</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELY'] = """
<li><b>Operator: EPELY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YY component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TFZ'] = """
<li><b>Operator: TFZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute elemental nodal Z heat flux</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SX'] = """
<li><b>Operator: SX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XX component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SXZ'] = """
<li><b>Operator: SXZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XZ component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_STAT'] = """
<li><b>Operator: ECT_STAT</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact status</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELX'] = """
<li><b>Operator: EPELX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XX component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['html_doc'] = """
<li><b>Operator: html_doc</b></li>
<ul>
<li>Description:</li>
<ul>Generates html doc :)</ul>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELZ'] = """
<li><b>Operator: EPELZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal ZZ component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_FLUX'] = """
<li><b>Operator: ECT_FLUX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Total heat flux at contact surface</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELXY'] = """
<li><b>Operator: EPELXY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XY component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::create_recursive_scopings'] = """
<li><b>Operator: mapdl::create_recursive_scopings</b></li>
<ul>
<li>Description:</li>
<ul>create a recursive scoping from recursive streams</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3:  streams </li>
<li> Pin 7:  meshController </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: ScopingsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLX'] = """
<li><b>Operator: EPPLX</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XX component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLY'] = """
<li><b>Operator: EPPLY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YY component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_TH'] = """
<li><b>Operator: mapdl::rst::ENG_TH</b></li>
<ul>
<li>Description:</li>
<ul>Read thermal dissipation energy form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['eqv_fc'] = """
<li><b>Operator: eqv_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise Von-Mises criteria for each tensor in the fields of the field container.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLXY'] = """
<li><b>Operator: EPPLXY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XY component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::V'] = """
<li><b>Operator: mapdl::rdsp::V</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup displacement expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['S1'] = """
<li><b>Operator: S1</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Principal stresses 1</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['S'] = """
<li><b>Operator: S</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SYZ'] = """
<li><b>Operator: SYZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YZ component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLYZ'] = """
<li><b>Operator: EPPLYZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal YZ component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['transpose_scoping'] = """
<li><b>Operator: transpose_scoping</b></li>
<ul>
<li>Description:</li>
<ul>transposes the input scopint (Elemental --> Nodal, or Nodal ---> Elemental), based on the input mesh region  
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: scoping </li>
<li> Pin 1: mesh region </li>
<li> Pin 2:  Int inclusive //Optional </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['S3'] = """
<li><b>Operator: S3</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Principal stresses 3</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['sin'] = """
<li><b>Operator: sin</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise sin(field1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field/or fields container containing only one field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['stream_provider'] = """
<li><b>Operator: stream_provider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate stream_provider based on the data sources</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: CDPFStreams </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPPLZ'] = """
<li><b>Operator: EPPLZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal ZZ component plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['conjugate'] = """
<li><b>Operator: conjugate</b></li>
<ul>
<li>Description:</li>
<ul>Computes element-wise conjugate of field containers containing complex fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['serializer'] = """
<li><b>Operator: serializer</b></li>
<ul>
<li>Description:</li>
<ul>Take any input and serialize them as file.
</ul>
<li>Inputs:</li>
<ol>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: file </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['deserializer'] = """
<li><b>Operator: deserializer</b></li>
<ul>
<li>Description:</li>
<ul>Take any input and serialize them as file.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: fileany output </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['eig_vectors_fc'] = """
<li><b>Operator: eig_vectors_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise eigen vecors for each tensor in the fields of the field container.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['text_parser'] = """
<li><b>Operator: text_parser</b></li>
<ul>
<li>Description:</li>
<ul>Take an input string and parse it into dataProcessing type
</ul>
<li>Inputs:</li>
<ol>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rth::JC'] = """
<li><b>Operator: mapdl::rth::JC</b></li>
<ul>
<li>Description:</li>
<ul>Read the elemental-nodal current density field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['min_max_scalar_field_fc'] = """
<li><b>Operator: min_max_scalar_field_fc</b></li>
<ul>
<li>Description:</li>
<ul>Compute the minimum (out 0) and maximum (out 1) over a container of scalar fields.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['min_max'] = """
<li><b>Operator: min_max</b></li>
<ul>
<li>Description:</li>
<ul>Compute the component-wise minimum (out 0) and maximum (out 1) over a field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field (min) </li>
<li> Pin 1: Field (max) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['EPELXZ'] = """
<li><b>Operator: EPELXZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XZ component elastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['scoping_provider_by_ns'] = """
<li><b>Operator: scoping_provider_by_ns</b></li>
<ul>
<li>Description:</li>
<ul>provides a scoping at a given location based on a given named selection
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: String location </li>
<li> Pin 4:  Datasources </li>
<li> Pin 5:  Int inclusive //Optional </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ECT_SFRIC'] = """
<li><b>Operator: ECT_SFRIC</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element Contact friction stress</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['MinMaxOverDomains'] = """
<li><b>Operator: MinMaxOverDomains</b></li>
<ul>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['MinMaxOverDomainsIncremental'] = """
<li><b>Operator: MinMaxOverDomainsIncremental</b></li>
<ul>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_SRAT'] = """
<li><b>Operator: mapdl::rst::ENL_SRAT</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal stress ratio form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['prns'] = """
<li><b>Operator: prns</b></li>
<ul>
<li>Description:</li>
<ul>write a filed into a prns equivalent format
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Integer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['S2'] = """
<li><b>Operator: S2</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Principal stresses 2</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['CPRNSolBinOperator'] = """
<li><b>Operator: CPRNSolBinOperator</b></li>
<ul>
<li>Description:</li>
<ul>???
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: String Unit </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Integer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['component_selector'] = """
<li><b>Operator: component_selector</b></li>
<ul>
<li>Description:</li>
<ul>Create a scalar field based on the selected component
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: index </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AccumulatorLevelOverDomains'] = """
<li><b>Operator: AccumulatorLevelOverDomains</b></li>
<ul>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENG_INC'] = """
<li><b>Operator: mapdl::rst::ENG_INC</b></li>
<ul>
<li>Description:</li>
<ul>Read incremental energy (magnetics) form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ElementalNodal_To_NodalElemental'] = """
<li><b>Operator: ElementalNodal_To_NodalElemental</b></li>
<ul>
<li>Description:</li>
<ul>Transform ElementalNodal field to NodalElemental, compute result on a given node scoping.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['to_nodal_fc'] = """
<li><b>Operator: to_nodal_fc</b></li>
<ul>
<li>Description:</li>
<ul>Transform input fields into Nodal fields using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ElementalNodal_To_NodalElemental_fc'] = """
<li><b>Operator: ElementalNodal_To_NodalElemental_fc</b></li>
<ul>
<li>Description:</li>
<ul>Transform ElementalNodal fields to NodalElemental, compute result on a given node scoping.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: Scoping (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ResultInfoProvider'] = """
<li><b>Operator: mapdl::rst::ResultInfoProvider</b></li>
<ul>
<li>Description:</li>
<ul>read result info from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['elemental_to_nodal'] = """
<li><b>Operator: elemental_to_nodal</b></li>
<ul>
<li>Description:</li>
<ul>Transform Elemental field into Nodal field using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['cyclic_expansion_analytic_max_disp_norm'] = """
<li><b>Operator: cyclic_expansion_analytic_max_disp_norm</b></li>
<ul>
<li>Description:</li>
<ul>Expand cyclic results from a stream for a given set and given sector (optionals).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
<li> Pin 7: set to expand vector<dp_int> (optional) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rdsp::S'] = """
<li><b>Operator: mapdl::rdsp::S</b></li>
<ul>
<li>Description:</li>
<ul>Computes msup stress expansion
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['TEMP'] = """
<li><b>Operator: TEMP</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Temperature field</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_PLWK'] = """
<li><b>Operator: mapdl::rst::ENL_PLWK</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal plastic strain energy density form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['to_nodal'] = """
<li><b>Operator: to_nodal</b></li>
<ul>
<li>Description:</li>
<ul>Transform input field into Nodal field using an averaging process, result is computed on a given node scoping (in 1).
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Scoping  (optional Nodal scoping) </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mid_node_mapping_provider'] = """
<li><b>Operator: mid_node_mapping_provider</b></li>
<ul>
<li>Description:</li>
<ul>Provide a Mapping object that interpolate results at mid nodes</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Mesh </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Mapping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['invariants_deriv_fc'] = """
<li><b>Operator: invariants_deriv_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise invariants of each tensor field in the fields container, the invariants are: the stress intensity, the equivalent stress and the maximum shear stress.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer (stress intensity) </li>
<li> Pin 1: FieldsContainer (equivalent stress) </li>
<li> Pin 2: FieldsContainer (maximum shear stress) </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['eig_values'] = """
<li><b>Operator: eig_values</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise eigen values of a tensor field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::rst_file_mesh_information'] = """
<li><b>Operator: mapdl::rst::rst_file_mesh_information</b></li>
<ul>
<li>Description:</li>
<ul>Take an rst stream at input and provide a set of base informations about the model, element volume, nodal volume, elemental mass, nodal mass</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: RstFile/Stream </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AY'] = """
<li><b>Operator: AY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Y  acceleration</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['GetNodeScopingFromMesh'] = """
<li><b>Operator: GetNodeScopingFromMesh</b></li>
<ul>
<li>Description:</li>
<ul>Computes centroid of field1 and field2. fieldOut = fieldIn*(1.-fact)+Field2*(fact)
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 3: scalar </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['eqv'] = """
<li><b>Operator: eqv</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise Von-Mises criteria on a tensor field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_CRWK'] = """
<li><b>Operator: ENL_CRWK</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal creep strain energy density</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['invariants_deriv'] = """
<li><b>Operator: invariants_deriv</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise invariants of a tensor field, returns in this order: the stress intensity, the equivalent stress and the maximum shear stress.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 1: Field </li>
<li> Pin 2: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['eig_values_fc'] = """
<li><b>Operator: eig_values_fc</b></li>
<ul>
<li>Description:</li>
<ul>Computes the element-wise eigen values for each tensor in the fields of the field container.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['change_shellLayers'] = """
<li><b>Operator: change_shellLayers</b></li>
<ul>
<li>Description:</li>
<ul>Change number of layer for a shell field.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: EShellLayers </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['vtk::stream_provider'] = """
<li><b>Operator: vtk::stream_provider</b></li>
<ul>
<li>Description:</li>
<ul>Create vtk streams based on a given data sources 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 4: data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Streams </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['transform_cylindricalCS'] = """
<li><b>Operator: transform_cylindricalCS</b></li>
<ul>
<li>Description:</li>
<ul>Transform a field into local polar coordinates corresponding to the field position .
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Field </li>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::S'] = """
<li><b>Operator: mapdl::rst::S</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal component stresses form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ERP'] = """
<li><b>Operator: ERP</b></li>
<ul>
<li>Description:</li>
<ul>Compute the Equivalent Radiated Power (ERP) from a displacement field over time (in 0), on a mesh boundary (in 1) 
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: MeshBoundary </li>
<li> Pin 2: LoadStep </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['SXY'] = """
<li><b>Operator: SXY</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal XY component stresses</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ERPW'] = """
<li><b>Operator: ERPW</b></li>
<ul>
<li>Description:</li>
<ul>Compute the Equivalent Radiated Power (ERP) from a displacement field over time (in 0), on a mesh boundary (in 1) for multiple RPM conditions
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: FieldsContainer </li>
<li> Pin 1: MeshBoundary </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Field </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['MaterialsProvider'] = """
<li><b>Operator: MaterialsProvider</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and get result infos</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: result infos </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['MeshScopingProvider'] = """
<li><b>Operator: MeshScopingProvider</b></li>
<ul>
<li>Description:</li>
<ul>Take a mesh support and returns its nodes as a scoping.
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: MeshSupport </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Scoping </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::U'] = """
<li><b>Operator: mapdl::rst::U</b></li>
<ul>
<li>Description:</li>
<ul>read nodal displacments from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rfrq::TimeFreqSupportProvider'] = """
<li><b>Operator: mapdl::rfrq::TimeFreqSupportProvider</b></li>
<ul>
<li>Description:</li>
<ul>read time/freq support from the rfrq file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Time/Freq support </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::V'] = """
<li><b>Operator: mapdl::rst::V</b></li>
<ul>
<li>Description:</li>
<ul>read nodal velocity from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['AZ'] = """
<li><b>Operator: AZ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute nodal Z acceleration</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_HPRES'] = """
<li><b>Operator: mapdl::rst::ENL_HPRES</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal hydrostatic pressure form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::A'] = """
<li><b>Operator: mapdl::rst::A</b></li>
<ul>
<li>Description:</li>
<ul>read nodal acceleration from the rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['ENL_EPEQ'] = """
<li><b>Operator: ENL_EPEQ</b></li>
<ul>
<li>Description:</li>
<ul> Load the appropriate operator based on the data sources and Read/compute Element nodal accumulated equivalent plastic strain</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: streams (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_SEPL'] = """
<li><b>Operator: mapdl::rst::ENL_SEPL</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal equivalent stress parameter form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_EPEQ'] = """
<li><b>Operator: mapdl::rst::ENL_EPEQ</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal accumulated equivalent plastic strain form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_CREQ'] = """
<li><b>Operator: mapdl::rst::ENL_CREQ</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal accumulated equivalent creep strain form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['mapdl::rst::ENL_CRWK'] = """
<li><b>Operator: mapdl::rst::ENL_CRWK</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal creep strain energy density form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
<ol>
"""

DPF_HTML_OPERATOR_DOCS['<b>mapdl::rst::ENL_ELENG'] = """
<li><b>Operator: <b>mapdl::rst::ENL_ELENG</b></li>
<ul>
<li>Description:</li>
<ul>Read Element nodal elestic strain energy density form rst file
</ul>
<li>Inputs:</li>
<ol>
<li> Pin 0: Time scoping vector<int> </li>
<li> Pin 1: mesh entities scoping, unordered_map<int, int> id to index (optional) (index is optional, to be set if a user wants the results at a given order) </li>
<li> Pin 2: fileds container to update/create and set as output (optional) </li>
<li> Pin 3: stream (result file container) (optional) </li>
<li> Pin 4: dataSources // if stream is null then we need to get the file path from the data sources </li>
<li> Pin 5: boolean (optional) if false get the results in the solution CS </li>
</ol>
<li>Outputs:</li>
<ol>
<li> Pin 0: Fields container </li>
</ol>
</ol>
"""
