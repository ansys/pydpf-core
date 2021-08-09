"""
ElementDescriptor
=================
"""

class ElementDescriptor: 
    """Class that describes an element.
    
    Examples
    --------
    from ansys.dpf import core as dpf
    element = dpf.ElementDescriptor(10, "Linear 4-nodes Tetrahedron", "tet4", "solid", 4, 0, 4, true, false, false, false)   
    
    """
    
    def __init__(self, element_id, description, name, shape = None, number_of_corner_nodes = None, number_of_mid_nodes = None, 
                 number_of_nodes = None, is_solid = None, is_shell = None, is_beam = None, is_quadratic = None):
        """Constructor of ElementDescriptor.
        
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
        txt = 'Element descriptor \n'
        txt += '-'*18 + '\n'
        txt += "Enum id (dpf.element_types): "
        txt += str(self.element_id)
        txt += "\n"
        txt += "Element description: "
        txt += str(self.description)
        txt += "\n"
        txt += "Element name (short): "
        txt += str(self.name)
        txt += "\n"
        txt += "Element shape: "
        txt += str(self.shape)
        txt += "\n"
        txt += "Number of corner and mid-side nodes: "
        txt += str(self.number_of_corner_nodes)
        txt += str(", ")
        txt += str(self.number_of_mid_nodes)
        txt += "\n"
        txt += "Total number of nodes: "
        txt += str(self.number_of_nodes)
        txt += "\n"
        txt += "Is quadratic element: "
        txt += str(self.is_quadratic)
        txt += "\n"
        return txt
        
        