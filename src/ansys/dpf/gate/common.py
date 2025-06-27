import abc

def __getattr__(name):
    if name == "locations":
        from ansys.dpf.core.common import locations
        import warnings
        warnings.warn(message="Use ansys.dpf.core.common.locations", category=DeprecationWarning)
        return locations
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

elemental_property_type_dict = {
    "eltype": "ELEMENT_TYPE",
    "elshape": "ELEMENT_SHAPE",
    "mat": "MATERIAL",
    "connectivity": "CONNECTIVITY",
}


nodal_property_type_dict = {
    "coordinates": "COORDINATES",
    "reverse_connectivity": "NODAL_CONNECTIVITY",
}

class ProgressBarBase:
    def __init__(self, text, tot_size=None):
        self.current = 0
        self.tot_size = tot_size
        pass

    def start(self):
        pass

    @abc.abstractmethod
    def update(self, current_value):
        pass

    def finish(self):
        if self.tot_size is not None and self.current != self.tot_size:
            self.update(self.tot_size)