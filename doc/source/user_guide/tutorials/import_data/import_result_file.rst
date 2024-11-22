.. _ref_tutorials_import_result_file:

=========================
Import result file in DPF
=========================

.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`DataSources <ansys.dpf.core.data_sources.DataSources>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`
.. |set_result_file_path| replace:: :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
.. |add_file_path| replace:: :func:`add_file_path() <ansys.dpf.core.data_sources.DataSources.add_file_path>`

This tutorial shows how to import a result file in DPF.

You have two approaches to import a result file in DPF:

- Using the |DataSources| object
- Using the |Model| object

.. note::

    The |Model| extracts a large amount of information by default (results, mesh and analysis data).
    If using this helper takes a long time for processing the code, mind using a |DataSources| object
    and instantiating operators directly with it. Check the ":ref:`get_mesh_mesh_provider`" for more
    information on how to get a mesh from a result file.

Define the result file path
---------------------------

Both approaches need a file path to be defined. Here we will download result files available in
our |Examples| package.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops

            # Define the .rst result file
            result_file_path_11 = examples.find_static_rst()

            # Define the modal superposition harmonic analysis (.mode, .rfrq and .rst) result files
            result_file_path_12 = examples.download_msup_files_to_dict()

            print("1:", "\n",result_file_path_11, "\n")
            print("2:", "\n",result_file_path_12, "\n")

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops

            # Define the .d3plot result file
            result_file_path_21 = examples.download_d3plot_beam()

            # Define the .binout result file
            result_file_path_22 = examples.download_binout_matsum()

            print("1:", "\n",result_file_path_21, "\n")
            print("2:", "\n",result_file_path_22, "\n")

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops

            # Define the project .flprj result file
            result_file_path_31 = examples.download_fluent_axial_comp()["flprj"]

            # Define the CFF .cas.h5/.dat.h5 result files
            result_file_path_32 = examples.download_fluent_axial_comp()

            print("1:", "\n",result_file_path_31, "\n")
            print("2:", "\n",result_file_path_32, "\n")

    .. tab-item:: CFX

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops

            # Define the project .res result file
            result_file_path_41 = examples.download_cfx_mixing_elbow()

            # Define the CFF .cas.cff/.dat.cff result files
            result_file_path_42 = examples.download_cfx_heating_coil()

            print("1:", "\n",result_file_path_41, "\n")
            print("2:", "\n",result_file_path_42, "\n")

Use a |DataSources|
-------------------

The |DataSources| object manages paths to their files. Use this object to declare data
inputs for DPF operators and define their locations.

.. tab-set::

    .. tab-item:: MAPDL

        **a) `.rst` result file**

        You create the |DataSources| object by defining the the path to the main result file.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_11 = dpf.DataSources(result_path=result_file_path_11)

        **b) `.mode`, `.rfrq` and `.rst` result files**

        In the modal superposition, modal coefficients are multiplied by mode shapes (of a previous modal analysis)
        to analyse a structure under given boundary conditions in a range of frequencies. Doing this expansion “on demand”
        in DPF instead of in the solver reduces the size of the result files.

        The expansion is recursive in DPF: first the modal response is read. Then, “upstream” mode shapes are found in
        the data sources, where they are read and expanded.

        To create a recursive workflow you have to add the upstream data to the main |DataSources| object. Upstream refers
        to a source that provides data to a particular process.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_12 = dpf.DataSources()
            # Define the main result data
            my_data_sources_12.set_result_file_path(filepath=result_file_path_12["rfrq"], key='rfrq')

            # Create the upstream DataSources object with the main upstream data
            up_stream_ds_12 = dpf.DataSources(result_path=result_file_path_12["mode"])
            # Add the additional upstream data to the upstream DataSources object
            up_stream_ds_12.add_file_path(filepath=result_file_path_12["rst"])

            # Add the upstream DataSources to the main DataSources object
            my_data_sources_12.add_upstream(upstream_data_sources=up_stream_ds_12)

    .. tab-item:: LSDYNA

        **a) `.d3plot` result file**

        This LS-DYNA d3plot file contains several individual results, each at different times.
        The d3plot file does not contain information related to Units.  In this case, as the
        simulation was run  through Mechanical, a ``file.actunits``  file is produced. If this
        file is supplemented in the |DataSources|, the units will be correctly fetched for all
        results in the file as well as for the mesh.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_21 = dpf.DataSources()
            my_data_sources_21.set_result_file_path(filepath=result_file_path_21[0], key="d3plot")
            my_data_sources_21.add_file_path(filepath=result_file_path_21[3], key="actunits")

        **b) `.binout` result file**

        The extension key ``.binout`` is not specified in the result file. Thus, we use the
        |set_result_file_path| method to correctly implement the result file to the |DataSources| by giving
        explicitly the extension key as an argument.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_22 = dpf.DataSources()
            # Define the the path to the main result
            my_data_sources_22.set_result_file_path(filepath=result_file_path_22, key="binout")

    .. tab-item:: Fluent

        **a) `.flprj` result file**

        You create the |DataSources| object by defining the the path to the main result file.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_31 = dpf.DataSources(result_path=result_file_path_31)

        **b) `.cas.h5`, `.dat.h5` result files**

        Here we have a main and an additional result files. Thus, we use the
        |set_result_file_path| method, to correctly implement the result file to the |DataSources| by giving
        explicitly the first extension key as an argument, and the |add_file_path| method, to add the additional
        result file.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_32 = dpf.DataSources()
            # Define the path to the main result file
            my_data_sources_32.set_result_file_path(filepath=result_file_path_32['cas'][0], key="cas")
            # Add the additional result file to the DataSources
            my_data_sources_32.add_file_path(filepath=result_file_path_32['dat'][0], key="dat")

    .. tab-item:: CFX

        **a) `.res` result file**

        You create the |DataSources| object by defining the the path to the main result file.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_41 = dpf.DataSources(result_path=result_file_path_41)

        **b) `.cas.cff`, `.dat.cff` result files**

        Here we have a main and an additional result files. Thus, we use the
        |set_result_file_path| method, to correctly implement the result file to the |DataSources| by giving
        explicitly the first extension key as an argument, and the |add_file_path| method, to add the additional
        result file.

        .. jupyter-execute::

            # Create the DataSources object
            my_data_sources_42 = dpf.DataSources()
            # Define the path to the main result file
            my_data_sources_42.set_result_file_path(filepath=result_file_path_42["cas"], key="cas")
            # Add the additional result file to the DataSources
            my_data_sources_42.add_file_path(filepath=result_file_path_42["dat"], key="dat")

Use a |Model|
-------------

The |Model| is a helper designed to give shortcuts to the user to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.

To create a |Model| you can provide the result file path, in the case you are working with a single result
file with an explicit extension key, or a |DataSources| as an argument.

.. tab-set::

    .. tab-item:: MAPDL

        **a) `.rst` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            my_model_11 = dpf.Model(data_sources=result_file_path_11)

            # Create the model with the DataSources
            my_model_12 = dpf.Model(data_sources=my_data_sources_11)

        **b) `.mode`, `.rfrq` and `.rst` result files**

        .. jupyter-execute::

            # Create the model with the DataSources
            my_model_13 = dpf.Model(data_sources=my_data_sources_12)

    .. tab-item:: LSDYNA

        **a) `.d3plot` result file**

        .. jupyter-execute::

            # Create the model with the DataSources
            my_model_21 = dpf.Model(data_sources=my_data_sources_21)

        **b) `.binout` result file**

        .. jupyter-execute::

            # Create the model with the DataSources
            my_model_22 = dpf.Model(data_sources=my_data_sources_22)

    .. tab-item:: Fluent

        **a) `.flprj` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            my_model_31 = dpf.Model(data_sources=result_file_path_31)

            # Create the model with the DataSources
            my_model_32 = dpf.Model(data_sources=my_data_sources_31)

        **b) `.cas.h5`, `.dat.h5` result files**

        .. jupyter-execute::

            # Create the model with the DataSources
            my_model_33 = dpf.Model(data_sources=my_data_sources_32)

    .. tab-item:: CFX

        .. jupyter-execute::

        **a) `.res` result file**

        .. jupyter-execute::

            # Create the model with the result file path
            my_model_41 = dpf.Model(data_sources=result_file_path_41)

            # Create the model with the DataSources
            my_model_42 = dpf.Model(data_sources=my_data_sources_41)

        **b) `.cas.cff`, `.dat.cff` result files**

        .. jupyter-execute::

            # Create the model with the DataSources
            my_model_43 = dpf.Model(data_sources=my_data_sources_42)

