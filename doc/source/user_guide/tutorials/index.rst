.. _ref_tutorials_index:

Tutorials
---------

What you need to know
+++++++++++++++++++++

These tutorials go through the steps required to access, analyze,
and transform simulation data using  PyDPF-Core.

Tutorials are more substantive and complex than examples. They are designed to teach how to perform a task and understand
the underlying concepts, providing detailed explanations at each stage, whereas examples showcase end-to-end specific processes.

DPF interacts with data stored in DPF data structures.
These DPF data structures are generated automatically when reading data from results file (`ref_to_section`) but they can also be generated from scratch (`ref_to_section`) when no supported result file is available.

Overview
++++++++

There are four main steps to transform simulation data into output data that can
be used to visualize and analyze simulation results:

    :bdg-dark-line:`Define simulation data` :octicon:`arrow-right;1em` :bdg-dark-line:`Store input data in DPF` :octicon:`arrow-right;1em` :bdg-dark-line:`Transform available data` :octicon:`arrow-right;1em` :bdg-dark-line:`Extract data`

The following tutorials go through each of these steps. Each tutorial presents code snippets specific to each supported file format.


.. topic:: Importing and opening results files


    .. grid:: 3

        .. grid-item-card:: I have one file
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Import and open a single result file with PyDPF-Core.

        .. grid-item-card:: I have more than one file
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Import and open multiple result files to be used in the same
           post-processing operation.

        .. grid-item-card:: I don’t know my file(s) type(s)
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           The result file extension key is unknown by the user.

.. topic:: Declare data from scratch


    .. grid:: 3

        .. grid-item-card:: Creating your own storage structures
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Create a field, fields container, mesh ... from scratch.

.. topic::  Access and extract results


    .. grid:: 3

        .. grid-item-card:: Narrow down data
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Scope the data by subsets of time (time sets, time steps.. )
           or space (nodes, elements... ).

        .. grid-item-card:: Extract and explore results data
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Get the available results data, results information ...

        .. grid-item-card:: Extract and explore results metadata
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Get the available results metadata (meshed region, mesh info... )
           and explore the mesh.

.. topic::  Transform data

    .. grid:: 3

        .. grid-item-card:: Using operators
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Read, manipulate, analyse the results data using PyDPF-Core operators.

        .. grid-item-card:: Create an workflow
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Create more complex operations and customizable results,
           by chaining operators together to create workflows.

.. topic::  Visualize the results


    .. grid:: 3

        .. grid-item-card:: Plotting
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Plotting methods for generating 3D plots of Ansys models directly from Python

        .. grid-item-card:: Animations
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center

           Animate the results over their evolution during the analysis

.. topic:: Export data


    .. grid:: 3

        .. grid-item-card:: Serialization
           :link: ref_tutorials_model
           :link-type: ref
           :text-align: center
