"""
.. _ref_operator_specification:

Operator Specification
======================
The OperatorSpecification Provides a documentation for each Operator
"""

import abc
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import operator_specification_capi, operator_specification_grpcapi,\
    integral_types
from ansys.dpf.core import mapping_types, common
from ansys.dpf.core.check_version import version_requires


class PinSpecification:
    """Documents an input or output pin of an Operator

    Parameters
    ----------
    name : str
        Name of the Pin.
    type_names : list[str], list[type], list[ansys.dpf.core.types], ansys.dpf.core.types, type, str
        List of accepted types.
    document : str, optional
        Explains what the pin is used for and what should be connect to it.
    optional : bool, optional
        Whether it is optional to connect to Pin or not. Default is False.
    ellipsis : bool, optional
        Whether data respecting this PinSpecification can be connected
        from this pin number to infinity. Default is False.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> operator = dpf.operators.result.displacement()
    >>> pin_spec = operator.specification.inputs[4]
    >>> pin_spec.name
    'data_sources'
    >>> pin_spec.type_names
    ['data_sources']
    >>> pin_spec.document
    'result file path container, used if no streams are set'
    >>> pin_spec.optional
    False
    """
    name: str
    _type_names: list
    document: str
    optional: bool
    ellipsis: bool

    def __init__(self, name, type_names, document="", optional=False, ellipsis=False):
        self.name = name
        self.type_names = type_names
        self.optional = optional
        self.document = document
        self.ellipsis = ellipsis

    @property
    def type_names(self):
        """
        Returns
        -------
        list[str], list[type]
            List of accepted types.
        """
        return self._type_names

    @type_names.setter
    def type_names(self, val):
        if isinstance(val, str):
            self._type_names = [val]
            return
        elif isinstance(val, type):
            self._type_names = [mapping_types.map_types_to_cpp[val.__name__]]
            return
        elif isinstance(val, common.types):
            self._type_names = [mapping_types.map_types_to_cpp[
                                    common.types_enum_to_types()[val].__name__
                                ]]
            return
        elif isinstance(val, list):
            if len(val) > 0 and isinstance(val[0], type):
                self._type_names = [mapping_types.map_types_to_cpp[ival.__name__] for ival in val]
                return
            if len(val) > 0 and isinstance(val[0], common.types):
                self._type_names = [
                    mapping_types.map_types_to_cpp[
                        common.types_enum_to_types()[ival].__name__
                    ] for ival in val
                ]
                return
        self._type_names = val

    @staticmethod
    def _get_copy(other, changed_types):
        return PinSpecification(other.name,
                                changed_types,
                                other.document,
                                other.optional,
                                other.ellipsis)

    def __repr__(self):
        return '{class_name}({params})'.format(
            class_name=self.__class__.__name__,
            params=', '.join('{param}={value}'.format(
                param=k, value=f"'{v}'" if isinstance(v, str) else v) for k, v in
                             vars(self).items()))

    def __eq__(self, other):
        return str(self) == str(other)


class ConfigSpecification(dict):
    """Dictionary of the available configuration options and their specification
    (:class:`ansys.dpf.core.operator_specification.ConfigOptionSpec`)
    """
    def __init__(self, *arg, **kw):
        super(ConfigSpecification, self).__init__(*arg, **kw)


class ConfigOptionSpec:
    """Documentation of a configuration option available for a given
     Operator (:class:`ansys.dpf.core.Operator`)

    Attributes
    ----------
    name : str
        Name of the Configuration Option.
    type_names : list[str]
        List of accepted types.
    default_value_str : str
        Gives the stringified value of the default.
    document : str
        Documents the Configuration Option.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> operator = dpf.operators.math.add()
    >>> config_spec = operator.specification.config_specification
    >>> config_spec.keys()
    dict_keys(['binary_operation', 'inplace', 'mutex', 'num_threads', 'permissive', \
    'run_in_parallel', 'use_cache', 'work_by_index'])
    >>> config_spec['inplace']
    ConfigOptionSpec(name='inplace', type_names=['bool'], default_value_str='false', \
    document='The output is written over the input to save memory if this config is set to true.')

    """

    name: str
    type_names: list
    default_value_str: str
    document: str

    def __init__(self, name, type_names, default_value_str, document):
        self.name = name
        self.type_names = type_names
        self.default_value_str = default_value_str
        self.document = document

    def __repr__(self):
        return '{class_name}({params})'.format(
            class_name=self.__class__.__name__,
            params=', '.join('{param}={value}'.format(
                param=k, value=f"'{v}'" if isinstance(v, str) else v) for k, v in
                             vars(self).items()))


class SpecificationBase:
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def inputs(self):
        pass

    @property
    @abc.abstractmethod
    def outputs(self):
        pass


class Specification(SpecificationBase):
    """Documents an Operator with its description (what the Operator does),
    its inputs and outputs and some properties.

    Examples
    --------
    Get the Specification of an operator by its name
    >>> from ansys.dpf import core as dpf
    >>> spec = dpf.operator_specification.Specification("U")
    >>> # or
    >>> spec = dpf.Operator.operator_specification("U")

    Get the specification of an instantiated operator
    >>> from ansys.dpf import core as dpf
    >>> operator = dpf.operators.result.displacement()
    >>> spec = operator.specification

    Display the Specification attributes
    >>> spec.description
    'Read/compute nodal displacements by calling the readers defined by the datasources.'
    >>> 4 in spec.inputs.keys()
    True
    >>> spec.outputs.keys()
    dict_keys([0])
    >>> spec.inputs[4].document
    'result file path container, used if no streams are set'
    """

    def __init__(self, operator_name=None, specification=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=operator_specification_capi.OperatorSpecificationCAPI,
            grpcapi=operator_specification_grpcapi.OperatorSpecificationGRPCAPI)

        # step3: init environment
        self._api.init_operator_specification_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it (specification)
        if specification is not None:
            self.internal_obj = specification
        else:
            if operator_name:
                if self._server.has_client():
                    self._internal_obj = self._api.operator_specification_new_on_client(
                        self._server.client, operator_name)
                else:
                    self._internal_obj = self._api.operator_specification_new(operator_name)
            else:
                if self._server.has_client():
                    raise NotImplementedError(
                        "Creating an empty specification on a gRPC client is not implemented"
                    )
                self._internal_obj = self._api.operator_empty_specification_new()

        self.operator_name = operator_name
        self._map_output_pin_spec = None
        self._map_input_pin_spec = None
        self._properties = None
        self._config_specification = None

    @property
    def properties(self):
        """Returns some additional properties of the Operator, like the category, the exposure,
        the scripting and user names and the plugin

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> operator = dpf.operators.math.add()
        >>> operator.specification.properties
        {'category': 'math', 'exposure': 'public', 'plugin': 'core', 'user_name': '+'}
        """
        if self._properties is None:
            temp_properties = dict()
            if self._internal_obj is not None:
                num_properties = self._api.operator_specification_get_num_properties(self)
                for i_property in range(num_properties):
                    property_key = self._api.operator_specification_get_property_key(
                        self, i_property
                    )
                    prop = self._api.operator_specification_get_properties(self, property_key)
                    temp_properties[property_key] = prop
            # Reorder the properties for consistency
            self._properties = dict()
            for key in sorted(temp_properties.keys()):
                self._properties[key] = temp_properties[key]
        return self._properties

    @property
    def description(self) -> str:
        """Returns a description of the operation applied by the Operator

        Returns
        -------
        str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> operator = dpf.operators.math.scale_by_field()
        >>> operator.specification.description
        "Scales a field (in 0) by a scalar field (in 1). If one field's ... the entire other field."
        """
        if self._internal_obj is not None:
            return self._api.operator_specification_get_description(self)
        return ""

    @property
    def inputs(self) -> dict:
        """Returns a dictionary mapping the input pin numbers to their ``PinSpecification``

        Returns
        -------
        inputs : dict[int:PinSpecification]

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> operator = dpf.operators.mesh.mesh_provider()
        >>> 4 in operator.specification.inputs.keys()
        True
        >>> operator.specification.inputs[4]
        PinSpecification(name='data_sources', _type_names=['data_sources'], ...set', ellipsis=False)
        """
        if self._map_input_pin_spec is None:
            self._map_input_pin_spec = {}
            self._fill_pins(True, self._map_input_pin_spec)
        return self._map_input_pin_spec

    @property
    def outputs(self) -> dict:
        """Returns a dictionary mapping the output pin numbers to their ``PinSpecification``

        Returns
        -------
        outputs : dict[int:PinSpecification]

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> operator = dpf.operators.mesh.mesh_provider()
        >>> operator.specification.outputs
        {0: PinSpecification(name='mesh', _type_names=['abstract_meshed_region'], ...=False)}
        """
        if self._map_output_pin_spec is None:
            self._map_output_pin_spec = {}
            self._fill_pins(False, self._map_output_pin_spec)
        return self._map_output_pin_spec

    def _fill_pins(self, binput, to_fill):
        if self._internal_obj is not None:
            num_pins = self._api.operator_specification_get_num_pins(self, binput)

            pins = integral_types.MutableListInt32(size=num_pins)
            self._api.operator_specification_fill_pin_numbers(self, binput, pins)
            pins = pins.tolist()

            for i_pin in pins:
                pin_name = self._api.operator_specification_get_pin_name(self, binput, i_pin)
                pin_opt = self._api.operator_specification_is_pin_optional(self, binput, i_pin)
                pin_doc = self._api.operator_specification_get_pin_document(self, binput, i_pin)
                n_types = self._api.operator_specification_get_pin_num_type_names(self, binput,
                                                                                  i_pin)
                pin_type_names = [
                    self._api.operator_specification_get_pin_type_name(self, binput,
                                                                       i_pin,
                                                                       i_type)
                    for i_type in range(n_types)]

                pin_ell = self._api.operator_specification_is_pin_ellipsis(self, binput, i_pin)
                to_fill[i_pin] = PinSpecification(pin_name,
                                                  pin_type_names,
                                                  pin_doc,
                                                  pin_opt,
                                                  pin_ell)

    @property
    def config_specification(self) -> ConfigSpecification:
        """Documents the available configuration options supported by the Operator

        Returns
        -------
        ConfigSpecification
        """
        if self._config_specification is None:
            self._config_specification = ConfigSpecification()
            num_options = self._api.operator_specification_get_num_config_options(self)
            for i in range(num_options):
                option_name = self._api.operator_specification_get_config_name(self, i)
                n_types = self._api.operator_specification_get_config_num_type_names(self, i)
                option_type_names = [self._api.operator_specification_get_config_type_name(
                    self, i, n_type) for n_type in range(n_types)]
                option_default_value = \
                    self._api.operator_specification_get_config_printable_default_value(self, i)
                option_doc = self._api.operator_specification_get_config_description(self, i)
                self._config_specification[option_name] = ConfigOptionSpec(
                    name=option_name,
                    type_names=option_type_names,
                    default_value_str=option_default_value,
                    document=option_doc)
        return self._config_specification


class CustomConfigOptionSpec(ConfigOptionSpec):
    def __init__(self, option_name: str, default_value, document: str):
        type_names = [mapping_types.map_types_to_cpp[type(default_value).__name__]]
        super().__init__(name=option_name, type_names=list(type_names),
                         default_value_str=str(default_value), document=document)


class Exposures:
    private = "private"
    public = "public"
    hidden = "hidden"


class Categories:
    result = "result"
    math = "math"
    mesh = "mesh"
    min_max = "min_max"
    scoping = "scoping"
    mapping = "mapping"
    geo = "geo"
    filter = "filter"
    utility = "utility"
    averaging = "averaging"
    serialization = "serialization"
    invariant = "invariant"
    logic = "logic"
    metadata = "metadata"


class SpecificationProperties:
    """Properties of an Operator.

    Parameters
    ----------
    user_name : str
        Readable lower case name of the Operator. example: "custom operator".

    category : str, Categories
        Choose from Categories options. Arrange the different Operators in the documentation
        and in the code generation.

    scripting_name : str
        Snake case name of the Operator. example: "custom_operator".

    exposure : Exposures
        Public by default, a hidden or private Operator doesn't appear in the documentation.

    plugin : str
        Snake case name of the plugin it belongs to.

    """
    def __init__(self, user_name: str = None, category: str = None, scripting_name: str = None,
                 exposure: Exposures = Exposures.public,
                 plugin: str = None, spec=None,
                 **kwargs):
        self._spec = spec
        self.__dict__.update(
            user_name=user_name, category=category, exposure=exposure,
            scripting_name=scripting_name, plugin=plugin, **kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __setitem__(self, key, value):
        if self._spec is not None:
            if value is not None:
                self._spec._api.operator_specification_set_property(self._spec, key, value)
                self._spec._properties = None
        setattr(self, key, value)

    def __getitem__(self, item : str):
        return getattr(self, item)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class CustomSpecification(Specification):
    """Allows to create an Operator Specification with its description (what the Operator does),
    its inputs and outputs and some properties.
    Inherits from Specification (which has only getters) to implement setters.

    Designed to be used in an implementation of
    :class:`CustomOperatorBase <ansys.dpf.core.custom_operator.CustomOperatorBase>` for
    the property ``specification``.

    Notes
    -----
    Is only implemented for usage with type(server)=
    :class:`ansys.dpf.core.server_types.InProcessServer`
    and server version higher than 4.0.

    Examples
    --------
    >>> from ansys.dpf.core.custom_operator import CustomOperatorBase
    >>> from ansys.dpf.core import Field
    >>> from ansys.dpf.core.operator_specification import CustomSpecification, \
    SpecificationProperties, PinSpecification
    >>> class AddFloatToFieldData(CustomOperatorBase):
    ...     def run(self):
    ...         field = self.get_input(0, Field)
    ...         to_add = self.get_input(1, float)
    ...         data = field.data
    ...         data += to_add
    ...         self.set_output(0, field)
    ...         self.set_succeeded()
    ...
    ...     @property
    ...     def specification(self):
    ...         spec = CustomSpecification()
    ...         spec.description = "Add a custom value to all the data of an input Field"
    ...         spec.inputs = {
    ...             0: PinSpecification("field", [Field], "Field on which float value is added."),
    ...             1: PinSpecification("to_add", [float], "Data to add.") }
    ...         spec.outputs = {
    ...             0: PinSpecification("field", [Field], "Updated field.")}
    ...         spec.properties = SpecificationProperties("custom add to field", "math")
    ...         return spec
    ...
    ...     @property
    ...     def name(self):
    ...         return "custom_add_to_field"
    """

    def __init__(self, description=None, server=None):
        super().__init__(server=server)
        if description is not None:
            self.description = description

    @property
    @version_requires("4.0")
    def description(self) -> str:
        """Description of the operation applied by the Operator"""
        return super().description

    @description.setter
    def description(self, value) -> str:
        self._api.operator_specification_set_description(self, value)

    @property
    @version_requires("4.0")
    def inputs(self) -> dict:
        """Dictionary mapping the input pin numbers to their ``PinSpecification``

        Returns
        -------
        inputs : dict[int:PinSpecification]
        """
        return super().inputs

    @inputs.setter
    def inputs(self, val: dict):
        for key, value in val.items():
            list_types = integral_types.MutableListString(value.type_names)
            self._api.operator_specification_set_pin(
                self, True, key, value.name, value.document, len(value.type_names)
                , list_types, value.optional, value.ellipsis)

    @property
    @version_requires("4.0")
    def outputs(self) -> dict:
        """Returns a dictionary mapping the output pin numbers to their ``PinSpecification``

        Returns
        -------
        outputs : dict[int:PinSpecification]
        """
        return super().outputs

    @outputs.setter
    def outputs(self, val: dict):
        for key, value in val.items():
            list_types = integral_types.MutableListString(value.type_names)
            self._api.operator_specification_set_pin(
                self, False, key, value.name, value.document, len(value.type_names),
                list_types, value.optional, value.ellipsis)

    @property
    @version_requires("4.0")
    def config_specification(self) -> ConfigSpecification:
        """Documents the available configuration options supported by the Operator

        Returns
        -------
        ConfigSpecification
        """
        return super().config_specification

    @config_specification.setter
    def config_specification(self, val: list):
        if isinstance(val, dict):
            val = [value for key, value in val.items()]
        for value in val:
            for type in value.type_names:
                if type == "double":
                    self._api.operator_specification_add_double_config_option(
                        self, value.name,
                        float(value.default_value_str),
                        value.document)
                elif type == "int32":
                    self._api.operator_specification_add_int_config_option(
                        self, value.name,
                        int(float(value.default_value_str)),
                        value.document)
                elif type == "bool":
                    self._api.operator_specification_add_bool_config_option(
                        self, value.name,
                        value.default_value_str == "True",
                        value.document)
                else:
                    raise TypeError(
                        "config options are expected to be either boolean, integer or double values"
                    )

    @property
    @version_requires("4.0")
    def properties(self) -> SpecificationProperties:
        """Returns some additional properties of the Operator, like the category, the exposure,
        the scripting and user names and the plugin"""
        return SpecificationProperties(**super().properties, spec=self)

    @properties.setter
    def properties(self, val: SpecificationProperties):
        if isinstance(val, SpecificationProperties):
            val = val.__dict__
        for key, value in val.items():
            if value is not None:
                self._api.operator_specification_set_property(self, key, value)
