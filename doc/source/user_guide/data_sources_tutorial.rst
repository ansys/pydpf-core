.. _user_guide_data_sources:

===============
DPF DataSources
===============

The DataSources is a class available as a submodule of the 'ansys.dpf.core'
package. It contains files with the analysis results. So this object is used in
the first basic step: define simulation data, by defining where it is located.

This example will describe the functionalities and functions of the class DataSources
and can be generalised for all the files formats accepted by Py-DPF:

.. _list_extensions_solvers:
**Supported apps by DPF and their related formats**


   - MAPDL files: .rst, .mode, .rfrq, .rdsp
   - LS-DYNA files: .d3plot, .binout
   - Fluent files: CFF restart files(.cas/dat.h5) and Project files (.flprj)
   - CFX files: CFF files(.cas/dat.cff.res) and Project files (.flprj)

DataSources creation
--------------------

**a) Class** :class:`DataSources <ansys.dpf.core.data_sources.DataSources>`
If you are sure that your file has exactly the extensions keys listed above,
the DataSources object can be created by directly calling the class with the
file path as an argument :

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object containing the given file
    my_data_sources_a = dpf.DataSources(result_path=r'file.extension')

It is preferable to generate a raw string (by putting the letter 'r' before
the file path string) in order to ensure the file path will be correctly read.

**b) Function** :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>`

If the extension key is not in the list above (For example: a file.binout can
sometimes be named as 'file.binout0000') but you know what the extension key is,
the DataSources object can be created by:

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_b = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_b.set_result_file_path(filepath=r'file.extension1234', key='extension')

**c) Function** :func:`guess_result_key() <ansys.dpf.core.data_sources.DataSources.guess_result_key>`

If the extension key is not in the list above (For example: a file.binout can
sometimes be named as 'file.binout0000') but you don't know what the extension
key is, the DataSources object can be created by:

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_c = dpf.DataSources()
    # Define the extension key for the file in the given path
    my_file_key = my_data_sources_c.guess_result_key(filepath=r'file.extension1234')
    # Define the path and extension where the main result data can be found
    my_data_sources_c.set_result_file_path(filepath=r'file.extension1234', key=my_file_key)

**d) Function** :func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`

If the results are not entirely in the same file you need to use this function.
For example the '.d3plot' files does not contain information related to Units,
however, if the simulation was run through Mechanical, a file.actunits file is
produced and need to be added.

.. code-block:: python
    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_d = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_d.set_result_file_path(filepath=r'file.extension', key='extension')
    # Add the additional result data to the DataSources object
    my_data_sources_d.add_file_path(filepath=r'file2.extension')

**e) Function** :func:`guess_second_key() <ansys.dpf.core.data_sources.DataSources.guess_second_key>`

If the results file have different extensions keys you need to use this function.
For example, we have a particular case for the Fluent and CFX results files that
often have one case and one data file (``file.cas.h5`` and ``file.dat.h5`` respectively).
In this case, you need to use the two following functions:
:func:`guess_second_key() <ansys.dpf.core.data_sources.DataSources.guess_second_key>` and
:func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`

Note that the ``file.cas.h5`` have to be declared as the main result data source (by the
:func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function)

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_e = dpf.DataSources()
    # Define the extensions keys for the files in the given paths
    my_file_key1 = my_data_sources_e.guess_result_key(filepath=r'file1.extension1.extension2')
    my_file_key2 = my_data_sources_e.guess_result_key(filepath=r'file2.extension3.extension4')
    # Define the path where the main result data can be found
    my_data_sources_e.set_result_file_path(filepath=r'file1.extension1.extension2', key=my_file_key1)
    # Add the additional result data to the DataSources object
    my_data_sources_e.add_file_path(filepath=r'file2.extension3.extension4', key=my_file_key2)

If you know the extensions keys you can the first extension key as an argument

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_e = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_e.set_result_file_path(filepath=r'file1.extension1.extension2', key="extension1")
    # Add the additional result data to the DataSources object
    my_data_sources_e.add_file_path(filepath=r'file2.extension3.extension4', key="extension3")

**f) Function** :func:`add_upstream() <ansys.dpf.core.data_sources.DataSources.add_upstream>`

If you believe needing a recursive workflow, you need to create a new ``DataSources``
object with the involved data and then add it as an upstream in the main ``DataSources``
object. Upstream refers to a source that provides data to a particular process.
For example, the expansion of the analysis results data is recursive in DPF.

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the main DataSources object
    my_data_sources_f = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_f.set_result_file_path(filepath=r'file0.extension0', key='extension0')

    # Create the DataSources object for the upstream data
    my_data_sources_upstream_f = dpf.DataSources()
    # Define the path where the main upstream data can be found
    my_data_sources_upstream_f.set_result_file_path(filepath=r'file1.extension1', key='extension1')

    # Add the upstream DataSources to the main DataSources object
    my_data_sources_f.add_upstream(upstream_data_sources=my_data_sources_upstream_f)

**g) Functions** :func:`set_domain_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_domain_result_file_path>`
and :func:`add_domain_file_path() <ansys.dpf.core.data_sources.DataSources.add_domain_file_path>`

If you need to post-process an analysis results that are distributed in two files,
you can merge them directly at the DataSources indentation.

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_g = dpf.DataSources()
    # Define the path where the main result data can be found and specify its domain
    my_data_sources_g.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
    # Add the additional result data to the DataSources object and specify its domain
    my_data_sources_g.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

If you need to post-process an analysis results from/into different servers, you
can also work in different remotes processes. This application is explained in
details in the :ref:`Examples for postprocessing on distributed processes <distributed_post>`
section in the examples documentation webpage

**h) Function** :func:`add_upstream_for_domain() <ansys.dpf.core.data_sources.DataSources.add_upstream_for_domain>`

If you believe needing a recursive workflow, and you have more than one results file,
you need to create a new ``DataSouces`` object with the involved data and then add
it as an upstream in the correspondent main ``DataSources`` object.

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the main DataSources object
    my_data_sources_h = dpf.DataSources()
    # Define the path where the main result data can be found and specify its domain
    my_data_sources_h.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
    # Add the additional result data to the DataSources object and specify its domain
    my_data_sources_h.add_domain_file_path(filepath=r"file1.extension1", key='extension1', domain_id=1)

    # Create the DataSources object for the upstream data
    my_data_sources_upstream_g = dpf.DataSources()
    # Define the path where the main upstream data can be found
    my_data_sources_upstream_g.set_result_file_path(filepath=r'file2.extension2', key='extension2')

    # Add the upstream DataSources to the main DataSources object and specify its domain
    my_data_sources_g.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g, domain_id=1)

**i) Function** :func:`add_file_path_for_specified_result() <ansys.dpf.core.data_sources.DataSources.add_file_path_for_specified_result>`

**j) Function** :func:`register_namespace() <ansys.dpf.core.data_sources.DataSources.register_namespace>`

When using an operator that requires data from a DataSources, DPF needs to find
in its code an internal correspondence to this call. This correspondence is given
by the namespace, the file extension and the operator name: ``namespace::key::operator_name``.

For example, if the results file comes from a MAPDL solver and has an '.rst' extension
and you want to get the displacement results in this file, DPF code will get the
correspondence: ``mapdl::rst::displacement``.

So, if you have an extension that is not
know by DPF you have to define its namespace. This function is mainly used when
creating your own operators and plugins, or when you have a file with an unknown
namespace but you know that it corresponds to certain solver.

The accepted namespaces are those that combine the solvers and its extensions in the
list: :ref:`Supported apps by DPF and their related formats <list_extensions_solvers>`

.. code-block:: python
    from ansys.dpf import core as dpf
    # Create the main DataSources object
    my_data_sources_j = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_j.set_result_file_path(filepath=r'file.extension', key='extension')
    # Define the namespace for the results in the given path
    my_data_sources_j.register_namespace(result_key='extension', namespace='namespace')


DataSources exploring
---------------------

You can check some properties that your ``DataSources`` object have by using
a helper. They are:

**k) Helper** :attr:`result_key <ansys.dpf.core.data_sources.DataSources.result_key>`

Give which file extension was used by your ``DataSources``.

This extension correspond to the given file, either with the :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function,
either if you called the class with the file path as an argument

If the file that you set had more than one extension, only the first one will be returned

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_k = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_k.set_result_file_path(filepath=r'file.extension', key='extension')

    # Print the result file extension key
    print(my_data_sources_k.result_key)
    # 'extension'

**l) Helper** :attr:`result_files <ansys.dpf.core.data_sources.DataSources.result_files>`

Give the list o list of result files contained in the ``DataSources``. It
returns the file path of those files

- If you use the :py:func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function it will return only the file path given as an argument to this function

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_l1 = dpf.DataSources()
    # Define the path where the main result data can be found
    my_data_sources_l1.set_result_file_path(filepath=r'file.extension', key='extension')
    # Add the additional result data to the DataSources object
    my_data_sources_l1.add_file_path(filepath=r'file2.extension')

    # Print the path to the main file
    print(my_data_sources_l1.result_files)
    # ['/folder/file.extension]

- If you added an upstream result file, it will not be listed in the main ``DataSources`` object. You have to check directly in the ``DataSources`` object created to define the upstream data

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the main DataSources object containing the given file
    my_data_sources_l2 = dpf.DataSources(result_path=r'file0.extension0')

    # Create the DataSources object for the upstream data
    my_data_sources_upstream_l2 = dpf.DataSources(result_path=r'file1.extension1')
    # Add the additional upstream data to the upstream DataSources object
    my_data_sources_upstream_l2.add_file_path(filepath=r'file2.extension2')

    # Add the upstream DataSources to the main DataSources object
    my_data_sources_l2.add_upstream(upstream_data_sources=my_data_sources_upstream_l2)

    # Print the path to the main file of the main DataSources object
    print(my_data_sources_l2.result_files)
    # ['/folder/file0.extension0]

- If your checking the DataSources object created to define the upstream data, only the first one will be listed

.. code-block:: python

    # Print the path to the upstream file of the upstream DataSources object
    print(my_data_sources_upstream_l2.result_files)
    # ['/folder/file1.extension1]

- If you have a ``DataSources`` object with more than one domain, a empty list will be returned

.. code-block:: python

    from ansys.dpf import core as dpf
    # Create the DataSources object
    my_data_sources_l3 = dpf.DataSources()
    # Define the path where the main result data can be found and specify its domain
    my_data_sources_l3.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
    # Add the additional result data to the DataSources object and specify its domain
    my_data_sources_l3.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

    print(my_data_sources_l3.result_files)
    # [None,None]
