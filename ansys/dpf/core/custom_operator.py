"""
CustomOperatorBase
==================
Contains utilities enabling to implement and record custom python operators.
"""

import abc
import ctypes

from ansys.dpf import core as dpf
from ansys.dpf.core import settings, server, server_factory, operator_specification
from ansys.dpf.core._custom_operators_helpers import __operator_main__, functions_registry, external_operator_api, _type_to_output_method, _type_to_input_method
from ansys.dpf.gate import object_handler, capi


def record_operator(operator_type, *args) -> None:
    """
    Add an operator (with its name, run callback and specification) to DPF core registry.

    Parameters
    ----------
    operator_type : type, CustomOperatorBase
        class type inheriting from CustomOperatorBase. ``name`` and ``specification`` properties are called
        and run method callback is given to DataProcessingCore.

    *args
        Forwarded arguments passed in ``load_operators`` method

    """
    if isinstance(operator_type, type):
        operator = operator_type()
    else:
        operator = operator_type
    if dpf.SERVER is None:
        settings.set_server_configuration(server_factory.ServerConfig(None, False))
        server.start_local_server()
    if len(args) == 2:
        external_operator_api.external_operator_record_with_abstract_core_and_wrapper(
            operator._call_back(), __operator_main__, operator.name, operator._internal_specification,
            ctypes.c_void_p(*args[0]), ctypes.c_void_p(*args[1]))
    else:
        external_operator_api.external_operator_record_with_abstract_core(operator._call_back(),
                                                                                                __operator_main__,
                                                                                                operator.name,
                                                                                                operator._internal_specification,
                                                                                                ctypes.c_void_p(*args))




class CustomOperatorBase:
    """
    Base class interfacing CPython Custom Operators which can be used as regular
    DPF Operators in any API.
    A CustomOperator is defined by its name, its specification and its run method. These 3 abstract methods
    should be implemented to create a CustomOperator.

    Examples
    --------
    Create a Custom Operator which adds an input float value to the data of an input Field.

    >>> from ansys.dpf.core.custom_operator import CustomOperatorBase
    >>> from ansys.dpf.core import Field
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
    ...         return None
    ...
    ...     @property
    ...     def name(self):
    ...         return "custom_add_to_field"

    And record it:

    >>> from ansys.dpf.core.custom_operator import record_operator
    >>> def load_operators(*args):
    ...     record_operator(AddFloatToFieldData, *args)

    """
    def set_output(self, index: int, data) -> None:
        """
        Add an output to this Operator at the given index.
        To use in the ``run`` method.

        Parameters
        ----------
        index : int
            Index of the output.

        data: int, float, Field, Scoping, DataSources, FieldsContainer...
            Data of any supported type to return.

        """
        for type_tuple in _type_to_output_method:
            if isinstance(data, type_tuple[0]):
                return type_tuple[1](self._operator_data, index, data)
        raise TypeError(f"unable to set output of type type(data).__name__")
        # TO DO: handle lists

    def get_input(self, index, type: type):
        """
        Method used to get an input of a requested type at a given index in the ``run`` method.
        The correct input type should have been connected to this Operator beforehand.

        Parameters
        ----------
        index : int
            Index of the input.

        type : type
            Expected type of the data.

        Returns
        -------
        data: type
        """
        for type_tuple in _type_to_input_method:
            if type is type_tuple[0]:
                if len(type_tuple) >= 3:
                    parameters = {type_tuple[2]: type_tuple[1](self._operator_data, index)}
                    return type(**parameters)
                return type(type_tuple[1](self._operator_data, index))

    def set_failed(self) -> None:
        """
        Set the Operator's status to "failed".
        To use in the ``run`` method if an error occurred.
        This "failed" status is automatically set when an exception is raised in the ``run`` method.
        """
        external_operator_api.external_operator_put_status(self._operator_data, 1)

    def set_succeeded(self) -> None:
        """
        Set the Operator's status to "succeeded".
        To use at the end of the ``run`` method.
        """
        external_operator_api.external_operator_put_status(self._operator_data, 0)

    def _call_back(self):
        def _self_call_back(op):
            self._operator_data = op
            try:
                self.run()
            except:
                import traceback
                external_operator_api.external_operator_put_exception(self._operator_data, 4,
                                                                      str(traceback.format_exc()))

        functions_registry.append(capi.OperatorMainCallback(_self_call_back))
        return functions_registry[-1]

    @property
    def _internal_specification(self):
        if isinstance(self.specification, operator_specification.Specification):
            return self.specification
        else:
            return object_handler.ObjHandler(ctypes.c_void_p(self.specification))

    @abc.abstractmethod
    def run(self) -> None:
        """
        Callback of the Operator to implement.
        The implementation should first request the inputs with the method ``get_input``,
        compute the output data, then add the outputs with the method ``set_output`` and finally
        call ``set_succeeded``.
        """
        pass

    @property
    @abc.abstractmethod
    def specification(self):
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        Returns the identifier or name of the operator.
        This name can then be used to instantiate the Operator.
        """
        pass
