.. _user_guide_server_context:

==============
Server context
==============

What is server context
----------------------

The :class:`ServerContext <ansys.dpf.core.server_context.ServerContext>` class drives the
default capabilities a server starts with.

The server context is composed of the following information:

- ``context_type``, a :class:`LicensingContextType <ansys.dpf.core.server_context.LicensingContextType>`
  class object that defines if a License checkout is required or not.
- the ``xml_path`` that sets DPF default operators capabilities.

For more information,
see :class:`AvailableServerContexts <ansys.dpf.core.server_context.AvailableServerContexts>`
and :ref:`user_guide_xmlfiles`.

Two main licensing context type capabilities are available: 

- Entry (default): Loads the minimum capabilities without requiring any license checkout.
- Premium: Enables the entry capabilities and the capabilities that requires a license checkout.
  More operators are available.

The operators list for each licensing context type is available at
:ref:`ref_dpf_operators_reference`.

Getting started with Entry capabilities
---------------------------------------

Find the list of operators available when the context is Entry at :ref:`ref_dpf_operators_reference`.
This won't check out any license.

.. code-block::
	   
    from ansys.dpf import core as dpf
    entry_server = dpf.start_local_server()
    print(entry_server.context)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.entry with no xml path

Getting started with Premium capabilities
-----------------------------------------

Find the list of operators available when the context is Premium at :ref:`ref_dpf_operators_reference`.
This checks out a license.

.. code-block::
	   
    from ansys.dpf import core as dpf
    premium_server_context = dpf.AvailableServerContexts.premium
    premium_server = dpf.start_local_server(
        context=premium_server_context
    )
    print(premium_server.context)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path
	   
Changing server context from Entry to Premium
---------------------------------------------

Once an Entry server is started, it can be upgraded to Premium:

.. code-block::

    from ansys.dpf import core as dpf
    # start a server with entry capabilities
    server = dpf.start_local_server()
    print(server.context)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.entry with no xml path

.. code-block::
 
    # apply a premium context on the server
    server.apply_context(dpf.AvailableServerContexts.premium)
    print(server.context)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path


Changing the default server context
-----------------------------------

Entry is the default server context. This can be changed either using the ANSYS_DPF_SERVER_CONTEXT
environment variable (see `<ansys.dpf.core.server_context>`) or writing:

.. code-block::

    from ansys.dpf import core as dpf
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    print(dpf.server_context.SERVER_CONTEXT)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path


Release History
---------------

The Entry server context is available starting with server version 6.0 
(Ansys 2023 R2). 

With a server version lower than 6.0, Premium is the default server
context and all the Premium operators at :ref:`ref_dpf_operators_reference` 
are available (depending only on their release date).