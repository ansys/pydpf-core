"""
time_freq_scoping_factory
=========================

Contains functions to make easy time frequency scopings creation.
"""

from ansys.dpf import core
from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import Scoping

def scoping_by_load_step(load_step, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific time_freq_support element for a given load_step. 

    Parameters
    ----------
    load_step : int
        Load step id of the specific time_freq scoping
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping targeting one load_step."""
    scoping = Scoping(server = server, ids = [ load_step ], location = locations.time_freq_step)
    return scoping

def scoping_by_load_steps(load_steps, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific time_freq_support element for a given 
    list of load_steps. 

    Parameters
    ----------
    load_steps : List of int
        Load steps ids of the specific time_freq scoping
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping targeting several load_steps."""
    if not isinstance(load_steps, list):
        raise dpf_errors.InvalidTypeError("list", "load_steps") 
    scoping = Scoping(server = server, ids = load_steps, location = locations.time_freq_step)
    return scoping

def scoping_by_set(cumulative_set, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific time_freq_support element for a given
    cumulative set index. 

    Parameters
    ----------
    cumulative_set : int
        Cumulative index of the set
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping targeting one set (referenced by cumulative index)."""
    scoping = Scoping(server = server, ids = [ cumulative_set ], location = locations.time_freq)
    return scoping

def scoping_by_sets(cumulative_sets, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific time_freq_support element for a given 
    list of cumulative_sets. 

    Parameters
    ----------
    cumulative_sets : List of int
        Cumulative indices of the sets 
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping targeting severals sets (referenced by cumulative indices)."""
    if not isinstance(cumulative_sets, list):
        raise dpf_errors.InvalidTypeError("list", "cumulative_sets") 
    scoping = Scoping(server = server, ids = cumulative_sets, location = locations.time_freq)
    return scoping

def scoping_by_step_and_substep(load_step_id, subset_id, time_freq_support, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific time_freq_support element for a given 
    step, substep. 

    Parameters
    ----------
    load_step_id : int
    
    subset_id : int
    
    time_freq_support : ansys.dpf.core.TimeFreqSupport()
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping based on a given step/substep of a time_freq_support."""
    set_index = time_freq_support.get_cumulative_index(load_step_id - 1, subset_id - 1)
    scoping = Scoping(ids = [ set_index + 1], location = locations.time_freq)
    return scoping

def scoping_by_step_and_substep_from_model(load_step_id, subset_id, model, server = None):
    """Helper function to create a specific ``ansys.dpf.core.Scoping``.
    The returned scoping will describe a specific model's time_freq_support element for a given 
    step, substep. 

    Parameters
    ----------
    load_step_id : int
    
    subset_id : int
    
    time_freq_support : ansys.dpf.core.TimeFreqSupport()
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    scoping : ansys.dpf.core.Scoping
        Scoping based on a given step/substep of a model's time_freq_support."""
    return scoping_by_step_and_substep(load_step_id, subset_id, model.metadata.time_freq_support)