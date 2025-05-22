.. _ref_write_code:

============
Develop code
============

You can help improve PyDPF-Core by fixing a bug. To do it, you must set up the repository
on your local machine as per the following steps:

- :ref:`ref_write_code_install`
- :ref:`ref_write_code_clone`
- :ref:`ref_write_code_check_install`
- :ref:`ref_write_code_develop_code`

.. _ref_write_code_install:

Install the repository and the DPF server
-----------------------------------------

Install the PyDPF-Core repository by following the steps in :ref:`installation` and :ref:`ref_dpf_server`.

.. _ref_write_code_clone:

Clone the repository
--------------------

Before cloning the PyDPF-Core repository, you must install a version control system such as Git.

Then, clone the latest version of PyDPF-Core in development mode (using ``pip`` with the ``-e``
development flag) by running this code:

.. code::

    git clone https://github.com/ansys/pydpf-core
    cd pydpf-core
    pip install -e .

.. _ref_write_code_check_install:

Check the installation
----------------------

Run the following Python code to verify your PyDPF-Core installation:

.. code::

   from ansys.dpf.core import Model
   from ansys.dpf.core import examples
   model = Model(examples.find_simple_bar())
   print(model)

.. _ref_write_code_develop_code:

Develop the PyDPF-Core code
---------------------------

Overall guidance on contributing to the code of a PyAnsys repository appears in
`Contributing <dev_guide_contributing_>`_ in the *PyAnsys Developer's Guide*.

You must also follow the `Coding style <dev_guide_coding_style_>`_ guide to ensure
that all source code looks the same across the project.