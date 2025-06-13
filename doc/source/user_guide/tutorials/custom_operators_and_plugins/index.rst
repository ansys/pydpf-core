.. _ref_tutorials_custom_operators_and_plugins:

Custom Operators and Plugins
----------------------------
You can enhance and customize your DPF installation by creating new operators and libraries of operators, called 'plugins'.

DPF offers multiple development APIs depending on your environment.

With support for custom operators, PyDPF-Core becomes a development tool offering:

- **Accessibility:** A simple script can define a basic operator plugin.

- **Componentization:** Operators with similar applications can be grouped in Python plug-in packages.

- **Easy distribution:** Standard Python tools can be used to package, upload, and download custom operators.

- **Dependency management:** Third-party Python modules can be added to the Python package.

- **Reusability:** A documented and packaged operator can be reused in an infinite number of workflows.

- **Remotable and parallel computing:** Native DPF capabilities are inherited by custom operators.

The only prerequisite for creating custom operators is to be familiar with native operators.
For more information, see :ref:`ref_user_guide_operators`.

.. note:
    You can create custom operators in CPython using PyDPF-Core for use with DPF in Ansys 2023 R1 and later.

The following tutorials demonstrate how to develop such plugins using PyDPF-Core (CPython based) and how to use them.

For comprehensive examples on writing operator plugins, see :ref:`python_operators`.

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Create a DPF plugin with a single operator
       :link: tutorials_custom_operators_and_plugins_custom_operator
       :link-type: ref
       :text-align: center

       This tutorial shows how to create, load, and use a custom plugin containing a single custom operator.

    .. grid-item-card:: Create a DPF plugin with multiple operators
       :link: tutorials_others_custom_plug_ins_packages
       :link-type: ref
       :text-align: center

       This tutorial shows how to create, load, and use a custom plugin with multiple operators or with complex routines.

    .. grid-item-card:: Create a custom DPF plugin with third-party dependencies using Python
       :link: tutorials_others_custom_plug_ins_packages_third_deps
       :link-type: ref
       :text-align: center

       This tutorial shows how to create a Python plug-in package with third-party dependencies.

    .. grid-item-card:: Update PyDPF-Core in the DPF installation
        :link: tutorials_custom_operators_update_pydpf_core
        :link-type: ref
        :text-align: center

        This tutorial shows how to update PyDPF-Core in your DPF installation.

.. toctree::
    :maxdepth: 2
    :hidden:

    custom_operators.rst
    custom_plug_in_package.rst
    custom_plug_in_package_third_deps.rst
    update_pydpf_core.rst

