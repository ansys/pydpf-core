# How to use data containers

## Scoping

### Create a Scoping

The Scoping is a set of entity ids defined on a location (the location is optional).



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::Scoping my_scoping;
my_scoping.setLocation(ansys::dpf::locations::nodal);

// 1/ entity by entity
my_scoping.emplace(0, 1);
my_scoping.emplace(1, 2);
my_scoping.emplace(2, 3);
// 2/ or the entire vector of ids
std::vector<int> my_ids = { 1,2,3 };
my_scoping.setIds(my_ids);
// or
my_scoping.setIds(my_ids.data(), (int)my_ids.size());
```

### Get Scoping's data

The Scoping's location and ids can be accessed with:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::Location my_loc = my_scoping.location();
std::vector<int> my_ids_out;
my_scoping.getIds(my_ids_out);

int size = 0;
const int* ids = my_scoping.ids(size);

// or entity by entity
int id = my_scoping.idByIndex(0);
int index = my_scoping.indexById(1);
```

## Field

### Create a Field

The minimum requirement for a well defined Field is for it to have a dimensionality (scalar, 3 components vector, 6 components symmetrical matrix...), a location ("Nodal", "Elemental", "ElementalNodal", "Timefrq"...), a data vector and a scoping with ids. The user can also set the number of shell layers. If the field has one elementary data by entity (elementary data size = number of components for "Nodal" or "Elemental" field for example), then the data vector can be set directly. If a more complex field is required ("ElementalNodal" Field for example), the data can be set entity by entity.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

int num_entities = 2;

// for the most common dimensionalities
ansys::dpf::Field my_field(num_entities, { 1 }, ansys::dpf::locations::nodal); //nodal scalar
my_field = ansys::dpf::Field(num_entities, { 3 }, ansys::dpf::locations::elemental_nodal); //elemental nodal vector
my_field = ansys::dpf::Field(num_entities, { 3,3 }, ansys::dpf::locations::elemental); //elemental sym matrix

// 1/ fill the entire Scoping and data
std::vector<double> my_data = { 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 2.3, 1.0, 1.0, 0.0, 0.0, 1.0 };
my_field.scoping().setIds({ 5,22 });
my_field.setData(my_data);

// 2/ or fill entity by entity
my_field = ansys::dpf::Field(num_entities, { 3,3 }, ansys::dpf::locations::elemental); //elemental sym matrix
// sym matrix are defined by 6 components in the order XX, YY, ZZ, XY, YZ, XZ
std::vector<double> my_elem_data = { 1.0, 1.0, 1.0, 0.0, 0.0, 0.0 };
my_field.push_back(5, my_elem_data);

std::vector<double> my_elem_data2 = { 2.3, 1.0, 1.0, 0.0, 0.0, 1.0 };
my_field.push_back(22, my_elem_data2);

//optional, set the field's unit
ansys::dpf::FieldDefinition field_def = my_field.fieldDefinition();
field_def.setUnit(ansys::dpf::Unit("m"));
my_field.setFieldDefinition(field_def);
```

### Get Field's data

The Field's side information as well as the data in itself can be accessed with:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

int ncomp = my_field.numberOfComponents(); //returns the nuber of component of the elementary data
ansys::dpf::Location loc = my_field.fieldDefinition().location();
ansys::dpf::Unit unit = my_field.fieldDefinition().unit();
ansys::dpf::Scoping scoping = my_field.scoping();

int size = 0;
double* data = my_field.data(size); //returns the ptr to the full list of data
int entity_size = 0;
int index = 1;
double* data_by_index = my_field.entityData(index, entity_size);//returns the ptr to the list of data of the second entity
int id = 22;
double* data_by_id = my_field.entityDataById(id, entity_size);//returns the ptr to the list of data of the second entity

//the cursor represents a complete entity data (id, size, num elementary data)
ansys::dpf::FieldCursor cursor;
my_field.fillCursor(1, cursor);//fills the cursor on the second entity
id = cursor.id();
entity_size = cursor.size();
int num_elem_data = cursor.n_elementary_data();
data_by_index = cursor.data();
```

## Fields Container

### Create a Fields Container

The Fields Container is a vector of Fields and all the Fields are ordered with labels and ids. Most commonly, the Fields Container is scoped on "time" label and the ids are the time or frequency sets. More generically, the Fields Container allows to split results on different criterions.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

//Create a generic fields container from scratch
//using generic fields container allows to define you own space splitting the fields
//labels define this space
//for example, the labels can be "time", "eltype" to define fields over time with one field by element type
//each field added need to be defined on that space :
//field1 : "time" : 1, "eltype" : 8
//field2 : "time" : 1, "eltype" : 10
//field3 : "time" : 2, "eltype" : 8
//field4 : "time" : 2, "eltype" : 10

ansys::dpf::Field field_1;
ansys::dpf::Field field_2;
ansys::dpf::Field field_3;
ansys::dpf::Field field_4;

ansys::dpf::FieldsContainer my_fc;
my_fc.addLabels({ ansys::dpf::labels::time, ansys::dpf::Label("eltype") });
ansys::dpf::LabelSpace label_space = { { ansys::dpf::labels::time,1 },{ ansys::dpf::Label("eltype"),8 } };
my_fc.add(label_space, field_1);
my_fc.add({ { ansys::dpf::labels::time,1 },{ ansys::dpf::Label("eltype"),10 } }, field_2);
my_fc.add({ { ansys::dpf::labels::time,2 },{ ansys::dpf::Label("eltype"),8 } }, field_3);
my_fc.add({ { ansys::dpf::labels::time,2 },{ ansys::dpf::Label("eltype"),10 } }, field_4);

//to create a fields container for complex results, use the ansys::dpf::labels::complex label
//with value 1 for imaginary fields and 0 for real fields:
ansys::dpf::FieldsContainer my_complex_fc;
my_complex_fc.addLabels({ ansys::dpf::labels::time, ansys::dpf::labels::complex });

//real part for time set 1
my_complex_fc.add({ { ansys::dpf::labels::time,1 },{ ansys::dpf::labels::complex, 0 } }, field_1);
//imaginary part for time set 1
my_complex_fc.add({ { ansys::dpf::labels::time,1 },{ ansys::dpf::labels::complex, 1 } }, field_2);
```

### Get Fields Container's data

The Fields Container is the main output of results providers:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::Operator u_op("U");
u_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
auto my_fields_container = u_op.getOutputFieldsContainer(0);

int num_fields = my_fields_container.size();

int index = 0;
//returns the labels and ids corresponding to the first Field
ansys::dpf::LabelSpace label_space = my_fields_container.getLabelSpace(index); //ie. {'time',1} for the first time set

                                                                               //return the real Fields on{ 'time',1 }
ansys::dpf::Field my_field = my_fields_container.getFields({ { ansys::dpf::labels::time,1 } })[0];
my_field = my_fields_container.getFieldsForTimeId(1)[0];

my_field = my_fields_container[0]; //returns the first field
```

## Data Sources

### Create Data Sources

Data Sources is the entity containing the different path to the result files of an analysis. An extension key ('rst' for example) is used to choose which files represent results files, the other one being accessory files. See more information for using Data Sources in mechanical in "How to use DPF's package / IPython" menu.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile("c:/temp/file.rst");
my_data_sources.addFile("c:/temp/ds.dat");
```

## Meshed Region

### Create a Meshed Region

The user can create his own data to manipulate it with dpf. THe Meshed Region can be created simply with:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

//create a new mesh with 1 quad, 1 beam, 1 point element and 1 tetra
ansys::dpf::MeshedRegion mesh;
mesh.prepareConstruction(11, 4); //reserve the size of the mesh
mesh.nodeScoping().size();
//return:
//0

mesh.elementScoping().size();
//return:
//0

//quad element with 4 nodes
mesh.addNode(1, { 0.0, 0.0, 0.0 });
mesh.addNode(2, { 1.0, 0.0, 0.0 });
mesh.addNode(3, { 1.0, 1.0, 0.0 });
mesh.addNode(4, { 0.0, 1.0, 0.0 });
mesh.addElement(ansys::dpf::elements::quad4, 1, { 0, 1, 2, 3 }); // connectivity is by node indexes

//point element
mesh.addNode(5, { 0.0, 0.0, 0.0 });
mesh.addElement(ansys::dpf::elements::point1, 2, { 4 });

//beam element
mesh.addNode(6, { 0.0, 0.0, 0.0 });
mesh.addNode(7, { 1.0, 0.0, 0.0 });
mesh.addElement(ansys::dpf::elements::line2, 3, { 5, 6 });

//tetra element with 4 nodes
mesh.addNode(8, { 0.0, 0.0, 0.0 });
mesh.addNode(9, { 1.0, 0.0, 0.0 });
mesh.addNode(10, { 1.0, 1.0, 0.0 });
mesh.addNode(11, { 0.0, 1.0, 1.0 });
mesh.addElement(ansys::dpf::elements::tet4, 4, { 7, 8, 9, 10 });

mesh.nodeScoping().size();
//return:
//11

mesh.elementScoping().size();
//return:
//4

ansys::dpf::ElementCursor el;
mesh.fillCursor(0, el);
el.numberOfNodes();
//return:
//4
```

### Get Meshed Region's data from DataSources

A model is usually represented by a Meshed Region in DPF. The mesh provider operator allows to access an analysis' mesh. The user can then get different information in the mesh like the coordinates of all the nodes and the connectivity between elements and nodes.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::Operator mesh_prov("MeshProvider");
mesh_prov.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
ansys::dpf::MeshedRegion mesh = mesh_prov.getOutputMeshedRegion(0);

//access elements Scoping
ansys::dpf::Scoping my_elements_scoping = mesh.elementScoping();

//access nodes Scoping
ansys::dpf::Scoping my_nodes_scoping = mesh.nodeScoping();

//get connectivity(ordered node indices) of one element
ansys::dpf::PropertyField connectivity = mesh.connectivity();
ansys::dpf::PropFieldCursor cursor;
connectivity.fillCursor(0, cursor); // connectivity of the first element
connectivity.fillCursor(my_elements_scoping.indexById(1), cursor); // connectivity of the element of id 1
int* node_indices = cursor.data();
int num_nodes_in_elem = cursor.size();

//get coordinates
ansys::dpf::Field coordinates = mesh.nodesCoordinates();
ansys::dpf::FieldCursor fcursor;
coordinates.fillCursor(0, fcursor); // coordinates of the first node
coordinates.fillCursor(my_nodes_scoping.indexById(1), fcursor); // coordinates of the node of id 1
double* node_coord = fcursor.data();

//get element types
ansys::dpf::PropertyField element_types = mesh.elementTypes();
element_types.fillCursor(0, cursor); // element_types of the first element
element_types.fillCursor(my_elements_scoping.indexById(1), cursor); // element_types of the element of id 1
int element_type = *cursor.data();
ansys::dpf::ElementDescriptor element_des = ansys::dpf::elements::descriptor(element_type);
std::string name = element_des.name;
int num_nodes = element_des.number_of_nodes;
int num_corner_nodes = element_des.number_of_corner_nodes;
int num_sec_nodes = element_des.number_of_mid_nodes;
bool issolid = element_des.solid;
```

## Time Freq Support

### Create Time Freq Support

The time or frequency space of an analysis is described by the Time Freq Support entity in DPF. It gives access to real and imaginary sets. User can create a time freq support to manage data.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

// create time_freq_support from scratch
ansys::dpf::TimeFreqSupport time_freq_support; 

// create time_frequencies, rpms and harmonic indices field
ansys::dpf::Field time_freq(3, { 1 }, ansys::dpf::locations::time_set); 
time_freq.scoping().setIds({ 1, 2, 3 });
time_freq.scoping().setLocation(ansys::dpf::locations::time_step); 
time_freq.setData({ 0.1, 0.21, 0.2 });
ansys::dpf::Field rpms(1, { 1 }, ansys::dpf::locations::time_step);
rpms.scoping().setIds({ 1 });
rpms.setData({ 30 });
ansys::dpf::Field harmonic_indices(0, { 1 }, ansys::dpf::locations::time_set);
harmonic_indices.scoping().setIds({ 1, 2, 3 });
harmonic_indices.scoping().setLocation(ansys::dpf::locations::time_step);
harmonic_indices.setData({ 1.0, 2.0, -1.0 }); 

// set the time_freq_support fields
time_freq_support.setTimeFrequencies(time_freq); 
time_freq_support.setRpms(rpms); 
time_freq_support.setHarmonicIndices(harmonic_indices); 

// set harmonic indices for a specific cyclic stage number
ansys::dpf::Field harmonic_indices_2(3, { 1 }, ansys::dpf::locations::time_set);
harmonic_indices_2.scoping().setIds({ 1, 2, 3 });
harmonic_indices_2.setData({ 1.0, 3.0, 2.0 });
time_freq_support.setHarmonicIndices(harmonic_indices_2, 2); // set indices for the second stage
```

### Get Time Freq Support's data from DataSources

Time Freq Support of a specific file can be accessed using the following methods.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

ansys::dpf::Operator time_freq_prov("TimeFreqSupportProvider");
time_freq_prov.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
ansys::dpf::TimeFreqSupport time_freq = time_freq_prov.getOutputTimeFreqSupport(0);

//get number of time/freq sets
int num_sets = time_freq.numberOfSets();

//get Field of real time freqs
ansys::dpf::Field my_time_freq_field = time_freq.frequencies();
ansys::dpf::Unit time_freq_unit = my_time_freq_field.fieldDefinition().unit(); //usually s or Hz

//get time or freqs on the first load step
int size;
double* freqs = my_time_freq_field.entityDataById(1, size);
```

## Model

### Explore a Model

The Model is built with DataSources that it will open (in a streams by default) to explore an analysis. Printing the model is a good tool to see the results that are available.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"
#include "helpers/dpf_result.h"
#include "helpers/dpf_model.h"


ansys::dpf::DataSources my_data_sources(my_path);

//create the model
ansys::dpf::Model my_model(my_data_sources);
//or
ansys::dpf::Model my_model(my_path);

//explore
ansys::dpf::TimeFreqSupport time_freq_support = my_model.getTimeFreqSupport();
ansys::dpf::MeshedRegion meshed_region = my_model.getMesh();
ansys::dpf::ResultInfo result_info = my_model.getResultInfo();

//instantiate result provider
//those providers are automatically connected to the streams
ansys::dpf::Result displacement = my_model.CreateResultEvaluationWorkflow("U");
ansys::dpf::Result stress = my_model.CreateResultEvaluationWorkflow("S");

//choose the time freq for the providers
ansys::dpf::DpfError error;
ansys::dpf::FieldsContainer fields = displacement.EvaluateAtGivenTime(0.0, error);
```
