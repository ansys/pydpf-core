"""
mesh_scoping_factory
====================

Contains functions to make easy mesh scopings creation.
"""

from ansys.dpf import core
from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import Scoping
from ansys.dpf.core import errors as dpf_errors

def nodal_scoping(node_ids, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``
    associated to a mesh. 

    Parameters
    ----------
    node_ids : List of int
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    if not isinstance(node_ids, list):
        raise dpf_errors.InvalidTypeError("list", "node_ids") 
    scoping = Scoping(server = server, ids = node_ids, location = locations.nodal)
    return scoping

def elemental_scoping(element_ids, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``
    associated to a mesh. 

    Parameters
    ----------
    element_ids : List of int
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    if not isinstance(element_ids, list):
        raise dpf_errors.InvalidTypeError("list", "element_ids") 
    scoping = Scoping(server = server, ids = element_ids, location = locations.elemental)
    return scoping

def named_selection_scoping(named_selection_name, model, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``
    associated to a specified model's mesh. 

    Parameters
    ----------
    named_selection_name : string
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
    """
    return model.metadata.named_selection(named_selection_name)