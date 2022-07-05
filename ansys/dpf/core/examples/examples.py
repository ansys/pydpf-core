"""
.. _ref_examples:

Result Files Examples
=====================
Examples result files.
"""

import os
import inspect

if os.environ.get("DPF_DOCKER", "").lower() == "true":
    # must pass a path that can be accessed by a docker image with
    # this directory mounted at the repository level for CI
    _module_path = r"/dpf/ansys/dpf/core/examples/"
else:
    _module_path = os.path.dirname(inspect.getfile(inspect.currentframe()))

# this files can be imported with from `ansys.dpf.core import examples`:
simple_bar = os.path.join(_module_path, "ASimpleBar.rst")
static_rst = os.path.join(_module_path, "static.rst")
complex_rst = os.path.join(_module_path, "complex.rst")
multishells_rst = os.path.join(_module_path, "model_with_ns.rst")
electric_therm = os.path.join(_module_path, "rth", "rth_electric.rth")
steady_therm = os.path.join(_module_path, "rth", "rth_steady.rth")
transient_therm = os.path.join(_module_path, "rth", "rth_transient.rth")
msup_transient = os.path.join(_module_path, "msup_transient_plate1.rst")
simple_cyclic = os.path.join(_module_path, "file_cyclic.rst")
distributed_msup_folder = os.path.join(_module_path, 'msup_distributed')