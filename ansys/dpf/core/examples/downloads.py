"""Download example datasets from https://github.com/pyansys/example-data"""
import shutil
import os
import urllib.request


EXAMPLE_REPO = "https://github.com/pyansys/example-data/raw/master/result_files/"


def delete_downloads():
    """Delete all downloaded examples to free space or update the files"""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH
    shutil.rmtree(LOCAL_DOWNLOADED_EXAMPLES_PATH)
    os.makedirs(LOCAL_DOWNLOADED_EXAMPLES_PATH)


def _get_file_url(directory, filename):
    return EXAMPLE_REPO + "/".join([directory, filename])


def _retrieve_file(url, filename, directory):
    """Download a file from a url"""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH, path_utilities

    # First check if file has already been downloaded
    local_path = os.path.join(LOCAL_DOWNLOADED_EXAMPLES_PATH, directory, os.path.basename(filename))
    local_path_no_zip = local_path.replace(".zip", "")
    if os.path.isfile(local_path_no_zip) or os.path.isdir(local_path_no_zip):
        return path_utilities.to_server_os(local_path_no_zip.replace(
            LOCAL_DOWNLOADED_EXAMPLES_PATH,
            path_utilities.downloaded_example_path()))

    # grab the correct url retriever
    urlretrieve = urllib.request.urlretrieve

    dirpath = os.path.dirname(local_path)
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

    # Perform download
    _, resp = urlretrieve(url, local_path)
    return path_utilities.to_server_os(local_path.replace(
        LOCAL_DOWNLOADED_EXAMPLES_PATH,
        path_utilities.downloaded_example_path()))


def _download_file(directory, filename):
    url = _get_file_url(directory, filename)
    local_path = _retrieve_file(url, filename, directory)
    return local_path


###############################################################################
# front-facing functions


def download_transient_result() -> str:
    """Download an example transient result file and return the download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.transient_result
    >>> path
    'C:/Users/user/AppData/local/temp/transient.rst'

    """
    return _download_file("transient", "transient.rst")


def download_all_kinds_of_complexity() -> str:
    """Download an example static result and return the download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Returns
    -------
    str
        Path to the example file.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_all_kinds_of_complexity
    >>> path
    'C:/Users/user/AppData/local/temp/allKindOfComplexity.rst'

    """
    return _download_file("testing", "allKindOfComplexity.rst")


def download_all_kinds_of_complexity_modal() -> str:
    """Download an example result file from a static modal analysis and
    return the download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    return _download_file("testing", "modal_allKindOfComplexity.rst")


def download_pontoon() -> str:
    """Download an example result file from a static modal analsys and
    return the download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    return _download_file("docs", "pontoon.rst")


def download_multi_harmonic_result() -> str:
    """Download an example multi-harmonic result file and return the
    download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    return _download_file("harmonic", "file_harmonic_5rpms.rst")


def download_multi_stage_cyclic_result() -> str:
    """Download an example multi stage result file and return the
    download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    return _download_file("multistage", "multistage.rst")


def download_sub_file() -> str:
    """Download an example .sub result file containing matrices and return the
    download path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
    return _download_file("sub", "cp56.sub")


def download_msup_files_to_dict() -> dict:
    """Download all the files necessary for a msup expansion and return the
    download paths into a dictionnary extension->path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
        "rfrq": _download_file("msup", "file.rfrq"),
        "mode": _download_file("msup", "file.mode"),
        "rst": _download_file("msup", "file.rst"),
    }


def download_distributed_files() -> dict:
    """Download distributed rst files and return the
    download paths into a dictionnary domain id->path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
        0: _download_file("distributed", "file0.rst"),
        1: _download_file("distributed", "file1.rst"),
    }


def download_fluent_files() -> dict:
    """Download the cas and dat file of a fluent analysis and return the
    download paths into a dictionnary extension->path.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

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
        "cas": _download_file("fluent", "FFF.cas.h5"),
        "dat": _download_file("fluent", "FFF.dat.h5"),
    }


def download_extrapolation_3d_result() -> dict:
    """Download example static results of reference and integrated points
    for extrapolation of 3d-element and return return the dictionary of 2 download paths.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Returns
    -------
    dict
        containing path to the example file of ref and path to the example
        file of integrated points.

    Examples
    --------
    Download 2 example result files and return the dictionary containing 2 files

    >>> from ansys.dpf.core import examples
    >>> dict = examples.download_extrapolation_ref_result
    >>> dict
    {
        'file_ref': 'C:/Users/user/AppData/local/temp/file_ref.rst',
        'file_integrated': 'C:/Users/user/AppData/local/temp/file.rst'
    }

    """
    dict = {
        "file_ref": _download_file("extrapolate", "file_ref.rst"),
        "file_integrated": _download_file("extrapolate", "file.rst"),
    }

    return dict


def download_extrapolation_2d_result() -> dict:
    """Download example static results of reference and integrated points
    for extrapolation of 2d-element and return the dictionary of 2 download paths.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Returns
    -------
    dict
        Contains path to the example file of ref and path to the example
        file of integrated points.

     Examples
    --------
    Download 2 example result files and return the dictionary containing 2 files

    >>> from ansys.dpf.core import examples
    >>> dict = examples.download_extrapolation_ref_result
    >>> dict
    {
        'file_ref': 'C:/Users/user/AppData/local/temp/extrapolate_2d_ref.rst',
        'file_integrated': 'C:/Users/user/AppData/local/temp/extrapolate_2d.rst'
    }

    """
    dict = {
        "file_ref": _download_file("extrapolate", "extrapolate_2d_ref.rst"),
        "file_integrated": _download_file("extrapolate", "extrapolate_2d.rst"),
    }

    return dict
