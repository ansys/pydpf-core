"""
TimeFreqSupport
===============
"""
from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.errors import protect_grpc
from ansys.grpc.dpf import (
    base_pb2,
    support_pb2,
    time_freq_support_pb2,
    time_freq_support_pb2_grpc,
)


class TimeFreqSupport:
    """Represents a time frequency support, which is a description of a temporal or frequency analysis.

    This class stores values such as the frequencies (time/complex), RPMs, and harmonic indices.
    The RPM value is a step (or load step)-based value.
    The time freqencies, complex frequencies, and harmonic indices are set-based values.
    There is one set value for each step/substep combination.

    Parameters
    ----------
    time_freq_support : ansys.grpc.dpf.time_freq_support_pb2.TimeFreqSupport
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
        if server is None:
            server = dpf.core._global_server()

        self._server = server
        self._stub = self._connect()
        if isinstance(time_freq_support, time_freq_support_pb2.TimeFreqSupport):
            self._message = time_freq_support
        elif isinstance(time_freq_support, support_pb2.Support):
            self._message = time_freq_support_pb2.TimeFreqSupport()
            self._message.id = time_freq_support.id
        else:
            request = base_pb2.Empty()
            self._message = self._stub.Create(request)

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        description : str
        """
        from ansys.dpf.core.core import _description

        return _description(self._message, self._server)

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
        array([0.        , 0.019975  , 0.039975  , 0.059975  , 0.079975  ,
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
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.freq_real.CopyFrom(frequencies._message)
        self._stub.Update(request)

    @time_frequencies.setter
    def time_frequencies(self, value):
        """Time frequencies that define the time_freq_support of the analysis.
        Frequencies field can have one value by set.

        Parameters
        ----------
        value : Field
            Field of time frequencies that must be set.
        """
        return self._set_time_frequencies(value)

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
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.freq_complex.CopyFrom(complex_frequencies._message)
        self._stub.Update(request)

    @complex_frequencies.setter
    def complex_frequencies(self, value):
        """Complex frequencies that define the time_freq_support of the analysis.
        Complex frequencies field can have one value by set.

        Parameters
        ----------
        value : Field
            Field of complex frequencies that must be set.
        """
        return self._set_complex_frequencies(value)

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
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.rpm.CopyFrom(rpms._message)
        self._stub.Update(request)

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
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        cyclic_data = time_freq_support_pb2.CyclicHarmonicData()
        request.time_freq_support.CopyFrom(self._message)
        cyclic_data.cyc_harmonic_index.CopyFrom(harmonic_indices._message)
        cyclic_data.stage_num = stage_num
        request.cyc_harmonic_data.CopyFrom(cyclic_data)
        self._stub.Update(request)

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

    @protect_grpc
    def _get_frequency(self, step, substep, cumulative_index, cplx):
        """Retrieves the frequence corresponding to the requested step/substep or
        cumulative index.
        """
        request = time_freq_support_pb2.GetRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.complex = cplx
        # request.complex = base_pb2.Complex.Value(cplx)
        if cumulative_index is None:
            request.step_substep.step = step
            request.step_substep.substep = substep
        else:
            request.cumulative_index = cumulative_index
        return self._stub.Get(request).frequency

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
            Whehter to return a complex frequency. The default is ``False``.

        Returns
        -------
        index : int
            Cumulative index based on either the step, substep, or
            frequency.
        """
        return self._get_cumulative_index(step, substep, freq, cplx)

    @protect_grpc
    def _get_cumulative_index(self, step, substep, freq, cplx):
        """Retrieve the cumulative index corresponding to the requested step/substep
        or frequency."""
        request = time_freq_support_pb2.GetRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.bool_cumulative_index = True
        request.complex = cplx
        if freq is not None:
            request.frequency = freq
        else:
            request.step_substep.step = step
            request.step_substep.substep = substep
        return self._stub.Get(request).cumulative_index

    @protect_grpc
    def _sets_count(self):
        """
        Returns
        -------
        count : int
        """
        request = time_freq_support_pb2.CountRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.entity = base_pb2.NUM_SETS
        return self._stub.Count(request).count

    @protect_grpc
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
        request = time_freq_support_pb2.ListRequest()
        request.time_freq_support.CopyFrom(self._message)

        list_response = self._stub.List(request)
        if cplx is True and list_response.freq_complex.id != 0:
            return dpf.core.Field(server=self._server, field=list_response.freq_complex)
        elif cplx is False and list_response.freq_real.id != 0:
            return dpf.core.Field(server=self._server, field=list_response.freq_real)
        return None

    @protect_grpc
    def _get_rpms(self):
        """Retrieves a field of all the RPMs in the model.

        Returns
        -------
        field : dpf.core.Field
            Field of all the RPMs in the model (complex or real).
        """
        request = time_freq_support_pb2.ListRequest()
        request.time_freq_support.CopyFrom(self._message)

        list_response = self._stub.List(request)
        if list_response.rpm.id != 0:
            return dpf.core.Field(server=self._server, field=list_response.rpm)
        return None

    @protect_grpc
    def _get_harmonic_indices(self, stage_num=0):
        """Retrieves a field of all the harmonic indices in the model.

        Returns
        -------
        field : dpf.core.Field
            Field of all the harmonic indices in the model (complex or real).

        stage_num: int, optional, default = 0
            Targeted stage number.
        """
        request = time_freq_support_pb2.ListRequest()
        request.time_freq_support.CopyFrom(self._message)
        request.cyclic_stage_num = stage_num

        list_response = self._stub.List(request)
        if list_response.cyc_harmonic_index.id != 0:
            return dpf.core.Field(
                server=self._server, field=list_response.cyc_harmonic_index
            )
        return None

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
        The values for time freqencies, complex frequencies, and harmonic indices are set-based.
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

        This methos is useful for passing data from one server instance to another.

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

    def _connect(self):
        """Connect to the gRPC service."""
        return time_freq_support_pb2_grpc.TimeFreqSupportServiceStub(
            self._server.channel
        )

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass
