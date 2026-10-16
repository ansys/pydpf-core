.. _user_guide_stepbystep:

=======================
Using DPF: Step by Step
=======================
The goal of using DPF is to transform simulation data into output data 
that can be used to visualize and analyze simulation results.

This process has two main steps:

- Step 1: :ref:`define_sim_data`
- Step 2: :ref:`transform_the_data`

.. _define_sim_data:

Define Simulation Data
----------------------
Data can come from two sources: 

- ``Simulation result files``. DPF automatically recognizes the fields in result files. When using a result file as input you must specify the data source file(s). 
- ``Manual input in DPF``. You create fields of data in DPF. 

Once a data source has been selected, or fields have been manually defined,
you create field containers (if applicable) and define scopings to identify 
the subset of data that you want to evaluate. 

Selecting a Data Source
~~~~~~~~~~~~~~~~~~~~~~~ 
When you want to evaluate the data in simulation result files, 
you must specify the ``data source``. This is folder containing analysis 
results. Typically the data source consists of a path to the result or 
data files.

**Creating a data source and setting the result file path**
 
.. code-block:: python

   from ansys.dpf import core as dpf
   data_sources = dpf.DataSources()
   data_sources.set_result_file_path('/tmp/file.rst')
   data_sources.result_files
   ['/tmp/file.rst']  

To evaluate data files, they need to be opened. To open data files, you 
define ``streams``. A stream is an entity that contains the data sources. 
Streams keep the data files open and keep some data cached to make the next 
evaluation faster. Streams are particularly convenient when using large files. 
They save time when opening and closing files. When a stream is released, 
files are closed. 

Defining Fields
~~~~~~~~~~~~~~~
A ``field`` is a container of simulation data. In numerical simulations, 
results data is defined by values associated with entities:

.. image:: ../images/drawings/values-entities.png

Therefore, a field of data may look something like this:

.. image:: ../images/drawings/field.png

**Creating a field from scratch**

.. code-block:: python

   from ansys.dpf.core import fields_factory
   from ansys.dpf.core import locations
   from ansys.dpf import core as dpf
   field_with_classic_api = dpf.Field()
   field_with_classic_api.location = locations.nodal
   field_with_factory = fields_factory.create_scalar_field(10)

In DPF, field data is always associated with its ``scoping`` and ``support``, 
making it a self-describing piece of data. A field can also be defined by its 
dimensionality, unit, and location. To learn more see :ref:`user_guide_concepts`.

Defining Scoping
~~~~~~~~~~~~~~~~
In most cases you will not want to work with an entire field, but rather a 
subset of entities in the field. To achieve this you define ``scoping`` for 
the field. Scoping is a set of entity IDs on a location. For example, this may 
be a set of mesh IDs, geometric entity IDs, time domain, frequency domain, 
and so on. You specify the set of entities by defining a range of IDs:

.. image:: ../images/drawings/scoping-eg.png

A scoping must be defined prior to its use in the transformation data workflow.

**Creating a mesh scoping**

.. code-block:: python

   from ansys.dpf import core as dpf
   # 1. using the mesh_scoping_factory
   from ansys.dpf.core import mesh_scoping_factory
   # a. scoping with elemental location that targets the elements with id 2, 7 and 11
   my_elemental_scoping = mesh_scoping_factory.elemental_scoping([2, 7, 11])
   # b. scoping with nodal location that targets the elements with id 4 and 6
   my_nodal_scoping = mesh_scoping_factory.nodal_scoping([4, 6])
   #2. using the classic API
   my_scoping = dpf.Scoping()
   my_scoping.location = "Nodal" #optional
   my_scoping.ids = list(range(1,11))

Defining Field Containers
~~~~~~~~~~~~~~~~~~~~~~~~~
A ``field container`` holds a set of fields. It is used mainly for 
transient, harmonic, modal, or multi-step analyses. For example:

.. image:: ../images/drawings/field-con-overview.png

A field container is a vector of fields. Fields are ordered with labels 
and IDs. Most commonly, the field container is scoped on the “time” label 
and the IDs are the time or frequency sets:

.. image:: ../images/drawings/field-con.png

You can define a field container in multiple ways:

- Extract labeled data from a results file 
- Create a field container from a CSV file
- Convert existing fields to a field container

**Creating a field container from scratch**

.. code-block:: python

   from ansys.dpf import core as dpf
   fc= dpf.FieldsContainer()
   fc.labels =['time','complex']
   for i in range(0,20): #real fields
       mscop = {"time":i+1,"complex":0}
       fc.add_field(mscop,dpf.Field(nentities=i+10))
   for i in range(0,20): #imaginary fields
       mscop = {"time":i+1,"complex":1}
       fc.add_field(mscop,dpf.Field(nentities=i+10))

Some operators can operate directly on field containers instead of fields. 
Field containers are identified by the “FC” suffix in their name. 
Operators and field containers are explained in more detail 
in :ref:`transform_the_data`.

.. _transform_the_data:

Transform the Data
------------------
Once you have defined the simulation data to be evaluated, you use operators 
to transform the data to obtain the desired output. Operators can be chained 
together to create simple or complex data transformation workflows. 

Using Operators 
~~~~~~~~~~~~~~~
Operators can be used to import, export, transform, and analyze data. 

An operator is analogous to an integrated circuit in electronics which 
has a set of input and output pins. Pins allow data to be passed to 
each operator.  

An operator takes input from a field, field container, or scoping using 
an input pin, and computes output based on what the operator is designed 
to do. The output is passed to a field or field container using 
an output pin.

.. image:: ../images/drawings/circuit.png

To use operators you should consult the online help:

#. In the table of contents, select ``Operators``.
#. To search for an operator, type a keyword in the ``Search`` field or 
   browse each category to display the list of available operators for 
   each category:
   
.. image:: ../images/drawings/help-operators.png

The help page for each operator describes how the operator transforms data, 
indicates the required input data, and provides usage examples.

Defining Operators
~~~~~~~~~~~~~~~~~~
An operator definition consists of three steps:

- Operator instantiation
- Input definition
- Output storage

Each operator’s help page provides a sample definition in each available
language (IronPython, CPython, C++).

.. image:: ../images/drawings/operator-def.png

**Creating an operator from a model**

.. code-block:: python

   from ansys.dpf.core import Model
   from ansys.dpf.core import examples
   model = Model(examples.static_rst)
   disp_oper = model.results.displacement()

Defining Workflows
~~~~~~~~~~~~~~~~~~
In most cases, using a single operator is not sufficient to obtain the 
desired result. In DPF you can chain operators together to create a complete 
data transformation workflow, enabling you to perform all operations necessary 
to get the result you want.  

In a workflow, the output pins of one operator are connected to the input pins 
of another operator, allowing output data from one operator to be passed as 
input to the other operator.     

The following example illustrates how you would get the norm of a resulting 
vector from the dot product of two vectors:

.. image:: ../images/drawings/connect-operators.png 

**Creating a generic workflow computing the minimum of displacement by chaining the 'U'**
**and 'min_max_fc' operators**
	
.. code-block:: python

   from ansys.dpf import core as dpf
   disp_op = dpf.operators.result.displacement()
   max_fc_op = dpf.operators.min_max.min_max_fc(disp_op)
   workflow = dpf.Workflow()
   workflow.add_operators([disp_op,max_fc_op])
   workflow.set_input_name("data_sources", disp_op.inputs.data_sources)
   workflow.set_output_name("min", max_fc_op.outputs.field_min)
   workflow.set_output_name("max", max_fc_op.outputs.field_max)

.. code-block:: python

   from ansys.dpf.core import examples
   data_src = dpf.DataSources(examples.multishells_rst)
   workflow.connect("data_sources", data_src)
   min = workflow.get_output("min", dpf.types.field)
   max = workflow.get_output("max", dpf.types.field)              