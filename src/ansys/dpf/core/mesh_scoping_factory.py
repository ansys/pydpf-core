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
mesh_scoping_factory.

Contains functions to simplify creating a mesh scoping.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: nocover
    from ansys.dpf.core.model import Model
    from ansys.dpf.core.scoping import IdVectorType
    from ansys.dpf.core.server_types import AnyServerType

from ansys.dpf.core import Scoping
from ansys.dpf.core.common import locations


def nodal_scoping(node_ids: IdVectorType, server: AnyServerType = None) -> Scoping:
    """Create a nodal :class:`ansys.dpf.core.Scoping` defining a list of node IDs.

    Parameters
    ----------
    node_ids:
        List of node IDs.
    server:
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping:
        A nodal scoping containing the node IDs provided.
    """
    scoping = Scoping(server=server, ids=node_ids, location=locations.nodal)
    return scoping


def elemental_scoping(element_ids: IdVectorType, server: AnyServerType = None) -> Scoping:
    """Create an elemental :class:`ansys.dpf.core.Scoping` defining a list of element IDs.

    Parameters
    ----------
    element_ids:
        List of element IDs.
    server:
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping:
        An elemental scoping containing the element IDs provided.
    """
    scoping = Scoping(server=server, ids=element_ids, location=locations.elemental)
    return scoping


def face_scoping(face_ids: IdVectorType, server: AnyServerType = None) -> Scoping:
    """Create a face :class:`ansys.dpf.core.Scoping`defining a list of face IDs.

    Parameters
    ----------
    face_ids:
        List of face IDs.
    server:
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping:
        A face scoping containing the face IDs provided.
    """
    scoping = Scoping(server=server, ids=face_ids, location=locations.faces)
    return scoping


def named_selection_scoping(
    named_selection_name: str, model: Model, server: AnyServerType = None
) -> Scoping:
    """Create a :class:`ansys.dpf.core.Scoping` based on a named selection in a model.

    Parameters
    ----------
    named_selection_name:
        Name of the named selection.
    model:
        Model where the named selection exists.

    Returns
    -------
    scoping:
        A scoping containing the IDs of the entities in the named selection.
        The location depends on the type of entities targeted by the named selection.
    """
    return model.metadata.named_selection(named_selection=named_selection_name, server=server)
