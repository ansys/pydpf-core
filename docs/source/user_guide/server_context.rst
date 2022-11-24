.. _user_guide_server_context:

==============
Server context
==============

What is server context
----------------------

The :class:`ServerContext <ansys.dpf.core.server_context>` class drives the
default capabilities a server will be started with. 

The server context is composed of two main information: 
- context_type, :class:`LicensingContextType <ansys.dpf.core.server_context>`
class object, that defines if a License check out is required or not.
- the xml_path that sets DPF default operators capabilities. For more
information, see :class:`AvailableServerContexts <ansys.dpf.core.server_context>`
and :ref:`_user_guide_xmlfiles`.

Two main licensing context type capabilities are available: 
- Entry (default) that will load the minimum capabilities without requiring 
any license check out.
- Premium that will enable the entry capabilities and the capabilities that
requires a license check out. More operators will be available.

The operators list for each licensing context type is available at
:ref:`_ref_dpf_operators_reference`.

Getting started with Entry capabilities
---------------------------------------

Entry operators list is available at :ref:`_ref_dpf_operators_reference`.
This won't check out any license.

.. code-block::
	   
    from ansys.dpf import core as dpf
    entry_server = dpf.start_local_server()
    entry_server.context

Getting started with Premium capabilities
-----------------------------------------

Entry operators list is available at :ref:`_ref_dpf_operators_reference`.
This will check out a license.

.. code-block::
	   
    from ansys.dpf import core as dpf
    premium_server_context = dpf.AvailableServerContexts.premium
    premium_server = dpf.start_local_server(
        context=premium_server_context
    )
    print(premium_server.context)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path
	   
Changing server context from entry to Premium
---------------------------------------------

Once an entry server is started, it can be upgraded to premium:

.. code-block::

    from ansys.dpf import core as dpf
    # start a server with entry capabilities
    server = dpf.start_local_server()
    print(server.context)
	
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    Server Context of type LicensingContextType.entry with no xml path

.. code-block::
 
    # apply a premium context on the server
    server.apply_context(dpf.AvailableServerContexts.premium)
    print(server.context)

.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path


Changing default server context
-------------------------------

Entry is the default server context. This can be changed either using ANSYS_DPF_SERVER_CONTEXT
environment variable (see `<ansys.dpf.core.server_context>`) or writing:

.. code-block::

    from ansys.dpf import core as dpf
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    print(dpf.server_context.SERVER_CONTEXT)
	
.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path


