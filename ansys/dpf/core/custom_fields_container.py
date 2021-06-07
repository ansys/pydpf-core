"""
Custom FieldsContainers
=======================
Contains inherited class of the FieldsContainer.
Those new classes offer helpers to access data for specific usage:
results splitted by body, by material...
"""
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.grpc.dpf import meshed_region_pb2


class ElShapeFieldsContainer(FieldsContainer):
    """A class used to represent a FieldsContainer with fields splitted by
    element shapes : solid, shell, beam...
    Instances of this class are created by a result of the model asked to be 
    splitted by element shape

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or FieldsContainer, optional
        Create a fields container from a Collection message or create a copy from an existing fields container

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    >>> fc = model.results.displacement.on_all_time_freqs.splitted_by_shape.eval()
    >>> len(fc.solid_fields())
    45
    >>> solid_f_time_2 = fc.solid_field(2)
    
    """
    
    def __init__(self, fields_container=None, server=None):
        super().__init__(fields_container, server)
        if not fields_container:
            self.add_label("elshape")
    
    def solid_fields(self, timeid=None, complexid=None):
        """Returns a list of all the fields with solid element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the list of fields returned are solid fields for a given time and/or 
        complex type
        
        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
        
        Examples
        --------
        >>> len(fc.solid_fields())
        45
        >>> len(fc.solid_fields(timeid=3))
        1
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("SOLID")
        return self.get_fields(label_space)
    
    def shell_fields(self, timeid=None, complexid=None):
        """Returns a list of all the fields with shell element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the list of fields returned are shell fields for a given time and/or 
        complex type
        
        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
        
        Examples
        --------
        >>> len(fc.shell_fields())
        45
        >>> len(fc.shell_fields(timeid=3))
        1
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("SHELL")
        return self.get_fields(label_space)
    
    def beam_fields(self, timeid=None, complexid=None):
        """Returns a list of all the fields with beam element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the list of fields returned are beam fields for a given time and/or 
        complex type
        
        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
        
        Examples
        --------
        >>> len(fc.beam_fields())
        45
        >>> len(fc.beam_fields(timeid=3))
        1
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("BEAM")
        return self.get_fields(label_space)
    
    def solid_field(self, timeid=None, complexid=None):
        """Returns the requested field with solid element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the field returned is a solid field for a given time and/or 
        complex type. It throws if the number of fields matching the request is 
        higher than 1.
        
        Returns
        -------
        fields: Field
            field corresponding to the request
        
        Examples
        --------
        >>> field = fc.solid_field(timeid=3)
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("SOLID")
        return self.get_field(label_space)
    
    def shell_field(self, timeid=None, complexid=None):
        """Returns the requested field with shell element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the field returned is a shell field for a given time and/or 
        complex type. It throws if the number of fields matching the request is 
        higher than 1.
        
        Returns
        -------
        fields: Field
            field corresponding to the request
        
        Examples
        --------
        >>> field = fc.shell_field(timeid=3)
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("SHELL")
        return self.get_field(label_space)
    
    def beam_field(self, timeid=None, complexid=None):
        """Returns the requested field with beam element shapes.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the field returned is a beam field for a given time and/or 
        complex type. It throws if the number of fields matching the request is 
        higher than 1.
        
        Returns
        -------
        fields: Field
            field corresponding to the request
        
        Examples
        --------
        >>> field = fc.beam_field(timeid=3)
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["elshape"]= meshed_region_pb2.ElementShape.Value("BEAM")
        return self.get_field(label_space)
    

class BodyFieldsContainer(FieldsContainer):
    """A class used to represent a FieldsContainer with fields splitted by
    body (mapdl material property)
    Instances of this class are created by a result of the model asked to be 
    splitted by body

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or FieldsContainer, optional
        Create a fields container from a Collection message or create a copy from an existing fields container

    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.
    
    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    >>> fc = model.results.displacement.on_all_time_freqs.splitted_by_body.eval()
    >>> fc.get_mat_scoping().ids[3]
    45
    >>> len(fc.get_fields_by_mat_id(45))
    45
    >>> f_time_2 = fc.get_field_by_mat_id(45, timeid=2)
    
    """
    
    def __init__(self, fields_container=None, server=None):
        super().__init__(fields_container, server)
        if not fields_container:
            self.add_label("elshape")
    
    def get_fields_by_mat_id(self, matid, timeid=None, complexid=None):
        """Returns a list of all the fields with the given material id.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the list of fields returned are fields for a given time and/or 
        complex type. The available mat id can be requested with `get_mat_scoping`
        
        Returns
        -------
        fields : list[Field]
            fields corresponding to the request
        
        Examples
        --------
        >>> len(fc.get_fields_by_mat_id(1))
        45
        >>> len(fc.get_fields_by_mat_id(1, timeid=3))
        1
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["mat"]= matid
        return self.get_fields(label_space)
    
    def get_field_by_mat_id(self, matid, timeid=None, complexid=None):
        """Returns a a field with the given material id.
        If a timeid or a complexid (0 for real and 1 for imaginary) are given, 
        the field returned is for a given time and/or 
        complex type. The available mat id can be requested with `get_mat_scoping`
        
        Returns
        -------
        fields : Field
            field corresponding to the request
        
        Examples
        --------
        >>> f_time_2 = fc.get_field_by_mat_id(45, timeid=2)
        
        """
        label_space = self.__time_complex_label_space__(timeid,complexid)
        label_space["mat"]= matid
        return self.get_field(label_space)
    
    def get_mat_scoping(self):
        """Returns the material or body scoping containing the mat ids
        
        Returns
        -------
        scoping: Scoping
            scoping containing the mat ids available in the fields container
        """
        return self.get_label_scoping("mat")