.. _ref_user_guide_operators:

=========
Operators
=========

..    include:: <isonum.txt>

The Operator is the only object used to create and transform the data
and is the fundamental method by which DPF loads, operates on, and
outputs data. Each operator contain the ``input`` and ``output``
attribute, which allows you to connect various inputs and outputs to
each operator. When the operator is evaluated, it will process the input information to compute its output with respect to its description:

.. figure:: ../images/drawings/operator_drawing.svg

Operators can be chained together in workflows to conduct simple or
complex data processing by attaching one operator's outputs to
another's inputs.  Through lazy evaluation, DPF approaches data
processing in an efficient manner by only evaluating each operator
when the final operator is evaluated and the data is requested.

For example, if you desire the maximum normalized displacement of a
result, you will construct operators in the following order:

.. figure:: ../images/drawings/max_u_norm.png

By writing:

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()
    norm = ops.math.norm(displacement)
    min_max = ops.min_max.min_max(norm)
    max_diplacement = min_max.outputs.field_max()
 
 
With this approach, you can efficiently compute the maximum
displacement of a result entirely within the DPF service without
transferring any data from DPF to Python until DPF arrives at the
solution data you desire.

DPF's library of operators is large and includes files reader, mathematical, 
geometrical or logical transformations... This library can be found in :ref:`ref_dpf_operators_reference` 
and is growing release after release.


Creating Operators
~~~~~~~~~~~~~~~~~~
Each operator is of type :ref:`ref_operator`. An Operator's instance 
can be created in Python with any of the derived class available in the 
package :ref:`ref_operators_package` or directly with the class :ref:`ref_operator`
using the internal name string (see :ref:`ref_dpf_operators_reference`) indicating the operator type.

For example, to create the displacement operator, use:

.. code-block:: python

   from ansys.dpf.core import operators as ops
   op = ops.result.displacement() # or op = ansys.dpf.core.Operator("U")

The description, available inputs, and available outputs of this
particular operator can be viewed by printing the operator:

.. code-block:: python

    print(op)
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPF U Operator: 
      Read/compute nodal displacements by calling the readers defined by the datasources. 
      Inputs:
             time_scoping (optional) [scoping, int32, vector<int32>, double, field, vector<double>]: time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) requiered in output 
             mesh_scoping (optional) [scopings_container, scoping]: nodes or elements scoping requiered in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains 
             fields_container (optional) [fields_container]: Fields container already allocated modified inplace 
             streams_container (optional) [streams_container]: result file container allowed to be kept open to cache data 
             data_sources [data_sources]: result file path container, used if no streams are set 
             bool_rotate_to_global (optional) [bool]: if true the field is rotated to global coordinate system (default true) 
             mesh (optional) [abstract_meshed_region, meshes_container]: prevents from reading the mesh in the result files 
             read_cyclic (optional) [enum dataProcessing::ECyclicReading, int32]: if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1) 
      Outputs:
             fields_container [fields_container] 


Alternatively, result providers can be instanciated via the model. With this
model's result usage (see :ref:`user_guide_model`), the results file paths 
are directly connected to the operator and the user can only instanciate available
results for his/her result files:


.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.simple_bar)
    displacement = model.results.displacement()


Connecting Operators
~~~~~~~~~~~~~~~~~~~~
The only required input for the displacement operator is the ``data_sources`` (see above). 
Providing the result files paths to the operator is necessary to compute in
output the ``fields_container`` containing the displacement results.
There are two ways of creating the data source, use the :ref:`ref_model`
class, or use the :ref:`ref_data_sources` class. 
This example will explain the data sources approach as the model approach 
is used in several other examples.

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

Connect this data sources to the displacement operator with:

.. code-block:: python

    op.inputs.data_sources(data_src)
    
Other optional inputs can be connected to the displacement operator.
Printing the operator above showed that a mesh_scoping of type :ref:`ref_scoping`
can be connected to work on a spatial subset. A time scoping of type list[int] 
can also be connected to work on a temporal subset:


.. code-block:: python

    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping([1,2])
    op.inputs.mesh_scoping(mesh_scoping)
    op.inputs.time_scoping([1])
    
    
Evaluating Operators
~~~~~~~~~~~~~~~~~~~~
With all the required inputs assigned, the fields_container can now be
output from the operator with:

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

Please note that the operator checks at run-time if all the required
inputs have been assigned.  Evaluating an operator with missing inputs
will raise a ``DPFServerException``:


Purposely not assigning inputs in this example:
    
.. code-block:: python

    new_oper = ops.result.displacement()
    fc = new_oper.outputs.fields_container()
    
    
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    DPFServerException: U<-Data sources not defined

See the :ref:`ref_user_guide_fields_container` for the user guide
details regarding the use of the ``FieldsContainer``.


Chaining Operators
~~~~~~~~~~~~~~~~~~

To create more complex operations and customizable results, operators can be 
chained together to create workflows.
With the large library of ``Operators`` that DPF offers, customizing results 
to get a specific output is very easy.
Note that doing those result customization manually on Python side instead of
using operators will be far less efficient. 
While for a very small model, it would be acceptable to bring all the displacement 
data on the client side to compute the maximum with:

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

On industrial model, the user should do:

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
    

Here, the only the maximum displacements in the X, Y, and Z components
were transferred and returned as a numpy array.


For small data sets, it is perfectly acceptable to compute the maximum
of the array in numpy.  Indeed, there are times where it may be
necessary to have the entire data array for a given result type, but
many times it is not strictly necessary.  In those cases, it is faster
to not transfer the array to Python, but rather compute the maximum of
the fields container within DPF and then return the result to Python.


Note that here we are instanciating operators with other operators with other operators:


.. code-block:: python

    min_max = ops.min_max.min_max(displacement)

This automatically connects the matching ``displacement`` output with the 
matching ``min_max`` input. It can also be done manually using the :py:meth:`connect()
<ansys.dpf.core.dpf_operator.Operator.connect>` method to connect the outputs of
one operator to the inputs of another operator with:

.. code-block:: python

    min_max = ops.min_max.min_max()
    min_max.inputs.connect(displacement.outputs)
    #or
    min_max.inputs.field.connect(displacement.outputs.fields_container)


While this last approach is more verbose, it can be usefull for operators 
having several matching inputs/outputs.


Types of operators
~~~~~~~~~~~~~~~~~~
3 main types of operators can  be listed in DPF:

- Operators importing/reading data
- Operators transforming existing data
- Operators exporting data

**********************************
Operators importing / reading data
**********************************

Those operators allow to read data from solver files or from standard file types. 
Different solver format are handled by DPF like rst/mode/rfrq/rdsp.. for MAPDL, 
d3plot for LsDyna, cas.h5/dat.h5/res/flprj for CFX and Fluent, odb for Abaqus... 
To read those, different readers have been implemented in plugins. 
Plugins can be loaded on demand in any dpf's scripting language with the "load library" methods. 
File readers can be used generically thanks to dpf's result providers, which means that the same operators can be used for any file types.
For example, reading a displacement or a stress for any files will be done with:

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   data_src = dpf.DataSources(examples.multishells_rst)
   disp = ops.result.displacement(data_sources = data_src)
   stress = ops.result.stress(data_sources = data_src)

Standards file formats reader are also supported to import custom data. Fields can be imported from csv, vtk or hdf5 files.

See :ref:`ref_basic_load_file_example` for an example importing and exporting csv files.

************************************
Operators transforming existing data
************************************

The field being the main data container in DPF, most of the operator transforming
the data take a field or fields container in input and return a transformed 
field or fields container in output. Analytic, averaging or filtering operations 
can be performed on the simulation data:

Here is an example, where, after creation of a field, scaling and filtering 
operators are used:

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
       
 
*************************
Operators exporting data
*************************

After transforming or reading simulation data with DPF, the user might want 
to export the results in a given format to use it in another environment or 
to save it for future use with dpf. Vtk, h5, csv and txt (serializer operator) 
are examples of supported exports. Export operators often match with import 
operators allowing user to reuse their data. The "serialization" operators menu 
lists the available import/export operators.


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   model = dpf.Model(examples.multishells_rst)
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path='c:/temp/file.vtk',
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   
Note that a file uploading/dowloading service has been implemented to use 
those importing exporting data operators in the case where the python
client is not on the same machine as the server. Here is the same example
in the case of distant machines:


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
   dpf.download_file(server_dir+"\\file.vtk",r"c:/temp/file_dowloaded.vtk")
   

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
     C:\Users\cbellot\AppData\Local\Temp\dataProcessingTemp17168
     Downloading...: 759 KB|
 

API Reference
~~~~~~~~~~~~~
See :ref:`ref_dpf_operators_reference` or :ref:`ref_operators_package` for a full list of all
available operators within DPF.  For additional details regarding the
operator class itself, see :ref:`ref_operator`.
