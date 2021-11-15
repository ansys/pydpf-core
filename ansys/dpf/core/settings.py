from ansys.dpf.core.misc import module_exists
from ansys.dpf.core import misc

def disable_off_screen_rendering() -> None:
    # enable matplotlib off_screen plotting to avoid test interruption
    if module_exists("matplotlib"):
        import matplotlib as mpl

        mpl.use("Agg")

    # enable off_screen plotting to avoid test interruption
    if module_exists("pyvista"):
        import pyvista as pv

        pv.OFF_SCREEN = True

def set_default_pyvista_config():
    # Configure PyVista's ``rcParams`` for dpf
    if module_exists("pyvista"):
        import pyvista as pv

        pv.rcParams["interactive"] = True
        pv.rcParams["cmap"] = "jet"
        pv.rcParams["font"]["family"] = "courier"
        pv.rcParams["title"] = "DPF"

def disable_interpreter_properties_evaluation() -> bool:
    if module_exists("jedi"):
        import jedi
        jedi.Interpreter._allow_descriptor_getattr_default = False
        return True
    return False

def set_upload_chunk_size(num_bytes = misc.DEFAULT_FILE_CHUNK_SIZE) -> None:
    misc.DEFAULT_FILE_CHUNK_SIZE = num_bytes
