.. _ref_tutorials_data_sources:

===========
DataSources
===========

``DataSources`` is a class available as a submodule of the 'ansys.dpf.core'
package. It manages paths to their files. Use this object to declare data
inputs for DPF and define their locations.

This tutorial describes the behavior of the ``DataSources`` class
for all files formats accepted by PyDPF-Core:

.. include:: ../../substitution_solvers.rst

.. _ref_list_extensions_solvers:

Solver output formats supported by DPF
++++++++++++++++++++++++++++++++++++++

   - MAPDL files: |MAPDL_files|
   - LS-DYNA files: |LS-DYNA_files|
   - Fluent files: |Fluent_files1| and |Fluent_files2|
   - CFX files: |CFX_files1| and |CFX_files2|

This tutorial will present a general code, with generic files, and examples
with results files available with the PyDPF-Core package.

DataSources creation
--------------------

**a) Class** :class:`DataSources <ansys.dpf.core.data_sources.DataSources>`
When dealing with a single file of a format listed above,
instantiate a ``DataSources`` directly with the
file path as an argument :

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create a DataSources object for a single file
            my_data_sources_a = dpf.DataSources(result_path=r'file.extension')

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Create a DataSources object for a single file
            my_data_sources_a = dpf.DataSources(result_path=examples.find_simple_bar())

Generate a raw string (by putting the letter 'r' before
the file path string) in order to ensure the file path is read correctly.

**b) Function** :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>`

If the extension key is not in the list above (For example: a file.binout can
sometimes be named as 'file.binout0000') but you know what the extension key is,
the DataSources object can be created by:

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_b = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_b.set_result_file_path(filepath=r'file.extension1234', key='extension')

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Create the DataSources object
            my_data_sources_b = dpf.DataSources()
            # Define the path where the main result data can be found
            path = examples.find_simple_bar()
            'C:/Users/user/AppData/local/temp/ASimpleBar.rst'
            my_data_sources_b.set_result_file_path(filepath=r'C:/Users/user/AppData/local/temp/ASimpleBar.rst', key='rst')

**c) Function** :func:`guess_result_key() <ansys.dpf.core.data_sources.DataSources.guess_result_key>`

If the extension key is not in the list above (For example: a file.binout can
sometimes be named as 'file.binout0000') but you don't know what the extension
key is, the DataSources object can be created by:

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_c = dpf.DataSources()
            # Define the extension key for the file in the given path
            my_file_key = my_data_sources_c.guess_result_key(filepath=r'file.extension1234')
            # Define the path and extension where the main result data can be found
            my_data_sources_c.set_result_file_path(filepath=r'file.extension1234', key=my_file_key)

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result file
            path = examples.download_binout_matsum()
            print(path)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            path = examples.download_binout_matsum()
            print(path)

        .. code-block:: python

            # Create the DataSources object
            my_data_sources_c = dpf.DataSources()
            # Define the extension key for the file in the given path
            my_file_key = my_data_sources_c.guess_result_key(filepath=path)
            print(my_file_key)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            path = examples.download_binout_matsum()
            my_data_sources_c = dpf.DataSources()
            my_file_key = my_data_sources_c.guess_result_key(filepath=path)
            print(my_file_key)

        .. code-block:: python

            # Define the path and extension where the main result data can be found
            my_data_sources_c.set_result_file_path(filepath=path, key=my_file_key)


**d) Function** :func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`

If the results are not in the same file, you must use this function.
For example, if the '.d3plot' files does not contain information related to units, but
the simulation was run through Mechanical, a file.actunits file is
produced and must be added.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_d = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_d.set_result_file_path(filepath=r'file.extension', key='extension')
            # Add the additional result data to the DataSources object
            my_data_sources_d.add_file_path(filepath=r'file2.extension')

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result file
            paths = examples.download_d3plot_beam()
            print(paths)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_d3plot_beam()
            print(paths)

        .. code-block:: python

            # Create the DataSources object
            my_data_sources_d = dpf.DataSources()
            # Define the path where the main result data can be found
            # The variable 'paths' is a list so we chose the file by its index
            my_data_sources_d.set_result_file_path(filepath=paths[0], key='d3plot')
            # Add the additional result data to the DataSources object
            my_data_sources_d.add_file_path(filepath=paths[3], key='actunits')

**e) Function** :func:`guess_second_key() <ansys.dpf.core.data_sources.DataSources.guess_second_key>`

If the results file has different extensions keys, you must use this function.
For example, there is a specific case for the Fluent and CFX results files that
often have one case and one data file (``file.cas.h5`` and ``file.dat.h5`` respectively).
In this case, you must use the two following functions:
:func:`guess_second_key() <ansys.dpf.core.data_sources.DataSources.guess_second_key>` and
:func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`.

Note that ``file.cas.h5`` has to be declared as the main result data source (by the
:func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function).

.. tab-set::

    .. tab-item:: Generic code

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

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_fluent_axial_comp()
            print(paths)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_fluent_axial_comp()
            print(paths)

        .. code-block:: python

            # Create the DataSources object
            my_data_sources_e = dpf.DataSources()
            # Define the extensions keys for the files in the given paths
            # We see that the paths are given in a dictionary.
            # So to chose the correct file you need to give as an argument:
            # - the list label
            # - the file index in that list
            my_file_key1 = my_data_sources_e.guess_second_key(filepath=paths['cas'][0])
            my_file_key2 = my_data_sources_e.guess_second_key(filepath=paths['dat'][0])
            print(my_file_key1)
            print(my_file_key2)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_fluent_axial_comp()
            my_data_sources_e = dpf.DataSources()
            my_file_key1 = my_data_sources_e.guess_second_key(filepath=paths['cas'][0])
            my_file_key2 = my_data_sources_e.guess_second_key(filepath=paths['dat'][0])
            print(my_file_key1)
            print(my_file_key2)

        .. code-block:: python

            # Define the path where the main result data can be found
            my_data_sources_e.set_result_file_path(filepath=paths['cas'][0], key=my_file_key1)
            # Add the additional result data to the DataSources object
            my_data_sources_e.add_file_path(filepath=paths['dat'][0], key=my_file_key2)

If you know the two extensions keys, you can add the first extension key as the argument.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_e = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_e.set_result_file_path(filepath=r'file1.extension1.extension2', key="extension1")
            # Add the additional result data to the DataSources object
            my_data_sources_e.add_file_path(filepath=r'file2.extension3.extension4', key="extension3")

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_fluent_axial_comp()
            # Create the DataSources object
            my_data_sources_e = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_e.set_result_file_path(filepath=paths['cas'][0], key="cas")
            # Add the additional result data to the DataSources object
            my_data_sources_e.add_file_path(filepath=paths['dat'][0], key="dat")

**f) Function** :func:`add_upstream() <ansys.dpf.core.data_sources.DataSources.add_upstream>`

To create a recursive workflow, create a new ``DataSources``
object with the required data and then add it upstream in the main ``DataSources``
object. Upstream refers to a source that provides data to a particular process.
For example, the expansion of the analysis results data is recursive in DPF.

.. tab-set::

    .. tab-item:: Generic code

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

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_msup_files_to_dict()
            # Create the main DataSources object
            my_data_sources_f = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_f.set_result_file_path(filepath=paths["rfrq"],  key='rfrq')

            # Create the DataSources object for the upstream data
            my_data_sources_upstream_f = dpf.DataSources()
            # Define the path where the main upstream data can be found
            my_data_sources_upstream_f.set_result_file_path(filepath=paths["mode"])
            # Add the additional upstream data to the upstream DataSources object
            my_data_sources_upstream_f.add_file_path(filepath=paths["rst"], key='rst')

            # Add the upstream DataSources to the main DataSources object
            my_data_sources_f.add_upstream(upstream_data_sources=my_data_sources_upstream_f)


**g) Functions** :func:`set_domain_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_domain_result_file_path>`
and :func:`add_domain_file_path() <ansys.dpf.core.data_sources.DataSources.add_domain_file_path>`

To post-process analysis results that are distributed in two files,
you can merge them directly at the DataSources indentation.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_g = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            my_data_sources_g.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_g.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_distributed_files()
            # Create the DataSources object
            my_data_sources_g = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            my_data_sources_g.set_domain_result_file_path(path=paths[0], key='rst', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_g.add_domain_file_path(filepath=paths[1], key='rst', domain_id=1)

To post-process an analysis results from/into different servers, you
can also work in different remotes processes. This application is explained in
details in the :ref:`Examples for postprocessing on distributed processes <distributed_post>`
section in the examples documentation webpage

**h) Function** :func:`add_upstream_for_domain() <ansys.dpf.core.data_sources.DataSources.add_upstream_for_domain>`

To create a recursive workflow, and you have more than one results file,
create a new ``DataSouces`` object with the required data and then add
it as an upstream in the corresponding main ``DataSources`` object.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the main DataSources object
            my_data_sources_h = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            my_data_sources_h.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_h.add_domain_file_path(filepath=r"file1.extension1", key='extension1', domain_id=1)

            # Create the DataSources object for the upstream data
            my_data_sources_upstream_h = dpf.DataSources()
            # Define the path where the main upstream data can be found
            my_data_sources_upstream_h.set_result_file_path(filepath=r'file2.extension2', key='extension2')

            # Add the upstream DataSources to the main DataSources object and specify its domain
            my_data_sources_h.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_h, domain_id=1)

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.find_distributed_msup_folder()
            # Create the main DataSources object
            my_data_sources_h = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            # We use a format string here because the function used to define the path gives the path to a folder
            my_data_sources_h.set_domain_result_file_path(path=path=rf"{paths}\file_load_1.rfrq", key='rfrq', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_h.add_domain_file_path(filepath=rf"{paths}\file_load_2.rfrq", key='rfrq', domain_id=1)

            # Create the DataSources object for the first and second upstream datas
            my_data_sources_upstream_g0 = dpf.DataSources()
            my_data_sources_upstream_g1 = dpf.DataSources()
            # Define the path where the main upstream datas can be found
            my_data_sources_upstream_g0.set_result_file_path(filepath=rf"{paths}\file0.mode", key='mode')
            my_data_sources_upstream_g1.set_result_file_path(filepath=rf"{paths}\file1.mode", key='mode')
            # Add the additionalS upstream dataS to the upstream DataSources objectS
            my_data_sources_upstream_g0.add_file_path(filepath=rf"{paths}\file0.rst", key='rst')
            my_data_sources_upstream_g1.add_file_path(filepath=rf"{paths}\file1.rst", key='rst')

            # Add the upstream DataSources to the main DataSources object and specify its domain
            my_data_sources_g.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g0, domain_id=0)
            my_data_sources_g.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g1, domain_id=1)

**i) Function** :func:`add_file_path_for_specified_result() <ansys.dpf.core.data_sources.DataSources.add_file_path_for_specified_result>`

**j) Function** :func:`register_namespace() <ansys.dpf.core.data_sources.DataSources.register_namespace>`

When using an operator that requires data from a ``DataSources`` object, DPF must find
a corresponding entry to this call in its code. This entry is given
by the namespace, the file extension, and the operator name: ``namespace::key::operator_name``.

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

Give which file extension was used by your ``DataSources``. This extension corresponds to the given file,
either with the :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function,
either if you called the class with the file path as an argument.

If the file that you set had more than one extension, only the first one is returned:

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf

            # Create the DataSources object
            my_data_sources_k = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_k.set_result_file_path(filepath=r'file.extension', key='extension')

            # Print the result file extension key
            print(my_data_sources_k.result_key)
            'extension'

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result file
            path = examples.find_simple_bar()
            # Create the DataSources object
            my_data_sources_k = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_k.set_result_file_path(filepath=path)

            # Print the result file extension key
            print(my_data_sources_k.result_key)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            path = examples.find_simple_bar()
            my_data_sources_k = dpf.DataSources()
            my_data_sources_k.set_result_file_path(filepath=path)
            print(my_data_sources_k.result_key)


**l) Helper** :attr:`result_files <ansys.dpf.core.data_sources.DataSources.result_files>`

Give the list a list of result files contained in the ``DataSources`` object. It
returns the file path of those files.

- If you use the :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>` function, it will return only the file path given as an argument to this function.

.. tab-set::

    .. tab-item:: Generic code

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

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_d3plot_beam()
            # Create the DataSources object
            my_data_sources_l1 = dpf.DataSources()
            # Define the path where the main result data can be found
            my_data_sources_l1.set_result_file_path(filepath=paths[0], key='d3plot')
            # Add the additional result data to the DataSources object
            my_data_sources_l1.add_file_path(filepath=paths[3], key='actunits')

            # Print the path to the main file
            print(my_data_sources_l1.result_files)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_d3plot_beam()
            my_data_sources_l1 = dpf.DataSources()
            my_data_sources_l1.set_result_file_path(filepath=paths[0], key='d3plot')
            my_data_sources_l1.add_file_path(filepath=paths[3], key='actunits')
            print(my_data_sources_l1.result_files)


- If you added an upstream result file, it is not listed in the main ``DataSources`` object. You have to check directly in the ``DataSources`` object created to define the upstream data.

.. tab-set::

    .. tab-item:: Generic code

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
            '['/folder/file0.extension0]'

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_msup_files_to_dict()
            # Create the main DataSources object containing the given file
            my_data_sources_l2 = dpf.DataSources(result_path=paths["rfrq"])

            # Create the DataSources object for the upstream data
            my_data_sources_upstream_l2 = dpf.DataSources(result_path=paths["mode"])
            # Add the additional upstream data to the upstream DataSources object
            my_data_sources_upstream_l2.add_file_path(filepath=paths["rst"], key='rst')

            # Add the upstream DataSources to the main DataSources object
            my_data_sources_l2.add_upstream(upstream_data_sources=my_data_sources_upstream_l2)

            # Print the path to the main file of the main DataSources object
            print(my_data_sources_l2.result_files)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_msup_files_to_dict()
            my_data_sources_l2 = dpf.DataSources(result_path=paths["rfrq"])
            my_data_sources_upstream_l2 = dpf.DataSources(result_path=paths["mode"])
            my_data_sources_upstream_l2.add_file_path(filepath=paths["rst"], key='rst')
            my_data_sources_l2.add_upstream(upstream_data_sources=my_data_sources_upstream_l2)
            print(my_data_sources_l2.result_files)


- If you are checking the DataSources object created to define the upstream data, only the first one is listed.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            # Print the path to the upstream file of the upstream DataSources object
            print(my_data_sources_upstream_l2.result_files)
            ' ['/folder/file1.extension1]'

    .. tab-item:: Example

        .. code-block:: python

            # Print the path to the upstream file of the upstream DataSources object
            print(my_data_sources_upstream_l2.result_files)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_msup_files_to_dict()
            my_data_sources_l2 = dpf.DataSources(result_path=paths["rfrq"])
            my_data_sources_upstream_l2 = dpf.DataSources(result_path=paths["mode"])
            my_data_sources_upstream_l2.add_file_path(filepath=paths["rst"], key='rst')
            my_data_sources_l2.add_upstream(upstream_data_sources=my_data_sources_upstream_l2)
            print(my_data_sources_upstream_l2.result_files)

- If you have a ``DataSources`` object with more than one domain, a empty list is returned.

.. tab-set::

    .. tab-item:: Generic code

        .. code-block:: python

            from ansys.dpf import core as dpf
            # Create the DataSources object
            my_data_sources_l3 = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            my_data_sources_l3.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_l3.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

            print(my_data_sources_l3.result_files)
            '[None,None]'

    .. tab-item:: Example

        .. code-block:: python

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples

            # Download the result files
            paths = examples.download_distributed_files()
            # Create the DataSources object
            my_data_sources_l3 = dpf.DataSources()
            # Define the path where the main result data can be found and specify its domain
            my_data_sources_l3.set_domain_result_file_path(path=paths[0], key='rst', domain_id=0)
            # Add the additional result data to the DataSources object and specify its domain
            my_data_sources_l3.add_domain_file_path(filepath=paths[1], key='rst', domain_id=1)

            print(my_data_sources_l3.result_files)

        .. rst-class:: sphx-glr-script-out

         .. exec_code::
            :hide_code:

            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            paths = examples.download_distributed_files()
            my_data_sources_l3 = dpf.DataSources()
            my_data_sources_l3.set_domain_result_file_path(path=paths[0], key='rst', domain_id=0)
            my_data_sources_l3.add_domain_file_path(filepath=paths[1], key='rst', domain_id=1)
            print(my_data_sources_l3.result_files)