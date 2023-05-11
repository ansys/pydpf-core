"""
.. _ref_incremental_evaluation:
"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

def scop_from_ds(ds):
    time_freq_provider = dpf.operators.metadata.time_freq_provider(data_sources=ds)
    tf_support = time_freq_provider.get_output(output_type=dpf.types.time_freq_support)
    return dpf.time_freq_scoping_factory.scoping_on_all_time_freqs(tf_support)

path = examples.download_transient_result()
ds = dpf.DataSources(path)
scoping = scop_from_ds(ds)


result_op = dpf.operators.result.displacement()
norm_fc = dpf.operators.math.norm_fc(result_op)
final_op = dpf.operators.min_max.min_max_fc_inc(norm_fc)

min1 = final_op.get_output(0, dpf.types.field)
max1 = final_op.get_output(1, dpf.types.field)


from ansys.dpf.core import Splitter

splitter = Splitter(start_op=result_op, end_op=final_op)
result_op.connect(4, ds)
new_end_op = splitter.split(chunk_size=2, scoping=scoping)

min2 = new_end_op.get_output(0, dpf.types.field)
max2 = new_end_op.get_output(1, dpf.types.field)

