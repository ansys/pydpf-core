import os
import socket

from ansys.dpf.core._version import __version__

# environment variables for pyansys.com
if 'jupyter' in socket.gethostname():
    if 'ANSYS_PATH' not in os.environ:
        os.environ['ANSYS_PATH'] = '/mnt/ansys_inc/v212/'
    if 'DPF_PATH' not in os.environ:
        os.environ['DPF_PATH'] = '/mnt/ansys_inc/dpf/bin_v%s/Ans.dpf.core.Grpc.exe' % __version__
    if 'AWP_UNIT_TEST_FILES' not in os.environ:
        os.environ['AWP_UNIT_TEST_FILES'] = '/mnt/ansys_inc/dpf/test_files/'

from ansys.dpf.core.misc import module_exists, Report
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.model import Model
from ansys.dpf.core.field import Field
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.dpf.core.server import (start_local_server, _global_channel,
                                   connect_to_server)
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.core.common import types, natures, field_from_array, locations, ShellLayers
from ansys.dpf.core.core import BaseService
from ansys.dpf.core.time_freq_support import TimeFreqSupport
from ansys.dpf.core.operators_helper import sum, to_nodal, norm, eqv
from ansys.dpf.core.meshed_region import MeshedRegion
from ansys.dpf.core.result_info import ResultInfo
from ansys.dpf.core.collection import Collection

# for matplotlib
# solves "QApplication: invalid style override passed, ignoring it."
os.environ['QT_STYLE_OVERRIDE'] = ''

# Setup data directory
USER_DATA_PATH = None
EXAMPLES_PATH = None
if os.environ.get('DPF_DOCKER', False):  # pragma: no cover
    # Running DPF within docker (likely for CI)
    # path must be relative to DPF directory
    #
    # assumes the following docker mount:
    # -v /tmp:/dpf/_cache
    EXAMPLES_PATH = '/tmp'
else:
    try:
        import appdirs
        USER_DATA_PATH = appdirs.user_data_dir('ansys-dpf-core')
        if not os.path.exists(USER_DATA_PATH):  # pragma: no cover
            os.makedirs(USER_DATA_PATH)

        EXAMPLES_PATH = os.path.join(USER_DATA_PATH, 'examples')
        if not os.path.exists(EXAMPLES_PATH):  # pragma: no cover
            os.makedirs(EXAMPLES_PATH)
    except:  # pragma: no cover
        pass


# Configure PyVista's ``rcParams`` for dpf
if module_exists("pyvista"):
    import pyvista as pv
    pv.rcParams['interactive'] = True
    pv.rcParams["cmap"] = "jet"
    pv.rcParams["font"]["family"] = "courier"
    pv.rcParams["title"] = "DPF"


CHANNEL = None

def has_local_server():
    """Returns True when a local DPF gRPC server has been created"""
    return CHANNEL is not None


_server_instances = []
