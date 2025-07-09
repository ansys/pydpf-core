import os

try:
    import importlib.metadata as importlib_metadata
except ImportError:  # Python < 3.10 (backport)
    import importlib_metadata as importlib_metadata

__version__ = importlib_metadata.version("ansys-dpf-core")

# Setup data directory
USER_DATA_PATH = None
LOCAL_DOWNLOADED_EXAMPLES_PATH = None
try:
    import pkgutil

    spec = pkgutil.get_loader(__name__)
    USER_DATA_PATH = os.path.dirname(spec.get_filename(__name__))
    if not os.path.exists(USER_DATA_PATH):  # pragma: no cover
        os.makedirs(USER_DATA_PATH)

    LOCAL_DOWNLOADED_EXAMPLES_PATH = os.path.join(USER_DATA_PATH, "examples")
    if not os.path.exists(LOCAL_DOWNLOADED_EXAMPLES_PATH):  # pragma: no cover
        os.makedirs(LOCAL_DOWNLOADED_EXAMPLES_PATH)
except:  # pragma: no cover
    pass

installed = [d.metadata["Name"] for d in importlib_metadata.distributions()]
check_for = ["ansys-dpf-gatebin", "ansys-dpf-gate", "ansys-grpc-dpf"]
if any([c in installed for c in check_for]):
    raise ImportError(f"Error during import of ansys-dpf-core:\n"
                      f"detected one of {check_for} installed. "
                      f"The current version of ansys-dpf-core requires uninstalling these previous "
                      f"dependencies to run correctly.")

from ansys.dpf.core.dpf_operator import Operator, Config
from ansys.dpf.core.model import Model
from ansys.dpf.core.field import Field, FieldDefinition
from ansys.dpf.core.custom_type_field import CustomTypeField  # noqa: F401
from ansys.dpf.core.dimensionality import Dimensionality
from ansys.dpf.core.property_field import PropertyField
from ansys.dpf.core.string_field import StringField
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.dpf.core.meshes_container import MeshesContainer
from ansys.dpf.core.scopings_container import ScopingsContainer
from ansys.dpf.core.streams_container import StreamsContainer  # noqa: F401
from ansys.dpf.core.server import (
    start_local_server,
    _global_server,
    connect_to_server,
    has_local_server,
)
from ansys.dpf.core.server import _global_server as global_server
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.core.common import (
    types,
    natures,
    locations,
    shell_layers,
    config_options
    )
from ansys.dpf.core import help
from ansys.dpf.core import plugins
from ansys.dpf.core.core import (
    BaseService,
    load_library,
    download_file,
    upload_file,
    upload_file_in_tmp_folder,
    upload_files_in_folder,
    download_files_in_folder,
    make_tmp_dir_server,
)
from ansys.dpf.core.time_freq_support import TimeFreqSupport
from ansys.dpf.core.generic_support import GenericSupport
from ansys.dpf.core.meshed_region import MeshedRegion
from ansys.dpf.core.elements import element_types
from ansys.dpf.core.result_info import ResultInfo
from ansys.dpf.core.collection_base import CollectionBase
from ansys.dpf.core.workflow import Workflow
from ansys.dpf.core.cyclic_support import CyclicSupport
from ansys.dpf.core.element_descriptor import ElementDescriptor
from ansys.dpf.core.data_tree import DataTree
from ansys.dpf.core import operators
from ansys.dpf.core.fields_factory import field_from_array
from ansys.dpf.core import (
    fields_container_factory,
    fields_factory,
    mesh_scoping_factory,
    time_freq_scoping_factory,
)
from ansys.dpf.core import server
from ansys.dpf.core import check_version
from ansys.dpf.core import path_utilities
from ansys.dpf.core import settings
from ansys.dpf.core.server_factory import ServerConfig, AvailableServerConfigs
from ansys.dpf.core.server_context import (
    set_default_server_context,
    AvailableServerContexts,
    LicenseContextManager
)
from ansys.dpf.core.unit_system import UnitSystem, unit_systems
from ansys.dpf.core.incremental import IncrementalHelper, split_workflow_in_chunks
from ansys.dpf.core.any import Any
from ansys.dpf.core.mesh_info import MeshInfo
from ansys.dpf.core.generic_data_container import GenericDataContainer

from ansys.dpf.core.dpf_operator import available_operator_names


from ansys.dpf.core.collection import CollectionFactory as _CollectionFactory
from ansys.dpf.core.collection import Collection as _Collection
from ansys.dpf.core.label_space import LabelSpace


# register classes for collection types:
CustomTypeFieldsCollection:type = _CollectionFactory(CustomTypeField)
GenericDataContainersCollection:type = _CollectionFactory(GenericDataContainer)
StringFieldsCollection:type = _CollectionFactory(StringField)
OperatorsCollection: type = _CollectionFactory(Operator)
AnyCollection:type = _Collection

# for matplotlib
# solves "QApplication: invalid style override passed, ignoring it."
os.environ["QT_STYLE_OVERRIDE"] = ""


SERVER = None
SERVER_CONFIGURATION = None

_server_instances = []

settings.set_default_pyvista_config()
settings._forward_to_gate()

