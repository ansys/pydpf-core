"""
.. _ref_examples:

Result Files Examples
=====================
Examples result files.
"""

import os

from ansys.dpf.core import server as server_module
from ansys.dpf.core.core import upload_file_in_tmp_folder
from ansys.dpf.core import path_utilities
from ansys.dpf.core import DataSources


def get_example_required_minimum_dpf_version(file: os.PathLike) -> str:
    """Returns the minimal DPF server version required to run the example, as declared in a note.

    Parameters
    ----------
    file:
        Path to the example file in question.

    Returns
    -------
    Returns the minimal DPF server version required.
    """
    # Read the minimal server version required for the example
    header_flag = '"""'
    note_flag = r".. note::"
    version_flag = "This example requires DPF"
    in_header = False
    previous_line_is_note = False
    minimum_version_str = "0.0"
    with open(file, "r") as f:
        for line in f:
            if line[:3] == header_flag:
                if not in_header:
                    in_header = True
                    continue
                else:
                    break
            if (version_flag in line) and previous_line_is_note and in_header:
                minimum_version_str = line.strip(version_flag).split()[0]
                break
            if note_flag in line:
                previous_line_is_note = True
            else:
                previous_line_is_note = False
    return minimum_version_str


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


def fluid_axial_model() -> DataSources:
    """Download the files and create a DataSources.

    Returns
    -------
    DataSources
        DataSources to the example file.

    Examples
    --------

    >>> from ansys.dpf.core import examples
    >>> ds = examples.fluid_axial_model()
    """
    from .downloads import download_fluent_axial_comp

    aux = download_fluent_axial_comp()
    ds = DataSources()
    ds.set_result_file_path(aux["cas"][0], "cas")
    ds.add_file_path(aux["dat"][0], "dat")
    return ds
