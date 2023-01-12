.. _user_guide_server_context:

==============
Server context
==============

The :class:`ServerContext <ansys.dpf.core.server_context.ServerContext>` class drives the
default capabilities a server starts with.

The server context is composed of the following information:

- ``context_type``, a :class:`LicensingContextType <ansys.dpf.core.server_context.LicensingContextType>`
  class object that defines whether a license checkout is required.
- ``xml_path``, which sets DPF default operator capabilities.

For more information, see the :class:`AvailableServerContexts <ansys.dpf.core.server_context.AvailableServerContexts>`
class and :ref:`user_guide_xmlfiles`.

Two main licensing context type capabilities are available: 

- **Entry:** This context, which is the default, loads the minimum capabilities without requiring any license checkout.
- **Premium:** This context enables **Entry** capabilities and the capabilities that require a license checkout, making
  more operators available.

For the operator list for each licensing context type, see :ref:`ref_dpf_operators_reference`.

Entry capabilities
------------------

The following code finds the list of operators available when the :ref:`ref_dpf_operators_reference` context
is **Entry**. This context won't check out any license.

.. code-block::
	   
    from ansys.dpf import core as dpf
    entry_server = dpf.start_local_server()
    print(entry_server.context)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.entry with no xml path

Premium capabilities
--------------------

The following code find the list of operators available when the context is :ref:`ref_dpf_operators_reference`
context is **Premium**. This context checks out a license.

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
	   
Change server context from Entry to Premium
-------------------------------------------

Once a DPF Server is started in **Entry** context, it can be upgraded to the
**Premium** context:

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


Change the default server context
---------------------------------

The default context for the server is **Entry**. You can change the context using
the ``ANSYS_DPF_SERVER_CONTEXT`` environment variable. For more information, see
the :module: `<ansys.dpf.core.server_context>` module). You can also change the server context
with this code:

.. code-block::

    from ansys.dpf import core as dpf
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    print(dpf.server_context.SERVER_CONTEXT)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.premium with no xml path


Release history
---------------

The **Entry** server context is available in server version 6.0 
(Ansys 2023 R2) and later. 

With a server version earlier than 6.0, **Premium** is the default server
context and all **Premium** :ref:`ref_dpf_operators_reference` 
are available, depending only on their release date.