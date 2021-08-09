"""
ElementDescriptor
=================
"""

class ElementDescriptor: 
    """Class that describes an element.
    
    Parameters
    ----------
    element_id: int
    
    description: str
        Specifies the element geometry and integration order.
    
    name: str
    
    shape: str
        Can be "solid", "shell" of "beam". 
    
    number_of_corner_nodes: int
    
    number_of_mid_nodes: int
    
    number_of_nodes: int
        
    is_solid: bool
    
    is_shell: bool
    
    is_beam: bool
    
    is_quadratic: bool
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> descriptor = dpf.ElementDescriptor(10, "Linear 4-nodes Tetrahedron", "tet4", "solid", 4, 0, 4, True, False, False, False)   
    
    """
    
    def __init__(self, element_id, description, name, shape=None, 
                 number_of_corner_nodes=None, number_of_mid_nodes=None, 
                 number_of_nodes=None, is_solid=None, is_shell=None, 
                 is_beam=None, is_quadratic=None):
        """Constructor of ElementDescriptor."""
        self.element_id = element_id
        self.description = description
        self.name = name
        self.number_of_corner_nodes = number_of_corner_nodes
        self.number_of_mid_nodes = number_of_mid_nodes
        self.number_of_nodes = number_of_nodes
        self.shape = shape
        if self.shape is None:
            self.shape = "unknown_shape"
        self.is_solid = is_solid
        self.is_shell = is_shell
        self.is_beam = is_beam
        self.is_quadratic = is_quadratic
        
    def __str__(self):
        lines = []
        lines.append('Element descriptor')
        lines.append('-'*18)
        lines.append("Enum id (dpf.element_types): " + str(self.element_id))
        lines.append("Element description: " + str(self.description))
        lines.append("Element name (short): " + str(self.name))
        lines.append("Element shape: " + str(self.shape))
        nodes_txt = "Number of corner and mid-side nodes: " + str(self.number_of_corner_nodes)
        nodes_txt += str(", ") + str(self.number_of_mid_nodes)
        lines.append(nodes_txt)
        lines.append("Total number of nodes: " + str(self.number_of_nodes))
        lines.append("Is quadratic element: " + str(self.is_quadratic))
        return "\n".join(lines)
        
        