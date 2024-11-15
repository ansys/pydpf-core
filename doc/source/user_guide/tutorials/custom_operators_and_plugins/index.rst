.. _ref_tutorials_custom_operators_and_plugins:

Custom Operators and Plugins
----------------------------
The available DPF capabilities loaded in a DPF application can be enhanced
by creating new operator’s libraries. DPF offers multiple development APIs
depending on your environment.

These tutorials demonstrate how to develop those plugins for PyDPF-Core (CPython based)

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Create custom operators and plugins
       :link: user_guide_custom_operators
       :link-type: ref
       :text-align: center

       This tutorial shows how to create, load and use a basic operator plugin, which is for a single custom operator

    .. grid-item-card:: Create a plug-in package with multiple operators
       :link: tutorials_others_custom_plug_ins_packages
       :link-type: ref
       :text-align: center

       This tutorial shows how to create, load and use a custom plug-in package with multiple operators or with complex routines

    .. grid-item-card:: Create a plug-in package that has third-party dependencies
       :link: tutorials_others_custom_plug_ins_packages_third_deps
       :link-type: ref
       :text-align: center

       This tutorial shows how to create a Python plug-in package with third-party dependencies

.. toctree::
    :maxdepth: 2
    :hidden:

    custom_operators.rst
    custom_plug_in_package.rst
    custom_plug_in_package_third_deps.rst

