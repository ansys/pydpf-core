"""
Custom Fields Containers
========================
Contains the inherited classes from the
:class:`FieldsContainer <ansys.dpf.core.fields_container.FieldsContainer>` class.
These new classes offer helpers to access data for specific usage, such as
results split by body or split by material.
"""
from ansys.dpf.core.fields_container import FieldsContainer
from ansys.dpf.core import elements


class ElShapeFieldsContainer(FieldsContainer):
    """
    Represents a fields container with fields split by an element shape.

    Instances of this class are created when a model result is split by an
    element shape, such as a solid, shell, or beam.

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or FieldsContainer, optional
        Fields container created from either a collection message or by copying an existing
        fields container. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The default is
        ``None``, in which case an attempt is made to use the global server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
    >>> len(fc.solid_fields())
    45
    >>> solid_f_time_2 = fc.solid_field(2)

    """

    def __init__(self, fields_container=None, server=None):
        super().__init__(fields_container, server)
        if not fields_container:
            self.add_label("elshape")

    def solid_fields(self, timeid=None, complexid=None):
        """
        Retrieve a list of all fields with solid element shapes.

        You can filter the list of fields with solid element shapes based on a given time,
        complex type, or both.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with solid element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with solid element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        list
            List of fields corresponding to the request.

        Examples
        --------

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.split_by_shape.eval()
        >>> len(fc.solid_fields())
        1
        >>> len(fc.solid_fields(timeid=1))
        1

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.SOLID.value
        return self.get_fields(label_space)

    def shell_fields(self, timeid=None, complexid=None):
        """Retrieve a list of all fields with shell element shapes.

        You can filter the list of fields with shell element shapes based on
        a given time, complex type, or both.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with shell element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with shell element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        list
            List of fields corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
        >>> len(fc.shell_fields())
        45
        >>> len(fc.shell_fields(timeid=3))
        1

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.SHELL.value
        return self.get_fields(label_space)

    def beam_fields(self, timeid=None, complexid=None):
        """Retrieve a list of all fields with beam element shapes.

        You can filter the list of fields with beam element shapes based on
        a given time, complex type, or both.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with beam element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with beam element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        list
            List of fields corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
        >>> len(fc.beam_fields())
        45
        >>> len(fc.beam_fields(timeid=3))
        1

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.BEAM.value
        return self.get_fields(label_space)

    def solid_field(self, timeid=None, complexid=None):
        """Retrieve a field with a solid element shape.

        You can give a time, complex type, or both. If the number of fields
        matching the request is higher than one, an exception is raised.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with solid element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with solid element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        :class:`Field <ansys.dpf.core.field>`
            Field corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
        >>> field = fc.solid_field(timeid=3)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.SOLID.value
        return self.get_field(label_space)

    def shell_field(self, timeid=None, complexid=None):
        """Retrieve a field with a shell element shape.

        You can give a time, complex type, or both. If the number of fields
        matching the request is higher than one, an exception is raised.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with shell element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with shell element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.


        Returns
        -------
        :class:`Field <ansys.dpf.core.field>`
            Field corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
        >>> field = fc.shell_field(timeid=3)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.SHELL.value
        return self.get_field(label_space)

    def beam_field(self, timeid=None, complexid=None):
        """Retrieve a field with a beam element shape.

        You can give a time, complex type, or both. If the number of fields
        matching the request is higher than one, an exception is raised.

        Parameters
        ----------
        timeid : int, optional
            Time ID for filtering fields with solid element shapes.
        complexid : int, optional
            Complex type ID for filtering fields with solid element shapes.
            0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        :class:`Field <ansys.dpf.core.field>`
            Field corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_shape.eval()
        >>> field = fc.beam_field(timeid=3)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["elshape"] = elements._element_shapes.BEAM.value
        return self.get_field(label_space)


class BodyFieldsContainer(FieldsContainer):
    """Represents a fields container with fields split by a body.

    Instances of this class are created when a model result is split by a
    body, which is an MAPDL material property.

    Parameters
    ----------
    fields_container : ansys.grpc.dpf.collection_pb2.Collection or FieldsContainer, optional
        Fields container created from either a collection message or by copying an existing
        fields container. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The default is
        ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
    >>> fc = model.results.displacement.on_all_time_freqs.split_by_body.eval()
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
        """Retrieve a list of all fields for a material ID.
        You can filter the list of fields for a material ID based on
        a given time, complex type, or both.

        Parameters
        ----------
        matid : int, optional
           Material ID. To request available material IDs, you can use
           the `get_mat_scoping` method.
        timeid : int, optional
            Time ID for filtering fields with the given material ID.
        complexid : int, optional
            Complex type ID for filtering fields with the given material
            ID. 0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        List
            List of fields corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_body.eval()
        >>> len(fc.get_fields_by_mat_id(1))
        45
        >>> len(fc.get_fields_by_mat_id(1, timeid=3))
        1

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["mat"] = matid
        return self.get_fields(label_space)

    def get_field_by_mat_id(self, matid, timeid=None, complexid=None):
        """Retrieve a field with a given material ID.
        You can filter the field based on a given time, complex type, or both.

        Parameters
        ----------
        matid : int, optional
           Material ID. To request available material IDs, you can use
           the `get_mat_scoping` method.
        timeid : int, optional
            Time ID for filtering fields with the given material ID.
        complexid : int, optional
            Complex type ID for filtering fields with the given material
            ID. 0 is for real numbers, and 1 is for imaginary numbers.

        Returns
        -------
        :class:`Field <ansys.dpf.core.field>`
            Field corresponding to the request.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_all_kinds_of_complexity_modal())
        >>> fc = model.results.displacement.on_all_time_freqs.split_by_body.eval()
        >>> f_time_2 = fc.get_field_by_mat_id(45, timeid=2)

        """
        label_space = self.__time_complex_label_space__(timeid, complexid)
        label_space["mat"] = matid
        return self.get_field(label_space)

    def get_mat_scoping(self):
        """Retrieves the material or body scoping containing material IDs.

        Returns
        -------
        :class:`Scoping <ansys.dpf.core.scoping>`
            Field corresponding to the request.
            Scoping containing the material IDs available in the fields container.
        """
        return self.get_label_scoping("mat")
