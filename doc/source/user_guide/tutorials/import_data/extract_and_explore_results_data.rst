.. _ref_tutorials_extract_and_explore_results_data:

====================
Explore results data
====================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`

This tutorial shows how to extract and explore results data from a result file.

When you extract a result from a result file DPF stores it in a |Field|.
This |Field| will then contain the data of the result associated with it.

When DPF-Core returns the |Field| object, what Python actually has is a client-side
representation of the |Field|, not the entirety of the |Field| itself. This means
that all the data of the field is stored within the DPF service. This is important
because when building your workflows, the most efficient way of interacting with result data
is to minimize the exchange of data between Python and DPF, either by using operators
or by accessing exclusively the data that is needed.



