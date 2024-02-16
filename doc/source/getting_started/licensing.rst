.. _ref_licensing:

===============
About licensing
===============

This section details what the user should expect in terms of limitations or license usage
when running PyDPF scripts.
As explained in "", DPF follows a client-server architecture,
which means that the PyDPF client library must interact with a DPF server.
It thus either starts a DPF server via a local installation of DPF,
or it connects to an already running local or remote DPF server.

DPF is installed along with ANSYS since ANSYS 2021R1 (see :ref:`ref_compatibility`).
It is also available as a standalone application (see :ref:`_ref_getting_started_with_dpf_server`).


License agreement
-----------------

When using the DPF Server from an ANSYS installation, the user has already agreed to the licensing
terms when installing ANSYS, thus there is no required step.

When using a standalone DPF Server, the user needs to accept the ``DPF Preview License Agreement``
by following indications in :ref:`_target_to_license_terms`.
Starting a DPF Server without agreeing to the ``DPF Preview License Agreement`` throws an exception.


License checks and usage
------------------------

Some DPF operators require DPF to check for an existing license
and some require DPF to check-out a compatible license increment.

To check which ANSYS licensing increments provide rights to use DPF Server,
go to :ref:`_target_to_ansys_license_increments_list`.

DPF is by default allowed to check-out license increments as needed.
To change this behavior, see :ref:`_user_guide_server_context`.

To know if operators require a license increment check-out to run, check their ``license``
attribute in :ref:`_ref_dpf_operators_reference` or directly in Python by checking the operator's
properties for a ``license`` key:

.. code-block:: python

    import ansys.dpf.core as dpf

    operator = dpf.operators.averaging.elemental_difference()
    print(operator.specification.properties)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    {'category': 'averaging', 'exposure': 'public', 'license': 'any_dpf_supported_increments', 'plugin': 'core', 'scripting_name': 'elemental_difference', 'user_name': 'elemental difference (field)'}


Even if an operator does not require a license check-out to run, most DPF operators still require
DPF to check for an reachable license server or license file.

Operators which do not perform any kind of license check are source operators (data extraction
operators) which do not perform any data transformation.

For example, most ``metadata`` operators do not perform data transformation and are license-free.

When considering ``result`` operators, they only perform data transformation if the requested
``location`` is not the native result location. In that case, averaging occurs which is considered
as data transformation.


Summary
-------

The following user actions may fail due to licensing:

- Starting a standalone DPF Server (a.k.a. not using an ANSYS installation) may fail due to the
  ``DPF Preview License Agreement`` (see **License agreement** above).
- Creating an operator may fail if the operator performs data transformation and no license server
  or license file is found (see **License checks and usage** above).
- Running an operator requiring a license checkout may fail if no license increment is available
  or if the DPF Server context is Entry, preventing any license check-out
  (see **License checks and usage** above).
