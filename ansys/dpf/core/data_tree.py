"""
.. _ref_data_tree:

DataTree
========
"""

from ansys.dpf.core.errors import protect_grpc
from ansys.dpf.core.mapping_types import types


class DataTree:
    """Represents an entity mapping attributes names to values.

    Parameters
    ----------
    data: dict(string:object)
        Dictionary attributes names to its associated data to add to the data tree.
    data_tree : ansys.grpc.dpf.data_tree_pb2.DataTree message, optional
    server : DPFServer, optional
        Server with the channel connected to the remote or local instance.
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

    """

    def __init__(self, data=None, data_tree=None, server=None):
        if server is None:
            import ansys.dpf.core.server as serverlib
            server = serverlib._global_server()
        # __set_attr__ method has been overridden, self._common_keys is used to list the "real"
        # names used as its class attributes
        self._common_keys = ["_common_keys", "_server", "_message", "_stub", "_owner_data_tree", "_dict"]
        self._server = server
        self._stub = self._connect()

        if data_tree is None:
            from ansys.grpc.dpf import base_pb2
            request = base_pb2.Empty()
            self._message = self._stub.Create(request)
        else:
            self._message = data_tree

        if data:
            self.add(data)

    @protect_grpc
    def add(self, *args, **kwargs):
        """
        Add attributes with their value to the data tree.

        Parameters
        ----------
        args : dict[string:object], optional
        kwargs : int, double, string, list[int], list[double], list[str], DataTree
            Attributes names and their values to add.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> data_tree = dpf.DataTree()
        >>> data_tree.add(id=3, qualities=["nice", "funny"], name="George")

        """
        from ansys.grpc.dpf import data_tree_pb2
        request = data_tree_pb2.UpdateRequest()
        request.data_tree.CopyFrom(self._message)

        def add_data(key, value):
            data = data_tree_pb2.Data()
            data.name = key
            if isinstance(value, str):
                data.string = value
            elif isinstance(value, float):
                data.double = value
            elif isinstance(value, int):
                data.int = value
            elif isinstance(value, list):
                if len(value) > 0 and isinstance(value[0], float):
                    data.vec_double.rep_double.extend(value)
                elif len(value) > 0 and isinstance(value[0], str):
                    data.vec_string.rep_string.extend(value)
                else:
                    data.vec_int.rep_int.extend(value)
            elif isinstance(value, DataTree):
                data.data_tree.CopyFrom(value._message)
            request.data.append(data)

        for entry in args:
            for key, value in entry.items():
                add_data(key, value)
        for key, value in kwargs.items():
            add_data(key, value)
        self._stub.Update(request)

    def to_fill(self):
        """
        This method allows to access and modify the local copy of the data_tree
        without sending a request to the server. It should be used in a ``with``
        statement so that the local data tree is released and the data is sent to
        the server in one action. If it is not used in a ``with`` statement,
        :func:`<release_data> DataTree.release_data()` should be used to update the data tree.

        Warning
        -------
        If this :func:`<release_data> DataTree.to_fill()` method is not used as a context manager in a
        ``with`` statement or if the method `release_data()` is not called,
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
    @protect_grpc
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
    @protect_grpc
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

    @protect_grpc
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
        from ansys.grpc.dpf import data_tree_pb2
        request = data_tree_pb2.HasRequest()
        request.data_tree.CopyFrom(self._message)
        request.names.append(entry)
        return self._stub.Has(request).has_each_name[entry]

    @protect_grpc
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
        from ansys.grpc.dpf import base_pb2, data_tree_pb2
        request = data_tree_pb2.GetRequest()
        request.data_tree.CopyFrom(self._message)
        stype = base_pb2.Type.Value(type.name.upper())
        request.data.append(data_tree_pb2.SingleDataRequest(name=name, type=stype))
        data = self._stub.Get(request).data[0]
        if data.HasField("string"):
            return data.string
        elif data.HasField("int"):
            return data.int
        elif data.HasField("double"):
            return data.double
        elif data.HasField("vec_int"):
            return data.vec_int.rep_int
        elif data.HasField("vec_double"):
            return data.vec_double.rep_double
        elif data.HasField("vec_string"):
            return data.vec_string.rep_string
        elif data.HasField("data_tree"):
            return DataTree(data_tree=data.data_tree, server=self._server)

    @protect_grpc
    def __setattr__(self, key, value):
        if key == "_common_keys" or key in self._common_keys:
            return super.__setattr__(self, key, value)
        self.add({key: value})

    def _connect(self):
        """Connect to the gRPC service containing the reader."""
        from ansys.grpc.dpf import data_tree_pb2_grpc
        return data_tree_pb2_grpc.DataTreeServiceStub(self._server.channel)

    def __del__(self):
        try:
            self._stub.Delete(self._message)
        except:
            pass


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
        kwargs: int, double, string, list[int], list[double], list[str], DataTree
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
