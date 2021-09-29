from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous
from functools import wraps

_COMPLEX_PLOTTING_ERROR_MSG = """
Complex fields cannot be plotted. Use operators to get the amplitude
or the result at a defined sweeping phase before plotting.
"""

_FIELD_CONTAINER_PLOTTING_MSG = """"
This fields_container contains multiple fields.  Only one time-step
result can be plotted at a time. Extract a field with
``fields_container[index]``.
"""


class DpfVersionNotSupported(RuntimeError):
    """Error raised when the dpf-core/grpc-dpf python features are not
    supported by the DPF gRPC server version."""

    def __init__(self, version, msg=None):
        if msg is None:
            msg = "Feature not supported. Upgrade the server to "
            msg += str(version)
            msg += " version (or above)."
        RuntimeError.__init__(self, msg)


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
    """Error raised when the Ansys verion is invalid."""

    def __init__(self, msg=""):
        RuntimeError.__init__(self, msg)


class DPFServerException(Exception):
    """Error raised when the DPF server has encountered an error."""

    def __init__(self, msg=""):
        Exception.__init__(self, msg)


class DPFServerNullObject(Exception):
    """Error raised when the DPF server cannot find an object."""

    def __init__(self, msg=""):
        Exception.__init__(self, msg)


class InvalidPortError(OSError):
    """Error raised when used an invalid port when starting DPF."""

    def __init__(self, msg=""):
        OSError.__init__(self, msg)


def protect_grpc(func):
    """Capture gRPC exceptions and return a more succinct error message."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Capture gRPC exceptions."""
        # Capture gRPC exceptions
        try:
            out = func(*args, **kwargs)
        except (_InactiveRpcError, _MultiThreadedRendezvous) as error:
            details = error.details()
            if "object is null in the dataBase" in details:
                raise DPFServerNullObject(details) from None
            raise DPFServerException(details) from None

        return out

    return wrapper
