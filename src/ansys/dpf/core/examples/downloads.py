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
Downloads.

Download example datasets from https://github.com/ansys/example-data
"""

import os
from pathlib import Path
from typing import Union
import urllib.request
import warnings

from ansys.dpf.core.examples.examples import find_files

EXAMPLE_REPO = "https://github.com/ansys/example-data/raw/master/"

GITHUB_SOURCE_URL = (
    "https://github.com/ansys/pydpf-core/raw/"
    "master/doc/source/examples/07-python-operators/plugins/"
)


def delete_downloads(verbose=True):
    """Delete all downloaded examples to free space or update the files."""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH, examples

    not_to_remove = [
        Path(getattr(examples.examples, item))
        for item in dir(examples.examples)
        if not item.startswith("_")
        and not item.endswith("_")
        and isinstance(getattr(examples.examples, item), str)
    ]
    not_to_remove.extend(
        [
            Path(examples.__file__).parent / "__init__.py",
            Path(examples.__file__).parent / "downloads.py",
            Path(examples.__file__).parent / "examples.py",
        ]
    )
    for root, dirs, files in os.walk(LOCAL_DOWNLOADED_EXAMPLES_PATH, topdown=False):
        root = Path(root)
        if root not in not_to_remove:
            for name in files:
                file_path = root / name
                if not file_path in not_to_remove:
                    try:
                        file_path.unlink()
                        if verbose:
                            print(f"deleting {file_path}")
                    except Exception as e:
                        warnings.warn(f"couldn't delete {file_path} with error:\n {e.args}")
    for root, dirs, files in os.walk(LOCAL_DOWNLOADED_EXAMPLES_PATH, topdown=False):
        if len(dirs) == 0 and len(files) == 0:
            try:
                root = Path(root)
                root.rmdir()
                if verbose:
                    print(f"deleting {root}")
            except Exception as e:
                warnings.warn(f"couldn't delete {root} with error:\n {e.args}")


def _get_file_url(directory, filename):
    return EXAMPLE_REPO + "/".join([directory, filename])


def _retrieve_file(url, filename, directory):
    """Download a file from a url."""
    from ansys.dpf.core import LOCAL_DOWNLOADED_EXAMPLES_PATH

    # First check if file has already been downloaded
    local_examples_download_path = Path(LOCAL_DOWNLOADED_EXAMPLES_PATH)
    local_path = local_examples_download_path / directory / filename
    local_path_no_zip = Path(str(local_path).replace(".zip", ""))
    if local_path_no_zip.is_file() or local_path_no_zip.is_dir():
        return str(local_path_no_zip)

    # grab the correct url retriever
    urlretrieve = urllib.request.urlretrieve

    dirpath = local_path.parent
    if not dirpath.is_dir():
        dirpath.mkdir(parents=True, exist_ok=True)

    # Perform download
    _, resp = urlretrieve(url, local_path)
    return str(local_path)


def _download_file(directory, filename, should_upload: bool, server, return_local_path):
    url = _get_file_url(directory, filename)
    local_path = _retrieve_file(url, filename, directory)
    return find_files(local_path, should_upload, server, return_local_path)


###############################################################################
# front-facing functions


def download_transient_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example transient result file and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/transient", "transient.rst", should_upload, server, return_local_path
    )


def download_all_kinds_of_complexity(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example static result and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/testing", "allKindOfComplexity.rst", should_upload, server, return_local_path
    )


def download_all_kinds_of_complexity_modal(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example result file from a static modal analysis and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/testing",
        "modal_allKindOfComplexity.rst",
        should_upload,
        server,
        return_local_path,
    )


def download_pontoon(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a static modal analsys and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/docs", "pontoon.rst", should_upload, server, return_local_path
    )


def download_multi_harmonic_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example multi-harmonic result file and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/harmonic", "file_harmonic_5rpms.rst", should_upload, server, return_local_path
    )


def download_multi_stage_cyclic_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example multi-stage result file and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/multistage", "multistage.rst", should_upload, server, return_local_path
    )


def download_sub_file(should_upload: bool = True, server=None, return_local_path=False) -> str:
    r"""Download an example .sub result file containing matrices and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file("result_files/sub", "cp56.sub", should_upload, server, return_local_path)


def download_msup_files_to_dict(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download necessary files for an msup expansion and return a dictionary mapping each file extension to its server-side download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
        "rfrq": _download_file(
            "result_files/msup", "file.rfrq", should_upload, server, return_local_path
        ),
        "mode": _download_file(
            "result_files/msup", "file.mode", should_upload, server, return_local_path
        ),
        "rst": _download_file(
            "result_files/msup", "file.rst", should_upload, server, return_local_path
        ),
    }


def download_distributed_files(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download distributed rst files and return the download paths into a dictionary domain id->path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
        0: _download_file(
            "result_files/distributed", "file0.rst", should_upload, server, return_local_path
        ),
        1: _download_file(
            "result_files/distributed", "file1.rst", should_upload, server, return_local_path
        ),
    }


def download_fluent_multi_species(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""
    Download the cas and dat files from a multiple species Fluent analysis and return a dictionary of file extensions to download paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_fluent_multi_species()
    >>> paths
    {'cas': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-multi_species\\FFF.cas.h5',
     'dat': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-multi_species\\FFF.dat.h5'} # noqa: E501

    """
    return {
        "cas": _download_file(
            "result_files/fluent-multi_species",
            "FFF.cas.h5",
            should_upload,
            server,
            return_local_path,
        ),
        "dat": _download_file(
            "result_files/fluent-multi_species",
            "FFF.dat.h5",
            should_upload,
            server,
            return_local_path,
        ),
    }


def download_fluent_multi_phase(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""
    Download the cas and dat files from a multiple phases Fluent analysis and return a dictionary of file extensions to download paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_fluent_multi_phase()
    >>> paths
    {'cas': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-multi_phase\\fluentMultiphase.cas.h5',
     'dat': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-multi_phase\\fluentMultiphase.dat.h5'} # noqa: E501

    """
    return {
        "cas": _download_file(
            "result_files/fluent-multi_phase",
            "fluentMultiphase.cas.h5",
            should_upload,
            server,
            return_local_path,
        ),
        "dat": _download_file(
            "result_files/fluent-multi_phase",
            "fluentMultiphase.dat.h5",
            should_upload,
            server,
            return_local_path,
        ),
    }


def download_extrapolation_3d_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    """Download example static results for extrapolation and return a dictionary of two download paths.

    Download example static results of reference and integrated points
    for extrapolation of 3d-element and return the dictionary of 2 download paths.
    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
        "file_ref": _download_file(
            "result_files/extrapolate", "file_ref.rst", should_upload, server, return_local_path
        ),
        "file_integrated": _download_file(
            "result_files/extrapolate", "file.rst", should_upload, server, return_local_path
        ),
    }

    return path_dict


def download_extrapolation_2d_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    """Download 2D extrapolation results and return two server-side paths.

    Download example static results of reference and integrated points
    for extrapolation of 2d-element and return the dictionary of 2 download paths.
    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
        "file_ref": _download_file(
            "result_files/extrapolate",
            "extrapolate_2d_ref.rst",
            should_upload,
            server,
            return_local_path,
        ),
        "file_integrated": _download_file(
            "result_files/extrapolate",
            "extrapolate_2d.rst",
            should_upload,
            server,
            return_local_path,
        ),
    }

    return path_dict


def download_hemisphere(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a static analysis and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/hemisphere", "hemisphere.rst", should_upload, server, return_local_path
    )


def download_example_asme_result(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example result file from a static analysis and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/postprocessing", "asme_example.rst", should_upload, server, return_local_path
    )


def download_crankshaft(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a crankshaft under load and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/crankshaft", "crankshaft.rst", should_upload, server, return_local_path
    )


def download_piston_rod(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a piston rod under load and return the download path available server side.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    return _download_file(
        "result_files/piston_rod", "piston_rod.rst", should_upload, server, return_local_path
    )


def download_d3plot_beam(should_upload: bool = True, server=None, return_local_path=False) -> list:
    """Download the result file of an example of a d3plot file with beam elements and return the download paths available on the server side.

    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    on the server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded to the server side when the server is remote.
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
    Download an example result file and return the path of the files.

    >>> from ansys.dpf.core import examples
    >>> paths = examples.download_d3plot_beam()
    >>> paths
    ['C:/Users/user/AppData/local/temp/d3plot',
     'C:/Users/user/AppData/local/temp/d3plot01',
     'C:/Users/user/AppData/local/temp/d3plot02'
     'C:/Users/user/AppData/local/temp/file.actunits']

    """
    return [
        _download_file(
            "result_files/d3plot_beam", "d3plot", should_upload, server, return_local_path
        ),
        _download_file(
            "result_files/d3plot_beam", "d3plot01", should_upload, server, return_local_path
        ),
        _download_file(
            "result_files/d3plot_beam", "d3plot02", should_upload, server, return_local_path
        ),
        _download_file(
            "result_files/d3plot_beam", "file.actunits", should_upload, server, return_local_path
        ),
    ]


def download_binout_matsum(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a binout file with matsum branch and return the download path available on the server side.

    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    on the server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded to the server side when the server is remote.
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
    Download an example result file and return the path of the file.

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_binout_matsum()
    >>> path
    'C:/Users/user/AppData/local/temp/binout_matsum'

    """
    return _download_file(
        "result_files/binout", "binout_matsum", should_upload, server, return_local_path
    )


def download_binout_glstat(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download the result file of an example of a binout file with glstat branch and return the download path available on the server side.

    If the server is remote (or doesn't share the memory), the file is uploaded or made available
    on the server side.

    Examples files are downloaded to a persistent cache to avoid
    re-downloading the same file twice.

    Parameters
    ----------
    should_upload : bool, optional (default True)
        Whether the file should be uploaded to the server side when the server is remote.
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
    Download an example result file and return the path of the file.

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_binout_glstat()
    >>> path
    'C:/Users/user/AppData/local/temp/binout_glstat'

    """
    return _download_file(
        "result_files/binout", "binout_glstat", should_upload, server, return_local_path
    )


def download_cycles_to_failure(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example result file from a cyclic analysis and return the download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> path = examples.download_cycles_to_failure()
    >>> path
    'C:/Users/user/AppData/local/temp/cycles_to_failure.rst'

    """
    return _download_file(
        "result_files/cyclic", "cyclic_to_failure.rst", should_upload, server, return_local_path
    )


def download_modal_frame(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a modal analysis on a frame and return the download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> path = examples.download_modal_frame()

    """
    return _download_file(
        "result_files/modal", "frame.rst", should_upload, server, return_local_path
    )


def download_harmonic_clamped_pipe(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Download an example result file from a harmonic analysis on a clamped pipe and return the download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> path = examples.download_modal_frame()

    """
    return _download_file(
        "result_files/harmonic", "clamped_pipe.rst", should_upload, server, return_local_path
    )


def download_modal_cyclic(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Download an example result file from a cyclic modal analysis and return the download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> path = examples.download_modal_cyclic()

    """
    return _download_file(
        "result_files/cyclic", "modal_cyclic.rst", should_upload, server, return_local_path
    )


def download_fluent_axial_comp(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download flprj, cas, and dat files of an axial compressor sector analysis and return a dictionary of file extensions to paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_fluent_axial_comp()
    >>> paths
    {'flprj': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp_reduced.flprj',
     'cas': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01438.cas.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01439.cas.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01440.cas.h5',
     ],
     'dat': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01438.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01439.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-axial_comp\\axial_comp-1-01440.dat.h5',
     ]}

    """
    return {
        "flprj": _download_file(
            "result_files/fluent-axial_comp",
            "axial_comp_reduced.flprj",
            should_upload,
            server,
            return_local_path,
        ),
        "cas": [
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01438.cas.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01439.cas.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01440.cas.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
        "dat": [
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01438.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01439.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-axial_comp",
                "axial_comp-1-01440.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
    }


def download_fluent_mixing_elbow_steady_state(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download the flprj, cas, and dat files of a steady-state mixing elbow analysis and return a dictionary mapping extensions to paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_fluent_mixing_elbow_steady_state()
    >>> paths
    {'flprj': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow.flprj',
     'cas': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2.cas.h5',
     ],
     'dat': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00005.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00010.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00015.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00020.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00025.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00030.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00035.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00040.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00045.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_steady-state\\elbow-2-00050.dat.h5',
     ]} # noqa: E501

    """
    return {
        "flprj": _download_file(
            "result_files/fluent-mixing_elbow_steady-state",
            "elbow.flprj",
            should_upload,
            server,
            return_local_path,
        ),
        "cas": [
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2.cas.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
        "dat": [
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00005.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00010.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00015.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00020.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00025.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00030.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00035.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00040.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00045.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_steady-state",
                "elbow-2-00050.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
    }


def download_fluent_mixing_elbow_transient(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download the flprj, cas, and dat files of a transient mixing elbow analysis and return a dictionary mapping extensions to paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_fluent_mixing_elbow_transient()
    >>> paths
    {'flprj': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow.flprj',
     'cas': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2.cas.h5',
     ],
     'dat': [
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2-00001.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2-00002.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2-00003.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2-00004.dat.h5',
       'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\fluent-mixing_elbow_transient\\elbow-2-00005.dat.h5',
     ]}

    """
    return {
        "flprj": _download_file(
            "result_files/fluent-mixing_elbow_transient",
            "elbow.flprj",
            should_upload,
            server,
            return_local_path,
        ),
        "cas": [
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2.cas.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
        "dat": [
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2-00001.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2-00002.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2-00003.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2-00004.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
            _download_file(
                "result_files/fluent-mixing_elbow_transient",
                "elbow-2-00005.dat.h5",
                should_upload,
                server,
                return_local_path,
            ),
        ],
    }


def download_cfx_heating_coil(
    should_upload: bool = True, server=None, return_local_path=False
) -> dict:
    r"""Download the flprj, cas, and dat files of a CFX heating coil analysis and return a dictionary mapping extensions to paths.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    >>> paths = examples.download_cfx_heating_coil()
    >>> paths
    {'cas': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\cfx-heating_coil\\def.cas.cff',
     'dat': 'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\cfx-heating_coil\\def.dat.cff'}

    """
    return {
        "cas": _download_file(
            "result_files/cfx-heating_coil",
            "def.cas.cff",
            should_upload,
            server,
            return_local_path,
        ),
        "dat": _download_file(
            "result_files/cfx-heating_coil",
            "def.dat.cff",
            should_upload,
            server,
            return_local_path,
        ),
    }


def download_cfx_mixing_elbow(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    r"""Download the res file of a CFX analysis of a mixing elbow and return the download path.

    If the server is remote (or doesn't share memory), the file is uploaded or made available
    on the server side.

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
    str:
        Path to the example file.

    Examples
    --------
    Download an example result file and return the path of the file

    >>> from ansys.dpf.core import examples
    >>> path = examples.download_cfx_mixing_elbow()
    >>> path
    'C:\\Users\\user\\AppData\\Local\\ansys-dpf-core\\ansys-dpf-core\\examples\\cfx-mixing_elbow\\InjectMixer.res' # noqa: E501

    """
    return _download_file(
        "result_files/cfx-mixing_elbow",
        "InjectMixer.res",
        should_upload,
        server,
        return_local_path,
    )


def find_simple_bar(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side; if the server is remote, upload the file and return the file path.

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
    return _download_file(
        "result_files", "ASimpleBar.rst", should_upload, server, return_local_path
    )


def find_static_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side; if the server is remote, upload the file and return the file path.

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
    return _download_file("result_files", "static.rst", should_upload, server, return_local_path)


def find_complex_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return the file path.

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
    return _download_file("result_files", "complex.rst", should_upload, server, return_local_path)


def find_multishells_rst(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    return _download_file(
        "result_files", "model_with_ns.rst", should_upload, server, return_local_path
    )


def find_electric_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    return _download_file(
        "result_files/rth", "rth_electric.rth", should_upload, server, return_local_path
    )


def find_steady_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    'C:/Users/user/AppData/local/temp/rth_steady.rth'

    """
    return _download_file(
        "result_files/rth", "rth_steady.rth", should_upload, server, return_local_path
    )


def find_transient_therm(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    'C:/Users/user/AppData/local/temp/rth_transient.rth'

    """
    return _download_file(
        "result_files/rth", "rth_transient.rth", should_upload, server, return_local_path
    )


def find_msup_transient(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    return _download_file(
        "result_files", "msup_transient_plate1.rst", should_upload, server, return_local_path
    )


def find_simple_cyclic(should_upload: bool = True, server=None, return_local_path=False) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    return _download_file(
        "result_files", "file_cyclic.rst", should_upload, server, return_local_path
    )


def find_distributed_msup_folder(
    should_upload: bool = True, server=None, return_local_path=False
) -> str:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

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
    # In this case we return the path to the folder with all the downloaded files
    _download_file(
        "result_files/msup_distributed", "file0.mode", should_upload, server, return_local_path
    )
    _download_file(
        "result_files/msup_distributed", "file0.rst", should_upload, server, return_local_path
    )
    _download_file(
        "result_files/msup_distributed", "file1.mode", should_upload, server, return_local_path
    )
    _download_file(
        "result_files/msup_distributed", "file1.rst", should_upload, server, return_local_path
    )
    _download_file(
        "result_files/msup_distributed",
        "file_load_1.rfrq",
        should_upload,
        server,
        return_local_path,
    )
    path = _download_file(
        "result_files/msup_distributed",
        "file_load_2.rfrq",
        should_upload,
        server,
        return_local_path,
    )
    return str(Path(path).parent)


def download_average_filter_plugin(
    should_upload: bool = True, server=None, return_local_path=False
) -> Union[str, None]:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

    Parameters
    ----------
    should_upload:
        Whether the file should be uploaded server side when the server is remote.
    server:
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path:
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the plugin folder.

    Examples
    --------
    >>> from ansys.dpf.core import examples
    >>> path = examples.download_average_filter_plugin()

    """
    file_list = [
        "average_filter_plugin/__init__.py",
        "average_filter_plugin/operators.py",
        "average_filter_plugin/operators_loader.py",
        "average_filter_plugin/common.py",
    ]
    return _retrieve_plugin(
        file_list=file_list,
        should_upload=should_upload,
        server=server,
        return_local_path=return_local_path,
    )


def download_gltf_plugin(
    should_upload: bool = True, server=None, return_local_path=False
) -> Union[str, None]:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

    Parameters
    ----------
    should_upload:
        Whether the file should be uploaded server side when the server is remote.
    server:
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path:
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the plugin folder.

    Examples
    --------
    >>> from ansys.dpf.core import examples
    >>> path = examples.download_gltf_plugin()

    """
    file_list = [
        "gltf_plugin.xml",
        "gltf_plugin/__init__.py",
        "gltf_plugin/operators.py",
        "gltf_plugin/operators_loader.py",
        "gltf_plugin/requirements.txt",
        "gltf_plugin/gltf_export.py",
        "gltf_plugin/texture.png",
    ]
    return _retrieve_plugin(
        file_list=file_list,
        should_upload=should_upload,
        server=server,
        return_local_path=return_local_path,
    )


def download_easy_statistics(
    should_upload: bool = True, server=None, return_local_path=False
) -> Union[str, None]:
    """Make the result file available server-side. If the server is remote, upload the file and return its path.

    Parameters
    ----------
    should_upload:
        Whether the file should be uploaded server side when the server is remote.
    server:
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the global server.
    return_local_path:
        If ``True``, the local path is returned as is, without uploading, nor searching
        for mounted volumes.

    Returns
    -------
    str
        Path to the plugin folder.

    Examples
    --------
    >>> from ansys.dpf.core import examples
    >>> path = examples.download_easy_statistics()

    """
    file_name = "easy_statistics.py"
    EXAMPLE_FILE = GITHUB_SOURCE_URL + file_name
    operator_file_path = _retrieve_file(
        EXAMPLE_FILE, filename=file_name, directory="python_plugins"
    )
    return find_files(operator_file_path, should_upload, server, return_local_path)


def _retrieve_plugin(
    file_list: list[str], should_upload: bool = True, server=None, return_local_path=False
) -> Union[str, None]:
    path = None
    for file in file_list:
        EXAMPLE_FILE = GITHUB_SOURCE_URL + file
        operator_file_path = _retrieve_file(EXAMPLE_FILE, file, directory="python_plugins")
        path = str(
            Path(find_files(operator_file_path, should_upload, server, return_local_path)).parent
        )
    return path
