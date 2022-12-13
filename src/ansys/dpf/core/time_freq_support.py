"""
.. _ref_timefreqsupport:

TimeFreqSupport
===============
"""
from ansys.dpf.gate import time_freq_support_capi, time_freq_support_grpcapi

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.support import Support


class TimeFreqSupport(Support):
    """Represents a time frequency support, a description of a temporal or frequency analysis.

    This class stores values such as the frequencies (time/complex), RPMs, and harmonic indices.
    The RPM value is a step (or load step)-based value.
    The time frequencies, complex frequencies, and harmonic indices are set-based values.
    There is one set value for each step/substep combination.

    Parameters
    ----------
    time_freq_support : ctypes.c_void_p, ansys.grpc.dpf.time_freq_support_pb2.TimeFreqSupport
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Create a time frequency support from a model.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = Model(transient)
    >>> time_freq_support = model.metadata.time_freq_support # printable

    """

    def __init__(self, time_freq_support=None, server=None):
        """Initialize the TimeFreqSupport with its TimeFreqSupport message (if possible)."""
        super(TimeFreqSupport, self).__init__(support=time_freq_support, server=server)

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=time_freq_support_capi.TimeFreqSupportCAPI,
            grpcapi=time_freq_support_grpcapi.TimeFreqSupportGRPCAPI)

        # step3: init environment
        self._api.init_time_freq_support_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if time_freq_support is not None:
            self._internal_obj = time_freq_support
            # Might to test for type for CLayer as I have not tested this for C
            #self._internal_obj = support_api.support_get_as_time_freq_support(self)
        else:
            if self._server.has_client():
                self._internal_obj = self._api.time_freq_support_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.time_freq_support_new()

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    @property
    def time_frequencies(self):
        """Field of time frequencies or time values for the active result.
        Frequencies field can have one value by set.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> time_freq_support = model.metadata.time_freq_support
        >>> freq = time_freq_support.time_frequencies
        >>> freq.data
        <BLANKLINE>
        ...rray([0.        , 0.019975  , 0.039975  , 0.059975  , 0.079975  ,
               0.099975  , 0.119975  , 0.139975  , 0.159975  , 0.179975  ,
               0.199975  , 0.218975  , 0.238975  , 0.258975  , 0.278975  ,
               0.298975  , 0.318975  , 0.338975  , 0.358975  , 0.378975  ,
               0.398975  , 0.417975  , 0.437975  , 0.457975  , 0.477975  ,
               0.497975  , 0.517975  , 0.53754972, 0.55725277, 0.57711786,
               0.59702054, 0.61694639, 0.63683347, 0.65673452, 0.67662783])

        """
        return self._get_frequencies()

    def _set_time_frequencies(self, frequencies):
        """Set the time frequencies of the time_freq_support.
        Frequencies field can have one value by set.

        Parameters
        ----------
        frequencies: Field
            Field of time frequencies that must be set.
        """
        self._api.time_freq_support_set_shared_time_freqs(self, frequencies)

    @time_frequencies.setter
    def time_frequencies(self, value):
        """Time frequencies that define the time_freq_support of the analysis.
        Frequencies field can have one value by set.

        Parameters
        ----------
        value : Field
            Field of time frequencies that must be set.
        """
        self._set_time_frequencies(value)

    @property
    def complex_frequencies(self):
        """Field of complex frequencies for the active result.
        Complex frequencies field can have one value by set.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> time_freq_support = model.metadata.time_freq_support
        >>> freq = time_freq_support.complex_frequencies

        """
        return self._get_frequencies(cplx=True)

    def _set_complex_frequencies(self, complex_frequencies):
        """Set the frequencies of the time_freq_support.
        Complex frequencies field can have one value by set.

        Parameters
        ----------
        complex_frequencies : Field
            Field of frequencies that must be set.
        """
        self._api.time_freq_support_set_shared_imaginary_freqs(self, complex_frequencies)

    @complex_frequencies.setter
    def complex_frequencies(self, value):
        """Complex frequencies that define the time_freq_support of the analysis.
        Complex frequencies field can have one value by set.

        Parameters
        ----------
        value : Field
            Field of complex frequencies that must be set.
        """
        self._set_complex_frequencies(value)

    @property
    def rpms(self):
        """Field of RPMs for the active result.
        The RPM field has one value by load step.

        Returns ``None`` if the result has no RPMs.
        """
        return self._get_rpms()

    def _set_rpms(self, rpms):
        """Set the RPMs values of the time_freq_support.
        RPMs field has one value by load step.

        Parameters
        ----------
        rpms : Field
            Field of RPMs that must be set.
        """
        self._api.time_freq_support_set_shared_rpms(self, rpms)

    @rpms.setter
    def rpms(self, value):
        """RPMs that define the time_freq_support of the analysis.
        RPMs field has one value by load step.

        Parameters
        ----------
        value : Field
            Field of RPMs that must be set.
        """
        return self._set_rpms(value)

    def get_harmonic_indices(self, stage_num=0):
        """Retrieve the field of harmonic indices for the active result.

        Returns
        -------
        field : dpf.core.Field
            Field of all harmonic indices in the model (complex or
            real).  ``None`` if result is not cyclic and contains no
            harmonic indices.

        stage_num: int, default: 0, optional
            Targeted stage number.

        """
        return self._get_harmonic_indices(stage_num)

    def set_harmonic_indices(self, harmonic_indices, stage_num=0):
        """Set the harmonic indices values of the time frequency support.

        Parameters
        ----------
        harmonic_indices : Field
            Field of harmonic indices that must be set.
        stage_num: int, default: 0, optional
            Stage number that is defined by these harmonic indices.
        """
        self._api.time_freq_support_set_harmonic_indices(self, harmonic_indices, stage_num)

    @property
    def n_sets(self):
        """Number of result sets.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> time_freq_support = model.metadata.time_freq_support
        >>> time_freq_support.n_sets
        35

        """
        return self._sets_count()

    def get_frequency(self, step=0, substep=0, cumulative_index=None, cplx=False):
        """Retrieve the frequence corresponding to a requested step/substep or
        cumulative index.

        Parameters
        ----------
        step : int, optional
            Index of the step (one-based).
        substep : int, optional
            Index of the substep (one-based).
        cumulative_index : int, optional
            Cumulative index (one-based).
        cplx: bool
            Whether to return a complex frequency. The  default is ``False``.

        Returns
        -------
        frequency : double
            Frequency of the step or substep.
        """
        return self._get_frequency(step, substep, cumulative_index, cplx)

    def _get_frequency(self, step, substep, cumulative_index, cplx):
        """Retrieves the frequence corresponding to the requested step/substep or
        cumulative index.
        """
        if cumulative_index is None:
            # Use by_step methods
            if cplx:
                # Call for imaginary
                return self._api.time_freq_support_get_imaginary_freq_by_step(self, step, substep)
            else:
                # Call for real
                return self._api.time_freq_support_get_time_freq_by_step(self, step, substep)
        else:
            # Use by_cumul_index methods
            if cplx:
                # Call for imaginary
                return self._api.time_freq_support_get_imaginary_freq_by_cumul_index(
                    self, cumulative_index)
            else:
                # Call for real
                return self._api.time_freq_support_get_time_freq_by_cumul_index(self,
                                                                                cumulative_index)

    def get_cumulative_index(self, step=0, substep=0, freq=None, cplx=False):
        """Retrieves the cumulative index corresponding to the requested step/substep
        or frequency.

        Parameters
        ----------
        step : int, optional
            Analysis step.
        substep : int, optional
            Analysis substep.
        freq  : double, optional
            Frequency in Hz.
        cplx : False, optional
            Whether to return a complex frequency. The default is ``False``.

        Returns
        -------
        index : int
            Cumulative index based on either the step, substep, or
            frequency.
        """
        return self._get_cumulative_index(step, substep, freq, cplx)

    def _get_cumulative_index(self, step, substep, freq, cplx):
        """Retrieve the cumulative index corresponding to the requested step/substep
        or frequency."""
        if freq is None:
            if cplx is False:
                return self._api.time_freq_support_get_time_freq_cummulative_index_by_step(self,
                                                                                           step,
                                                                                           substep)
            else:
                raise NotImplementedError("get_cumulative_index is not implemented for cplx=False")
        else:
            from ansys.dpf.gate import integral_types
            i1 = integral_types.MutableInt32()
            i2 = integral_types.MutableInt32()
            if cplx:
                return self._api.time_freq_support_get_imaginary_freqs_cummulative_index(
                    self, freq, i1, i2
                )
            else:
                return self._api.time_freq_support_get_time_freq_cummulative_index_by_value(
                    self, freq, i1, i2
                )

    def _sets_count(self):
        """
        Returns
        -------
        count : int
        """
        return self._api.time_freq_support_get_number_sets(self)

    def _get_frequencies(self, cplx=False):
        """Retrieves a field of all the frequencies in the model
        (complex or real).

        Parameters
        ----------
        cplx : bool, optional
            Whether to return a complex frequency. The default ``False``.

        Returns
        -------
        field : dpf.core.Field
            Field of all the frequencies in the model (complex or real).
        """

        # attributes_list = self._get_attributes_list()
        if cplx:  # and "freq_complex" in attributes_list:
            # return attributes_list["freq_complex"]
            freq = self._api.time_freq_support_get_shared_imaginary_freqs(self)
        # elif cplx != True and "freq_real" in attributes_list:
        else:
            # return attributes_list["freq_real"]
            freq = self._api.time_freq_support_get_shared_time_freqs(self)
        if freq is not None:
            return dpf.core.Field(server=self._server, field=freq)

    def _get_rpms(self):
        """Retrieves a field of all the RPMs in the model.

        Returns
        -------
        field : dpf.core.Field
            Field of all the RPMs in the model (complex or real).
        """
        rpm = self._api.time_freq_support_get_shared_rpms(self)
        if rpm is not None:
            return dpf.core.Field(server=self._server, field=rpm)

    def _get_harmonic_indices(self, stage_num=0):
        """Retrieves a field of all the harmonic indices in the model.

        Returns
        -------
        field : dpf.core.Field
            Field of all the harmonic indices in the model (complex or real).

        stage_num: int, optional, default = 0
            Targeted stage number.
        """
        harmonic_indices = self._api.time_freq_support_get_shared_harmonic_indices(self, stage_num)
        if harmonic_indices is not None:
            return dpf.core.Field(server=self._server, field=harmonic_indices)

    def append_step(
            self,
            step_id,
            step_time_frequencies,
            step_complex_frequencies=None,
            rpm_value=None,
            step_harmonic_indices=None,
    ):
        """Append a step with all its field values in the time frequencies support.
        The RPM value is a step (or load step)-based value.
        The values for time frequencies, complex frequencies, and harmonic indices are set-based.
        There is one set value for each step/substep combination.

        It is necessary that each call of my_time_freq_support.append_step(kwargs**) contains
        the same arguments.

        It is necessary that time_frequencies/complex_frequencies/harmonic_indices lists have
        the same size if specified in the same my_time_freq_support.append_step(kwargs**) call.

        Parameters
        ----------
        step_id: int
            ID of the step to add.
        step_time_frequencies: list of int/float
            Values for time frequencies related to the specified step.
        step_complex_frequencies: list of int/float, optional
            Values for complex frequencies related to the specified step.
        rpm_value: int/float, optional
            Value for RPM value for the specified step.
        step_harmonic_indices: optional, dictionary or list
            Dictionary of ``{ int : list of int/float } = { stage_num : harmonic_indices }``
            or a list of int/float. In this case, stage_num default value is 0.
            Harmonic indices are values related to the specified step.

        Example
        -------
        >>> from ansys.dpf.core import TimeFreqSupport

        >>> tfq = TimeFreqSupport()
        >>> tfq.append_step(1, [0.1, 0.21, 1.0], rpm_value = 2.0)
        >>> tfq.append_step(2, [1.1, 2.0], rpm_value = 2.3)

        >>> tfq2 = TimeFreqSupport()
        >>> tfq2.append_step(1, [0.1, 0.21, 1.0], rpm_value = 2.0, step_harmonic_indices = [1.0, 2.0, 3.0])
        >>> tfq2.append_step(2, [1.1, 2.0], rpm_value = 2.3, step_harmonic_indices = [1.0, 2.0])
        >>> tfq2.append_step(3, [0.23, 0.25], rpm_value = 3.0, step_harmonic_indices = [1.0, 2.0])

        >>> tfq3 = TimeFreqSupport()
        >>> tfq3.append_step(1, [0.1, 0.21, 1.0], rpm_value = 2.0, step_harmonic_indices = {1: [1.0, 2.0, 3.0], 2: [1.0, 2.0, 2.5]})

        """  # noqa: E501

        time_frequencies = self.time_frequencies
        if time_frequencies is None:
            time_frequencies = core.Field(
                server=self._server,
                nature=core.natures.scalar,
                location=core.locations.time_freq,
            )
            time_frequencies.scoping.location = core.locations.time_freq_step
        time_frequencies.append(step_time_frequencies, step_id)
        self.time_frequencies = time_frequencies

        if step_complex_frequencies is not None:
            complex_frequencies = self.complex_frequencies
            if complex_frequencies is None:
                complex_frequencies = core.Field(
                    server=self._server,
                    nature=core.natures.scalar,
                    location=core.locations.time_freq,
                )
                complex_frequencies.scoping.location = core.locations.time_freq_step
            complex_frequencies.append(step_complex_frequencies, step_id)
            self.complex_frequencies = complex_frequencies

        if rpm_value is not None:
            rpms = self.rpms
            if rpms is None:
                rpms = core.Field(
                    server=self._server,
                    nature=core.natures.scalar,
                    location=core.locations.time_freq_step,
                )
            rpms.append([rpm_value], step_id)
            self.rpms = rpms

        if step_harmonic_indices is not None:
            if isinstance(step_harmonic_indices, list):
                self._set_harmonic_indices_at_stage(0, step_harmonic_indices, step_id)
            elif isinstance(step_harmonic_indices, dict):
                for key in step_harmonic_indices:
                    self._set_harmonic_indices_at_stage(
                        key, step_harmonic_indices[key], step_id
                    )
            else:
                raise dpf_errors.InvalidTypeError("list/dict", "step_harmonic_indices")

    def deep_copy(self, server=None):
        """Create a deep copy of the data for a time frequency support on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        tf_copy : TimeFreqSupport
        """
        tf = TimeFreqSupport(server=server)
        tf.time_frequencies = self.time_frequencies.deep_copy(server=server)
        if self.complex_frequencies:
            tf.complex_frequencies = self.complex_frequencies.deep_copy(server=server)
        if self.rpms:
            tf.rpms = self.rpms.deep_copy(server=server)
        i = 0
        while True:
            try:
                tf.set_harmonic_indices(
                    self.get_harmonic_indices(i).deep_copy(server=server), i
                )
                i += 1
            except:
                break
        return tf

    def _set_harmonic_indices_at_stage(self, stage_num, step_harmonic_indices, step_id):
        """Set values for harmonic indices for a specific stage number.

        Parameters
        ----------
        stage_num: int
            Stage number.
         harmonic_indices: list of int or float
            List of values for harmonic indices.
        """
        harmonic_indices = self.get_harmonic_indices(stage_num)
        if harmonic_indices is None:
            harmonic_indices = core.Field(
                server=self._server,
                nature=core.natures.scalar,
                location=core.locations.time_freq,
            )
            harmonic_indices.scoping.location = core.locations.time_freq_step
        harmonic_indices.append(step_harmonic_indices, step_id)
        self.set_harmonic_indices(harmonic_indices, stage_num)
