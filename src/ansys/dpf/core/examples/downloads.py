"""
Downloads
=========
Download example datasets from https://github.com/pyansys/example-data"""
import os
import urllib.request
import warnings
from ansys.dpf.core.examples.examples import find_files

EXAMPLE_REPO = "https://github.com/pyansys/example-data/raw/master/result_files/"


def delete_downloads():
    """Delete all downloaded examples to free space or update the files"""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH, examples
    not_to_remove = [getattr(examples.examples, item) for item in dir(examples.examples) if
                     not item.startswith("_") and not item.endswith("_") and isinstance(
                         getattr(examples.examples, item), str)]
    not_to_remove.extend([os.path.join(os.path.dirname(examples.__file__), "__init__.py"),
                          os.path.join(os.path.dirname(examples.__file__), "downloads.py"),
                          os.path.join(os.path.dirname(examples.__file__), "examples.py")])
    for root, dirs, files in os.walk(LOCAL_DOWNLOADED_EXAMPLES_PATH, topdown=False):
        if root not in not_to_remove:
            for name in files:
                if not os.path.join(root, name) in not_to_remove:
                    try:
                        os.remove(os.path.join(root, name))
                        print(f"deleting {os.path.join(root, name)}")
                    except Exception as e:
                        warnings.warn(
                            f"couldn't delete {os.path.join(root, name)} with error:\n {e.args}"
                        )
    for root, dirs, files in os.walk(LOCAL_DOWNLOADED_EXAMPLES_PATH, topdown=False):
        if len(dirs) == 0 and len(files) == 0:
            try:
                os.rmdir(root)
                print(f"deleting {root}")
            except Exception as e:
                warnings.warn(f"couldn't delete {root} with error:\n {e.args}")


def _get_file_url(directory, filename):
    return EXAMPLE_REPO + "/".join([directory, filename])


def _retrieve_file(url, filename, directory):
    """Download a file from a url"""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH
    # First check if file has already been downloaded
    local_path = os.path.join(LOCAL_DOWNLOADED_EXAMPLES_PATH, directory,
                              os.path.basename(filename))
    local_path_no_zip = local_path.replace(".zip", "")
    if os.path.isfile(local_path_no_zip) or os.path.isdir(local_path_no_zip):
        return local_path_no_zip

    # grab the correct url retriever
    urlretrieve = urllib.request.urlretrieve

    dirpath = os.path.dirname(local_path)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath, exist_ok=True)

    # Perform download
    _, resp = urlretrieve(url, local_path)
    return local_path


def _download_file(directory, filename, should_upload: bool, server, return_local_path):
    url = _get_file_url(directory, filename)
    local_path = _retrieve_file(url, filename, directory)
    return find_files(local_path, should_upload, server, return_local_path)


###############################################################################
# front-facing functions


def download_transient_result(should_upload: bool = True, server=None,
                              return_local_path=False) -> str:
    """Download an example transient result file and return the download path
    available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_transient_result()
    >>> path
    'C:/Users/user/AppData/local/temp/transient.rst'

    """
    return _download_file("transient", "transient.rst", should_upload, server, return_local_path)


def download_all_kinds_of_complexity(should_upload: bool = True, server=None
                                     , return_local_path=False) -> str:
    """Download an example static result and return the download path
    available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_all_kinds_of_complexity()
    >>> path
    'C:/Users/user/AppData/local/temp/allKindOfComplexity.rst'

    """
    return _download_file("testing", "allKindOfComplexity.rst", should_upload, server,
                          return_local_path)


def download_all_kinds_of_complexity_modal(should_upload: bool = True, server=None,
                                           return_local_path=False) -> str:
    """Download an example result file from a static modal analysis and
    return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_all_kinds_of_complexity_modal()
    >>> path
    'C:/Users/user/AppData/local/temp/modal_allKindOfComplexity.rst'

    """
    return _download_file("testing", "modal_allKindOfComplexity.rst", should_upload, server,
                          return_local_path)


def download_pontoon(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a static modal analsys and
    return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_pontoon()
    >>> path
    'C:/Users/user/AppData/local/temp/pontoon.rst'

    """
    return _download_file("docs", "pontoon.rst", should_upload, server, return_local_path)


def download_multi_harmonic_result(should_upload: bool = True, server=None,
                                   return_local_path=False) -> str:
    """Download an example multi-harmonic result file and return the
    download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_multi_harmonic_result()
    >>> path
    'C:/Users/user/AppData/local/temp/file_harmonic_5rpms.rst'
    """
    return _download_file("harmonic", "file_harmonic_5rpms.rst", should_upload, server,
                          return_local_path)


def download_multi_stage_cyclic_result(should_upload: bool = True, server=None,
                                       return_local_path=False) -> str:
    """Download an example multi stage result file and return the
    download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_multi_stage_cyclic_result()
    >>> path
    'C:/Users/user/AppData/local/temp/multistage.rst'

    """
    return _download_file("multistage", "multistage.rst", should_upload, server, return_local_path)


def download_sub_file(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example .sub result file containing matrices and return the
    download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_sub_file()
    >>> path
    'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\sub\\cp56.sub'

    """
    return _download_file("sub", "cp56.sub", should_upload, server, return_local_path)


def download_msup_files_to_dict(should_upload: bool = True, server=None,
                                return_local_path=False) -> dict:
    """Download all the files necessary for a msup expansion and return the
    download paths available server side into a dictionary extension->path.
    If the server is remote (or doesn't share the memory), the files are uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    dict[str:str]
        Path to the example files.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> paths = examples.download_msup_files_to_dict()
    >>> paths
    {'rfrq': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\msup\\file.rfrq',
     'mode': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\msup\\file.mode',
     'rst': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\msup\\file.rst'} # noqa: E501

    """
    return {
        "rfrq": _download_file("msup", "file.rfrq", should_upload, server, return_local_path),
        "mode": _download_file("msup", "file.mode", should_upload, server, return_local_path),
        "rst": _download_file("msup", "file.rst", should_upload, server, return_local_path),
    }


def download_distributed_files(should_upload: bool = True, server=None,
                               return_local_path=False) -> dict:
    """Download distributed rst files and return the
    download paths into a dictionary domain id->path.
    If the server is remote (or doesn't share the memory), the files are uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    dict[int:str]
        Path to the example files.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> paths = examples.download_distributed_files()
    >>> paths
    {0: 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\distributed\\file0.rst',
     1: 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\distributed\\file1.rst'} # noqa: E501

    """
    return {
        0: _download_file("distributed", "file0.rst", should_upload, server, return_local_path),
        1: _download_file("distributed", "file1.rst", should_upload, server, return_local_path),
    }


def download_fluent_files(should_upload: bool = True, server=None, return_local_path=False) -> dict:
    """Download the cas and dat file of a fluent analysis and return the
    download paths into a dictionary extension->path.
    If the server is remote (or doesn't share the memory), the files are uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    dict[str:str]
        Path to the example files.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> paths = examples.download_fluent_files()
    >>> paths
    {'cas': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent\\FFF.cas.h5',
     'dat': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent\\FFF.dat.h5'} # noqa: E501

    """
    return {
        "cas": _download_file("fluent", "FFF.cas.h5", should_upload, server, return_local_path),
        "dat": _download_file("fluent", "FFF.dat.h5", should_upload, server, return_local_path),
    }


def download_extrapolation_3d_result(should_upload: bool = True, server=None,
                                     return_local_path=False) -> dict:
    """Download example static results of reference and integrated points
    for extrapolation of 3d-element and return return the dictionary of 2 download paths.
    If the server is remote (or doesn't share the memory), the files are uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    dict
        containing path to the example file of ref and path to the example
        file of integrated points.

    Examples
    --------
    Download 2 example result files and return the dictionary containing 2 files

    >>> from ansys.dpf.core import examples
    >>> path_dict = examples.download_extrapolation_ref_result()
    >>> path_dict
    {
        'file_ref': 'C:/Users/user/AppData/local/temp/file_ref.rst',
        'file_integrated': 'C:/Users/user/AppData/local/temp/file.rst'
    }

    """
    path_dict = {
        "file_ref": _download_file("extrapolate", "file_ref.rst", should_upload, server,
                                   return_local_path),
        "file_integrated": _download_file("extrapolate", "file.rst", should_upload, server,
                                          return_local_path),
    }

    return path_dict


def download_extrapolation_2d_result(should_upload: bool = True, server=None,
                                     return_local_path=False) -> dict:
    """Download example static results of reference and integrated points
    for extrapolation of 2d-element and return the dictionary of 2 download paths.
    If the server is remote (or doesn't share the memory), the files are uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    dict
        Contains path to the example file of ref and path to the example
        file of integrated points.

    Examples
    --------
    Download 2 example result files and return the dictionary containing 2 files

    >>> from ansys.dpf.core import examples
    >>> path_dict = examples.download_extrapolation_ref_result()
    >>> path_dict
    {
        'file_ref': 'C:/Users/user/AppData/local/temp/extrapolate_2d_ref.rst',
        'file_integrated': 'C:/Users/user/AppData/local/temp/extrapolate_2d.rst'
    }

    """
    path_dict = {
        "file_ref": _download_file("extrapolate", "extrapolate_2d_ref.rst", should_upload, server,
                                   return_local_path),
        "file_integrated": _download_file("extrapolate", "extrapolate_2d.rst",
                                          should_upload, server, return_local_path),
    }

    return path_dict


def download_hemisphere(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a static analysis and
    return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_hemisphere()
    >>> path
    'C:/Users/user/AppData/local/temp/hemisphere.rst'

    """
    return _download_file("hemisphere", "hemisphere.rst", should_upload, server, return_local_path)


def download_example_asme_result(should_upload: bool = True, server=None,
                                 return_local_path=False) -> str:
    """Download an example result file from a static analysis and
    return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file
    >>> from ansys.dpf.core import examples
    >>> path = examples.download_example_asme_result()
    >>> path
    'C:/Users/user/AppData/local/temp/asme_example.rst'
    """
    return _download_file("postprocessing", "asme_example.rst", should_upload, server,
                          return_local_path)


def download_crankshaft(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a crankshaft
    under load and return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_crankshaft()
    >>> path
    'C:/Users/user/AppData/local/temp/crankshaft.rst'

    """
    return _download_file("crankshaft", "crankshaft.rst", should_upload, server, return_local_path)


def download_piston_rod(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a piston rod
    under load and return the download path available server side.
    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_piston_rod()
    >>> path
    'C:/Users/user/AppData/local/temp/piston_rod.rst'

    """
    return _download_file("piston_rod", "piston_rod.rst", should_upload, server, return_local_path)
