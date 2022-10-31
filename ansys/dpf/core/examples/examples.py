"""
.. _ref_examples:

Result Files Examples
=====================
Examples result files.
"""

import os
import inspect

from ansys.dpf.core import server as server_module
from ansys.dpf.core.core import upload_file_in_tmp_folder
from ansys.dpf.core import path_utilities

if os.environ.get("DPF_DOCKER", "").lower() == "true":
    # must pass a path that can be accessed by a docker image with
    # this directory mounted at the repository level for CI
    _module_path = r"/dpf/ansys/dpf/core/examples/"
else:
    _module_path = os.path.dirname(inspect.getfile(inspect.currentframe()))

# this files can be imported with from `ansys.dpf.core import examples`:
simple_bar = os.path.join(_module_path, "ASimpleBar.rst")
static_rst = os.path.join(_module_path, "static.rst")
complex_rst = os.path.join(_module_path, "complex.rst")
multishells_rst = os.path.join(_module_path, "model_with_ns.rst")
electric_therm = os.path.join(_module_path, "rth", "rth_electric.rth")
steady_therm = os.path.join(_module_path, "rth", "rth_steady.rth")
transient_therm = os.path.join(_module_path, "rth", "rth_transient.rth")
msup_transient = os.path.join(_module_path, "msup_transient_plate1.rst")
simple_cyclic = os.path.join(_module_path, "file_cyclic.rst")
distributed_msup_folder = os.path.join(_module_path, 'msup_distributed')


def find_files(local_path, should_upload=True, server=None, return_local_path=False):
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    local_path : str
        File path to make available server side.
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.
    """
    if return_local_path:
        return local_path
    if should_upload:
        server = server_module.get_or_create_server(server)
        if not server.local_server and not server.docker_config.use_docker:
            return upload_file_in_tmp_folder(local_path, server=server)

    return path_utilities.to_server_os(local_path, server)


def find_simple_bar(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_simple_bar()
    >>> path
    'C:/Users/user/AppData/local/temp/ASimpleBar.rst'

    """
    return find_files(simple_bar, should_upload, server, return_local_path)


def find_static_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_static_rst()
    >>> path
    'C:/Users/user/AppData/local/temp/static.rst'

    """
    return find_files(static_rst, should_upload, server, return_local_path)


def find_complex_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_complex_rst()
    >>> path
    'C:/Users/user/AppData/local/temp/complex.rst'

    """
    return find_files(complex_rst, should_upload, server, return_local_path)


def find_multishells_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_multishells_rst()
    >>> path
    'C:/Users/user/AppData/local/temp/model_with_ns.rst'

    """
    return find_files(multishells_rst, should_upload, server, return_local_path)


def find_electric_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_electric_therm()
    >>> path
    'C:/Users/user/AppData/local/temp/rth_electric.rth'

    """
    return find_files(electric_therm, should_upload, server, return_local_path)


def find_steady_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_steady_therm()
    >>> path
    'C:/Users/user/AppData/local/temp/rth_steady.rst'

    """
    return find_files(steady_therm, should_upload, server, return_local_path)


def find_transient_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_transient_therm()
    >>> path
    'C:/Users/user/AppData/local/temp/rth_transient.rst'

    """
    return find_files(transient_therm, should_upload, server, return_local_path)


def find_msup_transient(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_msup_transient()
    >>> path
    'C:/Users/user/AppData/local/temp/msup_transient_plate1.rst'

    """
    return find_files(msup_transient, should_upload, server, return_local_path)


def find_simple_cyclic(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_simple_cyclic()
    >>> path
    'C:/Users/user/AppData/local/temp/file_cyclic.rst'

    """
    return find_files(simple_cyclic, should_upload, server, return_local_path)


def find_distributed_msup_folder(
        should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Make the result file available server side, if the server is remote the file is uploaded
    server side. Returns the path on the file.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded server side when the server is remote.
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path: bool, optional
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> path = examples.find_distributed_msup_folder()
    >>> path
    'C:/Users/user/AppData/local/temp/msup_distributed'

    """
    return find_files(distributed_msup_folder, should_upload, server, return_local_path)
