import traceback
import warnings

from abc import abstractmethod
from ansys.dpf.gate.generated import field_abstract_api

from ansys.dpf.core import scoping
from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import errors
from ansys.dpf.core import server as server_module
from ansys.dpf.core.cache import _setter
from ansys.dpf.gate import (
    data_processing_capi,
    data_processing_grpcapi,
)

import numpy as np


class _FieldBase:
    """Contains base APIs for all implementations that follow DPF's field concept."""

    def __init__(
            self,
            nentities=0,
            nature=natures.vector,
            location=locations.nodal,
            field=None,
            server=None,
    ):
        """Initialize the field either with an optional field message or by connecting to a stub."""
        # step 1: get server
        self._server = server_module.get_or_create_server(
            field._server if isinstance(field, _FieldBase) else server
        )

        # step 2: get api
        self._api_instance = None  # see property self._api

        # step3: init environment
        if hasattr(self._api, "init_property_field_environment"):
            self._api.init_property_field_environment(self)  # creates stub when gRPC
        elif hasattr(self._api, "init_field_environment"):
            self._api.init_field_environment(self)  # creates stub when gRPC
        else:
            self._api.init_string_field_environment(self)

        # step4: if object exists, take the instance, else create it
        if field is not None:
            if isinstance(field, _FieldBase):
                self._server = field._server
                self._api_instance = None
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(field)
            else:
                self._internal_obj = field

        else:
            self._internal_obj = self.__class__._field_create_internal_obj(
                self._api,
                client=self._server.client,
                nature=nature,
                nentities=nentities,
                location=location)

    @property
    @abstractmethod
    def _api(self):
        pass

    @staticmethod
    @abstractmethod
    def _field_create_internal_obj(api: field_abstract_api.FieldAbstractAPI, client, nature,
                                   nentities, location=locations.nodal, ncomp_n=0, ncomp_m=0):
        """Returns a gRPC field message or C object instance of a new field.
        This new field is created with this functions parameter attributes

        Parameters
        ----------
        client : None, GrpcClient, GrpcServer

        snature : str
            Nature of the field entity data. For example:

            - :class:`ansys.dpf.core.natures.matrix`
            - :class:`ansys.dpf.core.natures.scalar`

        num_entities : int
            Number of entities to reserve.

        location : str, optional
            Location of the field. For example:

            - :class:`ansys.dpf.core.natures.nodal` (``"Nodal"``)
            - :class:`ansys.dpf.core.natures.elemental` (``"Elemental"``)
            - :class:`ansys.dpf.core.natures.elemental_nodal` (``"ElementalNodal"``)
            - ...

        ncomp_n : int
            Number of lines.
        ncomp_m : int
            Number of columns.

        Returns
        -------
        field : field_pb2.Field or ctypes.void_p
            DPF field in the requested format.
        """
        pass

    @property
    def shape(self):
        """Numpy-like shape of the field.

        Returns
        -------
        tuple

        Examples
        --------
        Shape of a stress field.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_transient_result())
        >>> s_op =model.results.stress()
        >>> s_fc = s_op.outputs.fields_container()
        >>> field = s_fc[0]
        >>> field.shape
        (5720, 6)

        """
        if self.component_count != 1:
            return (self.elementary_data_count, self.component_count)
        return self.elementary_data_count

    @property
    @abstractmethod
    def location(self):
        pass

    @property
    @abstractmethod
    def component_count(self):
        """Number of components in each elementary data of the field.

        Returns
        -------
        int
            Number of components in each elementary data of the field.
        """
        pass

    @property
    @abstractmethod
    def elementary_data_count(self):
        """Number of elementary data in the field.

        Returns
        -------
        int
            Number of elementary data in the field.

        """
        pass

    @property
    @abstractmethod
    def size(self):
        """Length of the data vector.

        The length is equal to the number of elementary data times the number of components.

        Returns
        -------
        int
            Length of the data vector.

        """
        pass

    @property
    def elementary_data_shape(self):
        """Numpy-like shape of the field."""
        if self.component_count != 1:
            return (1, self.component_count)
        else:
            return self.component_count

    @property
    def ndim(self):
        return self.component_count

    def __str__(self):
        """Describes the entity.

        Returns
        -------
        str
            Description of the entity.

        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def __len__(self):
        return self.size

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())

    @abstractmethod
    def _set_scoping(self, scoping):
        """Set the scoping.

        Parameters
        ----------
        scoping : :class:`ansys.dpf.core.scoping.Scoping`

        """
        self._api.csfield_set_cscoping(self, scoping)

    @abstractmethod
    def _get_scoping(self):
        """Retrieve the scoping.

        Returns
        -------
        scoping : :class:`ansys.dpf.core.scoping.Scoping`

        """
        return scoping.Scoping(scoping=self._api.csfield_get_cscoping(self), server=self._server)

    @property
    def scoping(self):
        """Scoping specifying where the data is.

        Each entity data is on a given scoping ID.

        Returns
        -------
        scoping : :class:`ansys.dpf.core.scoping.Scoping`

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> scoping = fields_container[0].scoping
        >>> scoping.location
        'Elemental'
        >>> scoping.id(3)
        586
        >>> #The fourth elementary data of the field corresponds to
        >>> #the element id number 586 in the mesh
        """

        return self._get_scoping()

    @scoping.setter
    def scoping(self, scoping):
        return self._set_scoping(scoping)

    @abstractmethod
    def get_entity_data(self, index):
        """Retrieves the elementary data of the scoping's index in an array.

        Returns
        --------
        numpy.ndarray

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> fields_container[0].get_entity_data(0)
        DPFArray([[-3.27795062e+05,  1.36012200e+06,  1.49090608e+08,
                -4.88688900e+06,  1.43038560e+07,  1.65455040e+07],
               [-4.63817550e+06,  1.29312225e+06,  1.20411832e+08,
                -6.06617800e+06,  2.34829700e+07,  1.77231120e+07],
               [-2.35684860e+07, -3.53474400e+07,  2.01501168e+08,
                -5.23361700e+06, -2.88789280e+07, -6.16478200e+06],
               [-3.92756960e+07, -2.72369280e+07,  1.81454016e+08,
                -3.75441450e+06, -3.62480300e+06, -3.26075620e+07],
               [ 1.63554530e+07,  2.83190520e+07,  1.05084256e+08,
                -1.30219020e+07,  5.19906719e+05,  8.82430200e+06],
               [ 1.80755620e+07,  5.25578750e+06,  7.76211600e+07,
                -7.53063750e+06,  2.44717000e+06,  2.92675125e+06],
               [ 9.25567760e+07,  8.15244320e+07,  2.77157632e+08,
                -1.48489875e+06,  5.89250600e+07,  2.05608920e+07],
               [ 6.70443680e+07,  8.70343440e+07,  2.73050464e+08,
                -2.48670150e+06,  1.52268930e+07,  6.09583280e+07]]...

        """
        pass

    @abstractmethod
    def get_entity_data_by_id(self, id):
        """Retrieve the data of the scoping's ID in the parameter of the field in an array.

        Returns
        -------
        numpy.ndarray
            Data based on the scoping ID.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> fields_container[0].get_entity_data_by_id(391)
        DPFArray([[-3.27795062e+05,  1.36012200e+06,  1.49090608e+08,
                -4.88688900e+06,  1.43038560e+07,  1.65455040e+07],
               [-4.63817550e+06,  1.29312225e+06,  1.20411832e+08,
                -6.06617800e+06,  2.34829700e+07,  1.77231120e+07],
               [-2.35684860e+07, -3.53474400e+07,  2.01501168e+08,
                -5.23361700e+06, -2.88789280e+07, -6.16478200e+06],
               [-3.92756960e+07, -2.72369280e+07,  1.81454016e+08,
                -3.75441450e+06, -3.62480300e+06, -3.26075620e+07],
               [ 1.63554530e+07,  2.83190520e+07,  1.05084256e+08,
                -1.30219020e+07,  5.19906719e+05,  8.82430200e+06],
               [ 1.80755620e+07,  5.25578750e+06,  7.76211600e+07,
                -7.53063750e+06,  2.44717000e+06,  2.92675125e+06],
               [ 9.25567760e+07,  8.15244320e+07,  2.77157632e+08,
                -1.48489875e+06,  5.89250600e+07,  2.05608920e+07],
               [ 6.70443680e+07,  8.70343440e+07,  2.73050464e+08,
                -2.48670150e+06,  1.52268930e+07,  6.09583280e+07]]...

        """
        pass

    @abstractmethod
    def append(self, data, scopingid):
        """Add an entity data to the existing data.

        Parameters
        ----------
        data : list of int, double, or array
          Data in the entity.
        scopingid : int
            ID of the scoping.

        Examples
        --------
        >>> from ansys.dpf.core import fields_factory
        >>> field = fields_factory.create_3d_vector_field(2)
        >>> field.append([1.,2.,3.],1)
        >>> field.append([1.,2.,3.],2)
        >>> field.data
        DPFArray([[1., 2., 3.],
               [1., 2., 3.]]...
        >>> field.scoping.ids
        <BLANKLINE>
        ...[1, 2]...

        """
        pass

    @property
    def _data_pointer(self):
        """First index of each entity data.

        Returns
        -------
        numpy.ndarray
            Data in the field.

        Notes
        -----
        Print a progress bar.

        """
        return self._get_data_pointer()

    @abstractmethod
    def _get_data_pointer(self):
        """First index of each entity data.

        Returns
        -------
        numpy.ndarray
            Data in the field.

        Notes
        -----
        Print a progress bar.

        """
        pass

    @property
    def _data_pointer_as_list(self):
        """First index of each entity data.

        Returns
        -------
        list
            List of first indexes of each data data.

        Notes
        -----
        Print a progress bar.

        """
        return self._data_pointer.tolist()

    @_data_pointer.setter
    def _data_pointer(self, data):
        self._set_data_pointer(data)

    @abstractmethod
    def _set_data_pointer(self, data):
        pass

    @property
    def data(self):
        """Data in the field as an array.

        Returns
        -------
        numpy.ndarray
            Data in the field.

        Notes
        -----
        Print a progress bar.
        """
        return self._get_data()

    @property
    def data_as_list(self):
        """Data in the field as a Python list.

        Returns
        -------
        List
            List of the data in the field.

        Notes
        -----
        Print a progress bar.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> # field.data_as_list

        """
        return self._get_data(np_array=False)

    @data.setter
    def data(self, data):
        self._set_data(data)

    @abstractmethod
    def _get_data(self, np_array=True):
        pass

    @abstractmethod
    def _set_data(self, data):
        pass


class _LocalFieldBase(_FieldBase):
    """Caches the internal data of the field so that it can be modified locally.

    A single update request is sent to the server when the local field is deleted.

    Parameters
    ----------
    field : _FieldBase
        Field to copy locally.

    """

    def __init__(self, field):
        self.__cache_data__(field)

    def __cache_data__(self, field):
        self._ncomp = super().component_count
        self._data_copy = super().data_as_list
        self._num_entities_reserved = len(self._data_copy)
        self._data_pointer_copy = super()._get_data_pointer().tolist()
        self._scoping_copy = super().scoping.as_local_scoping()
        self._has_data_pointer = len(self._data_pointer_copy) > 0

    @property
    def _num_entities(self):
        return len(self._scoping_copy)

    @property
    def size(self):
        """Length of the data vector.

        Length equals the number of elementary data times the number of components.

        Returns
        -------
        int
            Length of the data vector.

        """
        return len(self._data_copy)

    def get_entity_data(self, index):
        """Retrieve the elementary data of the scoping's index as an array.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     print(f.get_entity_data(0))
        [[-3.27795062e+05  1.36012200e+06  1.49090608e+08 -4.88688900e+06
           1.43038560e+07  1.65455040e+07]
         [-4.63817550e+06  1.29312225e+06  1.20411832e+08 -6.06617800e+06
           2.34829700e+07  1.77231120e+07]
         [-2.35684860e+07 -3.53474400e+07  2.01501168e+08 -5.23361700e+06
          -2.88789280e+07 -6.16478200e+06]
         [-3.92756960e+07 -2.72369280e+07  1.81454016e+08 -3.75441450e+06
          -3.62480300e+06 -3.26075620e+07]
         [ 1.63554530e+07  2.83190520e+07  1.05084256e+08 -1.30219020e+07
           5.19906719e+05  8.82430200e+06]
         [ 1.80755620e+07  5.25578750e+06  7.76211600e+07 -7.53063750e+06
           2.44717000e+06  2.92675125e+06]
         [ 9.25567760e+07  8.15244320e+07  2.77157632e+08 -1.48489875e+06
           5.89250600e+07  2.05608920e+07]
         [ 6.70443680e+07  8.70343440e+07  2.73050464e+08 -2.48670150e+06
           1.52268930e+07  6.09583280e+07]]

        """
        if index > self._num_entities:
            raise ValueError(
                f"Requested scoping {index} is greater than the number of "
                f"available indices {len(self._scoping_copy)}"
            )
        if self._has_data_pointer:
            first_index = self._data_pointer_copy[index]
            if index < len(self._data_pointer_copy) - 1:
                last_index = self._data_pointer_copy[index + 1] - 1
            else:
                last_index = len(self._data_copy) - 1
        else:
            first_index = self._ncomp * index
            last_index = self._ncomp * (index + 1) - 1
        if self._is_property_field:
            array = np.array(
                self._data_copy[first_index: last_index + 1], dtype=np.int32
            )
        else:
            array = np.array(self._data_copy[first_index: last_index + 1])

        if self._ncomp > 1:
            return array.reshape((array.size // self._ncomp, self._ncomp))
        else:
            return array

    def get_entity_data_by_id(self, id):
        """Retrieve the data of the scoping's ID in the parameter of the field.

        Returns
        -------
        numpy.ndarray
            Data based on the scoping ID.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.static_rst)
        >>> stress_op = model.results.stress()
        >>> fields_container = stress_op.outputs.fields_container()
        >>> with fields_container[0].as_local_field() as f:
        ...     for id in f.scoping_ids:
        ...         if id < 2:
        ...             print(f.get_entity_data_by_id(id))
        [[-5.83890625e+03 -1.04498969e+05 -5.83890625e+03  2.10637354e+03
          -2.10637354e+03 -1.45397385e+02]
         [ 3.53322632e+03 -1.00388367e+05  3.53322632e+03 -1.66410352e+03
           1.66410352e+03  5.36620178e+01]
         [-1.05799683e+03 -1.00437922e+05  2.14961670e+03  5.90637268e+02
           1.37861340e+03 -1.68223175e+02]
         [ 2.62742480e+03 -9.89340078e+04 -2.02909998e+03 -2.40310791e+03
          -1.84942798e+03  7.16406616e+02]
         [-2.02909998e+03 -9.89340078e+04  2.62742480e+03  1.84942798e+03
           2.40310791e+03  7.16406616e+02]
         [ 2.14961670e+03 -1.00437922e+05 -1.05799683e+03 -1.37861340e+03
          -5.90637268e+02 -1.68223175e+02]
         [-4.94986755e+02 -9.87357891e+04 -4.94986755e+02 -6.93923187e+01
           6.93923187e+01 -1.59779755e+02]
         [ 1.36953296e+03 -9.76330156e+04  1.36953296e+03 -7.69014221e+02
           7.69014221e+02  4.90502930e+02]]

        """
        index = self._scoping_copy.index(id)
        if index < 0:
            raise ValueError(f"The id {id} doesn't exist in the scoping")
        return self.get_entity_data(index)

    @_setter
    def append(self, data, scopingid):
        """Add an entity data to the existing data.

        Parameters
        ----------
        data : list of int, double or array
            Data for the entity.
        scopingid : int
            ID of the scoping.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities=100
        >>> field_to_local = dpf.fields_factory.create_3d_vector_field(
        ...     num_entities, location=dpf.locations.elemental_nodal
        ... )
        >>> with field_to_local.as_local_field() as f:
        ...     for i in range(1,num_entities+1):
        ...         f.append([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]],i)

        """
        if self._is_property_field:
            if isinstance(data[0], np.int64):
                data = np.array(data, dtype=np.int32)
            if not isinstance(data[0], int) and not isinstance(data[0], np.int32):
                raise errors.InvalidTypeError("data", "list of int")
        if (len(data) > 0 and isinstance(data, list)) or isinstance(
                data, (np.ndarray, np.generic)
        ):
            data = np.array(data).flatten().tolist()

        data_size = len(self._data_copy)
        self._scoping_copy.append(scopingid)
        if len(self._data_pointer_copy) > 0:
            self._data_pointer_copy.append(data_size)

        self._data_copy.extend(data)
        if self._has_data_pointer == False:
            if isinstance(data, (np.ndarray, np.generic)):
                data_size = data.size
            else:
                data_size = len(data)
            if data_size > self._ncomp:
                self._data_pointer_copy = [
                    i * self._ncomp for i in range(0, self._num_entities)
                ]
                self._has_data_pointer = True

    def data_as_list(self):
        """Retrieve the data in the field as a Python list.

        Returns
        -------
        list
            List of the data in the field.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     my_data_list = f.data_as_list

        """
        return self._data_copy

    @property
    def data(self):
        """Data in the field.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> with field.as_local_field() as f:
        ...     print(f.data)
        [[ 6.25586668e-03 -1.39243136e-02  2.42697211e-05]
         [ 1.79675948e-02 -2.74812825e-02  1.83822050e-05]
         [-6.72664571e-03 -3.21373459e-02  1.67159110e-04]
         ...
         [-6.07730368e-03  3.22569017e-02  3.10184480e-04]
         [-3.51074714e-06  2.16872928e-08  6.40738989e-05]
         [ 1.03542516e-02 -3.53018374e-03 -3.98914380e-05]]

        """

        if self._ncomp > 1:
            return np.array(self._data_copy).reshape(
                len(self._data_copy) // self._ncomp, self._ncomp
            )
        else:
            return np.array(self._data_copy)

    @data.setter
    @_setter
    def data(self, data):
        if self._is_property_field:
            if not isinstance(data[0], int) and not isinstance(data[0], np.int32):
                raise errors.InvalidTypeError("data", "list of int")
        else:
            if isinstance(data, (np.ndarray, np.generic)):
                if data.shape != self.shape and 0 != self.size:
                    raise ValueError(
                        f"An array of shape {self.shape} is expected and "
                        f"shape {data.shape} was input"
                    )
        if isinstance(data, (np.ndarray, np.generic)):
            self._data_copy = data.flatten().tolist()
        elif len(data) > 0 and isinstance(data, list):
            self._data_copy = np.array(data).flatten().tolist()
        else:
            self._data_copy = data

    @property
    def elementary_data_count(self):
        """Number of elementary data in the field.

        Returns
        -------
        int
           Number of elementary data in the field.

        """
        if hasattr(self, "_data_copy"):
            return len(self._data_copy) / self._ncomp
        else:
            return super().elementary_data_count

    @property
    def component_count(self):
        """Number of components in each elementary data of the field.

        Returns
        -------
        int
            Number of components in each elementary data of the field.
        """

        return self._ncomp

    @property
    def _data_pointer(self):
        """First index of each entity data in an array.

        Returns
        -------
        numpy.ndarray
            Array of first indexes of each entity data.
        """
        return np.array(self._data_pointer_copy)

    @property
    def _data_pointer_as_list(self):
        """First index of each entity data as a list.

        Returns
        -------
        List
            List of first indexes of each entity data.
        """
        return self._data_pointer_copy

    @_data_pointer.setter
    @_setter
    def _data_pointer(self, data):
        if isinstance(data, (np.ndarray, np.generic)):
            self._data_pointer_copy = data.tolist()
        else:
            self._data_pointer_copy = data
        if self._has_data_pointer == False and len(data) > 0:
            self._has_data_pointer = True

    @property
    def scoping_ids(self):
        """Scoping IDs of the field.

        Returns
        -------
        list
            List of integers representing the scoping IDs of the field.
        """
        return self._scoping_copy.ids

    @scoping_ids.setter
    def scoping_ids(self, data):
        self._scoping_copy.ids = data

    @property
    def scoping(self):
        """Scoping specifying where the data is.

        Each entity data is on a given scoping ID.

        Returns
        -------
        scoping : :class:`ansys.dpf.core.scoping.Scoping`
        """
        return self._scoping_copy

    @scoping.setter
    @_setter
    def scoping(self, data):
        if not isinstance(data, scoping._LocalScoping):
            self._scoping_copy = data.as_local_scoping()
        else:
            self._scoping_copy = data

    def release_data(self):
        """Release the data."""
        if hasattr(self, "_is_set") and self._is_set:
            super()._set_data(self._data_copy)
            super()._set_data_pointer(self._data_pointer_copy)
            super()._set_scoping(self._scoping_copy)
            self._scoping_copy = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if tb is None:
            self._is_exited = True
            self.release_data()
        else:
            print(tb)

    def __del__(self):
        if not hasattr(self, "_is_exited") or not self._is_exited:
            self._is_exited = True
            self.release_data()
        super(_LocalFieldBase, self).__del__()
        pass
