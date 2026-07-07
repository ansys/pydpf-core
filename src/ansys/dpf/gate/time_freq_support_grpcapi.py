from ansys.dpf.gate.generated import time_freq_support_abstract_api
from ansys.dpf.gate.data_processing_grpcapi import DataProcessingGRPCAPI
from ansys.dpf.gate.object_handler import ObjHandler
from ansys.dpf.gate import errors
# -------------------------------------------------------------------------------
# TimeFreqSupport
# -------------------------------------------------------------------------------


def _get_stub(server):
    return server.get_stub(TimeFreqSupportGRPCAPI.STUBNAME)


@errors.protect_grpc_class
class TimeFreqSupportGRPCAPI(time_freq_support_abstract_api.TimeFreqSupportAbstractAPI):
    STUBNAME = "time_freq_support_stub"

    @staticmethod
    def _cumulative_index_request(bIsComplex, timeFreq, freq):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.bool_cumulative_index = True
        request.complex = bIsComplex
        request.frequency = freq
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).cumulative_index

    @staticmethod
    def _copy_into(request, time_freq_support):
        from ansys.grpc.dpf import time_freq_support_pb2, support_pb2
        if isinstance(time_freq_support, time_freq_support_pb2.TimeFreqSupport):
            message = time_freq_support
        elif isinstance(time_freq_support, support_pb2.Support):
            message = time_freq_support_pb2.TimeFreqSupport()
            if isinstance(time_freq_support.id, int):
                message.id = time_freq_support.id
            else:
                message.id.CopyFrom(time_freq_support.id)
        request.CopyFrom(message)

    @staticmethod
    def init_time_freq_support_environment(obj):
        from ansys.grpc.dpf import time_freq_support_pb2_grpc
        obj._server.create_stub_if_necessary(TimeFreqSupportGRPCAPI.STUBNAME,
                                             time_freq_support_pb2_grpc.TimeFreqSupportServiceStub)
        obj._deleter_func = (_get_stub(obj._server).Delete, lambda obj: obj._internal_obj)

    @staticmethod
    def time_freq_support_new_on_client(client):
        from ansys.grpc.dpf import base_pb2
        request = base_pb2.Empty()
        return _get_stub(client).Create(request)

    @staticmethod
    def list(support, stage_num=None):
        from types import SimpleNamespace
        from ansys.grpc.dpf import time_freq_support_pb2
        server = support._server
        api = DataProcessingGRPCAPI

        # Get the ListResponse from the server
        request = time_freq_support_pb2.ListRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, support._internal_obj)
        if stage_num:
            request.cyclic_stage_num = stage_num
        list_response = _get_stub(server).List(request)

        # Wrap the ListResponse in a flat response with ObjHandlers to prevent memory leaks
        response = SimpleNamespace(
            freq_real=ObjHandler(api, list_response.freq_real, server),
            freq_complex=ObjHandler(api, list_response.freq_complex, server),
            rpm=ObjHandler(api, list_response.rpm, server),
            cyc_harmonic_index=ObjHandler(api, list_response.cyc_harmonic_index, server),
            cyclic_harmonic_index_scoping=ObjHandler(api, list_response.cyclic_harmonic_index_scoping, server) if hasattr(list_response, "cyclic_harmonic_index_scoping") else None)
        return response

    @staticmethod
    def get(timeFreq, request):
        return _get_stub(timeFreq._server).Get(request)

    @staticmethod
    def update(timeFreq, request):
        _get_stub(timeFreq._server).Update(request)

    @staticmethod
    def time_freq_support_get_number_sets(timeFreq):
        from ansys.grpc.dpf import time_freq_support_pb2, base_pb2
        request = time_freq_support_pb2.CountRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.entity = base_pb2.NUM_SETS
        return _get_stub(timeFreq._server).Count(request).count

    @staticmethod
    def time_freq_support_set_shared_time_freqs(timeFreq, frequencies):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.freq_real.CopyFrom(frequencies._internal_obj)
        TimeFreqSupportGRPCAPI.update(timeFreq, request)

    @staticmethod
    def time_freq_support_set_shared_imaginary_freqs(timeFreq, complex_frequencies):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.freq_complex.CopyFrom(complex_frequencies._internal_obj)
        TimeFreqSupportGRPCAPI.update(timeFreq, request)

    @staticmethod
    def time_freq_support_set_shared_rpms(timeFreq, rpms):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.rpm.CopyFrom(rpms._internal_obj)
        TimeFreqSupportGRPCAPI.update(timeFreq, request)

    @staticmethod
    def time_freq_support_set_harmonic_indices(timeFreq, field, stageNum):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.TimeFreqSupportUpdateRequest()
        cyclic_data = time_freq_support_pb2.CyclicHarmonicData()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        cyclic_data.cyc_harmonic_index.CopyFrom(field._internal_obj)
        cyclic_data.stage_num = stageNum
        request.cyc_harmonic_data.CopyFrom(cyclic_data)
        TimeFreqSupportGRPCAPI.update(timeFreq, request)

    @staticmethod
    def time_freq_support_get_shared_time_freqs(timeFreq):
        return TimeFreqSupportGRPCAPI.list(timeFreq).freq_real.get_ownership()

    @staticmethod
    def time_freq_support_get_shared_imaginary_freqs(timeFreq):
        return TimeFreqSupportGRPCAPI.list(timeFreq).freq_complex.get_ownership()

    @staticmethod
    def time_freq_support_get_shared_rpms(timeFreq):
        return TimeFreqSupportGRPCAPI.list(timeFreq).rpm.get_ownership()

    @staticmethod
    def time_freq_support_get_shared_harmonic_indices(timeFreq, stage):
        return TimeFreqSupportGRPCAPI.list(timeFreq,
                                           stage_num=stage).cyc_harmonic_index.get_ownership()

    @staticmethod
    def time_freq_support_get_imaginary_freqs_cummulative_index(timeFreq, dVal, i1, i2):
        return TimeFreqSupportGRPCAPI._cumulative_index_request(True, timeFreq, dVal)
    @staticmethod
    def time_freq_support_get_time_freq_cummulative_index_by_value(timeFreq, dVal, i1, i2):
        return TimeFreqSupportGRPCAPI._cumulative_index_request(False, timeFreq, dVal)


    @staticmethod
    def time_freq_support_get_time_freq_cummulative_index_by_value_and_load_step(timeFreq, step,
                                                                                 substep, freq,
                                                                                 cplx):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.bool_cumulative_index = True
        request.complex = cplx
        if freq is not None:
            request.frequency = freq
        else:
            request.step_substep.step = step
            request.step_substep.substep = substep
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).cumulative_index

    @staticmethod
    def time_freq_support_get_time_freq_cummulative_index_by_step(timeFreq, step, subStep):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.bool_cumulative_index = True
        request.step_substep.step = step
        request.step_substep.substep = subStep
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).cumulative_index

    @staticmethod
    def time_freq_support_get_time_freq_by_step(timeFreq, stepIndex, subStepIndex):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.complex = False
        request.step_substep.step = stepIndex
        request.step_substep.substep = subStepIndex
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).frequency

    @staticmethod
    def time_freq_support_get_imaginary_freq_by_step(timeFreq, stepIndex, subStepIndex):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.complex = True
        request.step_substep.step = stepIndex
        request.step_substep.substep = subStepIndex
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).frequency

    @staticmethod
    def time_freq_support_get_time_freq_by_cumul_index(timeFreq, iCumulativeIndex):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.complex = False
        request.cumulative_index = iCumulativeIndex
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).frequency

    @staticmethod
    def time_freq_support_get_imaginary_freq_by_cumul_index(timeFreq, iCumulativeIndex):
        from ansys.grpc.dpf import time_freq_support_pb2
        request = time_freq_support_pb2.GetRequest()
        TimeFreqSupportGRPCAPI._copy_into(request.time_freq_support, timeFreq._internal_obj)
        request.complex = True
        request.cumulative_index = iCumulativeIndex
        return TimeFreqSupportGRPCAPI.get(timeFreq, request).frequency
