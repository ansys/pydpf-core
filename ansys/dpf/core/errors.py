from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous


class DPFServerError(RuntimeError):
    """Raised when the DPF Server has encountered an error"""

    def __init__(self, msg=''):
        RuntimeError.__init__(self, msg)


class InvalidPortError(OSError):
    """Raised when used an invalid port when starting DPF"""

    def __init__(self, msg=''):
        OSError.__init__(self, msg)


def protect_grpc(func):
    """Capture gRPC exceptions and return a more succinct error message"""

    def wrapper(*args, **kwargs):
        """Capture gRPC exceptions"""

        # Capture gRPC exceptions
        try:
            out = func(*args, **kwargs)
        except (_InactiveRpcError, _MultiThreadedRendezvous) as error:
            raise DPFServerError(error.details()) from None

        return out

    return wrapper
