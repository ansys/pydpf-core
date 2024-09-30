.. _ref_tutorials_index:

Tutorials
---------

What do you need to know
++++++++++++++++++++++++

This tutorials will guide you through the steps required to access, analyze,
and transform simulation data using  PyDPF-Core.

The tutorials are more substantive and complex than examples found in the standard
documentation set. They are designed to teach how to perform a task and understand
some concepts, providing detailed explanations at each stage.

DPF interacts with results data that have to be stored in some kind  of structure.
They can be automatically generated from the results file (detailed in the access
and extract results part ) or generated from scripting.

Overview
++++++++

There are four main steps to transform simulation data into output data that can
be used to visualize and analyze simulation results:

    :bdg-dark-line:`Define simulation data` :octicon:`arrow-right;1em` :bdg-dark-line:`Store input data in DPF` :octicon:`arrow-right;1em` :bdg-dark-line:`Transform available data` :octicon:`arrow-right;1em` :bdg-dark-line:`Extract data`

The following tutorials will guide through those steps:


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
