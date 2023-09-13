import ctypes
from ansys.dpf.gate import utils
from ansys.dpf.gate import errors
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate.generated import time_freq_support_abstract_api
from ansys.dpf.gate.generated.data_processing_capi import DataProcessingCAPI

#-------------------------------------------------------------------------------
# TimeFreqSupport
#-------------------------------------------------------------------------------

class TimeFreqSupportCAPI(time_freq_support_abstract_api.TimeFreqSupportAbstractAPI):

	@staticmethod
	def init_time_freq_support_environment(object):
		# get core api
		DataProcessingCAPI.init_data_processing_environment(object)
		object._deleter_func = (DataProcessingCAPI.data_processing_delete_shared_object, lambda obj: obj)

	@staticmethod
	def time_freq_support_new():
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_new(ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_delete(support):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_delete(support._internal_obj if support is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_number_sets(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetNumberSets(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_number_singular_sets(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetNumberSingularSets(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_set_shared_time_freqs(timeFreq, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_SetSharedTimeFreqs(timeFreq._internal_obj if timeFreq is not None else None, field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_set_shared_imaginary_freqs(timeFreq, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_SetSharedImaginaryFreqs(timeFreq._internal_obj if timeFreq is not None else None, field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_set_shared_rpms(timeFreq, field):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_SetSharedRpms(timeFreq._internal_obj if timeFreq is not None else None, field._internal_obj if field is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_set_harmonic_indices(timeFreq, field, stageNum):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_SetHarmonicIndices(timeFreq._internal_obj if timeFreq is not None else None, field._internal_obj if field is not None else None, utils.to_int32(stageNum), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_shared_time_freqs(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetSharedTimeFreqs(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_shared_imaginary_freqs(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetSharedImaginaryFreqs(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_shared_rpms(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetSharedRpms(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_shared_harmonic_indices(timeFreq, stage):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetSharedHarmonicIndices(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(stage), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_shared_harmonic_indices_scoping(timeFreq):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetSharedHarmonicIndicesScoping(timeFreq._internal_obj if timeFreq is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_value(timeFreq, dVal, i1, i2):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValue(timeFreq._internal_obj if timeFreq is not None else None, ctypes.c_double(dVal) if isinstance(dVal, float) else dVal, ctypes.byref(utils.to_int32(i1)), ctypes.byref(utils.to_int32(i2)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_value_and_load_step(timeFreq, dVal, loadStep, i1, i2):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValueAndLoadStep(timeFreq._internal_obj if timeFreq is not None else None, ctypes.c_double(dVal) if isinstance(dVal, float) else dVal, utils.to_int32(loadStep), ctypes.byref(utils.to_int32(i1)), ctypes.byref(utils.to_int32(i2)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_step(timeFreq, step, subStep):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByStep(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(step), utils.to_int32(subStep), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_imaginary_freqs_cummulative_index(timeFreq, dVal, i1, i2):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetImaginaryFreqsCummulativeIndex(timeFreq._internal_obj if timeFreq is not None else None, ctypes.c_double(dVal) if isinstance(dVal, float) else dVal, ctypes.byref(utils.to_int32(i1)), ctypes.byref(utils.to_int32(i2)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_time_freq_by_step(timeFreq, stepIndex, subStepIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetTimeFreqByStep(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(stepIndex), utils.to_int32(subStepIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_imaginary_freq_by_step(timeFreq, stepIndex, subStepIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetImaginaryFreqByStep(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(stepIndex), utils.to_int32(subStepIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_time_freq_by_cumul_index(timeFreq, iCumulativeIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetTimeFreqByCumulIndex(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(iCumulativeIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_imaginary_freq_by_cumul_index(timeFreq, iCumulativeIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetImaginaryFreqByCumulIndex(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(iCumulativeIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_cyclic_harmonic_index(timeFreq, iCumulativeIndex):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetCyclicHarmonicIndex(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(iCumulativeIndex), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_step_and_sub_step(timeFreq, iCumulativeIndex, step, substep):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_GetStepAndSubStep(timeFreq._internal_obj if timeFreq is not None else None, utils.to_int32(iCumulativeIndex), ctypes.byref(utils.to_int32(step)), ctypes.byref(utils.to_int32(substep)), ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_new_on_client(client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_new_on_client(client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

	@staticmethod
	def time_freq_support_get_copy(id, client):
		errorSize = ctypes.c_int(0)
		sError = ctypes.c_wchar_p()
		res = capi.dll.TimeFreqSupport_getCopy(utils.to_int32(id), client._internal_obj if client is not None else None, ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError))
		if errorSize.value != 0:
			raise errors.DPFServerException(sError.value)
		return res

