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
mesh_scoping_factory

Contains functions to simplify creating mesh scopings.
"""

from ansys.dpf.core import Scoping
from ansys.dpf.core.common import locations


def nodal_scoping(node_ids, server=None):
    """Create a specific nodal :class:`ansys.dpf.core.Scoping` associated with a mesh.

    Parameters
    ----------
    node_ids : list[int]
        List of IDs for the nodes.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
    """
    scoping = Scoping(server=server, ids=node_ids, location=locations.nodal)
    return scoping


def elemental_scoping(element_ids, server=None):
    """Create a specific elemental :class:`ansys.dpf.core.Scoping` associated with a mesh.

    Parameters
    ----------
    element_ids : list[int]
        List of IDs for the elements.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
    """
    scoping = Scoping(server=server, ids=element_ids, location=locations.elemental)
    return scoping


def face_scoping(face_ids, server=None):
    """Create a specific face :class:`ansys.dpf.core.Scoping` associated with a mesh.

    Parameters
    ----------
    face_ids : list[int]
        List of IDs for the faces.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
    """
    scoping = Scoping(server=server, ids=face_ids, location=locations.faces)
    return scoping


def named_selection_scoping(named_selection_name, model, server=None):
    """Create a specific :class:`ansys.dpf.core.Scoping` associated with a specified model's mesh.

    Parameters
    ----------
    named_selection_name : str
        Name of the named selection.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
    """
    return model.metadata.named_selection(named_selection_name)
