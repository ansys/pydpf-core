.. _ref_tutorials_import_result_file:

=========================
Import result file in DPF
=========================

.. include:: ../../../links_and_refs.rst
.. |set_result_file_path| replace:: :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
.. |add_file_path| replace:: :func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`

This tutorial shows how to import a result file in DPF.

There are two approaches to import a result file in DPF:

- :ref:`Using the DataSources object <ref_import_result_file_data_sources>`
- :ref:`Using the Model object <ref_import_result_file_model>`

.. note::

    The |Model| extracts a large amount of information by default (results, mesh and analysis data).
    If using this helper takes a long time for processing the code, mind using a |DataSources| object
    and instantiating operators directly with it.

:jupyter-download-script:`Download tutorial as Python script<import_result_file>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<import_result_file>`

Define the result file path
---------------------------

Both approaches need a file path to be defined. For this tutorial, you can use a result file available in
the |Examples| module.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the .rst result file path
            result_file_path_11 = examples.find_static_rst()

            # Define the modal superposition harmonic analysis (.mode, .rfrq and .rst) result files paths
            result_file_path_12 = examples.download_msup_files_to_dict()

            print("Result file path 11:", "\n",result_file_path_11, "\n")
            print("Result files paths 12:", "\n",result_file_path_12, "\n")

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the .d3plot result files paths
            result_file_path_21 = examples.download_d3plot_beam()

            # Define the .binout result file path
            result_file_path_22 = examples.download_binout_matsum()

            print("Result files paths 21:", "\n",result_file_path_21, "\n")
            print("Result file path 22:", "\n",result_file_path_22, "\n")

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the project .flprj result file path
            result_file_path_31 = examples.download_fluent_axial_comp()["flprj"]

            # Define the CFF .cas.h5/.dat.h5 result files paths
            result_file_path_32 = examples.download_fluent_axial_comp()

            print("Result file path 31:", "\n",result_file_path_31, "\n")
            print("Result files paths 32:", "\n",result_file_path_32, "\n")

    .. tab-item:: CFX

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the project .res result file path
            result_file_path_41 = examples.download_cfx_mixing_elbow()

            # Define the CFF .cas.cff/.dat.cff result files paths
            result_file_path_42 = examples.download_cfx_heating_coil()

            print("Result file path 41:", "\n",result_file_path_41, "\n")
            print("Result files paths 42:", "\n",result_file_path_42, "\n")

.. _ref_import_result_file_data_sources:

Use a |DataSources|
-------------------

The |DataSources| object manages paths to their files. Use this object to declare data
inputs for PyDPF-Core APIs.

.. tab-set::

    .. tab-item:: MAPDL

        **a) `.rst` result file**

        Create the |DataSources| object and give the path to the result file to the *'result_path'* argument.

        .. jupyter-execute::

            # Create the DataSources object
            # Use the ``result_path`` argument and give the result file path
            ds_11 = dpf.DataSources(result_path=result_file_path_11)

        **b) `.mode`, `.rfrq` and `.rst` result files**

        In the modal superposition, modal coefficients are multiplied by mode shapes (of a previous modal analysis)
        to analyse a structure under given boundary conditions in a range of frequencies. Doing this expansion “on demand”
        in DPF instead of in the solver reduces the size of the result files.

        The expansion is recursive in DPF: first the modal response is read. Then, *upstream* mode shapes are found in
        the |DataSources|, where they are read and expanded. Upstream refers to a source that provides data to a
        particular process.

        To create a recursive workflow add the upstream |DataSources| object, that contains the upstream
        data files, to the main |DataSources| object.

        .. jupyter-execute::

            # Create the main DataSources object
            ds_12 = dpf.DataSources()
            # Define the main result file path
            ds_12.set_result_file_path(filepath=result_file_path_12["rfrq"], key='rfrq')

            # Create the upstream DataSources object with the main upstream file path
            upstream_ds_12 = dpf.DataSources(result_path=result_file_path_12["mode"])
            # Add the additional upstream file path to the upstream DataSources object
            upstream_ds_12.add_file_path(filepath=result_file_path_12["rst"])

            # Add the upstream DataSources to the main DataSources object
            ds_12.add_upstream(upstream_data_sources=upstream_ds_12)

    .. tab-item:: LSDYNA

        **a) `.d3plot` result file**

        The d3plot file does not contain information related to units. In this case, as the
        simulation was run  through Mechanical, a ``file.actunits``  file is produced. If this
        file is supplemented in the |DataSources|, the units will be correctly fetched for all
        results in the file as well as for the mesh.

        Thus, we must use the |set_result_file_path| and the |add_file_path| methods to add the main
        and the additional result file to the |DataSources| object.

        .. jupyter-execute::

            # Create the DataSources object
            ds_21 = dpf.DataSources()

            # Define the main result file path
            ds_21.set_result_file_path(filepath=result_file_path_21[0], key="d3plot")

            # Add the additional file path related to the units
            ds_21.add_file_path(filepath=result_file_path_21[3], key="actunits")

        **b) `.binout` result file**

        The extension key *`.binout`* is not explicitly specified in the result file. Thus, we use
        the |set_result_file_path| method and give the extension key to the *'key'* argument to correctly
        add the result file path to the |DataSources| object.

        .. jupyter-execute::

            # Create the DataSources object
            ds_22 = dpf.DataSources()

            # Define the path to the result file
            # Use the ``key`` argument and give the file extension key
            ds_22.set_result_file_path(filepath=result_file_path_22, key="binout")

    .. tab-item:: Fluent

        **a) `.flprj` result file**

        Create the |DataSources| object and give the path to the result file to the *'result_path'* argument.

        .. jupyter-execute::

            # Create the DataSources object
            # Use the ``result_path`` argument and give the result file path
            ds_31 = dpf.DataSources(result_path=result_file_path_31)

        **b) `.cas.h5`, `.dat.h5` result files**

        Here, we have a main and an additional result file with two extensions keys.

        Thus, you must use the |set_result_file_path| and the |add_file_path| methods to add the main and
        additional result file to the |DataSources| object and explicitly give the *first* extension key to
        their *'key'* argument.

        .. jupyter-execute::

            # Create the DataSources object
            ds_32 = dpf.DataSources()

            # Define the path to the main result file
            # Use the ``key`` argument and give the first extension key
            ds_32.set_result_file_path(filepath=result_file_path_32['cas'][0], key="cas")

            # Add the additional result file path to the DataSources
            # Use the ``key`` argument and give the first extension key
            ds_32.add_file_path(filepath=result_file_path_32['dat'][0], key="dat")

    .. tab-item:: CFX

        **a) `.res` result file**

        Create the |DataSources| object and give the path to the result file to the *'result_path'* argument.

        .. jupyter-execute::

            # Create the DataSources object
            # Use the ``result_path`` argument and give the result file path
            ds_41 = dpf.DataSources(result_path=result_file_path_41)

        **b) `.cas.cff`, `.dat.cff` result files**

        Here, we have a main and an additional result file with two extensions keys.

        Thus, you must use the |set_result_file_path| and the |add_file_path| methods to add the main and
        additional result file to the |DataSources| object. Also, you must explicitly give the *first* extension keys to
        the *'key'* argument.

        .. jupyter-execute::

            # Create the DataSources object
            ds_42 = dpf.DataSources()

            # Define the path to the main result file
            # Use the ``key`` argument and give the first extension key
            ds_42.set_result_file_path(filepath=result_file_path_42["cas"], key="cas")

            # Add the additional result file path to the DataSources
            # Use the ``key`` argument and give the first extension key
            ds_42.add_file_path(filepath=result_file_path_42["dat"], key="dat")

.. _ref_import_result_file_model:

Use a |Model|
-------------

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata and to instanciate results providers by opening a |DataSources| or a Streams.

To create a |Model| you can provide to the *'data_sources'* argument.:

- The result file path, in the case you are working with a single result file that has an explicit extension key;
- A |DataSources| object.

.. tab-set::

    .. tab-item:: MAPDL

        **a) `.rst` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            model_11 = dpf.Model(data_sources=result_file_path_11)

            # Create the model with the DataSources object
            model_12 = dpf.Model(data_sources=ds_11)

        **b) `.mode`, `.rfrq` and `.rst` result files**

        .. jupyter-execute::

            # Create the model with the DataSources object
            model_13 = dpf.Model(data_sources=ds_12)

    .. tab-item:: LSDYNA

        **a) `.d3plot` result file**

        .. jupyter-execute::

            # Create the model with the DataSources object
            model_21 = dpf.Model(data_sources=ds_21)

        **b) `.binout` result file**

        .. jupyter-execute::

            # Create the model with the DataSources object
            model_22 = dpf.Model(data_sources=ds_22)

    .. tab-item:: Fluent

        **a) `.flprj` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            model_31 = dpf.Model(data_sources=result_file_path_31)

            # Create the model with the DataSources object
            model_32 = dpf.Model(data_sources=ds_31)

        **b) `.cas.h5`, `.dat.h5` result files**

        .. jupyter-execute::

            # Create the model with the DataSources object
            model_33 = dpf.Model(data_sources=ds_32)

    .. tab-item:: CFX

        **a) `.res` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            model_41 = dpf.Model(data_sources=result_file_path_41)

            # Create the model with the DataSources object
            model_42 = dpf.Model(data_sources=ds_41)

        **b) `.cas.cff`, `.dat.cff` result files**

        .. jupyter-execute::

            # Create the model with the DataSources object
            model_43 = dpf.Model(data_sources=ds_42)

