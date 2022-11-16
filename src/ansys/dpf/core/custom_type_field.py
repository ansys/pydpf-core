"""
.. _ref_custom_type_field:

CustomTypeField
===============
"""
import warnings

import numpy as np

from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.core import scoping
from ansys.dpf.core.common import locations, _get_size_of_list
from ansys.dpf.core.field_base import _FieldBase
from ansys.dpf.core.field_definition import FieldDefinition
from ansys.dpf.core.support import Support
from ansys.dpf.gate import (
    dpf_array,
    dpf_vector,
    integral_types,
)


class dict_with_missing_numpy_type(dict):
    def __missing__(self, key):
        return key.name


numpy_type_to_dpf = dict_with_missing_numpy_type({
    np.float64: "double",
    np.float32: "float",
    np.int16: "short",
    np.byte: "char",
    np.int8: "char",
})


class CustomTypeField(_FieldBase):
    """Represents a simulation data container with each unitary data being of a custom type.
    When initiliazing the CustomTypeField, a unitary data type should be given.
    The ``CustomTypeField`` gives the ability to choose the most optimized unitary data type
    for a given usage, and hence, allows to optimize memory usage.

    This can be evaluated data from the :class:`Operator <ansys.dpf.core.Operator>` class
    or created directly by an instance of this class.

    A field's data is always associated to its scoping (entities
    associated to each value) and support (subset of the model where the
    data is), making the field a self-describing piece of data.

    Parameters
    ----------
    unitary_type : numpy.dtype
        The data vector of the Field will be a vector of this custom unitary type.
    nentities : int, optional
        Number of entities reserved. The default is ``0``.
    field : CustomTypeField, ansys.grpc.dpf.field_pb2.Field, ctypes.c_void_p, optional
        Field message generated from a gRPC stub, or returned by DPF's C clients.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create a custom type field from scratch.

    >>> from ansys.dpf.core import locations
    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
    >>> field.location = locations.nodal
    >>> field.append([1000000,2000000], 1)
    >>> float_field = dpf.CustomTypeField(unitary_type=np.float32)
    >>> float_field.is_of_type(np.float32)
    True

    Notes
    -----
    Class available with server's version starting at 5.0 (Ansys 2023R1).
    """

    def __init__(
            self,
            unitary_type=None,
            nentities=0,
            field=None,
            server=None,
    ):
        """Initialize the field either with an optional field message or
        by connecting to a stub.
        """
        self._server = server_module.get_or_create_server(server)
        if field is None and not self._server.meet_version("5.0"):
            raise errors.DpfVersionNotSupported("5.0")
        if unitary_type is not None:
            self._type = np.dtype(unitary_type)
        else:
            self._type = unitary_type
        super().__init__(nentities=nentities, field=field, server=server)
        self._load_type()
        self._field_definition = self._load_field_definition()

    def _load_type(self):
        if self._type is None:
            type_name = integral_types.MutableString(256)
            unitary_size = integral_types.MutableInt32(0)
            self._api.cscustom_type_field_get_type(self, type_name, unitary_size)
            try:
                self._type = np.dtype(str(type_name))
                if self._type.itemsize != int(unitary_size):
                    warnings.warn(f"The field unitary data type will be interpreted as a void, of "
                                  f"{int(unitary_size)} bytes because"
                                  f" a {str(type_name)} type was expected to have "
                                  f"{self._type.itemsize} bytes.")
                    raise TypeError()
            except TypeError:
                self._type = np.dtype(f"V{int(unitary_size)}")

    @property
    def _api(self):
        from ansys.dpf.gate import custom_type_field_capi, custom_type_field_grpcapi
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=custom_type_field_capi.CustomTypeFieldCAPI,
                grpcapi=custom_type_field_grpcapi.CustomTypeFieldGRPCAPI)
        return self._api_instance

    def _init_api_env(self):
        self._api.init_custom_type_field_environment(self)

    @staticmethod
    def _field_create_internal_obj(
            api,
            client,
            nature,
            nentities,
            location=locations.nodal,
            ncomp_n=0,
            ncomp_m=0,
            with_type=None,
    ):
        dpf_type_name = numpy_type_to_dpf[with_type]
        if client is not None:
            return api.cscustom_type_field_new_on_client(
                client, dpf_type_name, with_type.itemsize, nentities, nentities)
        else:
            return api.cscustom_type_field_new(
                dpf_type_name, with_type.itemsize, nentities, nentities)

    @property
    def location(self):
        """CustomTypeField location.

        Returns
        -------
        str
            Location string, which can be ``"Nodal"``, ``"Elemental"``,
            ``"ElementalNodal"``... See :class:`ansys.dpf.core.common.locations`.

        Examples
        --------
        >>> from ansys.dpf.core import locations
        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
        >>> field.location = locations.nodal
        >>> field.location
        'Nodal'

        """
        if self.field_definition:
            return self.field_definition.location

    @location.setter
    def location(self, location):
        """Change the field location.

        Parameters
        -------
        location : str or locations
             Location string, which can be ``"Nodal"``, ``"Elemental"``,
            ``"ElementalNodal"``... See :class:`ansys.dpf.core.common.locations`.

        Examples
        --------
        >>> from ansys.dpf.core import locations
        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
        >>> field.location = locations.nodal
        >>> field.location
        'Nodal'

        """
        fielddef = self.field_definition
        fielddef.location = location
        self.field_definition = fielddef

    def is_of_type(self, type_to_compare: np.dtype) -> bool:
        """Checks whether the Field's unitary type is the same as the input type.

        Parameters
        ----------
        type_to_compare: numpy.dtype

        Returns
        -------
        bool

        Examples
        --------
        Create a custom type field from scratch.

        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.int16)
        >>> field.is_of_type(np.int16)
        True
        >>> field.is_of_type(np.short)
        True
        >>> field.is_of_type(np.int32)
        False

        """
        return self.type == type_to_compare

    @property
    def type(self):
        """Type of unitary data in the Field's data vector.
        Should be properly set at the Field construction to have properly allocated data.

        Returns
        -------
        numpy.dtype

        Examples
        --------
        >>> from ansys.dpf.core import locations
        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
        >>> field.type
        dtype('uint64')

        """
        return self._type

    @property
    def component_count(self):
        return self._api.cscustom_type_field_get_number_of_components(self)

    @property
    def elementary_data_count(self):
        return self._api.cscustom_type_field_get_number_elementary_data(self)

    @property
    def size(self):
        return self._api.cscustom_type_field_get_data_size(self)

    def _set_scoping(self, scoping):
        self._api.cscustom_type_field_set_cscoping(self, scoping)

    def _get_scoping(self):
        obj = self._api.cscustom_type_field_get_cscoping(self)
        if obj is not None:
            return scoping.Scoping(scoping=obj, server=self._server)

    def get_entity_data(self, index):
        """Returns the array corresponding to the data of a given entity index.

        Parameters
        ----------
        index: int
            Index in the ``Scoping``.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> from ansys.dpf.core import locations
        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
        >>> field.append([1000000, 2000000], 1)
        >>> field.append([1000000, 2000000, 3000000], 2)
        >>> field.get_entity_data(0)
        DPFArray([1000000, 2000000]...
        >>> field.get_entity_data(1)
        DPFArray([1000000, 2000000, 3000000]...

        """
        try:
            vec = dpf_vector.DPFVectorCustomType(self._type, client=self._server.client)
            self._api.cscustom_type_field_get_entity_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, index
            )
            data = dpf_array.DPFArray(vec)

        except NotImplementedError:
            data = self._api.cscustom_type_field_get_entity_data(self, index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def get_entity_data_by_id(self, id):
        """Returns the array corresponding to the data of a given entity id.

        Parameters
        ----------
        id: int
            Entity ID in the ``Scoping``.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> from ansys.dpf.core import locations
        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> field = dpf.CustomTypeField(unitary_type=np.uint64)
        >>> field.append([1000000, 2000000], 1)
        >>> field.append([1000000, 2000000, 3000000], 2)
        >>> field.get_entity_data_by_id(1)
        DPFArray([1000000, 2000000]...
        >>> field.get_entity_data_by_id(2)
        DPFArray([1000000, 2000000, 3000000]...

        """
        try:
            vec = dpf_vector.DPFVectorCustomType(self._type, client=self._server.client)
            self._api.cscustom_type_field_get_entity_data_by_id_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, id)
            data = dpf_array.DPFArray(vec)

        except NotImplementedError:
            index = self.scoping.index(id)
            if index < 0:
                raise ValueError(f"The ID {id} must be greater than 0.")
            data = self.get_entity_data(index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def append(self, data, scopingid):
        if isinstance(data, list):
            data = np.array(data, dtype=self._type)
        self._api.cscustom_type_field_push_back(self, scopingid, _get_size_of_list(data), data)

    def _get_data_pointer(self):
        try:
            vec = dpf_vector.DPFVectorInt(client=self._server.client)
            self._api.cscustom_type_field_get_data_pointer_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return dpf_array.DPFArray(vec)

        except NotImplementedError:
            return self._api.cscustom_type_field_get_data_pointer(self, True)

    def _set_data_pointer(self, data):
        return self._api.cscustom_type_field_set_data_pointer(self, _get_size_of_list(data), data)

    def _get_data(self, np_array=True):
        try:
            vec = dpf_vector.DPFVectorCustomType(self._type, client=self._server.client)
            self._api.cscustom_type_field_get_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            data = dpf_array.DPFArray(vec) if np_array else dpf_array.DPFArray(vec).tolist()
        except NotImplementedError:
            data = self._api.cscustom_type_field_get_data(self, np_array)
        n_comp = self.component_count
        if np_array and n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def _set_data(self, data):
        if isinstance(data, (np.ndarray, np.generic)):
            if data.dtype != self._type:
                data = data.astype(self._type)
        else:
            data = np.array(data, dtype=self._type)
        size = _get_size_of_list(data)
        return self._api.cscustom_type_field_set_data(self, size, data)

    def resize(self, nentities, datasize):
        """Allocate memory.

        Parameters
        ----------
        nentities : int
            Number of IDs in the scoping.
        datasize : int
            Size of the data vector.

        """
        return self._api.cscustom_type_field_resize(self, datasize, nentities)

    def _load_field_definition(self):
        """Attempt to load the field definition for this field."""
        # try:
        out = self._api.cscustom_type_field_get_shared_field_definition(self)
        return FieldDefinition(out, self._server)

    @property
    def unit(self):
        """Units for the field.

        Returns
        ----------
        str
           Units for the field.

        Examples
        --------
        Units for a displacement field.

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.CustomTypeField(int, 10)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'

        """
        if self.field_definition:
            return self.field_definition.unit

    @unit.setter
    def unit(self, value):
        """Change the unit for the field

        Parameters
        ----------
        value : str
            Units for the field.

        Examples
        --------
        Units for a displacement field.

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.CustomTypeField(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'

        """
        fielddef = self.field_definition
        fielddef.unit = value
        self.field_definition = fielddef

    @property
    def dimensionality(self):
        """Dimensionality represents the shape of the elementary data contained in the field.

        Returns
        -------
        dimensionality : :class:`ansys.dpf.core.dimensionality.Dimensionality`
            Nature and size of the elementary data.
        """
        if self.field_definition:
            return self.field_definition.dimensionality

    @dimensionality.setter
    def dimensionality(self, value):
        fielddef = self.field_definition
        fielddef.dimensionality = value
        self.field_definition = fielddef

    @property
    def name(self):
        """Name of the field."""
        return self._field_definition.name

    def _set_field_definition(self, field_definition):
        """Set the field definition.

        Parameters
        ----------
        field_definition : :class"`ansys.dpf.core.field_definition.FieldDefinition`

        """
        self._api.cscustom_type_field_set_field_definition(self, field_definition)
        self._field_definition = self._load_field_definition()

    @property
    def field_definition(self):
        """CustomTypeField information, including its location, unit, dimensionality
        and shell layers.

        Returns
        -------
        :class:`ansys.dpf.core.field_definition.FieldDefinition`

        """
        return self._field_definition

    @field_definition.setter
    def field_definition(self, value):
        self._set_field_definition(value)

    def _set_support(self, support):
        self._api.cscustom_type_field_set_support(self, support)

    @property
    def support(self):
        obj = self._api.cscustom_type_field_get_support(self)
        if obj is not None:
            return Support(
                support=obj,
                server=self._server
            )

    @support.setter
    def support(self, val):
        self._set_support(val)
