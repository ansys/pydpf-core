import os

from ansys.dpf.core._version import __version__

# Setup data directory
USER_DATA_PATH = None
LOCAL_DOWNLOADED_EXAMPLES_PATH = None
try:
    import pkgutil

    spec = pkgutil.get_loader("ansys.dpf.core")
    USER_DATA_PATH = os.path.dirname(spec.get_filename())
    if not os.path.exists(USER_DATA_PATH):  # pragma: no cover
        os.makedirs(USER_DATA_PATH)

    LOCAL_DOWNLOADED_EXAMPLES_PATH = os.path.join(USER_DATA_PATH, "examples")
    if not os.path.exists(LOCAL_DOWNLOADED_EXAMPLES_PATH):  # pragma: no cover
        os.makedirs(LOCAL_DOWNLOADED_EXAMPLES_PATH)
except:  # pragma: no cover
    pass

from ansys.dpf.core import (
    check_version,
    fields_container_factory,
    fields_factory,
    help,
    mesh_scoping_factory,
    operators,
    path_utilities,
    server,
    settings,
    time_freq_scoping_factory,
)
from ansys.dpf.core.collection import Collection
from ansys.dpf.core.common import (
    config_options,
    locations,
    natures,
    shell_layers,
    types,
)
from ansys.dpf.core.core import (
    BaseService,
    download_file,
    download_files_in_folder,
    load_library,
    make_tmp_dir_server,
    upload_file,
    upload_file_in_tmp_folder,
    upload_files_in_folder,
)
from ansys.dpf.core.custom_type_field import CustomTypeField  # noqa: F401
from ansys.dpf.core.cyclic_support import CyclicSupport
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.data_tree import DataTree
from ansys.dpf.core.dimensionality import Dimensionality
from ansys.dpf.core.dpf_operator import Config, Operator
from ansys.dpf.core.element_descriptor import ElementDescriptor
from ansys.dpf.core.elements import element_types
from ansys.dpf.core.field import Field, FieldDefinition
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.dpf.core.fields_factory import field_from_array
from ansys.dpf.core.generic_support import GenericSupport
from ansys.dpf.core.meshed_region import MeshedRegion
from ansys.dpf.core.meshes_container import MeshesContainer
from ansys.dpf.core.model import Model
from ansys.dpf.core.property_field import PropertyField
from ansys.dpf.core.result_info import ResultInfo
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.core.scopings_container import ScopingsContainer
from ansys.dpf.core.server import _global_server
from ansys.dpf.core.server import _global_server as global_server
from ansys.dpf.core.server import (
    connect_to_server,
    has_local_server,
    start_local_server,
)
from ansys.dpf.core.server_context import (
    AvailableServerContexts,
    set_default_server_context,
)
from ansys.dpf.core.server_factory import AvailableServerConfigs, ServerConfig
from ansys.dpf.core.streams_container import StreamsContainer  # noqa: F401
from ansys.dpf.core.string_field import StringField
from ansys.dpf.core.time_freq_support import TimeFreqSupport
from ansys.dpf.core.workflow import Workflow

# for matplotlib
# solves "QApplication: invalid style override passed, ignoring it."
os.environ["QT_STYLE_OVERRIDE"] = ""


SERVER = None
SERVER_CONFIGURATION = None

_server_instances = []

settings.set_default_pyvista_config()
settings._forward_to_gate()
