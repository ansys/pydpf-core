"""
.. _ref_errors:

Errors
======

.. autoexception:: DpfVersionNotSupported
   :members:

.. autoexception:: DPFServerNullObject
   :members:
"""

from functools import wraps
from ansys.dpf.gate.errors import DPFServerException, \
    DPFServerNullObject, DpfVersionNotSupported  # noqa: F401

_COMPLEX_PLOTTING_ERROR_MSG = """
Complex fields cannot be plotted. Use operators to get the amplitude
or the result at a defined sweeping phase before plotting.
"""

_FIELD_CONTAINER_PLOTTING_MSG = """"
This fields_container contains multiple fields.  Only one time-step
result can be plotted at a time. Extract a field with
``fields_container[index]``.
"""


class DpfValueError(ValueError):
    """Error raised when a specific DPF error value must be defined."""

    def __init__(
        self, msg="A value that has been set leads to incorrect DPF behavior."
    ):
        ValueError.__init__(self, msg)


class InvalidTypeError(ValueError):
    """Error raised when a parameter has the wrong type."""

    def __init__(self, data_type, parameter_name):
        msg = (
            "A "
            + data_type
            + " must be used for the following parameter: "
            + parameter_name
            + "."
        )
        ValueError.__init__(self, msg)


class LocationError(ValueError):
    """Error raised when using an invalid location."""

    def __init__(self, msg="Invalid location"):
        ValueError.__init__(self, msg)


class ComplexPlottingError(ValueError):
    """Error raised when attempting to plot a field with complex data."""

    def __init__(self, msg=_COMPLEX_PLOTTING_ERROR_MSG):
        ValueError.__init__(self, msg)


class FieldContainerPlottingError(ValueError):
    """Error raised when attempting to plot a fields_container containing
    multiple fields."""

    def __init__(self, msg=_FIELD_CONTAINER_PLOTTING_MSG):
        ValueError.__init__(self, msg)


class InvalidANSYSVersionError(RuntimeError):
    """Error raised when the Ansys version is invalid."""

    def __init__(self, msg=""):
        RuntimeError.__init__(self, msg)


class InvalidPortError(OSError):
    """Error raised when used an invalid port when starting DPF."""

    def __init__(self, msg=""):
        OSError.__init__(self, msg)


class ServerTypeError(NotImplementedError):
    """Error raised when using a functionality unavailable for this server type"""
    pass


def protect_source_op_not_found(func):
    """Capture DPF's Server exceptions when a source operator is not found
    and return a more succinct error message.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Capture DPF's Server exceptions."""
        try:
            out = func(*args, **kwargs)
        except DPFServerException as error:
            details = str(error)
            if "source operator not found" in details:
                return None
            raise DPFServerException(details)

        return out

    return wrapper
