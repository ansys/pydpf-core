.. _ref_tutorials_import_data:

===========
Import Data
===========

These tutorials demonstrate how to represent data in DPF: either from manual input either
form simulation result files.

From user input
***************

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Use custom data
       :link: ref_tutorials_field_with_custom_data
       :link-type: ref
       :text-align: center

       Learn how to build DPF data storage structures from custom data.

From result files
*****************

.. grid:: 1 1 3 3
    :gutter: 2
    :padding: 2
    :margin: 2

    .. grid-item-card:: Import a result file in DPF
       :link: ref_tutorials_import_result_file
       :link-type: ref
       :text-align: center

       This tutorial shows how to import a result file in DPF.

    .. grid-item-card:: Extract and explore results metadata
       :link: ref_tutorials_extract_and_explore_results_metadata
       :link-type: ref
       :text-align: center

       This tutorial shows how to extract and explore results metadata (analysis type,
       physics type, unit system ... ) from a result file.

    .. grid-item-card:: Extract and explore results data
       :link: ref_tutorials_extract_and_explore_results_data
       :link-type: ref
       :text-align: center

       This tutorial shows how to extract and explore results data from a result file.

    .. grid-item-card:: Narrow down data
       :link: reft_tutorials_narrow_down_data
       :link-type: ref
       :text-align: center

       This tutorial explains how to scope (get a spatial and/or temporal subset of
       the simulation data) your results.


.. toctree::
    :maxdepth: 2
    :hidden:

    field_with_custom_data.rst
    import_result_file.rst
    extract_and_explore_results_metadata.rst
    extract_and_explore_results_data.rst
    narrow_down_data.rst