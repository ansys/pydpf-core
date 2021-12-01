from ansys.dpf import core


def join(left_path, right_path, server=None):
    """Join two strings to form a path, following the server
    architecture.
    Using a server version below 3.0, please ensure that the
    python client and the server's os are similar before
    using this method.

    Parameters
    ----------
    left_path : str
        Left part of the final requested path.

    right_path : str
        Right path of the final requested path.

    server : Server
        Specific server to use.

    Returns
    -------
    concatenated_file_path : str
        left_path + right_path concatenated into a single string value.

    """
    if not server:
        server = core.SERVER
    if not server:
        raise RuntimeError("A server must be connected to use this method.")

    os_info = server.os
    separator = "\\"
    if os_info == 'posix':
        separator = "/"

    path_to_return = left_path + separator + right_path
    return path_to_return
