"""
.. _ref_operator_specification:

OperatorSpecification
=====================
The OperatorSpecification Provides a documentation for each Operator
"""

import abc
from typing import NamedTuple
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import operator_specification_capi, operator_specification_grpcapi, integral_types


class PinSpecification:
    """Documents an input or output pin of an Operator"""
    name: str
    type_names: list
    optional: bool
    document: str
    ellipsis: bool

    def __init__(self, name, type_names, optional, document, ellipsis=False):
        self.name = name
        self.type_names = type_names
        self.optional = optional
        self.document = document
        self.ellipsis = ellipsis

    @staticmethod
    def _get_copy(other, changed_types):
        return PinSpecification(other.name,
                                changed_types,
                                other.optional,
                                other.document,
                                other.ellipsis)

class ConfigSpecification(dict):
   def __init__(self, *arg, **kw):
      super(ConfigSpecification, self).__init__(*arg, **kw)

class ConfigOptionSpec(NamedTuple):
    name: str
    type_names: list
    default_value_str: str
    document: str


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
    """Documents an Operator with its description (what the Operator does), its inputs and outputs and some properties

    Examples
    --------
    Get the Specification of an operator by its name
    >>> from ansys.dpf import core as dpf
    >>> spec = dpf.operator_specification.Specification("U")
    >>> # or
    >>> spec = dpf.Operator.operator_specification("U")

    Get the specification of an instanciated operator
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
                    raise NotImplementedError("Creating an empty specification on a gRPC client is not implemented")
                self._internal_obj = self._api.operator_empty_specification_new()

        self.operator_name = operator_name
        self._map_output_pin_spec = None
        self._map_input_pin_spec = None
        self._properties = None
        self._config_specification = None

    @property
    def properties(self):
        if self._properties is None:
            self._properties = dict()
            if self._internal_obj is not None:
                num_properties = self._api.operator_specification_get_num_properties(self)
                for i_property in range(num_properties):
                    property_key = self._api.operator_specification_get_property_key(self, i_property)
                    prop = self._api.operator_specification_get_properties(self, property_key)
                    self._properties[property_key] = prop
        return self._properties

    @property
    def description(self) -> str:
        """Returns a desription of the operation applied by the Operator

        Returns
        -------
        str
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
                                                  pin_opt,
                                                  pin_doc,
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
                option_default_value = self._api.operator_specification_get_config_printable_default_value(self, i)
                option_doc = self._api.operator_specification_get_config_description(self, i)
                self._config_specification[option_name] = ConfigOptionSpec(name=option_name,
                                                       type_names=option_type_names,
                                                       default_value_str=option_default_value,
                                                       document=option_doc)
        return self._config_specification
