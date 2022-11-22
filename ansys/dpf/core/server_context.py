"""
ServerContext
=============

Gives the ability to choose the context with which the server should be started.
The context allows to choose which capabilities are available.
"""
import os.path
from enum import Enum


class LicensingContextType(Enum):
    premium = 1
    """Allows capabilities requiring Licenses check out."""
    entry = 4
    """Loads minimum capabilities without requiring any Licenses check out."""

    def __int__(self):
        return self.value

    @staticmethod
    def same_licensing_context(first, second):
        if int(first) == int(LicensingContextType.entry) and int(second) != int(
                LicensingContextType.entry):
            return False
        elif int(second) == int(LicensingContextType.entry) and int(first) != int(
                LicensingContextType.entry):
            return False
        return True


class ServerContext:
    """The context allows to choose which capabilities are available server side.
    xml_path argument won't be taken into account if using LicensingContextType.entry.

    Parameters
    ----------
    context_type : LicensingContextType
        Type of context.
    xml_path : str, optional
        Path to the xml to load.
    """

    def __init__(self, context_type=LicensingContextType.premium, xml_path=""):
        self._context_type = context_type
        self._xml_path = xml_path

    @property
    def licensing_context_type(self):
        """Whether capabilities requiring Licenses check out should be allowed.

        Returns
        -------
        LicensingContextType
        """
        return self._context_type

    @property
    def xml_path(self):
        """Path to the xml listing the capabilities to load on the server.

        Returns
        -------
        str
        """
        return self._xml_path

    def __str__(self):
        return f"Server Context of type {self.licensing_context_type}" \
               f" with {'no' if len(self.xml_path) == 0 else ''} xml path" \
               f"{'' if len(self.xml_path) == 0 else ': ' + self.xml_path}"

    def __eq__(self, other):
        if not isinstance(other, ServerContext):
            return False
        return os.path.normpath(self.xml_path) == os.path.normpath(other.xml_path) \
               and LicensingContextType.same_licensing_context(self.licensing_context_type,
                                                               other.licensing_context_type)

    def __ne__(self, other):
        return not self == other


class AvailableServerContexts:
    pre_defined_environment = ServerContext(0)
    """DataProcessingCore.xml that is next to DataProcessingCore.dll/libDataProcessingCore.so will
    be taken"""
    premium = ServerContext(LicensingContextType.premium)
    """Gets the Specific premium DataProcessingCore.xml to load most plugins with their
    environments."""
    custom_defined = ServerContext(3)
    """Loads the xml named "DpfCustomDefined.xml" that the user can modify."""
    entry = ServerContext(LicensingContextType.entry)
    """Loads the minimum number of plugins for a basic usage. Is the default."""


SERVER_CONTEXT = AvailableServerContexts.entry


def set_default_server_context(context=AvailableServerContexts.entry) -> None:
    """This context will be applied by default to any new server as well as
    the global server, if it's running.

    The context allows to choose which capabilities are available server side.

    Parameters
    ----------
    context : ServerContext
        Context to apply to the given server or to the newly started servers (when no server
        is given).

    Notes
    -----
    Available with server's version starting at 6.0 (Ansys 2023R2).
    """
    from ansys.dpf.core import SERVER
    global SERVER_CONTEXT
    SERVER_CONTEXT = context
    if SERVER is not None:
        SERVER.apply_context(context)
