.. _ref_tutorials_custom_operators_and_plugins:

Custom Operators and Plugins
----------------------------
You can enhance and customize your DPF installation by creating new operators and libraries of operators, called 'plugins'.

DPF offers multiple development APIs depending on your environment.

The following tutorials demonstrate how to develop such plugins using PyDPF-Core (CPython based) and how to use them.

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

.. toctree::
    :maxdepth: 2
    :hidden:

    custom_operators.rst
    custom_plug_in_package.rst
    custom_plug_in_package_third_deps.rst

