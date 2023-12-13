"""
.. _ref_custom_type_fields_container:

CustomTypeFieldsContainer
===============
Contains classes associated with the DPF CustomTypeFieldsContainer.
"""
from __future__ import annotations
from ansys.dpf.core.collection import Collection
from typing import TYPE_CHECKING

from ansys.dpf.core.custom_type_field import CustomTypeField

if TYPE_CHECKING:  # pragma: no cover
    import numpy as np


class CustomTypeFieldsContainer(Collection):
    """Represents a custom type fields container, containing custom type fields for a common result.

    Parameters
    ----------
    unitary_type: numpy.dtype
        Type of data in the custom type fields.
    custom_type_fields_container : ansys.grpc.dpf.collection_pb2.Collection, ctypes.c_void_p,
    CustomTypeFieldsContainer, optional
        Custom type fields container created from either a collection message or by copying an
        existing custom type fields container. The default is "None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    """

    def __init__(
        self,
        unitary_type=None,
        custom_type_fields_container=None,
        server=None,
    ):
        super().__init__(collection=custom_type_fields_container, server=server)
        if self._internal_obj is None:
            if self._server.has_client():
                self._internal_obj = (
                    self._api.collection_of_custom_type_field_new_on_client(  # TODO
                        self._server.client
                    )
                )
            else:
                self._internal_obj = self._api.collection_of_custom_type_field_new()
        self._type = unitary_type
        self._component_index = None  # component index
        self._component_info = None  # for norm/max/min

    def create_subtype(self, obj_by_copy) -> CustomTypeField:
        return CustomTypeField(unitary_type=self._type, field=obj_by_copy, server=self._server)

    @property
    def type(self) -> np.dtype:
        """Type of unitary data in the CustomFieldsContainer."""
        return self._type

    def is_of_type(self, type_to_compare: np.dtype) -> bool:
        """Checks whether the CustomTypeFieldsContainer unitary type is the same as the input type.

        Parameters
        ----------
        type_to_compare: numpy.dtype

        Returns
        -------
        bool

        """
        return self.type == type_to_compare
