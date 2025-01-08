.. _ref_dpf_operators_reference:

=========
Operators
=========

DPF operators allow you to manipulate and transform simulation data.

.. grid:: 1

   .. grid-item::
        .. card:: Operators
            :link-type: doc
            :link: operator_reference_load

            Click here to get started with operators available in DPF.

            +++
            .. button-link:: OPEN
               :color: primary
               :expand:
               :outline:
               :click-parent:              


For Ansys 2023 R2 and later, the DPF Server licensing logic for operators in DPF depends on the active
server context.

The available contexts are **Premium** and **Entry**.
Licensed operators are marked as such in the documentation using the ``license`` property.
Operators with the ``license`` property set to **None** do not require a license checkout.
For more information on using these two contexts, see :ref:`user_guide_server_context`.

.. note::

    For Ansys 2023 R1 and earlier, the context is equivalent to **Premium**, with all operators loaded.
    For DPF Server 2023.2.pre0 specifically, the server context defines which operators are loaded and
    accessible. Use the `PyDPF-Core 0.7 operator documentation <https://dpf.docs.pyansys.com/version/0.7/operator_reference.html>`_ to learn more.
    Some operators in the documentation might not be available for a particular server version.
