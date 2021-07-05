"""
fields_container_factory
========================

Contains functions to make easy fields container creation.
"""

from ansys.dpf import core
from ansys.dpf.core import FieldsContainer, TimeFreqSupport
from ansys.dpf.core import fields_factory
from ansys.dpf.core.common import natures, locations
from ansys.grpc.dpf import base_pb2
from ansys.dpf.core import errors as dpf_errors

def over_time_freq_fields_container(fields, time_freq_unit = None, server = None):
    """Helper function to create a specific ``FieldsContainer``.
    The returned fields_container will contain one field by time set and, if needed, set
    the time freq support with the correct unit. 

    Parameters
    ----------
    fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary of Field entities to add to the fields container
    
    time_freq_unit : str , optional
        String that defines the unit symbol of the time_freq_support. Will be taken 
        into account if the fields attribute has a dictionary type.
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    fields_container : FieldsContainer
        FieldsContainer containing one field by time step.
    
    Examples
    --------
    Create a fields container based on time labels from scratch
    
    >>> from ansys.dpf import core as dpf
    >>> field1 = dpf.Field()
    >>> field2 = dpf.Field()
    >>> from ansys.dpf.core import fields_container_factory
    >>> my_fc = fields_container_factory.over_time_freq_fields_container([ field1, field2 ])    
    
    """
    if not isinstance(fields, dict) and not isinstance(fields, list):
        raise dpf_errors.InvalidTypeError("dictionary/list", "fields") 
    fc = FieldsContainer(server = server)
    fc.labels = { "time" }
    i = 0
    # dict case
    if isinstance(fields, dict):
        time_freq = []
        for field_key in fields:
            fc.add_field({ "time" : i + 1 }, fields[field_key])
            time_freq.append(field_key)
            i += 1
        time_freq_field = fields_factory.create_scalar_field(len(fields), location=locations.time_freq, server = server)
        time_freq_field.append(time_freq, 1)
        time_freq_field.unit = time_freq_unit
        time_freq_support = TimeFreqSupport(server = server)
        time_freq_support.time_frequencies = time_freq_field
        fc.time_freq_support = time_freq_support
    # list case
    elif isinstance(fields, list):
        for field in fields:
            fc.add_field({ "time" : i + 1 }, field)
            i += 1
    return fc

def over_time_freq_complex_fields_container(real_fields, imaginary_fields, time_freq_unit = None, server = None):
    """Helper function to create a specific ``FieldsContainer``.
    The returned fields_container will contain two fields (real and imaginary 
    fields) by time set.
    It sets the time freq support with the correct unit if needed (if the fields inputs 
    are dictionaries).

    Parameters
    ----------
    real_fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary or list of Field entities to add to the fields container
        
    imaginary_fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary or list of Field entities to add to the fields container
        
    time_freq_unit : str , optional
        String that defines the unit symbol of the time_freq_support. Will be taken 
        into account if the fields attribute has a dictionary type.
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    fields_container : FieldsContainer
        FieldsContainer containing two fields (real and imaginary ones)
        by time step.
    """
    if not isinstance(real_fields, dict) and not isinstance(real_fields, list):
        raise dpf_errors.InvalidTypeError("dictionary/list", "real_fields") 
    if not isinstance(imaginary_fields, dict) and not isinstance(imaginary_fields, list):
        raise dpf_errors.InvalidTypeError("dictionary/list", "imaginary_fields") 
        
    errorString = "Both real_fields and imaginary_fields must have the same type (list or dict)"
    if isinstance(real_fields, dict):
        if not isinstance(imaginary_fields, dict):
            raise dpf_errors.DpfValueError(errorString)
    elif isinstance(real_fields, list):
        if not isinstance(imaginary_fields, list):
            raise dpf_errors.DpfValueError(errorString)
            
    fc = FieldsContainer(server = server)
    fc.labels = ["time", "complex"]
    i = 0
    # dict case
    if isinstance(real_fields, dict):
        time_freq = []
        for field_key in real_fields:
            fc.add_field({"time": i + 1, "complex" : 0}, real_fields[field_key])
            time_freq.append(field_key)
            i += 1
        i = 0
        im_time_freq = []
        for field_key in imaginary_fields:
            fc.add_field({"time": i + 1, "complex" : 1}, imaginary_fields[field_key])
            im_time_freq.append(field_key)
            i += 1
        time_freq_field = fields_factory.create_scalar_field(len(real_fields), locations.time_freq, server = server)
        time_freq_field.append(time_freq, 1)
        time_freq_field.unit = time_freq_unit
        im_time_freq_field = fields_factory.create_scalar_field(len(imaginary_fields), locations.time_freq, server = server)
        im_time_freq_field.append(im_time_freq, 1)
        im_time_freq_field.unit = time_freq_unit
        time_freq_support = TimeFreqSupport(server = server)
        time_freq_support.time_frequencies = time_freq_field
        time_freq_support.complex_frequencies = im_time_freq_field
        fc.time_freq_support = time_freq_support
    # list case
    if isinstance(real_fields, list):
        for field in real_fields:
            fc.add_field({"time": i + 1, "complex" : 0}, field)
            i += 1
        i = 0
        for field in imaginary_fields:
            fc.add_field({"time": i + 1, "complex" : 1}, field)
            i += 1
    return fc
    

def complex_fields_container(real_field, imaginary_field, server = None):
    """Helper function to create a specific ``FieldsContainer``.
    The returned fields_container will contain two fields (real and imaginary 
    fields) and only one time set.

    Parameters
    ----------
    real_fields : Field
        Real ansys.dpf.core.Field entity to add to the fields container
        
    imaginary_fields : Field
        Imaginary ansys.dpf.core.Field entity to add to the fields container
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    fields_container : FieldsContainer
        FieldsContainer containing two fields (real and imaginary ones).
    """
    fc = FieldsContainer(server = server)
    fc.labels = ["complex"]
    fc.add_field({ "complex" : 0 }, real_field)
    fc.add_field({ "complex" : 1 }, imaginary_field)
    return fc