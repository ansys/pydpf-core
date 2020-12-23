"""
.. _ref_dpf_core:

Basic DPF-Core Usage
~~~~~~~~~~~~~~~~~~~~
This example shows how to open an example result file and do some
basic post-processing.

If you have ANSYS 2021R1 installed, getting running DPF is quite easy
as `ansys.dpf.core` takes care of launching all the services required
to start post-processing ANSYS files.

First, import the DPF-Core module as `dpf_core` and also import the
included examples file.


"""

from ansys.dpf import core as dpf_core
from ansys.dpf.core import examples

###############################################################################
# Next, open an example and then print out the ``model`` object
#
model = dpf_core.Model(examples.simple_bar)
print(model)
