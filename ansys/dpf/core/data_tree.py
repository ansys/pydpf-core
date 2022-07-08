"""
.. _ref_data_tree:

DataTree
========
"""
import enum
import traceback
import warnings

from ansys.dpf.core.mapping_types import types
from ansys.dpf.core import server as server_module
from ansys.dpf.core import errors
from ansys.dpf.gate import (
    dpf_data_tree_abstract_api,
    dpf_data_tree_capi,
    dpf_data_tree_grpcapi,
    data_processing_capi,
    data_processing_grpcapi,
    collection_capi,
    collection_grpcapi,
    object_handler,
    integral_types,
)


class DataTree:
    """Represents an entity mapping attributes names to values.

    Parameters
    ----------
    data: dict(string:object)
        Dictionary attributes names to its associated data to add to the data tree.
    data_tree : ctypes.c_void_p, ansys.grpc.dpf.data_tree_pb2.DataTree message, optional
    server : DPFServer, optional
        Server with channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Create a data tree from a dictionary.

    >>> from ansys.dpf import core as dpf
    >>> data_tree = dpf.DataTree({"num_entities":3, "list_of_raws":[1,2,3,4], "name": "George"})
    >>> data_tree.get_as("name", dpf.types.string)
    'George'
    >>> data_tree.get_as("list_of_raws", dpf.types.vec_int)
    [1, 2, 3, 4]

    Create a data tree with add.

    >>> from ansys.dpf import core as dpf
    >>> data_tree = dpf.DataTree()
    >>> data_tree.add(num_entities=3, list_of_raws=[1,2,3,4], name="George")
    >>> txt = data_tree.write_to_txt()

    Create a data tree with a context manager.

    >>> from ansys.dpf import core as dpf
    >>> data_tree = dpf.DataTree()
    >>> with data_tree.to_fill() as to_fill:
    ...     to_fill.num_entities = 3
    ...     to_fill.list_of_raws = [1,2,3,4]
    >>> json = data_tree.write_to_json()

    Notes
    -----
    Class available with server's version starting at 4.0.
    """

    def __init__(self, data=None, data_tree=None, server=None):
        # __set_attr__ method has been overridden, self._common_keys is used to list the "real"
        # names used as its class attributes
        self._common_keys = ["_common_keys", "_server", "_internal_obj", "_owner_data_tree",
                             "_dict", "_api_instance", "_deleter_func"]
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        if data_tree is None and not self._server.meet_version("4.0"):
            raise errors.DpfVersionNotSupported("4.0")

        # step 2: get api
        self._api_instance = None  # see property self._api

        # step3: init environment
        self._api.init_dpf_data_tree_environment(self)  # creates stub when gRPC

        # step4: if object exists, take the instance, else create it
        if data_tree is not None:
            self._internal_obj = data_tree
        else:
            if self._server.has_client():
                self._internal_obj = self._api.dpf_data_tree_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.dpf_data_tree_new()

        if data:
            self.add(data)

    @property
    def _api(self) -> dpf_data_tree_abstract_api.DpfDataTreeAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=dpf_data_tree_capi.DpfDataTreeCAPI,
                grpcapi=dpf_data_tree_grpcapi.DpfDataTreeGRPCAPI
            )
        return self._api_instance

    def add(self, *args, **kwargs):
        """
        Add attributes with their value to the data tree.

        Parameters
        ----------
        args : dict[string:object], optional
        kwargs : int, float, string, list[int], list[double], list[str], DataTree
            Attributes names and their values to add.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")

        """
        def add_data(self, key, value):
            if isinstance(value, str):
                self._api.dpf_data_tree_set_string_attribute(self, key, value, len(value))
            elif isinstance(value, float):
                self._api.dpf_data_tree_set_double_attribute(self, key, value)
            elif isinstance(value, (bool, int, enum.Enum)):
                self._api.dpf_data_tree_set_int_attribute(self, key, int(value))
            elif isinstance(value, list):
                if len(value) > 0 and isinstance(value[0], float):
                    self._api.dpf_data_tree_set_vec_double_attribute(
                        self, key, value, len(value)
                    )
                elif len(value) > 0 and isinstance(value[0], str):
                    if self._server.has_client():
                        coll_obj = object_handler.ObjHandler(
                            data_processing_api=self._core_api,
                            internal_obj=self._coll_api.collection_of_string_new_local(self._server.client))
                    else:
                        coll_obj = object_handler.ObjHandler(
                            data_processing_api=self._core_api,
                            internal_obj=self._coll_api.collection_of_string_new())
                    for s in value:
                        self._coll_api.collection_add_string_entry(coll_obj, s)
                    self._api.dpf_data_tree_set_string_collection_attribute(
                        self, key, coll_obj
                    )
                elif len(value) > 0 and isinstance(value[0], int):
                    self._api.dpf_data_tree_set_vec_int_attribute(
                        self, key, value, len(value)
                    )
                elif len(value) > 0:
                    raise TypeError(f"List of {type(value[0]).__name__} is not supported, "
                                    f"use list of int, float or strings.")
            elif isinstance(value, DataTree):
                self._api.dpf_data_tree_set_sub_tree_attribute(
                    self, key, value
                )
            else:
                raise TypeError(f"{type(value[0]).__name__} is not a supported type, "
                                "use lists, int, float, strings or DataTree.")
        for entry in args:
            for key, value in entry.items():
                add_data(self, key, value)

        for key, value in kwargs.items():
            add_data(self, key, value)

    @property
    def _core_api(self):
        core_api = self._server.get_api_for_type(
            capi=data_processing_capi.DataProcessingCAPI,
            grpcapi=data_processing_grpcapi.DataProcessingGRPCAPI)
        core_api.init_data_processing_environment(self)
        return core_api

    @property
    def _coll_api(self):
        coll_api = self._server.get_api_for_type(
            capi=collection_capi.CollectionCAPI,
            grpcapi=collection_grpcapi.CollectionGRPCAPI)
        coll_api.init_collection_environment(self)
        return coll_api

    def to_fill(self):
        """
        This method allows to access and modify the local copy of the data_tree
        without sending a request to the server. It should be used in a ``with``
        statement so that the local data tree is released and the data is sent to
        the server in one action. If it is not used in a ``with`` statement,
        :func:`<release_data> DataTree.release_data()` should be used to update the data tree.

        Warning
        -------
        If this :func:`<release_data> DataTree.to_fill()` method is not used as
        a context manager in a ``with`` statement or if the method `release_data()`
        is not called,
        the data will not be updated.

        Returns
        -------
        local_data_tree : DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> with data_tree.to_fill() as to_fill:
        ...     to_fill.name = "George"
        ...     to_fill.qualities=["nice", "funny"]
        ...     to_fill.id = 3

        """
        return _LocalDataTree(self)

    def write_to_txt(self, path=None):
        """
        Writes the data tree either as a file or as returned string in a text format.

        Parameters
        ----------
        path : str, optional
            If a path is specified the output is written to this file.

        Returns
        -------
        str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")
        >>> txt = data_tree.write_to_txt()
        >>> import tempfile
        >>> import os
        >>> data_tree.write_to_txt(os.path.join(tempfile.mkdtemp(), "data_tree.txt"))

        """
        from ansys.dpf.core.operators.serialization import data_tree_to_txt
        from ansys.dpf import core
        op = data_tree_to_txt(server=self._server)
        op.inputs.data_tree.connect(self)
        if path:
            directory = core.core.make_tmp_dir_server(self._server)
            server_path = core.path_utilities.join(directory, "tmp.txt", server=self._server)
            op.inputs.path.connect(server_path)
            op.run()
            return core.download_file(server_path, path)
        else:
            return op.get_output(0, core.types.string)

    def write_to_json(self, path=None):
        """
        Writes the data tree either as a file or as returned string in a json format.

        Parameters
        ----------
        path : str, optional
            If a path is specified the output is written to this file.

        Returns
        -------
        str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")
        >>> txt = data_tree.write_to_json()
        >>> import tempfile
        >>> import os
        >>> data_tree.write_to_json(os.path.join(tempfile.mkdtemp(), "data_tree.json"))

        """
        from ansys.dpf.core.operators.serialization import data_tree_to_json
        from ansys.dpf import core
        op = data_tree_to_json(server=self._server)
        op.inputs.data_tree.connect(self)
        if path:
            directory = core.core.make_tmp_dir_server(self._server)
            server_path = core.path_utilities.join(directory, "tmp.txt", server=self._server)
            op.inputs.path.connect(server_path)
            op.run()
            return core.download_file(server_path, path)
        else:
            return op.get_output(0, core.types.string)

    @staticmethod
    def read_from_json(path=None, txt=None, server=None):
        """
        Convert a json string or file to DataTree

        Parameters
        ----------
        path : str, optional
            If a path is specified the output is read from this file.

        txt : str, optional
            If a txt is specified the output is read from this string.

        server : DPFServer, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree({"num_entities":3, "list_of_raws":[1,2,3,4], "name": "George"})
        >>> txt = data_tree.write_to_json()
        >>> data_tree_copy = dpf.DataTree.read_from_json(txt=txt)

        """
        from ansys.dpf.core.operators.serialization import json_to_data_tree
        from ansys.dpf import core
        op = json_to_data_tree(server=server)
        if path:
            server_path = core.upload_file_in_tmp_folder(path, server=server)
            op.inputs.string_or_path.connect(core.DataSources(server_path, server=server))
        elif txt:
            op.inputs.string_or_path.connect(str(txt))
        return op.outputs.data_tree()

    @staticmethod
    def read_from_txt(path=None, txt=None, server=None):
        """
        Convert a text string or file to DataTree

        Parameters
        ----------
        path : str, optional
            If a path is specified the output is read from this file.

        txt : str, optional
            If a txt is specified the output is read from this string.

        server : DPFServer, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree({"num_entities":3, "list_of_raws":[1,2,3,4], "name": "George"})
        >>> txt = data_tree.write_to_txt()
        >>> data_tree_copy = dpf.DataTree.read_from_txt(txt=txt)

        """
        from ansys.dpf.core.operators.serialization import txt_to_data_tree
        from ansys.dpf import core
        op = txt_to_data_tree(server=server)
        if path:
            server_path = core.upload_file_in_tmp_folder(path, server=server)
            op.inputs.string_or_path.connect(core.DataSources(server_path, server=server))
        elif txt:
            op.inputs.string_or_path.connect(str(txt))
        return op.outputs.data_tree()

    def has(self, entry):
        """
        Return True if the entry exists

        Parameters
        ----------
        entry : str

        Returns
        -------
        bool

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")
        >>> data_tree.has("qualities")
        True
        >>> data_tree.has("flaws")
        False

        """
        return self._api.dpf_data_tree_has_attribute(self, entry)

    def get_as(self, name, type=types.string):
        """
        Returns an attribute value by its name in the required type.

        Parameters
        ----------
        name : str
            Name of the attribute to return
        type : types
            Type of the attribute to return. String is supported for all attributes.

        Returns
        -------
        str, int, float, list[int], list[float], list[str], DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")
        >>> data_tree.get_as("id")
        '3'
        >>> data_tree.get_as("id", dpf.types.int)
        3
        >>> data_tree.get_as("qualities", dpf.types.vec_string)
        ['nice', 'funny']

        """
        out = None
        if type == types.int:
            out = integral_types.MutableInt32()
            self._api.dpf_data_tree_get_int_attribute(self, name, out)
            out = int(out)
        elif type == types.double:
            out = integral_types.MutableDouble()
            self._api.dpf_data_tree_get_double_attribute(self, name, out)
            out = float(out)
        elif type == types.string:
            out = integral_types.MutableString(1)
            size = integral_types.MutableInt32(0)
            self._api.dpf_data_tree_get_string_attribute(self, name, out, size)
            out = str(out)
        elif type == types.vec_double:
            out = integral_types.MutableListDouble()
            self._api.dpf_data_tree_get_vec_double_attribute(self, name, out, out.internal_size)
            out = out.tolist()
        elif type == types.vec_int:
            out = integral_types.MutableListInt32()
            self._api.dpf_data_tree_get_vec_int_attribute(self, name, out, out.internal_size)
            out = out.tolist()
        elif type == types.vec_string:
            coll_obj = object_handler.ObjHandler(
                data_processing_api=self._core_api,
                internal_obj=self._api.dpf_data_tree_get_string_collection_attribute(self, name)
            )
            num = self._coll_api.collection_get_size(coll_obj)
            out = []
            for i in range(num):
                out.append(self._coll_api.collection_get_string_entry(coll_obj, i))
        elif type == types.data_tree:
            obj = self._api.dpf_data_tree_get_sub_tree(self, name)
            out = DataTree(data_tree=obj, server=self._server)
        return out

    def __setattr__(self, key, value):
        if key == "_common_keys" or key in self._common_keys:
            return super.__setattr__(self, key, value)
        self.add({key: value})

    def __del__(self):
        try:
            obj = self._deleter_func[1](self)
            if obj is not None:
                self._deleter_func[0](obj)
        except:
            warnings.warn(traceback.format_exc())


class _LocalDataTree(DataTree):
    def __init__(self, data_tree):
        self._common_keys = ["_owner_data_tree", "_dict", "_common_keys"]
        self._owner_data_tree = data_tree
        self.__cache_data__()

    def add(self, *args, **kwargs):
        """
        Add attributes with their value to the data tree.

        Parameters
        ----------
        kwargs: int, float, string, list[int], list[double], list[str], DataTree
            Data to add.
        """

        def add_data(key, value):
            self._dict[key] = value

        for entry in args:
            for key, value in entry.items():
                add_data(key, value)
        for key, value in kwargs.items():
            add_data(key, value)

    def __cache_data__(self):
        self._dict = {}

    def release_data(self):
        """Release the data."""
        self._owner_data_tree.add(self._dict)

    def __setattr__(self, key, value):
        if key == "_common_keys" or key in self._common_keys:
            return super.__setattr__(self, key, value)
        self.add({key: value})

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if tb is None:
            self._is_exited = True
            self.release_data()
        else:
            print(tb)

    def __del__(self):
        if not hasattr(self, "_is_exited") or not self._is_exited:
            self._is_exited = True
            self.release_data()
        pass
