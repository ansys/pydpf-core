"""
Operator Configuration
======================
"""

import functools
import warnings
import traceback

from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    operator_config_capi,
    operator_config_grpcapi,
    operator_config_abstract_api,
)
from ansys.dpf.core.operator_specification import Specification


class Config:
    """Represents an operator's configuration.

    You can use configurations to choose how an operator will run.
    This is an advanced feature for deep customization.
    The different options can change the way loops are done.
    They can also change whether the operator needs to perform checks on the input.

    Parameters
    ----------
    operator_name : str, optional
        Name of the operator. The default is ``None``.
    config : str, optional
        Name of the configuration. The default is ``None``.
    server : str, optional
        Server with the channel connected to the remote or local instance. The default is
        ``None``, in which case an attempt is made to use the global server.

    """

    def __init__(self, operator_name=None, config=None, server=None, spec=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._api_instance = None  # see _api property

        # step3: init environment
        self._api.init_operator_config_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it
        if config:
            self._internal_obj = config
        else:
            if self._server.has_client():
                if operator_name:
                    self._internal_obj = self._api.operator_config_default_new_on_client(
                        self._server.client, operator_name)
                else:
                    self._internal_obj = self._api.operator_config_empty_new_on_client(
                        self._server.client)
            else:
                if operator_name:
                    self._internal_obj = self._api.operator_config_default_new(operator_name)
                else:
                    self._internal_obj = self._api.operator_config_empty_new()

        self._operator_name = operator_name
        self._spec_instance = spec
        self._config_help_instance = None

        opt = self.options
        for name in opt:
            bound_method = self.config_option_value.__get__(self, self.__class__)
            method2 = functools.partial(bound_method, config_name=name)
            setattr(self, "get_" + name + "_option", method2)

            bound_method = self.__set_config_option__.__get__(self, self.__class__)
            method2 = functools.partial(bound_method, config_name=name)
            setattr(self, "set_" + name + "_option", method2)

    @property
    def _api(self) -> operator_config_abstract_api.OperatorConfigAbstractAPI:
        if self._api_instance is None:
            self._api_instance = self._server.get_api_for_type(
                capi=operator_config_capi.OperatorConfigCAPI,
                grpcapi=operator_config_grpcapi.OperatorConfigGRPCAPI)
        return self._api_instance

    @property
    def _spec(self):
        if self._spec_instance is None and self._operator_name is not None:
            self._spec_instance = Specification(self._operator_name, server=self._server)
        return self._spec_instance

    @property
    def _config_help(self):
        if self._spec:
            return self._spec.config_specification

    @property
    def options(self):
        """Retrieve a list of configuration options and their values.

        Returns
        -------
        list
            List of configuration options and their values.
        """
        options = {}
        num_options = self._api.operator_config_get_num_config(self)
        for i in range(num_options):
            options[
                self._api.operator_config_get_config_option_name(self, i)
            ] = self._api.operator_config_get_config_option_printable_value(
                self, i)
        return options

    def __set_config_option__(self, config_value, config_name):
        """Change the value of a configuration option.

        Parameters
        ----------
        config_value : bool, int, float
            Value to give to a configuration option.
        config_name : str
            Name of the configuration option.
        """
        if isinstance(config_value, bool):
            self._api.operator_config_set_bool(self, config_name, config_value)
        elif isinstance(config_value, int):
            self._api.operator_config_set_int(self, config_name, config_value)
        elif isinstance(config_value, float):
            self._api.operator_config_set_double(self, config_name, config_value)
        else:
            raise TypeError(
                "str, int, float are the accepted types for configuration options."
            )

    def set_config_option(self, config_name, config_value):
        """Change the value of a configuration option.

        Parameters
        ----------
        config_value : bool, int, float
            Value to give to a configuration option.
        config_name : str
            Name of the configuration option.
        """
        return self.__set_config_option__(config_value, config_name)

    def config_option_value(self, config_name):
        """Retrieve the value for a configuration option.

        Parameters
        ----------
        config_name : str
            Name of the configuration option.

        Returns
        ----------
        str
            Value for the configuration option.
        """
        opt = self.options
        if config_name in opt:
            return opt[config_name]
        else:
            raise KeyError(f"{config_name} option doesn't exist.")

    def __try_get_option__(self, config_name):
        if self._config_help:
            if config_name in self._config_help:
                return self._config_help[config_name]
        return None

    def config_option_documentation(self, config_name):
        """Retrieve the documentation for a configuration option.

        Parameters
        ----------
        config_name : str
            Name of the configuration option.

        Returns
        ----------
        str
           Documentation for the configuration option.
        """
        option = self.__try_get_option__(config_name)
        if option:
            return option.document
        return ""

    def config_option_accepted_types(self, config_name):
        """Retrieve accepted types for a configuration option.

        Parameters
        ----------
        config_name : str
            Name of the configuration option.

        Returns
        ----------
        list, str
            One or more accepted types for the configuration option.
        """
        option = self.__try_get_option__(config_name)
        if option:
            return option.type_names

    def config_option_default_value(self, config_name):
        """Retrieve the default value for a configuration option.

        Parameters
        ----------
        config_name : str
            Name of the configuration option.

        Returns
        ----------
        str
            Default value for the configuration option.
        """
        option = self.__try_get_option__(config_name)
        if option:
            return option.default_value_str
        return ""

    @property
    def available_config_options(self):
        """Available configuration options for the operator.

        Returns
        ----------
        list, str
           One or more available configuration options for the operator.
        """
        opt = self.options
        if opt:
            return [key for key in opt]
        return []

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description
        return _description(self._internal_obj, self._server)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
