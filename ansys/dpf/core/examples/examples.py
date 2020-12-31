import os
import inspect

if os.environ.get('DPF_DOCKER', '').lower() == 'true':
    # must pass a path that can be accessed by a docker image with
    # this directory mounted at the repository level for CI
    _module_path = '/dpf/ansys/dpf/core/examples/'
else:
    _module_path = os.path.dirname(inspect.getfile(inspect.currentframe()))

# this files can be imported with from `ansys.dpf.core import examples`:
simple_bar = os.path.join(_module_path, 'ASimpleBar.rst')
static_rst = os.path.join(_module_path, 'static.rst')
