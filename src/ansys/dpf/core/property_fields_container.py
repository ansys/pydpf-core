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
PropertyFieldsCollection.

Contains classes associated with the PropertyFieldsCollection.
"""

from __future__ import annotations

from ansys.dpf.core import PropertyField
from ansys.dpf.core.collection import Collection


class PropertyFieldsCollection(Collection[PropertyField]):
    """Represents a property fields collection, which contains property fields.

    A property fields collection is a set of property fields ordered by labels and IDs.
    Each property field in the collection has an ID for each label, allowing flexible
    organization and retrieval of property fields based on various criteria.

    Parameters
    ----------
    property_fields_collection : ansys.grpc.dpf.collection_message_pb2.Collection, ctypes.c_void_p,
        PropertyFieldsCollection, optional
        Property fields collection created from either a collection message or by copying
        an existing one. The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create a property fields collection from scratch.

    >>> from ansys.dpf import core as dpf
    >>> pfc = dpf.PropertyFieldsCollection()
    >>> pfc.labels = ['time', 'body']
    >>> for i in range(0, 5):
    ...     label_space = {"time": i+1, "body": 0}
    ...     pfield = dpf.PropertyField()
    ...     pfield.data = list(range(i*10, (i+1)*10))
    ...     pfc.add_field(label_space, pfield)

    """

    def __init__(self, property_fields_collection=None, server=None, entries_type: type = PropertyField):
        """Initialize a property fields container."""
        super().__init__(collection=property_fields_collection, server=server, entries_type=entries_type)
