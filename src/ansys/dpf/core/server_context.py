# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
ServerContext.

Gives the ability to choose the context with which the server should be started.
The context allows you to choose the licensing logic for operators.
For every context, DPF always checks if an Ansys license is available.
By default, a **Premium** type of :class:`ServerContext` is used,
meaning that any operator requiring a license check-out can do so.
The **Entry** context instead does not allow operators to check a license out,
which will result in failure of operators requiring it.
The default context can be overwritten using the ANSYS_DPF_SERVER_CONTEXT environment
variable.
ANSYS_DPF_SERVER_CONTEXT=ENTRY and ANSYS_DPF_SERVER_CONTEXT=PREMIUM can be used.
"""

from enum import Enum
import os
import warnings

from ansys.dpf.core import dpf_operator, errors


class LicensingContextType(Enum):
    """Enum representing different types of licensing contexts."""

    premium = 1
    """Checks if at least one license increment exists
    and allows operators to block an increment."""
    entry = 4
    """Checks if at least one license increment exists
    and does not allow operators to block an increment."""

    def __int__(self):
        """
        Return the integer values of the licensing context.

        Returns
        -------
        int
            Integer values corresponding to the licensing context.
        """
        return self.value

    @staticmethod
    def same_licensing_context(first, second):
        """
        Determine if two licensing contexts are compatible.

        Parameters
        ----------
        first : LicensingContextType
            The first licensing context to compare.
        second : LicensingContextType
            The second licensing context to compare.

        Returns
        -------
        bool
            True if the licensing contexts are compatible, False otherwise.
        """
        if int(first) == int(LicensingContextType.entry) and int(second) != int(
            LicensingContextType.entry
        ):
            return False
        elif int(second) == int(LicensingContextType.entry) and int(first) != int(
            LicensingContextType.entry
        ):
            return False
        return True


class LicenseContextManager:
    """Can optionally be used to check out a license before using licensed DPF Operators.

    Improves performance if you are using multiple Operators that require licensing.
    It can also be used to force checkout before running a script when few
    Ansys license increments are available.
    The license is checked in when the object is deleted.

    Parameters
    ----------
    increment_name: str, optional
         License increment to check out. To improve script efficiency, this license increment
         should be consistent with the increments required by the following Operators. If ``None``,
         the first available increment of this
         `list <https://dpf.docs.pyansys.com/version/stable/getting_started/licensing.html#compatible-ansys-license-increments>`_
         is checked out.
    license_timeout_in_seconds: float, optional
         If an increment is not available by the maximum time set here, check out fails. Default is:
         :py:func:`ansys.dpf.core.runtime_config.RuntimeCoreConfig.license_timeout_in_seconds`
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Using a context manager
    >>> from ansys.dpf import core as dpf
    >>> dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    >>> field = dpf.Field()
    >>> field.append([0., 0., 0.], 1)
    >>> op = dpf.operators.filter.field_high_pass()
    >>> op.inputs.field(field)
    >>> op.inputs.threshold(0.0)
    >>> with dpf.LicenseContextManager() as lic:
    ...    out = op.outputs.field()

    Using an instance
    >>> lic = dpf.LicenseContextManager()
    >>> op.inputs.field(field)
    >>> op.inputs.threshold(0.0)
    >>> out = op.outputs.field()
    >>> lic = None

    Using a context manager and choosing license options
    >>> op.inputs.field(field)
    >>> op.inputs.threshold(0.0)
    >>> out = op.outputs.field()
    >>> op = dpf.operators.filter.field_high_pass()
    >>> op.inputs.field(field)
    >>> op.inputs.threshold(0.0)
    >>> with dpf.LicenseContextManager(
    ...    increment_name="preppost", license_timeout_in_seconds=1.) as lic:
    ...    out = op.outputs.field()

    Notes
    -----
    Available from 6.1 server version.
    """

    def __init__(
        self, increment_name: str = None, license_timeout_in_seconds: float = None, server=None
    ):
        from ansys.dpf.core import server as server_module

        self._server = server_module.get_or_create_server(server)
        if not self._server.meet_version("6.1"):
            raise errors.DpfVersionNotSupported("6.1")
        self._license_checkout_operator = dpf_operator.Operator(
            "license_checkout", server=self._server
        )
        if increment_name is not None:
            self._license_checkout_operator.connect(0, increment_name)
        if license_timeout_in_seconds is not None:
            self._license_checkout_operator.connect(1, license_timeout_in_seconds)
        self._license_checkout_operator.run()

    def release_data(self):
        """Release the data."""
        self._license_checkout_operator = None

    def __enter__(self):
        """
        Enter the runtime context for the license context manager.

        This method is called when the object is used within a `with` statement.
        It ensures that the license is checked out before the operations within the context block are executed.

        Returns
        -------
        LicenseContextManager
            The current instance of the license context manager.
        """
        return self

    def __exit__(self, type, value, tb):
        """
        Exit the runtime context for the license context manager.

        This method is called at the end of a `with` statement. It ensures
        that the license is checked in and any resources allocated are released.

        Parameters
        ----------
        type : type or None
            The exception type, if an exception occurred within the context block, or None otherwise.
        value : Exception or None
            The exception instance, if an exception occurred within the context block, or None otherwise.
        tb : traceback or None
            The traceback object, if an exception occurred within the context block, or None otherwise.

        Returns
        -------
        bool
            If True, suppresses the exception. Otherwise, the exception is propagated.
        """
        if tb is None:
            self.release_data()

    def __del__(self):
        """Release the license when the instance is deleted."""
        self.release_data()
        pass

    @property
    def status(self):
        """Returns a string with the list of checked out increments.

        Returns
        -------
        str
        """
        status_operator = dpf_operator.Operator("license_status", server=self._server)
        return status_operator.eval()


class ServerContext:
    """The context defines whether DPF capabilities requiring a license checkout are allowed.

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
        """Whether capabilities requiring Licenses checkout should be allowed.

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
        """Return string representation of the ServerContext instance."""
        return (
            f"Server Context of type {self.licensing_context_type}"
            f" with {'no' if len(self.xml_path) == 0 else ''} xml path"
            f"{'' if len(self.xml_path) == 0 else ': ' + self.xml_path}"
        )

    def __eq__(self, other):
        """Compare two ServerContext instances for equality."""
        if not isinstance(other, ServerContext):
            return False
        return os.path.normpath(self.xml_path) == os.path.normpath(
            other.xml_path
        ) and LicensingContextType.same_licensing_context(
            self.licensing_context_type, other.licensing_context_type
        )

    def __ne__(self, other):
        """Check that two server contexts are not equal."""
        return not self == other


class AvailableServerContexts:
    """Defines available server contexts."""

    """Applies an empty plugins xml: no plugins are loaded."""
    no_context = ServerContext(2, "")  # 2 == ContextType.userDefined. This is not exposed publicly.
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


DPF_SERVER_CONTEXT_ENV = "ANSYS_DPF_SERVER_CONTEXT"

SERVER_CONTEXT = AvailableServerContexts.premium
if DPF_SERVER_CONTEXT_ENV in os.environ.keys():
    default_context = os.getenv(DPF_SERVER_CONTEXT_ENV)
    try:
        SERVER_CONTEXT = getattr(AvailableServerContexts, default_context.lower())
    except AttributeError:
        warnings.warn(
            UserWarning(
                f"{DPF_SERVER_CONTEXT_ENV} is set to {default_context}, which is not "
                f"recognized as an available DPF ServerContext type. \n"
                f"Accepted values are: {[t.name.upper() for t in LicensingContextType]}.\n"
                f"Using {LicensingContextType.premium.name.upper()} "
                f"as the default ServerContext type."
            )
        )


def set_default_server_context(context=AvailableServerContexts.premium) -> None:
    """Set this context as default for any new server.

    Also applies it to the global server if it is running as Entry and requested context is Premium.

    The context enables to choose whether DPF capabilities requiring a license checkout are allowed.

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
    if SERVER is not None and context == AvailableServerContexts.premium:
        SERVER.apply_context(context)
