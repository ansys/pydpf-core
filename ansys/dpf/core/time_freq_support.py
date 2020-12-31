import grpc

from ansys import dpf
from ansys.grpc.dpf import time_freq_support_pb2, time_freq_support_pb2_grpc, base_pb2


class TimeFreqSupport:
    """A class used to represent a TimeFreqSupport which is a
    description of the temporal/frequency analysis

    Parameters
    ----------
    time_freq_support : ansys.grpc.dpf.time_freq_support_pb2.TimeFreqSupport message

    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.
    """

    def __init__(self, time_freq_support, channel=None):
        """Initialize the TimeFreqSupport with its TimeFreqSupport message"""
        if channel is None:
            channel = dpf.core._global_channel()       

        self._channel = channel
        self._stub = self._connect()
        if isinstance(time_freq_support, time_freq_support_pb2.TimeFreqSupport):
            self._message = time_freq_support
        else:
            self._message = time_freq_support_pb2.TimeFreqSupport()
            self._message.id = time_freq_support.id

    def __str__(self):
        field_freq = self.frequencies
        field_freq_cplx = self.complex_frequencies
        rpms = self.rpms
        harmonic_indeces = self.harmonic_indeces
        txt = 'Time/Frequency Info:\n'
        txt += '\tNumber of sets: %d\n\n' % self.n_sets
        if field_freq_cplx is not None :
            txt += 'With complex values\n \n'
        freq_unit = field_freq.unit
        if freq_unit is not None:
            if 's' in freq_unit:
                line = ['Cumulative', f'Time ({freq_unit})', 'Loadstep', 'Substep']
            else:
                line = ['Cumulative', f'Frequency ({freq_unit})', 'Loadstep', 'Substep']
        else:
            line = ['Cumulative', 'Time', 'Loadstep', 'Substep']
        txt += '{:^12} {:^16} {:^12} {:^12}'.format(*line)
        if rpms is not None:
            txt += '{:^12}'.format('RPM')
        if harmonic_indeces != None:
            txt += '{:^18}'.format('Harmonic index')
        txt += '\n'
        cum_index = 1
        for loadstep in range(len(field_freq.scoping.ids)) :
            substeps = field_freq.get_entity_data(loadstep).tolist()
            if rpms is not None:
                rpm = rpms.get_entity_data(loadstep)
            if harmonic_indeces is not None:
                hi = harmonic_indeces.get_entity_data(loadstep)
            substep = 1
            if substeps is not None:
                for frequency in substeps:
                    line = [cum_index, frequency, loadstep+1, substep]
                    txt += '{:^12} {:^16.3} {:^12} {:^12}'.format(*line)
                    if rpms is not None:
                        txt += '{:^12.3}'.format(rpm[loadstep-1])
                    if harmonic_indeces != None:
                        txt += '{:^18}'.format(int(abs(hi[substep-1])))
                    txt += '\n'
                    cum_index += 1
                    substep += 1
            else :
                # line = [cum_index,frequency,loadstep+1]
                # txt+='{:^12} {:^16.3} {:^12}'.format(*line)
                # txt+='\n'
                cum_index += 1
        return txt

    @property
    def frequencies(self):
        """Field of frequencies for the active result"""
        return self._get_frequencies()

    @property
    def complex_frequencies(self):
        """Field of complex frequencies for the active result"""
        return self._get_frequencies(cplx=1)

    @property
    def rpms(self):
        """Field of rpms for the active result"""
        return self._get_rpms()

    @property
    def harmonic_indeces(self):
        """Field of rpms for the active result"""
        return self._get_harmonic_indeces()

    @property
    def n_sets(self):
        return self._sets_count()

    def get_frequency(self, step=0, substep=0, cumulative_index=None, cplx=False):
        """Returns the frequence corresponding to step/substep or
        cumulative_index asked.

        Parameters
        ----------
        step : int, optional
            Step index (one based).

        substep : int, optional
            Substep index (one based).

        cumulative_index : int, optional
            Cumulative index (one based).

        cplx: bool
            Return a complex frequency, default False

        Returns
        -------
        frequency : double
            Frequency of the step or substep.
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
        """Returns the cumulative index corresponding to step/substep
        or frequency requested.

        Parameters
        ----------
        step : int, optional
            Analysis step.

        substep : int, optional
            Analysis substep

        freq  : double, optional
            Frequency in Hz.

        cplx : False, optional
            Return a complex frequency.  Default False

        Returns
        -------
        index : int
            Cumulative index based on either the step, substep or
            frequency.
        """
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

    # TODO:  Consider depreciating in favor of n_sets
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

    def _get_frequencies(self, cplx=False):
        """Returns a field of all the frequencies in the model
        (complex or real).

        Parameters
        ----------
        cplx : int, optional
            Return a complex frequency.  Default False.

        Returns
        -------
        field : dpf.core.Field
            Field of all the frequencies in the model (complex or real)
        """
        request = time_freq_support_pb2.GetRequest()
        request.time_freq_support.CopyFrom(self._message)
        
        list_response = self._stub.List(request)
        if cplx == True and list_response.freq_complex.id!=0:
            return dpf.core.Field(channel=self._channel, field=list_response.freq_complex)
        elif list_response.freq_real.id!=0:
             return dpf.core.Field(channel=self._channel, field=list_response.freq_real)
        return None

    def _get_rpms(self):
        """Returns a field of all the rpms in the model

        Returns
        -------
        field : dpf.core.Field
            Field of all the rpms in the model (complex or real)
        """
        request = time_freq_support_pb2.GetRequest()
        request.time_freq_support.CopyFrom(self._message)

        list_response = self._stub.List(request)
        if list_response.rpm.id!=0:
            return dpf.core.Field(channel=self._channel, field=list_response.rpm)
        return None

    def _get_harmonic_indeces(self):
        """Returns a field of all the harmonic indices in the model

        Returns
        -------
        field : dpf.core.Field
            Field of all the harmonic indices in the model (complex or real)
        """
        request = time_freq_support_pb2.GetRequest()
        request.time_freq_support.CopyFrom(self._message)

        list_response = self._stub.List(request)
        if list_response.cyc_harmonic_index.id!=0:
            return dpf.core.Field(channel=self._channel, field=list_response.cyc_harmonic_index)
        return None

    def _connect(self):
        """Connect to the grpc service"""
        return time_freq_support_pb2_grpc.TimeFreqSupportServiceStub(self._channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass
