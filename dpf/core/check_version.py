"""
Check the matching for a client/server pair. 

Used to verify if the server version is a minimum value. 
"""

from ansys.dpf.core import errors as dpf_errors
import sys

def server_meet_version(required_version, server, msg = None):
    """
    Check if a given server version matches with a required version.
    
    Parameters
    ----------
    required_version : str
        Required version that will be compared with the server version.
    server : Server
        Dpf server object.
    msg : str, optional
        Message to be contained in the raised Exception if versions are
        not meeting.

    Raises
    ------
    dpf_errors : errors
        errors.DpfVersionNotSupported is raised if failure.

    Returns
    -------
    bool : 
        True if the server version meets the requirement.
    """
    version = get_server_version(server)
    meets = version_tuple(required_version)
    if not meets_version(version, meets):
        if msg is not None:
            raise dpf_errors.DpfVersionNotSupported(required_version, msg=msg)
        else: 
            raise dpf_errors.DpfVersionNotSupported(required_version)
    # server meets version if ends here
    return True
            
            
def meets_version(version, meets):
    """
    Check if a version string meets a minimum version.

    Parameters
    ----------
    version : str
        Version to check.
        For example ``'1.32.1'``.
    meets : str
        Required version (version must be compared to it).
        For example ``'1.32.2'``.

    Returns
    -------
    bool :
        True if the server version meets the requirements.
    """
    if not isinstance(version, tuple):
        va = version_tuple(version)
    else:
        va = version
        
    if not isinstance(meets, tuple):
        vb = version_tuple(meets)
    else:
        vb = meets

    if len(va) != len(vb):
        raise ValueError("Versions are not comparable.")

    for i in range(len(va)):
        if va[i] > vb[i]:
            return True
        elif va[i] < vb[i]:
            return False

    return True
            
def get_server_version(server = None):
    """Return server version as a string."""
    from ansys.dpf import core
    if server is None:
        version = core.SERVER.version
    else:
        version = server.version
    return version


def version_tuple(ver):
    """Convert a version string to a tuple containing ints.
    
    Parameters
    ----------
    ver : string
    
    Returns
    -------
    ver_tuple : tuple
        Length 3 tuple representing the major, minor, and patch
        version.
    """
    split_ver = ver.split(".")
    while len(split_ver) < 3:
        split_ver.append('0')

    if len(split_ver) > 3:
        raise ValueError('Version strings containing more than three parts '
                         'cannot be parsed')

    vals = []
    for item in split_ver:
        if item.isnumeric():
            vals.append(int(item))
        else:
            vals.append(0)

    return tuple(vals)

            
def version_requires(min_version):
    """Must be used as decorator. 
    Ensure the method called matches a certain server version."""

    def decorator(func):
        # first arg *must* be a tuple containing the version
        if not isinstance(min_version, str):
            raise TypeError('version_requires decorator must a string with dot separator.')

        def wrapper(self, *args, **kwargs):
            """Call the original function"""
            server = self._server
            func_name = func.__name__
            class_name = self.__class__.__name__
            
            # particular cases
            # scoping._set_ids case, must be checked in a particular way
            if func_name == "_set_ids" and class_name == "Scoping":
                from ansys.dpf.core.misc import DEFAULT_FILE_CHUNK_SIZE
                ids = args[0]
                size = len(ids)
                if size != 0:
                    max_size = DEFAULT_FILE_CHUNK_SIZE//sys.getsizeof(ids[0])
                    if (size > max_size):
                        server.check_version(min_version)
            # default case, just check the compatibility
            else: 
                server.check_version(min_version)

            return func(self, *args, **kwargs)

        return wrapper

    return decorator
    