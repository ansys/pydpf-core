import json
import re
import types
import sys
from collections import namedtuple
from functools import wraps

OperatorFrame = namedtuple("OperatorFrame", ["name", "id"])
"""An operator that a structured DPF error passed through (name and id)."""

# Legacy banners that may prefix a structured error, e.g.
# ``a 'data processing core error' error occurred: {...}`` (CAPI raise path) or
# ``DPF Error: {...}`` (server startup stderr).
_LEGACY_BANNER = re.compile(r"^(?:a '[^']*' error occurred: |DPF Error: )")


def _parse_structured_error(msg):
    """Return the parsed structured DPF error, or ``None`` when ``msg`` is not one.

    A structured error is a JSON document holding a ``"frames"`` mapping, keyed by
    string indices where ``"0"`` is the innermost root cause. A legacy C-layer
    banner (see :data:`_LEGACY_BANNER`) is stripped first; the remainder must then
    start with ``{`` to be considered a structured error.
    """
    if not isinstance(msg, str):
        return None
    text = _LEGACY_BANNER.sub("", msg.strip(), count=1)
    if not text.startswith("{"):
        return None
    try:
        data = json.loads(text)
    except ValueError:
        return None
    if not isinstance(data, dict) or "frames" not in data:
        return None
    return data


def format_dpf_error(msg):
    """Return a human-readable message for a possibly structured DPF error string.

    A structured error (optionally wrapped in a legacy banner) is rendered as its
    root-cause message, remediation suggestion and operator-chain note. The whole
    string is tried first, then each line, so a structured payload embedded in
    multi-line server stderr is still recognized. Non-structured messages are
    returned unchanged.
    """
    if not isinstance(msg, str):
        return msg
    for candidate in (msg, *msg.splitlines()):
        if _parse_structured_error(candidate) is not None:
            error = DPFServerException(candidate)
            notes = [note for note in getattr(error, "__notes__", []) if note]
            return "\n".join([str(error), *notes])
    return msg


class DPFServerException(Exception):
    """Error raised when the DPF server has encountered an error.

    When the server reports a structured error, these attributes are populated
    from the root cause and its nested chain:

    - ``type``: stable error type of the root cause (``None`` if unknown).
    - ``what``: root cause message.
    - ``suggestion``: remediation hint provided by the operator, if any.
    - ``fields``: remaining typed attributes of the root cause frame.
    - ``chain``: list of :class:`OperatorFrame` the error passed through, from
      the outermost operator down to the root cause.

    For legacy flat-string errors these attributes stay ``None``/empty and the
    behavior is unchanged.

    Examples
    --------
    Catch a server error raised while evaluating an operator and inspect the
    structured root cause:

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import operators as ops
    >>> data_sources = dpf.DataSources("non_existing_file.rst")
    >>> displacement = ops.result.displacement(data_sources=data_sources)
    >>> try:  # doctest: +SKIP
    ...     displacement.eval()
    ... except dpf.errors.DPFServerException as error:
    ...     # ``str(error)`` is a short, actionable message (root cause and,
    ...     # when available, a remediation suggestion).
    ...     print(str(error))
    ...     # The following attributes are populated when the server reports a
    ...     # structured error; otherwise they stay ``None``/empty.
    ...     print(error.type)  # stable category, e.g. "file_not_found"
    ...     print(error.suggestion)  # remediation hint, when the operator provides one
    ...     print(error.fields)  # extra typed data, e.g. {"filepath": "..."}
    ...     # ``chain`` lists the operators the error crossed, from the
    ...     # outermost operator down to the root cause.
    ...     for frame in error.chain:
    ...         print(frame.name, frame.id)
    ...     # Branch on the stable ``type`` to recover from a specific failure.
    ...     if error.type == "file_not_found":
    ...         pass  # e.g. prompt the user for a valid path and retry
    """

    def __init__(self, msg=""):
        self.type = None
        self.what = None
        self.suggestion = None
        self.fields = {}
        self.chain = []

        structured = _parse_structured_error(msg)
        if structured is not None:
            error_message, error_note = self._init_structured(structured)
        else:
            error_message, error_note = self._init_legacy(msg)

        Exception.__init__(self, error_message)
        if sys.version_info >= (3, 11): #add_note method is supported only in python >= 3.11
            self.add_note(error_note)
        else:
            if not hasattr(self, "__notes__"): #if the system is python < 3.11 we custom our own notes property
                self.__notes__ = []
            self.__notes__.append(error_note)

    def _init_structured(self, data):
        """Populate structured attributes and return the (message, note) pair."""
        frames_raw = data.get("frames", {})
        # Frames are keyed by string indices; "0" is the innermost root cause.
        frames = [frames_raw[key] for key in sorted(frames_raw, key=int)]
        root = frames[0] if frames else {}

        self.type = root.get("type")
        self.what = root.get("what", "")
        self.suggestion = root.get("suggestion")
        self.fields = {
            key: value
            for key, value in root.items()
            if key not in ("type", "what", "suggestion")
        }
        # Operator frames, from the outermost operator down to the root cause.
        self.chain = [
            OperatorFrame(frame.get("operator_name"), frame.get("operator_id"))
            for frame in reversed(frames)
            if frame.get("type") == "opframe"
        ]

        error_message = self.what
        if self.suggestion:
            error_message = f"{self.what}\nSuggestion: {self.suggestion}"

        if self.chain:
            error_note = "Operator chain: " + " <- ".join(
                f"{frame.name} ({frame.id})" for frame in self.chain
            )
        else:
            error_note = ""
        return error_message, error_note

    def _init_legacy(self, msg):
        """Split a legacy flat-string error into a (message, note) pair."""
        message_parts = msg.rsplit('<-', maxsplit=1)
        if len(message_parts) == 1:
            return message_parts[0], ""
        error_note, error_message = message_parts
        return error_message, error_note


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
