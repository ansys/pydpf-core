.. _ref_user_guide_operators:

=========
Operators
=========

..    include:: <isonum.txt>

An operator is the only object that is used to create and transform 
data. It is the fundamental method by which DPF loads, operates on, and
outputs data. Each operator contains the ``input`` and ``output``
attributed, which allow you to make various input and output connections. 

When the operator is evaluated, it processes the input information to 
compute its output with respect to its description:

.. figure:: ../images/drawings/operator_drawing.svg

By attaching one operator's outputs to another operator's inputs,
you can chain together operators to create workflows for conducting 
simple or complex data processing.  Through lazy evaluation, DPF 
approaches data processing in an efficient manner, evaluating each operator
only when the final operator is evaluated and the data is requested.

For example, if you desire the maximum normalized displacement of a
result, you construct operators in this order:

.. figure:: ../images/drawings/max_u_norm.png

To achieve this, you an use:

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()
    norm = ops.math.norm(displacement)
    min_max = ops.min_max.min_max(norm)
    max_displacement = min_max.outputs.field_max()
 
 
This approach efficiently computes the maximum
displacement of a result entirely within the DPF service, without
transferring any data from DPF to Python until DPF arrives at the
solution data that you want.

DPF's library of operators is large and includes file readers and mathematical, 
geometrical, and logical transformations. This library, found in 
:ref:`ref_dpf_operators_reference`, is progressively enhanced.


Creating Operators
~~~~~~~~~~~~~~~~~~
Each operator is of type :ref:`ref_operator`. You can create an instance 
in Python with any of the derived classes available in the 
package :ref:`ref_operators_package` or directly with the class :ref:`ref_operator`
using the internal name string that indicates the operator type. 
For more information, see :ref:`ref_dpf_operators_reference`).

For example, to create the displacement operator, use:

.. code-block:: python

   from ansys.dpf.core import operators as ops
   op = ops.result.displacement() # or op = ansys.dpf.core.Operator("U")

You can view the description, available inputs, and available outputs of this
particular operator by printing it:

.. code-block:: python

    print(op)
    
.. rst-class:: sphx-glr-script-out

 Out:

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


Alternatively, you can instantiate result providers via the model. For more 
information, see :ref:`user_guide_model`.

With this model's result usage, file paths for the results are directly  
connected to the operator, which means that you can only instantiate 
available results for your result files:


.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()


Connecting Operators
~~~~~~~~~~~~~~~~~~~~
The only required input for the displacement operator is ``data_sources`` (see above). 
Providing file paths for results to the operator is necessary to compute 
output in the ``fields_container``, which contains the displacement results.


There are two ways of creating data sources: use either the :ref:`ref_model`
class or the :ref:`ref_data_sources` class. 


Because several other examples use the model approach, this example uses the data 
sources approach:

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   data_src = dpf.DataSources(examples.multishells_rst)
   print(data_src)
   

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
  DPF  DataSources: 
  Result files:
     result key: rst and path: D:\ANSYSDev\dpf-python-core\ansys\dpf\core\examples\model_with_ns.rst 
  Secondary files:

Connect this data source to the displacement operator:

.. code-block:: python

    op.inputs.data_sources(data_src)
    
Other optional inputs can be connected to the displacement operator.
Printing the operator above showed that a ``mesh_scoping`` of type :ref:`ref_scoping`
can be connected to work on a spatial subset. A ``time_scoping`` of a list of integers 
can also be connected to work on a temporal subset:


.. code-block:: python

    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping([1,2])
    op.inputs.mesh_scoping(mesh_scoping)
    op.inputs.time_scoping([1])
    
    
Evaluating Operators
~~~~~~~~~~~~~~~~~~~~
With all the required inputs assigned, the :class:`ansys.dpf.core.fields_container` can be
outputted from the operator:

.. code-block:: python

    fc = op.outputs.fields_container()
    print(fc)
    
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPF displacement(s)Fields Container
      with 1 field(s)
      defined on labels: time 
    
      with:
      - field 0 {time:  1} with Nodal location, 3 components and 2 entities.

At run time, the operator checks if all required inputs have been assigned. 
Evaluating an operator with missing inputs will raise a ``DPFServerException`` 
like this one:
    
.. code-block:: python

    new_oper = ops.result.displacement()
    fc = new_oper.outputs.fields_container()
    
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPFServerException: U<-Data sources are not defined.

For information on using the field container, see :ref:`ref_user_guide_fields_container`.


Chaining Operators
~~~~~~~~~~~~~~~~~~

To create more complex operations and customizable results, operators can be 
chained together to create workflows.

With the large library of ``Operators`` that DPF offers, customizing results 
to get a specific output is very easy.

While manually customizing results on the Python side is far less efficient
than using operators, for a very small model, it is acceptable to bring all 
displacement data on the client side to compute the maximum:

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()
    fc = displacement.outputs.fields_container()

    # Compute the maximum displacement of the first field using numpy.
    # Note that the data returned is a numpy array.

    disp = fc[0].data
    disp.max(axis=0)
    

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    array([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])

On an industrial model, you should use:

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()
    min_max = ops.min_max.min_max(displacement)
    max_field = min_max.outputs.field_max()
    max_field.data
    

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    array([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])
    

Here, only the maximum displacements in the X, Y, and Z components
are transferred and returned as a numpy array.

For small data sets, you can compute the maximum of the array in Numpy.
While there may be times where having the entire data array for a given 
result type is necessary, many times it is not necessary.  In these 
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


Types of Operators
~~~~~~~~~~~~~~~~~~
DPF provides three main types of operators:

- Operators for importing or reading data
- Operators for transforming data
- Operators for exporting data

***************************************
Operators for Importing or Reading Data
***************************************

These operators provide for reading data from solver files or from standard file types:

- For MAPDL, supported solver file formats include RST, MODE, RFRQ, and RDSP.
- For LS DYNA, D3PLOT files are supported.
- For Fluent and CFX, CAS.H5, DAT.H5, RES, and FLPRJ files are supported.
- For Abaqus, ODB files are supported.

To read these files, different readers are implemented as plugins.
Plugins can be loaded on demand in any DPF's scripting language with the "load library" methods. 
File readers can be used generically thanks to DPF's result providers, which means that the same operators can be used for any file types.

For example, read a displacement or a stress for any file:

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   data_src = dpf.DataSources(examples.multishells_rst)
   disp = ops.result.displacement(data_sources = data_src)
   stress = ops.result.stress(data_sources = data_src)

Standard file format readers are also supported to import custom data. 
Fields can be imported from CSV, VTK, and HDF5 files.

For an example of importing and exporting a CSV file, see :ref:`ref_basic_load_file_example`.

*******************************
Operators for Transforming Data
*******************************

A field is the main data container in DPF. Most of the operators that transform
data take a field or a fields container as input and return a transformed 
field or fields container as output. You can perform analytic, averaging, 
or filtering operations on simulation data.

For example, after creation of a field, use scaling and filtering 
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

 Out:

 .. code-block:: none
 
     array([[ 2.,  4.,  6.],
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

 Out:

 .. code-block:: none
 
     array([[4., 5., 6.],
       [7., 8., 9.]])
       
 
****************************
Operators for Exporting Data
****************************

After using DPF to read or transform simulation data, you might want 
to export the results in a given format to either use it in another 
environment or save it for future use with DPF. Supported file formats 
for export include VTK, H5, CSV, and TEXT (serializer operator). Export 
operators often match with import operators, allowing you to reuse data. 
The "serialization" operators menu lists the available import and export 
operators.


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   model = dpf.Model(examples.multishells_rst)
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
   up_loaded_file = dpf.upload_file_in_tmp_folder(examples.multishells_rst)
   model = dpf.Model(up_loaded_file)
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path=server_dir+"\\file.vtk",
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   dpf.download_file(server_dir+"\\file.vtk",r"c:/temp/file_downloaded.vtk")
   

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
     C:\Users\cbellot\AppData\Local\Temp\dataProcessingTemp17168
     Downloading...: 759 KB|
 

API Reference
~~~~~~~~~~~~~
For a list of all operators in DPF, see :ref:`ref_dpf_operators_reference` 
or :ref:`ref_operators_package`.  For more information about the
class itself, see :ref:`ref_operator`.
