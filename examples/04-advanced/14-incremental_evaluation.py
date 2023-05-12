"""
.. _ref_incremental_evaluation:
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

path = examples.download_transient_result()
ds = dpf.DataSources(path)
scoping = dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(ds)

streams_provider = dpf.operators.metadata.streams_provider(data_sources=ds)
result_op = dpf.operators.result.stress(data_sources=ds, time_scoping=scoping,streams_container=streams_provider)
norm_fc = dpf.operators.math.norm_fc(result_op)
final_op = dpf.operators.min_max.min_max_fc_inc(norm_fc)


new_end_op = dpf.split_workflow_in_chunks(result_op, final_op, scoping)

min = new_end_op.get_output(0, dpf.types.field)
max = new_end_op.get_output(1, dpf.types.field)

