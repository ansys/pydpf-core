"""Wrappers for DPF operators.

These operators are available as functions from ``dpf.operators`` and
simplify the creation of new chained operators.
"""
from ansys import dpf
from ansys.dpf.core.common import types as dpf_types


def _check_type(instance, allowable_type):
    if not isinstance(instance, allowable_type):
        if isinstance(allowable_type, tuple):
            names = ', '.join([atype.__name__ for atype in allowable_type])
            raise TypeError('Input type must be one of (%s)' % names)
        else:
            raise TypeError('Input type must be a %s' % allowable_type.__name__)


def build_docs():
    """Build HTML documentation.  This outputs all available
    operator types for the loaded operators

    HTML is saved in the current python directory
    """
    dpf.core.Operator('html_doc').run()


def sum(var_inp):
    """Sum all the elementary data of a field to get one elementary
    data at the end.  If an Operator, must only contain one field.

    Parameters
    ----------
    var_inp : ansys.dpf.core.FieldsContainer, ansys.dpf.core.Field, or ansys.dpf.core.Operator
        Field/or fields container containing only one field.

    Returns
    -------
    sum : ansys.dpf.core.Field
        Sum of the input.

    Examples
    --------
    Sum element volume using a model

    >>> from ansys import dpf
    >>> model = dpf.core.Model(filename)
    >>> e_vol model.element_volume()
    >>> total_volume = e_vol.sum()

    Sum element volume using dpf.core.sum

    >>> model = dpf.core.Model(filename)
    >>> e_vol model.element_volume()
    >>> total_volume = dpf.core.sum(e_vol)
    """
    typ_err = TypeError('Input must be a Field or FieldsContainer containing '
                        'only one field, or an operator that returns one Field')

    # create an accumulate operator
    sum_op = dpf.core.Operator('accumulate')

    if isinstance(var_inp, dpf.core.Field):
        sum_op.connect(var_inp)
    elif isinstance(var_inp, dpf.core.FieldsContainer):
        if len(var_inp) > 1:
            raise typ_err
        sum_op.connect(var_inp)
    elif isinstance(var_inp, dpf.core.Operator):
        return _sum_oper(var_inp)
    else:
        raise typ_err

    return sum_op.get_output(0, dpf_types.field)


def _sum_oper(oper):
    """Sum all the elementary data of this operator.  Operator
    must contain only one field.

    Returns
    -------
    sum : ansys.dpf.core.Field
        Sum of this operator.

    """
    fields = oper.fields
    if len(fields) > 1:
        raise TypeError('Input must be a Field or FieldsContainer containing '
                        'only one field, or an operator that returns one Field')

    sum_op = dpf.core.Operator('accumulate')

    sum_op.connect(0, fields)
    field = sum_op.get_output(0, dpf_types.field)

    if oper.physics_name:
        field._name = f'Sum of {field.physics_name}'
    else:
        field._name = f'Sum'
    field._unit = field._unit
    return field


def to_nodal(var_inp):
    """Transform elemental field into a nodal field using an
    averaging process.

    Returns
    -------
    field : ansys.dpf.core.Field
        Field containing the nodal averaged field
    """
    # try to use the same server as input
    _check_type(var_inp, dpf.core.Field)
    if isinstance(var_inp, dpf.core.Field):
        oper = dpf.core.Operator('to_nodal')
        return oper.get_output(0, dpf_types.field)
    elif isinstance(var_inp, dpf.core.FieldsContainer):
        oper = dpf.core.Operator('to_nodal_fc')
        return oper.get_output(0, dpf_types.fields_container)
    else:
        raise TypeError('Input type must be a Field, FieldContainer')


def norm(var_inp):
    """Returns the euclidean norm of a Field, FieldContainer, or operator

    Returns
    -------
    field : ansys.dpf.core.Field, ansys.dpf.core.FieldContainer, or ansys.dpf.core.Operator
        The euclidean norm of this field.  Output type will match input type.
    """
    if isinstance(var_inp, dpf.core.Field):
        return _norm(var_inp)
    elif isinstance(var_inp, dpf.core.FieldsContainer):
        return _norm_fc(var_inp)
    elif isinstance(var_inp, dpf.core.Operator):
        return _norm_op(var_inp)
    else:
        raise TypeError('Input type must be a Field, FieldContainer, or an Operator')


def _norm(field):
    """Returns the euclidean norm of a field

    Returns
    -------
    field : ansys.dpf.core.Field
        The euclidean norm of this field.
    """
    _check_type(field, dpf.core.Field)
    norm_op = dpf.core.Operator('norm')
    norm_op.connect(0, field)
    norm_field = norm_op.get_output(0, dpf_types.field)
    return norm_field


def _norm_fc(fields):
    """Return the euclidean norm for the elementary data fields

    Returns
    -------
    fields : ansys.dpf.core.FieldsContainer
        Euclidean norm of the fields.
    """
    _check_type(fields, dpf.core.FieldsContainer)
    norm_op = dpf.core.Operator('norm_fc')
    norm_op.connect(0, fields)
    norm_fields = norm_op.get_output(0, dpf_types.fields_container)
    return norm_fields


def _norm_op(oper):
    """Returns a chained norm operator
    Returns
    -------
    oper : ansys.dpf.core.Operator
        Chained euclidean norm operator.
    """
    _check_type(oper, dpf.core.Operator)

    # try to use the same server as input    
    norm_op = dpf.core.Operator('norm_fc')
    norm_op.inputs.connect(oper.outputs)
    return norm_op


def eqv(var_inp):
    """Returns the von-mises stress of a Field or FieldContainer

    Returns
    -------
    field : ansys.dpf.core.Field, ansys.dpf.core.FieldContainer
        The von-mises stress of this field.  Output type will match input type.
    """
    if isinstance(var_inp, dpf.core.Field):
        return _eqv(var_inp)
    elif isinstance(var_inp, dpf.core.FieldsContainer):
        return _eqv_fc(var_inp)
    # elif isinstance(var_inp, dpf.core.Operator):
        # return _eqv_op(var_inp)
    else:
        raise TypeError('Input type must be a Field or FieldContainer')


# TODO: Consider combining eqv and eqv_fc
def _eqv(field):
    """Returns the von-mises stress field

    Parameters
    ----------
    field : ansys.dpf.core.Field
        Field containing component stresses.

    Returns
    -------
    field : ansys.dpf.core.Field
        Field containing the von-mises stress field
    """
    _check_type(field, dpf.core.Field)
    oper = dpf.core.operator('eqv')
    oper.connect(0, field)
    field = oper.get_output(0, dpf_types.field)
    return field


def _eqv_fc(fields):
    """Computes the element-wise Von-Mises criteria for each
    tensor in the fields of the field container.

    Returns
    -------
    fields : ansys.dpf.core.FieldsContainer
        Element-wise Von-Mises criteria field container.
    """
    _check_type(fields, dpf.core.FieldsContainer)
    oper = fields._model.operator('eqv_fc')
    oper.connect(0, fields)
    eqv_fields = oper.get_output(0, dpf_types.fields_container)
    return eqv_fields


def min_max(var_inp):
    """Returns a min_max operator for a Field, FieldsContainer, or
    Operator input.

    Returns
    -------
    oper : ansys.dpf.core.Operator
        Component-wise minimum/maximum operator over the input.
    """
    if isinstance(var_inp, dpf.core.Field):
        return _min_max(var_inp)
    elif isinstance(var_inp, dpf.core.FieldsContainer):
        return _min_max_fc(var_inp)
    elif isinstance(var_inp, dpf.core.Operator):
        return _min_max_oper(var_inp)
    else:
        raise TypeError('Input type must be a Field or FieldContainer')


def _min_max(field):
    """The min_max operator for a Field

    Returns
    -------
    oper : ansys.dpf.core.Operator
        Component-wise minimum/maximum operator over the input.
    """
    
    oper = dpf.core.Operator('min_max')
    oper.inputs.connect(field)
    return oper


def _min_max_fc(fields):
    """The min_max operator for a FieldContainer

    Returns
    -------
    oper : ansys.dpf.core.Operator
        Component-wise minimum/maximum operator over a field
        container.
    """
    oper = dpf.core.Operator('min_max_fc')
    oper.connect(0, fields)
    return oper


def _min_max_oper(oper):
    """Returns a chained min_max operator

    Returns
    -------
    oper : ansys.dpf.core.Operator
        Component-wise minimum/maximum operator.
    """
    
    min_max_oper = dpf.core.Operator('min_max_fc')
    min_max_oper.connect(0, oper, 0)
    return min_max_oper


def add(a, b):
    """Adds two fields together.

    Parameters
    ----------
    a : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    b : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    Returns
    -------
    field_sum : ansys.dpf.core.Field
        Sum of the two fields.
    """
    _check_type(a, (dpf.core.Field, dpf.core.FieldsContainer))
    _check_type(b, (dpf.core.Field, dpf.core.FieldsContainer))

    sum_oper = dpf.core.Operator('add')
    sum_oper.connect(0, a)
    sum_oper.connect(1, a)
    return sum_oper.get_output(0, dpf.core.types.field)


def element_dot(a, b):
    """Compute element-wise dot product between two vector fields.

    Parameters
    ----------
    a : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    b : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    Returns
    -------
    field_sum : ansys.dpf.core.Field
        Element-wise dot product of the two fields.

    Examples
    --------
    Compute the element-wise dot product

    >>> from ansys import dpf
    >>> data = np.random.random((10, 3))
    >>> field_a = dpf.core.field_from_array(data)
    >>> field_b = dpf.core.field_from_array(data)
    >>> fout = dpf.core.element_dot(field_a, field_b)
    >>> fout.shape
    (10, 1)

    Numpy equivalent

    >>> arr_a = np.random.random((10, 3))
    >>> arr_b = np.random.random((10, 3))
    >>> edot = np.sum(arr_a*arr_b, 1)
    >>> edot.shape
    (10,)

    """
    _check_type(a, (dpf.core.Field, dpf.core.FieldsContainer))
    _check_type(b, (dpf.core.Field, dpf.core.FieldsContainer))

    op = dpf.core.Operator('dot')
    op.connect(0, a)
    op.connect(1, b)
    return op.get_output(0, dpf.core.types.field)


def sqr(field):
    """Computes element-wise square of a field.

    Parameters
    ----------
    field : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    Returns
    -------
    field_sqr : ansys.dpf.core.Field
        Element-wise square of a field

    Examples
    --------
    Using built-in operator

    >>> field = dpf.core.field_from_array([1, 8])
    >>> field_sqr = field**2
    >>> print(field_sqr.data)
    [1, 64]

    Using operator method

    >>> field = dpf.core.field_from_array([1, 8])
    >>> field_sqr = dpf.core.operators.sqr(field)
    >>> print(field_sqr.data)
    [1, 64]

    """

    _check_type(field, (dpf.core.Field, dpf.core.FieldsContainer))
    op = dpf.core.Operator('sqr')
    op.connect(0, field)
    return op.get_output(0, dpf.core.types.field)


def dot_tensor(a, b):
    """Computes element-wise dot product between two tensor fields.

    Parameters
    ----------
    a : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    b : ansys.dpf.core.Field or ansys.dpf.core.FieldContainer
        Field/or fields container containing only one field.

    Returns
    -------
    field_sum : ansys.dpf.core.Field
        Element-wise dot product between two vector fields.

    Examples
    --------
    >>> from ansys import dpf
    >>> arr_a = np.ones((5, 3))
    >>> arr_a[:, 2] = 0
    >>> arr_b = np.ones((5, 3))
    >>> arr_b[:, 1] = 0
    >>> field_a = dpf.core.field_from_array(arr_a)
    >>> field_b = dpf.core.field_from_array(arr_b)
    >>> field_out = dpf.core.operators.dot_tensor(field_a, field_b)
    >>> print(field_out.asarray)
    array([[1., 1., 0., 0., 0., 0., 1., 1., 0.],
           [1., 1., 0., 0., 0., 0., 1., 1., 0.],
           [1., 1., 0., 0., 0., 0., 1., 1., 0.],
           [1., 1., 0., 0., 0., 0., 1., 1., 0.],
           [1., 1., 0., 0., 0., 0., 1., 1., 0.]])
    """
    _check_type(a, (dpf.core.Field, dpf.core.FieldsContainer))
    _check_type(b, (dpf.core.Field, dpf.core.FieldsContainer))

    op = dpf.core.Operator('dot_tensor')
    op.connect(0, a)
    op.connect(1, b)
    return op.get_output(0, dpf.core.types.field)


# TODO: Depreciate, appears unused
def component_selector(var_inp, index):
    """Select a component from either a field or a fields container.

    Parameters
    ----------
    var_inp : ansys.dpf.core.Field, ansys.dpf.core.FieldsContainer
        Fields or FieldsContainer to select the components from.

    index : int
        Index of the component to select.

    Returns
    -------
    fields : ansys.dpf.core.Field, ansys.dpf.core.FieldsContainer
        Fields container with one component selected in each field.
    """
    if not isinstance(index, int):
        if index < 0:
            # TODO: should we allow negative indexing?
            raise ValueError('Component index must be greater than 0')

    def check_component_available(field, index):
        """verify that the component index exists"""
        n_comp = field.component_count
        if index >= n_comp:
            raise ValueError('There are only %d components available in ' % n_comp +
                             '%s' % field.name)

    Operator = _acquire_operator(var_inp)

    if isinstance(var_inp, dpf.core.Field):
        check_component_available(var_inp, index)
        op = Operator('component_selector')
        op.connect(0, var_inp)
        op.connect(1, index)
        field = op.get_output(0, dpf_types.field)
        field._name = var_inp._name
        field._component_index = index
        return field

    elif isinstance(var_inp, dpf.core.FieldsContainer):
        for field in var_inp:
            check_component_available(field, index)

        op = Operator('component_selector_fc')
        op.connect(0, var_inp)
        op.connect(1, index)
        fields = op.get_output(0, dpf_types.fields_container)
        fields._name = var_inp._name
        fields._component_index = index
        return fields

    else:
        raise TypeError('Input type must be a Field or FieldContainer')
