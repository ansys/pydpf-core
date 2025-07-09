.. _user_guide_server_context:

==============
Server context
==============

The :class:`ServerContext <ansys.dpf.core.server_context.ServerContext>` class drives the
licensing logic a server starts with.

The server context is composed of the following information:

- ``context_type``, a :class:`LicensingContextType <ansys.dpf.core.server_context.LicensingContextType>`
  class object that defines whether DPF capabilities requiring a license checkout are allowed.
- ``xml_path``, which sets DPF default operator capabilities.

For more information, see the :class:`AvailableServerContexts <ansys.dpf.core.server_context.AvailableServerContexts>`
class and :ref:`user_guide_xmlfiles`.

Two main licensing context type capabilities are available: 

- **Premium:** This default context allows DPF to perform license checkouts,
  making licensed DPF operators available.
- **Entry:** This context does not allow DPF to perform any license checkout,
  meaning that licensed DPF operators fail.

For the operator list, see :ref:`ref_dpf_operators_reference`.
	   
Change server context from Entry to Premium
-------------------------------------------

Once a DPF Server is started in **Entry** context, it can be upgraded to the
**Premium** context:

.. code-block::

    from ansys.dpf import core as dpf
    # start a server with entry capabilities
    server = dpf.start_local_server(
        context=dpf.AvailableServerContexts.entry
    )
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

The default context for the server is **Premium**. You can change the context using
the ``ANSYS_DPF_SERVER_CONTEXT`` environment variable. For more information, see
the :module: `<ansys.dpf.core.server_context>` module. You can also change the server context
with this code:

.. code-block::

    from ansys.dpf import core as dpf
    dpf.set_default_server_context(dpf.AvailableServerContexts.entry)
    print(dpf.server_context.SERVER_CONTEXT)
	
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    Server Context of type LicensingContextType.entry with no xml path

.. warning::
    As starting an ``InProcess`` server means linking the DPF binaries to your current Python
    process, you cannot start a new ``InProcess`` server. If your local ``InProcess`` server
    is already **Premium**, you cannot set it back as **Entry**.
    ``InProcess`` being the default server type, the proper commands to work as **Entry** should be
    set at the start of your script.



Release history
---------------

The **Entry** server context is available in server version 6.0 
(Ansys 2023 R2) and later. 

With a server version earlier than 6.0, **Premium** is the default server
context and all **Premium** :ref:`ref_dpf_operators_reference` 
are available, depending only on their release date.