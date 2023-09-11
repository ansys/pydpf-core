#-------------------------------------------------------------------------------
# TimeFreqSupport
#-------------------------------------------------------------------------------

class TimeFreqSupportAbstractAPI:
	@staticmethod
	def init_time_freq_support_environment(object):
		pass

	@staticmethod
	def finish_time_freq_support_environment(object):
		pass

	@staticmethod
	def time_freq_support_new():
		raise NotImplementedError

	@staticmethod
	def time_freq_support_delete(support):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_number_sets(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_number_singular_sets(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_set_shared_time_freqs(timeFreq, field):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_set_shared_imaginary_freqs(timeFreq, field):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_set_shared_rpms(timeFreq, field):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_set_harmonic_indices(timeFreq, field, stageNum):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_shared_time_freqs(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_shared_imaginary_freqs(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_shared_rpms(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_shared_harmonic_indices(timeFreq, stage):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_shared_harmonic_indices_scoping(timeFreq):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_value(timeFreq, dVal, i1, i2):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_value_and_load_step(timeFreq, dVal, loadStep, i1, i2):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_time_freq_cummulative_index_by_step(timeFreq, step, subStep):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_imaginary_freqs_cummulative_index(timeFreq, dVal, i1, i2):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_time_freq_by_step(timeFreq, stepIndex, subStepIndex):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_imaginary_freq_by_step(timeFreq, stepIndex, subStepIndex):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_time_freq_by_cumul_index(timeFreq, iCumulativeIndex):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_imaginary_freq_by_cumul_index(timeFreq, iCumulativeIndex):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_cyclic_harmonic_index(timeFreq, iCumulativeIndex):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_step_and_sub_step(timeFreq, iCumulativeIndex, step, substep):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def time_freq_support_get_copy(id, client):
		raise NotImplementedError

