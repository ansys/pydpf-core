from average_filter_plugin import operators
from ansys.dpf.core.custom_operator import record_operator


def load_operators(*args):
    record_operator(operators.IdsWithDataHigherThanAverage, *args)
    record_operator(operators.IdsWithDataLowerThanAverage, *args)
