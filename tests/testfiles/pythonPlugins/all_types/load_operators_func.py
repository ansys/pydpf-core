from all_types import dpf_types_op, integral_types_op

from ansys.dpf.core.custom_operator import record_operator


def load_operators(*args):
    record_operator(integral_types_op.ForwardBoolOperator, *args)
    record_operator(integral_types_op.ForwardIntOperator, *args)
    record_operator(integral_types_op.ForwardFloatOperator, *args)
    record_operator(integral_types_op.ForwardStringOperator, *args)
    record_operator(integral_types_op.ForwardVecIntOperator, *args)
    record_operator(integral_types_op.SetOutVecDoubleOperator, *args)
    record_operator(integral_types_op.SetOutNpArrayIntOperator, *args)
    record_operator(integral_types_op.SetOutNpArrayDoubleOperator, *args)

    record_operator(dpf_types_op.ForwardFieldOperator, *args)
    record_operator(dpf_types_op.ForwardDataSourcesOperator, *args)
    record_operator(dpf_types_op.ForwardPropertyFieldOperator, *args)
    record_operator(dpf_types_op.ForwardStringFieldOperator, *args)
    record_operator(dpf_types_op.ForwardCustomTypeFieldOperator, *args)
    record_operator(dpf_types_op.ForwardScopingOperator, *args)
    record_operator(dpf_types_op.ForwardScopingsContainerOperator, *args)
    record_operator(dpf_types_op.ForwardFieldsContainerOperator, *args)
    record_operator(dpf_types_op.ForwardMeshesContainerOperator, *args)
    record_operator(dpf_types_op.ForwardWorkflowOperator, *args)
    record_operator(dpf_types_op.ForwardDataTreeOperator, *args)
