.. _ref_user_guide_operators:

=========
Operators
=========

..    include:: <isonum.txt>

An operator is the main object that is used to create, transform, and stream 
data. In DPF, you use operators to load, operate on, and output data.

Each operator contains ``input`` and ``output`` attributes, which
allow you to make various input and output connections. 

During an evaluation, an operator processes inputs to 
compute an output with respect to the operator's description:

.. figure:: ../images/drawings/operator_drawing.svg

You can attach one operator's outputs to another operator's inputs to
chain operators together, thereby creating workflows for conducting simple or
complex data processing. Through lazy evaluation, DPF approaches data processing
in an efficient manner, evaluating each operator only when the final operator
is evaluated and the data is requested.

For example, if you want the maximum normalized displacement of a
result, you construct operators in this order:

.. figure:: ../images/drawings/max_u_norm.png

This example shows how to compute the maximum normalized displacement
of a result:

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    norm = ops.math.norm(displacement)
    min_max = ops.min_max.min_max(norm)
    max_displacement = min_max.outputs.field_max()
 
 
This approach efficiently computes the maximum
displacement of a result entirely within the DPF service, without
transferring any data from DPF to Python until DPF arrives at the
solution data that you want.

A DPF operator can be licensed, meaning it requires a license checkout to run.
The license type can be specific, or amongst a given list, and is defined at the operator level.
For more information about the DPF licensing logic, see :ref:`user_guide_server_context`.

The library of DPF operators is large and includes file readers and mathematical,
geometrical, and logical transformations. For more information on this library,
which is progressively enhanced, see :ref:`ref_dpf_operators_reference`.


Create operators
~~~~~~~~~~~~~~~~
Each operator is of type :ref:`ref_operator`. You can create an instance 
in Python with any of the derived classes available in the
:ref:`ansys.dpf.core.operators package` or directly with the :ref:`ref_operator`
class using the internal name string that indicates the operator type. 
For more information, see :ref:`ref_dpf_operators_reference`.

This example shows how to create the displacement operator:

.. code-block:: python

   from ansys.dpf.core import operators as ops
   op = ops.result.displacement() # or op = ansys.dpf.core.Operator("U")

You can view the description and available inputs and available outputs of this
operator by printing it:

.. code-block:: python

    print(op)
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPF U Operator: 
      Read/compute nodal displacements by calling the readers defined by the datasources. 
      Inputs:
             time_scoping (optional) [scoping, int32, vector<int32>, double, field, vector<double>]: time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output 
             mesh_scoping (optional) [scopings_container, scoping]: nodes or elements scoping required in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains 
             fields_container (optional) [fields_container]: Fields container already allocated modified inplace 
             streams_container (optional) [streams_container]: result file container allowed to be kept open to cache data 
             data_sources [data_sources]: result file path container, used if no streams are set 
             bool_rotate_to_global (optional) [bool]: if true the field is rotated to global coordinate system (default true) 
             mesh (optional) [abstract_meshed_region, meshes_container]: prevents from reading the mesh in the result files 
             read_cyclic (optional) [enum dataProcessing::ECyclicReading, int32]: if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1) 
      Outputs:
             fields_container [fields_container] 


Alternatively, you can instantiate result providers using the ``Model`` object.
For more information, see :ref:`user_guide_model`.

When using this model's results, file paths for the results are directly  
connected to the operator, which means that you can only instantiate 
available results for your result files:


.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()


Connect operators
~~~~~~~~~~~~~~~~~
The only required input for the displacement operator is the ``data_sources``input (see above). 
To compute an output in the ``fields_container`` object, which contains the displacement
results, you must provide paths for the result files.

You can create data sources in two ways:

- Use the :ref:`ref_model` class.
- Use the :ref:`ref_data_sources` class. 


Because several other examples use the ``Model`` class, this example uses the
``DataSources`` class:

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   data_src = dpf.DataSources(examples.find_multishells_rst())
   print(data_src)
   

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
  DPF  DataSources: 
  Result files:
     result key: rst and path: path\...\ansys\dpf\core\examples\model_with_ns.rst
  Secondary files:

This code shows how to connect the data source to the displacement operator:

.. code-block:: python

    op.inputs.data_sources(data_src)
    
You can connect other optional inputs to the displacement operator. 
The output from printing the operator shows that a ``mesh_scoping`` of type :ref:`ref_scoping`
can be connected to work on a spatial subset. A ``time_scoping`` of a list of integers 
can also be connected to work on a temporal subset:


.. code-block:: python

    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping([1,2])
    op.inputs.mesh_scoping(mesh_scoping)
    op.inputs.time_scoping([1])
    
    
Evaluate operators
~~~~~~~~~~~~~~~~~~
With all the required inputs assigned, you can output the :class:`ansys.dpf.core.fields_container`
class from the operator:

.. code-block:: python

    fc = op.outputs.fields_container()
    print(fc)
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPF displacement(s)Fields Container
      with 1 field(s)
      defined on labels: time 
    
      with:
      - field 0 {time:  1} with Nodal location, 3 components and 2 entities.

At run time, the operator checks if all required inputs have been assigned. 
Evaluating an operator with missing inputs raises a ``DPFServerException`` 
like this one:
    
.. code-block:: python

    new_oper = ops.result.displacement()
    fc = new_oper.outputs.fields_container()
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFServerException: U<-Data sources are not defined.

For more information on using a fields container, see :ref:`ref_user_guide_fields_container`.


Chain operators
~~~~~~~~~~~~~~~

To create more complex operations and customizable results, you can chain operators
together to create workflows. Using the large library of DPF operators, you can
customize results to get a specific output.

While manually customizing results on the Python side is far less efficient
than using operators, for a very small model, it is acceptable to bring all 
displacement data on the client side to compute the maximum:

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    fc = displacement.outputs.fields_container()

    # Compute the maximum displacement of the first field using NumPy.
    # Note that the data returned is a numpy array.

    disp = fc[0].data
    disp.max(axis=0)
    

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFArray([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])

On an industrial model, however, you should use code like this:

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    min_max = ops.min_max.min_max(displacement)
    max_field = min_max.outputs.field_max()
    max_field.data
    

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFArray([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])
    

In the preceding example, only the maximum displacements in the X, Y, and Z
components are transferred and returned as a numpy array.

For small data sets, you can compute the maximum of the array in `NumpPy <https://numpy.org/>`_.
While there may be times where having the entire data array for a given 
result type is necessary, many times it is not necessary. In these 
cases, it is faster not to transfer the array to Python but rather to 
compute the maximum of the fields container within DPF and then return 
the result to Python.

This example instantiates operators with other operators:


.. code-block:: python

    min_max = ops.min_max.min_max(displacement)

This automatically connects the matching ``displacement`` output with the 
matching ``min_max`` input. You can also use the :py:meth:`connect()
<ansys.dpf.core.dpf_operator.Operator.connect>` method to manually connect 
the outputs of one operator to the inputs of another operator:

.. code-block:: python

    min_max = ops.min_max.min_max()
    min_max.inputs.connect(displacement.outputs)
    #or
    min_max.inputs.field.connect(displacement.outputs.fields_container)


While this last approach is more verbose, it can be useful for operators 
having several matching inputs or outputs.


Types of operators
~~~~~~~~~~~~~~~~~~
DPF provides three main types of operators:

- Operators for importing or reading data
- Operators for transforming data
- Operators for exporting data

***************************************
Operators for importing or reading data
***************************************

These operators provide for reading data from solver files or from standard file types
such as .RST (MAPDL), .D3Plot (LS DYNA), .CAS.H5/.DAT.H5 (Fluent), .CAS.CFF/.DAT.CFF (CFX)
or .OBD (Abaqus).

To read these files, different readers are implemented as plugins.
Plugins can be loaded on demand in any DPF scripting language with "load library" methods. 
File readers can be used generically thanks to the DPF result providers, which means that the same operators can be used for any file types.

This example shows how to read a displacement and a stress for any file:

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   data_src = dpf.DataSources(examples.find_multishells_rst())
   disp = ops.result.displacement(data_sources = data_src)
   stress = ops.result.stress(data_sources = data_src)

Standard file format readers are also supported to import custom data. 
Fields can be imported from CSV, VTK, and HDF5 files.

For an example of importing and exporting a CSV file, see :ref:`ref_basic_load_file_example`.

*******************************
Operators for transforming data
*******************************

A field is the main data container in DPF. Most of the operators that transform
data take a field or a fields container as input and return a transformed 
field or fields container as output. You can perform analytic, averaging, 
or filtering operations on simulation data.

For example, after creation of a field, you can use scaling and filtering 
operators:

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as ops
    
    field1 = dpf.Field(nentities=3)
    field1.data = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    field1.scoping.ids = [1,2,3]
    field1.unit = 'm'
    
    #example 1 analytic operator: scale operator
    op1 = ops.math.scale()
    op1.inputs.field.connect(field1)
    op1.inputs.ponderation.connect(2.0)
    out = op1.outputs.field()
    out.data
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     DPFArray([[ 2.,  4.,  6.],
          [ 8., 10., 12.],
          [14., 16., 18.]])


.. code-block:: python

    #example 2 filtering operator
    op2 = ops.filter.field_high_pass()
    op2.inputs.field.connect(field1)
    op2.inputs.threshold.connect(3.0)
    out = op2.outputs.field()
    out.data
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     DPFArray([[4., 5., 6.],
          [7., 8., 9.]])
       
 
****************************
Operators for exporting data
****************************

After using DPF to read or transform simulation data, you might want 
to export the results in a given format to either use them in another 
environment or save them for future use with DPF. Supported file formats 
for export include VTK, H5, CSV, and TXT (serializer operator). Export 
operators often match with import operators, allowing you to reuse data. 
In :ref:`ref_dpf_operators_reference`, both the **Entry**
and **Premium** sections have a **Serialization** category that
displays available import and export operators.


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   model = dpf.Model(examples.find_multishells_rst())
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path='c:/temp/file.vtk',
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   
This example demonstrates how to use import and export operators if the 
Python client is not on the same machine as the server:


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   server_dir = dpf.make_tmp_dir_server()
   print(server_dir)
   up_loaded_file = dpf.upload_file_in_tmp_folder(examples.find_multishells_rst())
   model = dpf.Model(up_loaded_file)
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path=server_dir+"\\file.vtk",
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   dpf.download_file(server_dir+"\\file.vtk",r"c:/temp/file_downloaded.vtk")
   

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     C:\Users\user_name\AppData\Local\Temp\dataProcessingTemp17168
     Downloading...: 759 KB|
 

API reference
~~~~~~~~~~~~~
For a list of all operators in DPF, see :ref:`ref_dpf_operators_reference` 
or the package :ref:`ansys.dpf.core.operators package`.  For more information about the
class itself, see :ref:`ref_operator`.
