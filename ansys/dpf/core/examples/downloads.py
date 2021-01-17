"""Download example datasets from https://github.com/pyansys/example-data"""
import shutil
import os
import urllib.request

from ansys.dpf.core import EXAMPLES_PATH
EXAMPLE_REPO = 'https://github.com/pyansys/example-data/raw/master/result_files/'


def delete_downloads():
    """Delete all downloaded examples to free space or update the files"""
    shutil.rmtree(EXAMPLES_PATH)
    os.makedirs(EXAMPLES_PATH)


def _get_file_url(directory, filename):
    return EXAMPLE_REPO + '/'.join([directory, filename])


def _retrieve_file(url, filename, directory):
    """Download a file from a url"""
    # First check if file has already been downloaded
    local_path = os.path.join(EXAMPLES_PATH, directory, os.path.basename(filename))
    local_path_no_zip = local_path.replace('.zip', '')
    if os.path.isfile(local_path_no_zip) or os.path.isdir(local_path_no_zip):
        return local_path_no_zip

    # grab the correct url retriever
    urlretrieve = urllib.request.urlretrieve

    dirpath = os.path.dirname(local_path)
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

    # Perform download
    _, resp = urlretrieve(url, local_path)
    return local_path


def _download_file(directory, filename):
    url = _get_file_url(directory, filename)
    local_path = _retrieve_file(url, filename, directory)

    if os.environ.get('DPF_DOCKER', False):  # pragma: no cover
        # override path if running on docker as path must be relative
        # to docker mount
        #
        # Assumes the following mapping in docker
        # DWN_CSH=/tmp/dpf_cache
        # -v $DWN_CSH:/dpf/_cache
        local_path = os.path.join('/dpf/_cache', directory, filename)
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
    return _download_file('transient', 'transient.rst')


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
    return _download_file('testing', 'allKindOfComplexity.rst')


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
    >>> path = examples.download_all_kinds_of_complexity_modal
    >>> path
    'C:/Users/user/AppData/local/temp/modal_allKindOfComplexity.rst'

    """
    return _download_file('testing', 'modal_allKindOfComplexity.rst')


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
    >>> path = examples.download_all_kinds_of_complexity_modal
    >>> path
    'C:/Users/user/AppData/local/temp/modal_allKindOfComplexity.rst'

    """
    return _download_file('docs', 'pontoon.rst')
