# How to use operators

## Operator types

In DPF, the operator is used to import and modify the simulation data. We can count 3 main types of operators:

- Operators importing/reading data
    
- Operators transforming existing data
    
- Operators exporting data
    

### Operators importing / reading data

Those operators allow to read data from solver files or from standard file types. Different solver format are handled by DPF like rst/mode/rfrq/rdsp.. for MAPDL, d3plot for LsDyna, cas.h5/dat.h5/res/flprj for CFX and Fluent, odb for Abaqus... To read those, different readers have been implemented in plugins. Plugins can be loaded on demand in any dpf's scripting language with the "load library" methods. File readers can be used generically thanks to dpf's result providers, which means that the same operators can be used for any file types. For example, reading a displacement or a stress for any files will be done with:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

std::string my_path = "c:/temp/file.rst"
//or
std::string my_path = "c:/temp/d3plot"

ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile(my_path, "rst");
//or
my_data_sources.addResultFile(my_path, "d3plot");

//displacement for any solver file
ansys::dpf::Operator u_op("U");
u_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
ansys::dpf::FieldsContainer my_u = u_op.getOutputFieldsContainer(0);


//stress for any solver file
ansys::dpf::Operator s_op("S");
s_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
ansys::dpf::FieldsContainer my_s = s_op.getOutputFieldsContainer(0);
```

Result providers can be customized to read a specific time frequency or to provide results on a subset of the mesh:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

std::string my_path = "c:/temp/file.rst"
//or
std::string my_path = "c:/temp/d3plot"

ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile(my_path, "rst");
//or
my_data_sources.addResultFile(my_path, "d3plot");

//displacement for any solver file
ansys::dpf::Operator u_op("U");
u_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);


/// Different ways to set the time scoping
// Select one time/frequency
u_op.connect(ansys::dpf::eTimeScopPin, 2); // Int : Select second time/freq set in the time freq support
u_op.connect(ansys::dpf::eTimeScopPin, 0.002); // Double : Gives a field interpolated at the given time/freq value


// Select multiple times/frequencies 
std::vector<int> time_sets = { 1,2,3 };
u_op.connect(ansys::dpf::eTimeScopPin, time_sets); // Vec Int: Select time/freq sets in the time freq support
std::vector<double> times = { 0.002, 0.003 };
u_op.connect(ansys::dpf::eTimeScopPin, times); // Vec Double : Gives fields interpolated at the given time/freq values
 
// Select all the time/frequencies of a load step
ansys::dpf::Scoping load_step({ 2 }, ansys::dpf::locations::time_step);
u_op.connect(ansys::dpf::eTimeScopPin, load_step);



/// Choose the mesh scoping
ansys::dpf::Scoping node_scoping({1,2,3}, ansys::dpf::locations::nodal)
u_op.connect(ansys::dpf::eMeshScopPin, node_scoping)


ansys::dpf::Scoping element_scoping({1,2,3}, ansys::dpf::locations::elemental)
u_op.connect(ansys::dpf::eMeshScopPin, element_scoping)

 
ansys::dpf::FieldsContainer my_u = u_op.getOutputFieldsContainer(0);
```

Standards file formats reader are also supported to import custom data. Fields can be imported from csv, vtk or hdf5 files:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

std::string my_path = "c:/temp/file.csv"
ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile(my_path);

ansys::dpf::Operator csv("csv_to_field");
csv.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
ansys::dpf::FieldsContainer my_fields = csv.getOutputFieldsContainer(0);
```

csv file example

### Operators transforming existing data

The field being the main data container in DPF, most of the operator transforming the data take a field or fields container in input and return a transformed field or fields container in output. Analytic, averaging or filtering operations can be performed on the simulation data:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"


ansys::dpf::Field field1(3, { 3 }, ansys::dpf::locations::nodal);
field1.setData({1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0});
field1.scoping().setIds({ 1,2,3 });

//example 1 analytic operator: scale operator
ansys::dpf::Operator op1("scale");
op1.connect(0,field1);
op1.connect(1,2.0);
ansys::dpf::Field out = op1.getOutputField(0);
int size=0;
ansys::dpf::dp_double*const data = out.data(size);
// returns:
// { 2.,  4.,  6., 8., 10., 12., 14., 16., 18.}

// example 2 filtering operator
ansys::dpf::Operator op2("core::field::high_pass");
op2.connect(0,field1);
op2.connect(1,3.0);
out = op2.getOutputField(0);
ansys::dpf::dp_double*const data2 = out.data(size);
// returns:
// {4., 5., 6., 7., 8., 9.}
```

### Operators exporting data

After transforming or reading simulation data with DPF, the user might want to export the results in a given format to use it in another environment or to save it for future use with dpf. Vtk, h5, csv and txt (serializer operator) are examples of supported exports. Export operators often match with import operators allowing user to reuse their data. The "serialization" operators menu lists the available import/export operators.



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

//example import/export vtk file

std::string my_path = "c:/temp/file.vtk"
ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile(my_path);

ansys::dpf::Operator my_u_op("vtk::vtk::FieldProvider");
my_u_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);
my_u_op.conect(0, "displacement_mode_6"); // name of the field in the vtk file
ansys::dpf::FieldsContainer my_fields = my_u_op.getOutputFieldsContainer(0);

//scale it by 2.0
ansys::dpf::Operator my_scale_op("scale_fc");
my_scale_op.connect(0,my_fields);
my_scale_op.connect(1,2.0);

//get the mesh
ansys::dpf::Operator my_mesh_op("MeshProvider");
my_mesh_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);

//export the result in vtk
ansys::dpf::Operator my_export("vtk_export");
my_export.connect(0, std::string("C:/temp/fileNew.vtk"));
my_export.connect(1, my_mesh_op, 0);
my_export.connect(2, my_scale_op, 0);
my_export.run();
```

vtk file example

## Chaining operators together

To create more complex operations and customizable results, operators can be chained together to create workflows. This way a result can be read from a solver result file and directly transformed in a single workflow. Examples can be found in APIs/Workflow examples menu. 2 syntaxes can be used to create and connect operators together:



```c++
#include "dpf_api.h"
#include "dpf_api_i.cpp"

std::string my_path = "c:/temp/file.rst"
ansys::dpf::DataSources my_data_sources;
my_data_sources.addResultFile(my_path);

ansys::dpf::Operator u_op("U");
u_op.connect(ansys::dpf::eDataSourcesPin, my_data_sources);

ansys::dpf::Operator norm_op("norm_fc");
norm_op.connect(0, u_op, 0); //connect norm_op input pin 0 to u_op output pin 0
 
ansys::dpf::FieldsContainer my_u_norm = norm_op.getOutputFieldsContainer(0);
```

## Configurating operators

Advanced user might want to configurate an operator's behavior during its running phase. This can be done through the "config". This option allows to choose if an operator can directly modify the input data container instead of creating a new one with the "inplace" configuration, to choose if an operation between to fields should use their indices or mesh ids with the "work_by_index" configuration... Each operator's description explains which configuration are supported.



```c++
//use config for add operator

#include "dpf_api.h"
#include "dpf_api_i.cpp"


ansys::dpf::Field field1(3, { 3 }, ansys::dpf::locations::nodal);
field1.setData({1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0});
field1.scoping().setIds({ 1,2,3 });

ansys::dpf::Field field2(3, { 3 }, ansys::dpf::locations::nodal);
field2.setData({1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0});
field2.scoping().setIds({ 3,4,5 });

ansys::dpf::OperatorConfig config = ansys::dpf::core::defaultOperatorConfig("add");

bool current_value = config.getBoolValue("work_by_index");//returns current values of configuration

//modify work_by_index config (default is false)
config.set("work_by_index", true);


//instantiate the operator with the config
ansys::dpf::Operator op1("add", config);
op1.connect(0,field1);
op1.connect(1,field2);
ansys::dpf::Field out = op1.getOutputField(0);
int size=0;
ansys::dpf::dp_double*const data = out.data(size);
// returns:
// { 2.,  4.,  6., 8., 10., 12., 14., 16., 18.}

//use default config value
config.set("work_by_index", false);
op1 = ansys::dpf::Operator("add", config);
op1.connect(0,field1);
op1.connect(1,field2); 
out = op1.getOutputField(0);
ansys::dpf::dp_double*const data2 = out.data(size);
// returns:
// { 1.,  2.,  3., 4.,  5.,  6., 8., 10., 12., 4.,  5.,  6., 7.,  8.,  9.}

// changing the "permissive" config could allow to add fields of different homogeneities
// changing the "binary_operation" config could allow to keep only the intersection between fields ids and not the union
//...
```
