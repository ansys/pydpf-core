import abc


class locations:
    """Contains strings for scoping and field locations.

    Attributes
    -----------
    none = "none"

    elemental = "Elemental"
        data is one per element

    elemental_nodal = "ElementalNodal"
        one per node per element

    nodal = "Nodal"
        one per node

    time_freq = "TimeFreq_sets"
        one per time set

    overall = "overall"
        applies everywhere

    time_freq_step = "TimeFreq_steps"
        one per time step

    faces = "Faces"
        one per face

    zone = "zone"
        one per zone

    elemental_and_faces = "ElementalAndFaces"
        data available in elements and faces of the model
    """

    none = "none"

    # data is one per element
    elemental = "Elemental"

    # one per node per element
    elemental_nodal = "ElementalNodal"

    # one per node
    nodal = "Nodal"

    # one per time set
    time_freq = "TimeFreq_sets"

    # applies everywhere
    overall = "overall"

    # one per time step
    time_freq_step = "TimeFreq_steps"

    # one per face
    faces = "Faces"

    # one per zone
    zone = "zone"

    # data available in elements and faces of the model
    elemental_and_faces = "ElementalAndFaces"


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