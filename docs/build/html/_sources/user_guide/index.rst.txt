.. _ref_user_guide:

==========
User Guide
==========

The ansys.dpf.core package is a python client API giving an easy access to
Data Processing Framework (DPF) post processing capabilities. Highly efficient computation, customization and remote post processing
is made accessible in python with this package.

This guide provides a general overview of the basics and usage of DPF.
The most common entities are presented :

- the Model in :ref:`user_guide_model` helps to access results and metadata from result files
- the Operator in :ref:`ref_user_guide_operators` is the only object used to create and transform the data
- the Field (contained in the Fields Container) :ref:`ref_user_guide_fields_container` is the main simulation data container.

A quick explaination on how to plot results via pyVista is also provided in :ref:`user_guide_plotting`.

.. toctree::
   :maxdepth: 2
   :hidden:

   model
   operators
   fields_container
   plotting
