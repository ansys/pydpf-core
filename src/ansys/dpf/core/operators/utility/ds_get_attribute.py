"""
ds_get_attribute
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class ds_get_attribute(Operator):
    """A DataSources in pin 0 and a property name (string) in pin 1 are
    expected in input. An index refering to the property can also be
    provided.

    Parameters
    ----------
    data_sources : DataSources
    property_name : str
        Accepted inputs are: 'file_path' (returns
        string), 'result_file_name' (returns
        string), 'domain_file_path' (returns
        string), 'domain_result_file_name'
        (returns string), 'num_keys' (returns
        int), num_result_key (returns int),
        num_file_path (returns int),
        'num_result_file_path' (returns int),
        'key_by_index' (returns string),
        'result_key_by_index' (returns
        string), 'path_by_index' (returns
        string), 'path_key_by_index' (returns
        string).
    property_index : int, optional
        Index for the property. must be set for
        'domain_file_path',
        'domain_result_file_name'
        'key_by_index',
        'result_key_by_index',
        'path_by_index' and
        'path_key_by_index' properties.
    property_key : str, optional
        Key to look for. must be set for 'file_path'
        and 'domain_file_path' properties.
    property_result_key : str, optional
        Result key to look for. can be used for
        'file_path', 'result_file_name',
        'domain_file_path' and
        'domain_result_file_name'.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.ds_get_attribute()

    >>> # Make input connections
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_index = int()
    >>> op.inputs.property_index.connect(my_property_index)
    >>> my_property_key = str()
    >>> op.inputs.property_key.connect(my_property_key)
    >>> my_property_result_key = str()
    >>> op.inputs.property_result_key.connect(my_property_result_key)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.ds_get_attribute(
    ...     data_sources=my_data_sources,
    ...     property_name=my_property_name,
    ...     property_index=my_property_index,
    ...     property_key=my_property_key,
    ...     property_result_key=my_property_result_key,
    ... )

    >>> # Get output data
    >>> result_property = op.outputs.property()
    """

    def __init__(
        self,
        data_sources=None,
        property_name=None,
        property_index=None,
        property_key=None,
        property_result_key=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="datasources::get_attribute", config=config, server=server
        )
        self._inputs = InputsDsGetAttribute(self)
        self._outputs = OutputsDsGetAttribute(self)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if property_name is not None:
            self.inputs.property_name.connect(property_name)
        if property_index is not None:
            self.inputs.property_index.connect(property_index)
        if property_key is not None:
            self.inputs.property_key.connect(property_key)
        if property_result_key is not None:
            self.inputs.property_result_key.connect(property_result_key)

    @staticmethod
    def _spec():
        description = """A DataSources in pin 0 and a property name (string) in pin 1 are
            expected in input. An index refering to the property can
            also be provided."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="property_name",
                    type_names=["string"],
                    optional=False,
                    document="""Accepted inputs are: 'file_path' (returns
        string), 'result_file_name' (returns
        string), 'domain_file_path' (returns
        string), 'domain_result_file_name'
        (returns string), 'num_keys' (returns
        int), num_result_key (returns int),
        num_file_path (returns int),
        'num_result_file_path' (returns int),
        'key_by_index' (returns string),
        'result_key_by_index' (returns
        string), 'path_by_index' (returns
        string), 'path_key_by_index' (returns
        string).""",
                ),
                2: PinSpecification(
                    name="property_index",
                    type_names=["int32"],
                    optional=True,
                    document="""Index for the property. must be set for
        'domain_file_path',
        'domain_result_file_name'
        'key_by_index',
        'result_key_by_index',
        'path_by_index' and
        'path_key_by_index' properties.""",
                ),
                3: PinSpecification(
                    name="property_key",
                    type_names=["string"],
                    optional=True,
                    document="""Key to look for. must be set for 'file_path'
        and 'domain_file_path' properties.""",
                ),
                4: PinSpecification(
                    name="property_result_key",
                    type_names=["string"],
                    optional=True,
                    document="""Result key to look for. can be used for
        'file_path', 'result_file_name',
        'domain_file_path' and
        'domain_result_file_name'.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="property",
                    type_names=["string", "int32"],
                    optional=False,
                    document="""Property value.""",
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
        return Operator.default_config(name="datasources::get_attribute", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsDsGetAttribute
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsDsGetAttribute
        """
        return super().outputs


class InputsDsGetAttribute(_Inputs):
    """Intermediate class used to connect user inputs to
    ds_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.ds_get_attribute()
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_property_name = str()
    >>> op.inputs.property_name.connect(my_property_name)
    >>> my_property_index = int()
    >>> op.inputs.property_index.connect(my_property_index)
    >>> my_property_key = str()
    >>> op.inputs.property_key.connect(my_property_key)
    >>> my_property_result_key = str()
    >>> op.inputs.property_result_key.connect(my_property_result_key)
    """

    def __init__(self, op: Operator):
        super().__init__(ds_get_attribute._spec().inputs, op)
        self._data_sources = Input(ds_get_attribute._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._data_sources)
        self._property_name = Input(ds_get_attribute._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._property_name)
        self._property_index = Input(ds_get_attribute._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._property_index)
        self._property_key = Input(ds_get_attribute._spec().input_pin(3), 3, op, -1)
        self._inputs.append(self._property_key)
        self._property_result_key = Input(
            ds_get_attribute._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._property_result_key)

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.ds_get_attribute()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator.

        Accepted inputs are: 'file_path' (returns
        string), 'result_file_name' (returns
        string), 'domain_file_path' (returns
        string), 'domain_result_file_name'
        (returns string), 'num_keys' (returns
        int), num_result_key (returns int),
        num_file_path (returns int),
        'num_result_file_path' (returns int),
        'key_by_index' (returns string),
        'result_key_by_index' (returns
        string), 'path_by_index' (returns
        string), 'path_key_by_index' (returns
        string).

        Parameters
        ----------
        my_property_name : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.ds_get_attribute()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> # or
        >>> op.inputs.property_name(my_property_name)
        """
        return self._property_name

    @property
    def property_index(self):
        """Allows to connect property_index input to the operator.

        Index for the property. must be set for
        'domain_file_path',
        'domain_result_file_name'
        'key_by_index',
        'result_key_by_index',
        'path_by_index' and
        'path_key_by_index' properties.

        Parameters
        ----------
        my_property_index : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.ds_get_attribute()
        >>> op.inputs.property_index.connect(my_property_index)
        >>> # or
        >>> op.inputs.property_index(my_property_index)
        """
        return self._property_index

    @property
    def property_key(self):
        """Allows to connect property_key input to the operator.

        Key to look for. must be set for 'file_path'
        and 'domain_file_path' properties.

        Parameters
        ----------
        my_property_key : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.ds_get_attribute()
        >>> op.inputs.property_key.connect(my_property_key)
        >>> # or
        >>> op.inputs.property_key(my_property_key)
        """
        return self._property_key

    @property
    def property_result_key(self):
        """Allows to connect property_result_key input to the operator.

        Result key to look for. can be used for
        'file_path', 'result_file_name',
        'domain_file_path' and
        'domain_result_file_name'.

        Parameters
        ----------
        my_property_result_key : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.ds_get_attribute()
        >>> op.inputs.property_result_key.connect(my_property_result_key)
        >>> # or
        >>> op.inputs.property_result_key(my_property_result_key)
        """
        return self._property_result_key


class OutputsDsGetAttribute(_Outputs):
    """Intermediate class used to get outputs from
    ds_get_attribute operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.ds_get_attribute()
    >>> # Connect inputs : op.inputs. ...
    >>> result_property = op.outputs.property()
    """

    def __init__(self, op: Operator):
        super().__init__(ds_get_attribute._spec().outputs, op)
        self.property_as_string = Output(
            _modify_output_spec_with_one_type(
                ds_get_attribute._spec().output_pin(0), "string"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_string)
        self.property_as_int32 = Output(
            _modify_output_spec_with_one_type(
                ds_get_attribute._spec().output_pin(0), "int32"
            ),
            0,
            op,
        )
        self._outputs.append(self.property_as_int32)