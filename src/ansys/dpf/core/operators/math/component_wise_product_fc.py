"""
component_wise_product_fc
=========================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class component_wise_product_fc(Operator):
    """Computes component-wise product between two fields of same
    dimensionality. If one field's scoping has an 'overall' location,
    then this field's values are applied on the other field entirely.
    When using a constant or 'work_by_index', you can use 'inplace' to
    reuse one of the fields.

    Parameters
    ----------
    fields_container : FieldsContainer
        Field or fields container with only one field
        is expected
    fieldB : Field or FieldsContainer
        Field or fields container with only one field
        is expected


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.math.component_wise_product_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.math.component_wise_product_fc(
    ...     fields_container=my_fields_container,
    ...     fieldB=my_fieldB,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, fields_container=None, fieldB=None, config=None, server=None):
        super().__init__(name="component_wise_product_fc", config=config, server=server)
        self._inputs = InputsComponentWiseProductFc(self)
        self._outputs = OutputsComponentWiseProductFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if fieldB is not None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        description = """Computes component-wise product between two fields of same
            dimensionality. If one field's scoping has an 'overall'
            location, then this field's values are applied on the
            other field entirely. When using a constant or
            'work_by_index', you can use 'inplace' to reuse one of the
            fields."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
                1: PinSpecification(
                    name="fieldB",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""Field or fields container with only one field
        is expected""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="component_wise_product_fc", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComponentWiseProductFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComponentWiseProductFc
        """
        return super().outputs


class InputsComponentWiseProductFc(_Inputs):
    """Intermediate class used to connect user inputs to
    component_wise_product_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.component_wise_product_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_fieldB = dpf.Field()
    >>> op.inputs.fieldB.connect(my_fieldB)
    """

    def __init__(self, op: Operator):
        super().__init__(component_wise_product_fc._spec().inputs, op)
        self._fields_container = Input(
            component_wise_product_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._fieldB = Input(component_wise_product_fc._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._fieldB)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.component_wise_product_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator.

        Field or fields container with only one field
        is expected

        Parameters
        ----------
        my_fieldB : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.component_wise_product_fc()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> # or
        >>> op.inputs.fieldB(my_fieldB)
        """
        return self._fieldB


class OutputsComponentWiseProductFc(_Outputs):
    """Intermediate class used to get outputs from
    component_wise_product_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.math.component_wise_product_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(component_wise_product_fc._spec().outputs, op)
        self._fields_container = Output(
            component_wise_product_fc._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.math.component_wise_product_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container