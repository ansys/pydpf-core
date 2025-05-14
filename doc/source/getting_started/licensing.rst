.. _ref_licensing:

=========
Licensing
=========

This section describes how to properly set up licensing, as well as limitations and license usage when running PyDPF scripts.

DPF follows a client-server architecture, so the PyDPF client library must interact with a running DPF Server.
It either starts a DPF Server via a local DPF Server installation, or it connects to an already running local or remote DPF Server.

DPF Server is packaged within the **Ansys installer** in Ansys 2021 R1 and later.
It is also available as a standalone application.
For more information on installing DPF Server, see :ref:`ref_dpf_server`.


.. _target_to_license_terms:

License terms
-------------

When using the DPF Server from an Ansys installation, you have already agreed to the licensing
terms when installing Ansys.

When using a standalone DPF Server, you must accept the ``DPF Preview License Agreement``
by following the indications below.
Starting a DPF Server without agreeing to the ``DPF Preview License Agreement`` creates an exception.

DPF Preview License Agreement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The standalone versions of DPF Server are protected using license terms specified in the `DPFPreviewLicenseAgreement <https://download.ansys.com/-/media/dpf/dpfpreviewlicenseagreement.ashx?la=en&hash=CCFB07AE38C638F0D43E50D877B5BC87356006C9>`_
file that can be found on the `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_
of the Ansys Customer Portal.
The ``DPFPreviewLicenseAgreement`` file is a text file, which means that you can open it with a text editor, such as ``Notepad``.

To accept the terms of this license agreement, you must set the following environment variable:

.. code::

    ANSYS_DPF_ACCEPT_LA=Y

The ``ANSYS_DPF_ACCEPT_LA`` environment variable confirms your acceptance of the DPF License Agreement.
By passing the value ``Y`` to this environment variable, you are indicating that you have a valid and
existing license for the edition and version of DPF Server that you intend to use.


.. _configure_licensing:

Configure licensing
-------------------

If your machine does not have a local Ansys installation, you must define where DPF should look for a valid license.

To use a local license file, set the ``ANSYSLMD_LICENSE_FILE`` environment
variable to point to an Ansys license file ``<license_file_to_use>``:

.. code::

    ANSYSLMD_LICENSE_FILE=<license_file_to_use>

To use a remote license, set the ``ANSYSLMD_LICENSE_FILE`` environment
variable to point to an Ansys license server ``<license_server_to_use>``:

.. code::

    ANSYSLMD_LICENSE_FILE=1055@<license_server_to_use>

For DPF Docker container usage only, you can use the following code to set both the ``ANSYS_DPF_ACCEPT_LA``
and ``ANSYSLMD_LICENSE_FILE`` environment variables. For the ``ANSYSLMD_LICENSE_FILE`` environment variable,
ensure that you replace ``<license_server_to_use>`` to point to the Ansys license server.

.. code::

    docker run -e "ANSYS_DPF_ACCEPT_LA=Y" -e ANSYSLMD_LICENSE_FILE=1055@<license_server_to_use> -p 50052:50052 -e DOCKER_SERVER_PORT=50052 --expose=50052 dpf-core:v2024_2_pre0

The next section provides information on
the Ansys license mechanism that is used with DPF Server.


.. _target_to_ansys_license_mechanism:

License checks and usage
------------------------

Some DPF operators require DPF to check for an existing license
and some require DPF to checkout a compatible license increment.

DPF is by default allowed to checkout license increments as needed.
To change this behavior, see :ref:`here <licensing_server_context>`.

To know if operators require a license increment checkout to run, check their ``license``
attribute in :ref:`ref_dpf_operators_reference` or directly in Python by checking the operator's
properties for a ``license`` key:

.. code-block:: python

    import ansys.dpf.core as dpf

    operator = dpf.operators.averaging.elemental_difference()
    print(operator.specification.properties)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    {'category': 'averaging', 'exposure': 'public', 'license': 'any_dpf_supported_increments', 'plugin': 'core', 'scripting_name': 'elemental_difference', 'user_name': 'elemental difference (field)'}


To check which Ansys licensing increments correspond to ``any_dpf_supported_increments``,
see :ref:`Compatible Ansys license increments<target_to_ansys_license_increments_list>`.

Even if an operator does not require a license checkout to run, most DPF operators still require
DPF to check for a reachable license server or license file.

Operators that do not perform any kind of license check are source operators (data extraction
operators). These operators do not perform any data transformation.

For example, when considering result operators, they perform data transformation if the requested
location is not the native result location. In that case, averaging occurs which is considered
as data transformation (such as elemental to nodal, nodal to elemental, or any other location change).

.. _licensing_server_context:

Server context
~~~~~~~~~~~~~~

You can allow or prevent licensed operators from running and using a license with a
:ref:`server context <user_guide_server_context>`:

- **Premium:** This default context allows DPF to perform license checkouts,
  making licensed DPF operators available.
- **Entry:** This context does not allow DPF to perform any license checkout,
  meaning that licensed DPF operators fail.

To update the context, apply a new server context:

.. code::

    server.apply_context(dpf.AvailableServerContexts.premium)

.. _licensing_errors:

Licensing errors
~~~~~~~~~~~~~~~~

The following user actions may fail due to licensing:

- Starting a standalone DPF Server may fail due to the
  ``DPF Preview License Agreement`` (see :ref:`target_to_license_terms`).
- Creating an operator may fail if the operator performs data transformation and no license server
  or license file is found (see :ref:`target_to_ansys_license_mechanism`).
- Running an operator requiring a license checkout may fail if no
  :ref:`compatible license increment <target_to_ansys_license_increments_list>`
  is available or if the DPF Server context is **Entry**, preventing any license check-out
  (see :ref:`licensing_server_context`).


.. _target_to_ansys_license_increments_list:

Compatible Ansys license increments
-----------------------------------

The following Ansys licensing increments provide rights to use the licensed DPF capabilities:

- ``preppost`` available in the ``Ansys Mechanical Enterprise PrepPost`` product
- ``meba`` available in the ``ANSYS Mechanical Enterprise Solver`` product
- ``mech_2`` available in the ``ANSYS Mechanical Premium`` product
- ``mech_1`` available in the ``ANSYS Mechanical Pro`` product
- ``ansys`` available in the ``ANSYS Mechanical Enterprise`` product
- ``dynapp`` available in the ``ANSYS LS-DYNA PrepPost`` product
- ``dyna`` available in the ``ANSYS LS-DYNA`` product
- ``vmotion`` available in the ``Ansys Motion`` product
- ``acpreppost`` available in the ``Ansys Mechanical Enterprise`` product
- ``acdi_adprepost`` available in the ``Ansys AUTODYN`` and ``Ansys AUTODYN PrepPost`` products
- ``cfd_preppost`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_preppost_pro`` available in the ``Ansys CFD Enterprise`` product
- ``vmotion_post`` available in the ``Ansys Motion Post`` product
- ``vmotion_pre`` available in the ``Ansys Motion Pre`` product
- ``advanced_meshing`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_meshing_pro`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_setup_post`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_setup_post_pro`` available in the ``Ansys CFD Enterprise`` product
- ``acfx_pre`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_base`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level1`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level2`` available in the ``Ansys CFD Enterprise`` product
- ``cfd_solve_level3`` available in the ``Ansys CFD Enterprise`` product
- ``fluent_meshing`` available in the ``Ansys CFD Enterprise`` product
- ``avrxp_snd_level1`` available in the ``Ansys Sound Pro`` product
- ``sherlock`` available in the ``Ansys Sherlock`` product

Each increment may be available in other products. On the Ansys Customer Portal,
the `Licensing section <https://download.ansys.com/Installation%20and%20Licensing%20Help%20and%20Tutorials>`_
provides product/increment mapping.
