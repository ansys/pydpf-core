from .examples import *
from .downloads import *


# called if module.<name> fails
def __getattr__(name):
    if name == "simple_bar":
        global simple_bar
        simple_bar = find_simple_bar()
        return simple_bar
    elif name == "static_rst":
        global static_rst
        static_rst = find_static_rst()
        return static_rst
    elif name == "complex_rst":
        global complex_rst
        complex_rst = find_complex_rst()
        return complex_rst
    elif name == "multishells_rst":
        global multishells_rst
        multishells_rst = find_multishells_rst()
        return multishells_rst
    elif name == "electric_therm":
        global electric_therm
        electric_therm = find_electric_therm()
        return electric_therm
    elif name == "steady_therm":
        global steady_therm
        steady_therm = find_steady_therm()
        return steady_therm
    elif name == "transient_therm":
        global transient_therm
        transient_therm = find_transient_therm()
        return transient_therm
    elif name == "msup_transient":
        global msup_transient
        msup_transient = find_msup_transient()
        return msup_transient
    elif name == "simple_cyclic":
        global simple_cyclic
        simple_cyclic = find_simple_cyclic()
        return simple_cyclic
    elif name == "distributed_msup_folder":
        global distributed_msup_folder
        distributed_msup_folder = find_distributed_msup_folder()
        return distributed_msup_folder
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
