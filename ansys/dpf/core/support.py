"""
.. _ref_support:

Support
=======
"""
import traceback
import warnings
from ansys.dpf.gate import support_capi, support_grpcapi
from ansys.dpf.core.check_version import version_requires

from ansys.dpf.core import server as server_module
from ansys.dpf.core import collection


class Support:
    """Base class for support (supporting Field's location, Scoping's location,
    Collection's labels...)

    Field, PropertyField and StringField support can be accessed generically via this base class.

    Parameters
    ----------
    support : ctypes.c_void_p, ansys.grpc.dpf.support_pb2.Support
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Create a time frequency support from a model.

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = Model(transient)
    >>> time_freq_support = model.metadata.time_freq_support # printable
    >>> time_freq_support.available_field_supported_properties()
    ['time_freqs']
    >>> field = time_freq_support.field_support_by_property("time_freqs")

    """

    def __init__(self, support, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(server)

        # step 2: get api
        self._support_api = self._server.get_api_for_type(
            capi=support_capi.SupportCAPI,
            grpcapi=support_grpcapi.SupportGRPCAPI)

        # step3: init environment
        self._support_api.init_support_environment(self)  # creates stub when gRPC

        # step4: take instance:
        # object_name -> protobuf.message, DPFObject*
        self._internal_obj = support

    @version_requires("5.0")
    def field_support_by_property(self, property_name: str):
        """Returns a Field supporting (describing) a given property.

        Returns
        -------
        Field

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.field import Field
        out = self._support_api.support_get_field_support_by_property(self, property_name)
        if out is not None:
            return Field(field=out, server=self._server)

    @version_requires("5.0")
    def prop_field_support_by_property(self, property_name: str):
        """Returns a PropertyField supporting (describing) a given property.

        Returns
        -------
        PropertyField

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.property_field import PropertyField
        out = self._support_api.support_get_property_field_support_by_property(self, property_name)
        if out is not None:
            return PropertyField(property_field=out, server=self._server)

    @version_requires("5.0")
    def string_field_support_by_property(self, property_name: str):
        """Returns a StringField supporting (describing) a given property.

        Returns
        -------
        StringField

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        from ansys.dpf.core.string_field import StringField
        out = self._support_api.support_get_string_field_support_by_property(self, property_name)
        if out is not None:
            return StringField(string_field=out, server=self._server)

    @version_requires("5.0")
    def available_field_supported_properties(self):
        """Returns the list of property names supported by a Field.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection.StringCollection(
            collection=self._support_api.support_get_property_names_as_string_coll_for_fields(self),
            server=self._server
        )
        return coll_obj.get_integral_entries()

    @version_requires("5.0")
    def available_prop_field_supported_properties(self):
        """Returns the list of property names supported by a PropertyField.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection.StringCollection(
            collection=
            self._support_api.support_get_property_names_as_string_coll_for_property_fields(self),
            server=self._server
        )
        return coll_obj.get_integral_entries()

    @version_requires("5.0")
    def available_string_field_supported_properties(self):
        """Returns the list of property names supported by a StringField.

        Returns
        -------
        list

        Notes
        -----
        Available with server's version starting at 5.0.
        """
        coll_obj = collection.StringCollection(
            collection=
            self._support_api.support_get_property_names_as_string_coll_for_string_fields(self),
            server=self._server
        )
        return coll_obj.get_integral_entries()

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
