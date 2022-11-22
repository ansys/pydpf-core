"""
ServerContext
=============

Gives the ability to choose the context with which the server should be started.
The context allows to choose which capabilities are available.
By default, an **Entry** type of :class:`ServerContext` is used.
The default context can be overwritten using the ANSYS_DPF_SERVER_CONTEXT environment
variable.
ANSYS_DPF_SERVER_CONTEXT=ENTRY and ANSYS_DPF_SERVER_CONTEXT=PREMIUM can be used.
"""
import os
import warnings
from enum import Enum


class EContextType(Enum):
    pre_defined_environment = 0
    """DataProcessingCore.xml that is next to DataProcessingCore.dll/libDataProcessingCore.so will
    be taken"""
    premium = 1
    """Gets the Specific premium DataProcessingCore.xml."""
    user_defined = 2
    """Load a user defined xml using its path."""
    custom_defined = 3
    """Loads the xml named "DpfCustomDefined.xml" that the user can modify."""
    entry = 4
    """Loads the minimum number of plugins for a basic usage."""


class ServerContext:
    """The context allows to choose which capabilities are available server side.

    Parameters
    ----------
    context_type : EContextType
        Type of context.
    xml_path : str, optional
        Path to the xml to load.
    """
    def __init__(self, context_type=EContextType.user_defined, xml_path=""):
        self._context_type = context_type
        self._xml_path = xml_path

    @property
    def context_type(self):
        return self._context_type

    @property
    def xml_path(self):
        return self._xml_path

    def __str__(self):
        return f"Server Context of type {self.context_type}" \
               f" with {'no' if len(self.xml_path)==0 else ''} xml path" \
               f"{'' if len(self.xml_path)==0 else ': ' + self.xml_path}"


class AvailableServerContexts:
    pre_defined_environment = ServerContext(EContextType.pre_defined_environment)
    """DataProcessingCore.xml that is next to DataProcessingCore.dll/libDataProcessingCore.so will
    be taken"""
    premium = ServerContext(EContextType.premium)
    """Gets the Specific premium DataProcessingCore.xml to load most plugins with their
    environments."""
    custom_defined = ServerContext(EContextType.custom_defined)
    """Loads the xml named "DpfCustomDefined.xml" that the user can modify."""
    entry = ServerContext(EContextType.entry)
    """Loads the minimum number of plugins for a basic usage. Is the default."""


DPF_SERVER_CONTEXT_ENV = "ANSYS_DPF_SERVER_CONTEXT"

SERVER_CONTEXT = AvailableServerContexts.entry
if DPF_SERVER_CONTEXT_ENV in os.environ.keys():
    default_context = os.getenv(DPF_SERVER_CONTEXT_ENV)
    try:
        SERVER_CONTEXT = getattr(AvailableServerContexts, default_context.lower())
    except AttributeError:
        warnings.warn(UserWarning(
                      f"{DPF_SERVER_CONTEXT_ENV} is set to {default_context}, which is not "
                      f"recognized as an available DPF ServerContext type. \n"
                      f"Accepted values are: {[t.name.upper() for t in EContextType]}.\n"
                      f"Using {EContextType.entry.name.upper()} "
                      f"as the default ServerContext type."))


def apply_server_context(context=AvailableServerContexts.entry, server=None) -> None:
    """Allows to apply a context globally (if no server is specified) or to a
    given server.
    When called before any server is started, the context will be applied by default to any
    new server.

    The context allows to choose which capabilities are available server side.

    Parameters
    ----------
    context : ServerContext
        Context to apply to the given server or to the newly started servers (when no server
        is given).
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.

    Notes
    -----
    Available with server's version starting at 6.0 (Ansys 2023R2).
    """
    from ansys.dpf.core import SERVER
    if server is None:
        server = SERVER
        global SERVER_CONTEXT
        SERVER_CONTEXT = context
    if server is not None:
        from ansys.dpf.core.core import BaseService
        base = BaseService(server, load_operators=False)
        base.apply_context(context)
