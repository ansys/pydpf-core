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
    
    n_corner_nodes: int
    
    n_mid_nodes: int
    
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
    
    def __init__(self, enum_id, description, name, shape=None, 
                 n_corner_nodes=None, n_mid_nodes=None, 
                 n_nodes=None, is_solid=None, is_shell=None, 
                 is_beam=None, is_quadratic=None):
        """Constructor of ElementDescriptor."""
        self.enum_id = enum_id
        self.description = description
        self.name = name
        self.n_corner_nodes = n_corner_nodes
        self.n_mid_nodes = n_mid_nodes
        self.n_nodes = n_nodes
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
        lines.append(f"Enum id (dpf.element_types): {self.enum_id}")
        lines.append(f"Element description: {self.description}")
        lines.append(f"Element name (short): {self.name}")
        lines.append(f"Element shape: {self.shape}")
        lines.append(f"Number of corner nodes: {self.n_corner_nodes}")
        lines.append(f"Number of mid-side nodes: {self.n_mid_nodes}")
        lines.append(f"Total number of nodes: {self.n_nodes}")
        lines.append(f"Quadratic element: {self.is_quadratic}")
        return "\n".join(lines)
        
        