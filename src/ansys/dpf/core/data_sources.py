# Copyright (C) 2020 - 2024 ANSYS, Inc. and/or its affiliates.
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
.. _ref_data_sources:

Data Sources
============
"""

from __future__ import annotations

import os
import warnings
import traceback
from typing import Union, Optional, TYPE_CHECKING

from ansys.dpf.core import server as server_module
from ansys.dpf.gate import (
    data_sources_capi,
    data_sources_grpcapi,
    integral_types,
    data_processing_capi,
    data_processing_grpcapi,
)

from ansys.dpf.core.check_version import version_requires
from ansys.dpf.core import errors

if TYPE_CHECKING:
    from ansys.dpf import core as dpf
    from ansys.dpf.core import server_types
    from ansys.grpc.dpf import data_sources_pb2 as DataSourcesPB2


class DataSources:
    """Manages paths to files as sources of data.

    Use this object to declare data inputs for DPF and define their locations.

    An extension key (``'rst'`` for example) is used to choose which files represent
    results files versus accessory files. You can set a result file path when
    initializing this class.


    Parameters
    ----------
    result_path :
        Path of the result. The default is ``None``.
    data_sources :
        gRPC data sources message. The default is ``None``.
    server :
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Initialize a model from a result path.

    >>> from ansys.dpf import core as dpf
    >>>
    >>> # Create the DataSources object with a main file path
    >>> my_data_sources = dpf.DataSources(result_path='file.rst')
    >>> # Get the path to the main result file
    >>> my_data_sources.result_files
    ['file.rst']

    """

    def __init__(
        self,
        result_path: Optional[str, os.PathLike] = None,
        data_sources: Optional[dpf.DataSources, int, DataSourcesPB2.DataSources] = None,
        server: Optional[type[server_types.BaseServer]] = None,
    ):
        """Initialize a connection with the server."""
        # step 1: get server
        self._server = server_module.get_or_create_server(
            data_sources._server if isinstance(data_sources, DataSources) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=data_sources_capi.DataSourcesCAPI,
            grpcapi=data_sources_grpcapi.DataSourcesGRPCAPI,
        )

        # step3: init environment
        self._api.init_data_sources_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if data_sources is not None:
            if isinstance(data_sources, DataSources):
                # Make a Copy
                core_api = self._server.get_api_for_type(
                    capi=data_processing_capi.DataProcessingCAPI,
                    grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI,
                )
                core_api.init_data_processing_environment(self)
                self._internal_obj = core_api.data_processing_duplicate_object_reference(
                    data_sources
                )
            elif hasattr(data_sources, "DESCRIPTOR") or isinstance(data_sources, int):
                # It should be a message (usually from a call to operator_getoutput_data_sources)
                self._internal_obj = data_sources
            else:
                self._internal_obj = None
                raise errors.DpfValueError("Data source must be gRPC data sources message type")
        else:
            if self._server.has_client():
                self._internal_obj = self._api.data_sources_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.data_sources_new("data_sources")

        if result_path is not None:
            self.set_result_file_path(result_path)

    def set_result_file_path(
        self, filepath: Union[str, os.PathLike], key: Optional[str] = ""
    ) -> None:
        """Set the main result file path to the data sources.

        Parameters
        ----------
        filepath :
            Path to the result file.
        key :
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.

        Examples
        --------
        Create a DataSources object and set the result file path.

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result file can be found
        >>> my_data_sources.set_result_file_path(filepath='/tmp/file.rst', key='rst')
        >>> # Get the path to the main result file
        >>> my_data_sources.result_files
        ['/tmp/file.rst']

        """
        extension = os.path.splitext(filepath)[1]
        # Handle .res files from CFX
        if key == "" and extension == ".res":
            key = "cas"
            self.add_file_path(filepath, key="dat")
        # Handle no key given and no file extension
        if key == "" and extension == "":
            key = self.guess_result_key(str(filepath))
        # Look for another extension for .h5 and .cff files
        if key == "" and extension in [".h5", ".cff"]:
            key = self.guess_second_key(str(filepath))
        if key == "":
            self._api.data_sources_set_result_file_path_utf8(self, str(filepath))
        else:
            self._api.data_sources_set_result_file_path_with_key_utf8(self, str(filepath), key)

    @staticmethod
    def guess_result_key(filepath: str) -> str:
        """Guess result key for files without an explicit file extension.

        Parameters
        ----------
        filepath :
            Path to the file.

        Returns
        ----------
        str
            Extension key name

        Examples
        --------
        Gives the result key for the result file of the given path

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the extension key for the file in the given path
        >>> my_file_key = my_data_sources.guess_result_key(filepath=r'file.extension1234')
        'extension1234'

        """
        result_keys = ["d3plot", "binout"]
        base_name = os.path.basename(filepath)
        # Handle files without extension
        for result_key in result_keys:
            if result_key in base_name:
                return result_key
        return ""

    @staticmethod
    def guess_second_key(filepath: str) -> str:
        """For files with an h5 or cff second extension, look for the first extension.

        Parameters
        ----------
        filepath :
            Path to the file.

        Returns
        ----------
        str
            First extension key name

        Examples
        --------
        Find the first extension key of a result file with multiple extensions keys

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>>
        >>> # Download the result files
        >>> paths = examples.download_fluent_axial_comp()
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the extensions keys for the files in the given paths
        >>> # We see that the paths are given in a dictionary.
        >>> # So to choose the correct file you need to give as an argument:
        >>> # - the list label
        >>> # - the file index in that list
        >>> my_file_key = my_data_sources.guess_second_key(filepath=paths['cas'][0])
        'cas'

        """
        accepted = ["cas", "dat"]
        without_ext = os.path.splitext(filepath)[0]
        new_split = os.path.splitext(without_ext)
        new_key = ""
        if len(new_split) > 1:
            key = new_split[1][1:]
            if key in accepted:
                new_key = key
        return new_key

    def set_domain_result_file_path(
        self, path: Union[str, os.PathLike], domain_id: int, key: Optional[str] = None
    ) -> None:
        """Set a result file path by domain.

        This method is used to handle files created by a
        distributed solve.

        Parameters
        ----------
        path:
            Path to the file.
        domain_id:
            Domain ID for the distributed files.
        key:
            Key to associate to the file.

        Examples
        --------
        Set the main result file path to the data sources in their respective domains.

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result data can be found and specify its domain
        >>> my_data_sources.set_domain_result_file_path(path='/tmp/file0.rst', key='rst', domain_id=0)
        >>> my_data_sources.set_domain_result_file_path(path='/tmp/file1.rst', key='rst', domain_id=1)

        """
        if key:
            self._api.data_sources_set_domain_result_file_path_with_key_utf8(
                self, str(path), key, domain_id
            )
        else:
            self._api.data_sources_set_domain_result_file_path_utf8(self, str(path), domain_id)

    def add_file_path(
        self,
        filepath: Union[str, os.PathLike],
        key: Optional[str] = "",
        is_domain: Optional[bool] = False,
        domain_id: Optional[int] = 0,
    ) -> None:
        """Add the acccesory file path to the data sources.

        Files not added as main result files are accessory files, which contain accessory
        information not present in the main result files.

        Parameters
        ----------
        filepath :
            Path of the file.
        key :
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        is_domain:
            Whether the file path is the domain path. The default is ``False``.
        domain_id:
            Domain ID for the distributed files. The default is ``0``. For this
            parameter to be taken into account, ``domain_path=True`` must be set.

        Examples
        --------
        Add an accessory file to the DataSources object

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result file can be found
        >>> my_data_sources.set_result_file_path(filepath='/tmp/file.cas', key='cas')
        >>> # Add the additional result file to the DataSources object
        >>> my_data_sources.add_file_path(filepath='/tmp/ds.dat', key='dat')

        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))
        if is_domain:
            if key == "":
                raise NotImplementedError("A key must be given when using is_domain=True.")
            else:
                self._api.data_sources_add_domain_file_path_with_key_utf8(
                    self, str(filepath), key, domain_id
                )
        else:
            if key == "":
                self._api.data_sources_add_file_path_utf8(self, str(filepath))
            else:
                self._api.data_sources_add_file_path_with_key_utf8(self, str(filepath), key)

    def add_domain_file_path(
        self, filepath: Union[str, os.PathLike], key: str, domain_id: int
    ) -> None:
        """Add a file path to the data sources in the given domain.

        Files not added as main result files are accessory files, which contain accessory
        information not present in the main result files.

        Parameters
        ----------
        filepath:
            Path of the file.
        key:
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator.
        domain_id:
            Domain ID for the distributed files.

        Examples
        --------
        Add an accessory file to its domain

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>># Define the path where the main result data can be found and specify its domain
        >>> my_data_sources.set_domain_result_file_path(path='/tmp/ds.cas', key='cas', domain_id=1)
        >>> # Add the additional result data to the DataSources object and specify its domain
        >>> my_data_sources.add_domain_file_path(path='/tmp/ds.dat', key="dat", domain_id=1)

        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))
        self._api.data_sources_add_domain_file_path_with_key_utf8(
            self, str(filepath), key, domain_id
        )

    def add_file_path_for_specified_result(
        self,
        filepath: Union[str, os.PathLike],
        key: Optional[str] = "",
        result_key: Optional[str] = "",
    ):
        """Add a file path for a specified result file key to the data sources.

        This method can be used when results files with different keys (extensions) are
        contained in the data sources. For example, a solve using two different solvers
        could generate two different sets of files.

        Parameters
        ----------
        filepath :
            Path of the file.
        key :
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator. The default is ``""``,
            in which case the key is found directly.
        result_key:
            Extension of the results file that the specified file path belongs to.
            The default is ``""``, in which case the key is found directly.

        """
        # The filename needs to be a fully qualified file name
        if not os.path.dirname(filepath):
            # append local path
            filepath = os.path.join(os.getcwd(), os.path.basename(filepath))

        self._api.data_sources_add_file_path_for_specified_result_utf8(
            self, str(filepath), key, result_key
        )

    def add_upstream(
        self, upstream_data_sources: DataSources, result_key: Optional[str] = ""
    ) -> None:
        """Add upstream data sources to the main DataSources object.

        This is used to add a set of path creating an upstream for
        recursive workflows.

        Parameters
        ----------
        upstream_data_sources:
            Set of paths creating an upstream for recursive workflows.

        result_key:
            Extension of the result file group with which this upstream belongs

        Examples
        --------
        Add an upstream data to the main DataSources object of an expansion analysis

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>>
        >>> # Download the result files
        >>> paths = examples.download_msup_files_to_dict()
        >>> # Create the main DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result data can be found
        >>> my_data_sources.set_result_file_path(filepath=paths["rfrq"],  key='rfrq')
        >>>
        >>> # Create the DataSources object for the upstream data
        >>> my_data_sources_upstream = dpf.DataSources()
        >>> # Define the path where the main upstream data can be found
        >>> my_data_sources_upstream.set_result_file_path(filepath=paths["mode"])
        >>> # Add the additional upstream data to the upstream DataSources object
        >>> my_data_sources_upstream.add_file_path(filepath=paths["rst"], key='rst')
        >>>
        >>> # Add the upstream DataSources to the main DataSources object
        >>> my_data_sources.add_upstream(upstream_data_sources=my_data_sources_upstream)

        """
        if result_key == "":
            self._api.data_sources_add_upstream_data_sources(self, upstream_data_sources)
        else:
            self._api.data_sources_add_upstream_data_sources_for_specified_result(
                self, upstream_data_sources, result_key
            )

    def add_upstream_for_domain(self, upstream_data_sources: DataSources, domain_id: int) -> None:
        """Add an upstream data sources to the main DataSources object for a given domain.

        This is used to add a set of path creating an upstream for
        recursive workflows in a distributed solve.

        Parameters
        ----------
        upstream_data_sources :
            Set of paths creating an upstream for recursive workflows.

        domain_id:
            Domain id for distributed files.

        Examples
        --------
        Add an upstream data to the main DataSources object of an expansion distributed analysis

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples

        >>> # Download the result files
        >>> paths = examples.find_distributed_msup_folder()
        >>> # Create the main DataSources object
        >>>  my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result file can be found and specify its domain
        >>> # We use a format string here because the function used to define the path gives the path to a folder
        >>> my_data_sources.set_domain_result_file_path(path=rf"{paths}\file_load_1.rfrq", key='rfrq', domain_id=0)
        >>> # Add the additional result file to the DataSources object and specify its domain
        >>> my_data_sources.add_domain_file_path(filepath=rf"{paths}\file_load_2.rfrq", key='rfrq', domain_id=1)
        >>>
        >>> # Create the DataSources object for the first and second upstream files
        >>> my_data_sources_upstream_g0 = dpf.DataSources()
        >>> my_data_sources_upstream_g1 = dpf.DataSources()
        >>> # Define the path where the main upstream files can be found
        >>> my_data_sources_upstream_g0.set_result_file_path(filepath=rf"{paths}\file0.mode", key='mode')
        >>> my_data_sources_upstream_g1.set_result_file_path(filepath=rf"{paths}\file1.mode", key='mode')
        >>> # Add the additional upstream files to the upstream DataSources objectS
        >>> my_data_sources_upstream_g0.add_file_path(filepath=rf"{paths}\file0.rst", key='rst')
        >>> my_data_sources_upstream_g1.add_file_path(filepath=rf"{paths}\file1.rst", key='rst')

        >>> # Add the upstream DataSources to the main DataSources object and specify its domain
        >>> my_data_sources.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g0, domain_id=0)
        >>> my_data_sources.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g1, domain_id=1)

        """
        self._api.data_sources_add_upstream_domain_data_sources(
            self, upstream_data_sources, domain_id
        )

    @property
    def result_key(self) -> str:
        """Result key used by the data sources.

        Returns
        -------
        str
           Result key.

        Examples
        --------

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result file can be found
        >>> my_data_sources.set_result_file_path(filepath='/tmp/file.rst', key='rst')
        >>> # Get the to the main result file
        >>> my_data_sources.result_key
        'rst'

        """
        return self._api.data_sources_get_result_key(self)

    @property
    def result_files(self):
        """List of result files contained in the data sources.

        Returns
        ----------
        list
            List of result files.

        Notes
        -----
        - If you use the :func:`set_result_file_path() <ansys.dpf.core.data_sources.DataSources.set_result_file_path>`
        function, it will return only the file path given as an argument to this function.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result file can be found
        >>> my_data_sources.set_result_file_path(filepath='/tmp/file.cas', key='cas')
        >>> # Add the additional result file to the DataSources object
        >>> my_data_sources.add_file_path(filepath='/tmp/ds.dat', key='dat')
        >>> # Get the path to the main result file
        >>> my_data_sources.result_files
        ['/tmp/file.cas']

        - If you added an upstream result file, it is not listed in the main ``DataSources`` object. You have to
        check directly in the ``DataSources`` object created to define the upstream data.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>>
        >>> # Download the result files
        >>> paths = examples.download_msup_files_to_dict()
        >>> # Create the main DataSources object with a main file path
        >>> my_data_sources = dpf.DataSources(result_path=paths["rfrq"])
        >>>
        >>> # Create the DataSources object for the upstream data
        >>> my_data_sources_upstream = dpf.DataSources(result_path=paths["mode"])
        >>> # Add the additional upstream data to the upstream DataSources object
        >>> my_data_sources_upstream.add_file_path(filepath=paths["rst"], key='rst')
        >>>
        >>> # Add the upstream DataSources to the main DataSources object
        >>> my_data_sources.add_upstream(upstream_data_sources=my_data_sources_upstream)
        >>>
        >>> # Get the path to the main result file of the main DataSources object
        >>> my_data_sources.result_files
        [..\\.venv\\Lib\\site-packages\\ansys\\dpf\\core\\examples\\result_files\\msup\\file.rfrq']

        - If you are checking the DataSources object created to define the upstream data, only the first one is listed.

        >>> # Get the path to the upstream file of the upstream DataSources object
        >>> my_data_sources_upstream.result_files
        [..\\.venv\\Lib\\site-packages\\ansys\\dpf\\core\\examples\\result_files\\msup\\file.mode']

        - If you have a ``DataSources`` object with more than one domain, a empty list is returned.

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result data can be found and specify its domain
        >>> my_data_sources.set_domain_result_file_path(path='/tmp/file0.rst', key='rst', domain_id=0)
        >>> my_data_sources.set_domain_result_file_path(path='/tmp/file1.rst', key='rst', domain_id=1)
        >>>
        >>> # Get the path to the main result files of the DataSources object
        >>> my_data_sources.result_files
        [None, None]

        """
        result_key = self.result_key
        if result_key == "":
            return None
        else:
            response = []
            num_keys = self._api.data_sources_get_num_keys(self)
            for i_key in range(num_keys):
                num_paths = integral_types.MutableInt32()
                key = self._api.data_sources_get_key(self, i_key, num_paths)
                if key == result_key:
                    for i_path in range(int(num_paths)):
                        path = self._api.data_sources_get_path(self, key, i_path)
                        response.append(path)
            return response

    @version_requires("7.0")
    def register_namespace(self, result_key: str, namespace: str):
        """Adds a link from this ``result_key`` to this ``namespace`` in the DataSources.

        When using an operator that requires data from a ``DataSources`` object, DPF must find
        a corresponding entry to this call in its code. This entry is given
        by the namespace, the file extension, and the operator name: ``namespace::key::operator_name``.

        For example, if the results file comes from a MAPDL solver and has an '.rst' extension
        and you want to get the displacement results in this file, DPF code will get the
        corresponding operator: ``mapdl::rst::displacement``.

        So, if you have an extension that is not
        registered in DPF you have to define its namespace. This function is mainly used when
        creating your own operators and plugins, or when you have a file with an unknown
        namespace, but you know that it corresponds to a given solver.

        Parameters
        ----------
        result_key:
            Extension of the file, which is used as a key for choosing the correct
            plugin when a result is requested by an operator.
        namespace:
            Namespace to associate the file extension to.

        Notes
        -----
        Available with server's version starting at 7.0.

        Examples
        --------

        >>> from ansys.dpf import core as dpf
        >>>
        >>> # Create the main DataSources object
        >>> my_data_sources = dpf.DataSources()
        >>> # Define the path where the main result data can be found
        >>> my_data_sources.set_result_file_path(filepath=r'file.extension', key='extension')
        >>> # Define the namespace for the results in the given path
        >>> my_data_sources.register_namespace(result_key='extension', namespace='namespace')

        """
        self._api.data_sources_register_namespace(self, result_key, namespace)

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
            pass
