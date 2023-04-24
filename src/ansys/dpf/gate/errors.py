import types
from functools import wraps

class DPFServerException(Exception):
    """Error raised when the DPF server has encountered an error."""

    def __init__(self, msg=""):
        Exception.__init__(self, msg)


class DPFServerNullObject(Exception):
    """Error raised when the DPF server cannot find an object."""

    def __init__(self, msg=""):
        Exception.__init__(self, msg)


class DpfVersionNotSupported(RuntimeError):
    """Error raised when the dpf-core/grpc-dpf python features are not
    supported by the DPF gRPC server version."""

    def __init__(self, version, msg=None):
        if msg is None:
            msg = "Feature not supported. Upgrade the server to "
            msg += str(version)
            msg += " version (or above)."
        RuntimeError.__init__(self, msg)


def protect_grpc(func):
    """Capture gRPC exceptions and return a more succinct error message."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Capture gRPC exceptions."""
        from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous
        try:
            out = func(*args, **kwargs)
        except (_InactiveRpcError, _MultiThreadedRendezvous) as error:
            details = error.details()
            if "object is null in the dataBase" in details:
                raise DPFServerNullObject(details) from None
            elif "Unable to open the following file" in details:
                raise DPFServerException(
                    "The result file could not be found or could not be opened, the server raised an error message: \n" + details) from None
            raise DPFServerException(details) from None

        return out

    return wrapper



def protect_grpc_class(cls):
    """Add a protect_grpc decorator on all functions, class methods and static methods of a
    class having this decorator to capture gRPC exceptions and return a more succinct error message.
    """
    for name, member in vars(cls).items():
        # Good old function object, just decorate it
        if isinstance(member, (types.FunctionType, types.BuiltinFunctionType)):
            setattr(cls, name, protect_grpc(member))
            continue

        # Static and class methods: do the dark magic
        if isinstance(member, (classmethod, staticmethod)):
            inner_func = member.__func__
            method_type = type(member)
            decorated = method_type(protect_grpc(inner_func))
            setattr(cls, name, decorated)
            continue

    return cls
