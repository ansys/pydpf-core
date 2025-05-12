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
Check the matching for a client/server pair.

Used to verify if the server version is a minimum value.
"""

from __future__ import annotations

from functools import wraps
import sys
import weakref

from ansys.dpf.core import errors as dpf_errors


def server_meet_version(required_version, server: BaseServer):
    """Check if a given server version matches with a required version.

    Parameters
    ----------
    required_version : str
        Required version to compare with the server version.
    server : :class:`ansys.dpf.core.server_types.BaseServer`
        DPF server object.

    Returns
    -------
    bool
        ``True`` when successful, ``False`` when failed.
    """
    return server.meet_version(required_version)


def server_meet_version_and_raise(required_version, server, msg=None):
    """Check if a given server version matches with a required version and raise an exception if it does not match.

    Parameters
    ----------
    required_version : str
        Required version to compare with the server version.
    server : :class:`dpf.core.server_types.BaseServer`
        DPF server object.
    msg : str, optional
        Message contained in the raised exception if the versions do
        not match. The default is ``None``, in which case the default message
        is used.

    Raises
    ------
    dpf_errors : errors
        errors.DpfVersionNotSupported is raised if the versions do not match.

    Returns
    -------
    bool
        ``True`` when successful, ``False`` when failed.
    """
    if not server_meet_version(required_version, server):
        if msg is not None:
            raise dpf_errors.DpfVersionNotSupported(required_version, msg=msg)
        else:
            raise dpf_errors.DpfVersionNotSupported(required_version)
    # server meets version if ends here
    return True


def meets_version(version, meets):
    """Check if a version string meets a minimum version.

    Parameters
    ----------
    version : str
        Version string to check. For example, ``"1.32.1"``.
    meets : str
        Required version for comparison. For example, ``"1.32.2"``.

    Returns
    -------
    bool
         ``True`` when successful, ``False`` when failed.
    """
    from packaging.version import parse

    return parse(version) >= parse(meets)


def get_server_version(server=None):
    """Retrieve the server version as a string.

    Parameters
    ----------
    server : :class:`ansys.dpf.core.server`, optional
        DPF server object. The default is ``None``.

    Returns
    -------
    str
        Server version.
    """
    if server is None:
        from ansys.dpf.core import SERVER  # to keep here, cannot import in __del__

        version = SERVER.version
    else:
        version = server.version
    return version


def version_requires(min_version):
    """Check that the method being called matches a certain server version.

    .. note::
       The method must be used as a decorator.
    """

    def decorator(func):
        # first arg *must* be a tuple containing the version
        if not isinstance(min_version, str):
            raise TypeError("version_requires decorator must be a string with a dot separator.")

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """Call the original function."""
            if isinstance(self._server, weakref.ref):
                server = self._server()
            else:
                server = self._server
            func_name = func.__name__

            # particular cases
            # scoping._set_ids case, must be checked in a particular way
            from ansys.dpf.core import scoping

            if func_name == "_set_ids" and isinstance(self, scoping.Scoping):
                ids = args[0]
                size = len(ids)
                if size != 0:
                    max_size = 8.0e6 // sys.getsizeof(ids[0])
                    if size > max_size:
                        server.check_version(min_version, " called from " + func.__name__)
            # default case, just check the compatibility
            else:
                server.check_version(min_version, " called from " + func.__name__)

            return func(self, *args, **kwargs)

        return wrapper

    return decorator
