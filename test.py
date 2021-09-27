from ansys.dpf import core as dpf
from ansys.dpf.core import examples


class A:
    def b():
        my_name_is_model = dpf.Model(examples.msup_transient)
        my_name_is_model.results.displacement.on_last_time_freq.on_named_selection(
            "_CONSTRAINEDNODES"
        )
