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
fields_factory.

Contains functions to simplify creating fields.
"""

import numpy as np

from ansys.dpf.core import Field, server as server_module
from ansys.dpf.core.common import locations, natures
from ansys.dpf.gate import field_capi, field_grpcapi


def field_from_array(arr, server=None):
    """Create a DPF vector or scalar field from a numpy array or a Python list.

    Parameters
    ----------
    arr : np.ndarray or List
        Numpy array or Python list containing either 1 or 3 dimensions.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        Field constructed from the array.
    """
    from ansys.dpf.core import Field, natures

    arr = np.asarray(arr)

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Array must be a numeric type")

    shp_err = ValueError(
        "Array must be either contain 1 dimension or " "2 dimensions with three components."
    )
    if arr.ndim == 1:
        nature = natures.scalar
    elif arr.ndim == 2:
        if arr.shape[1] == 1:
            arr = arr.ravel()
            nature = natures.scalar
        elif arr.shape[1] == 3:
            nature = natures.vector
        elif arr.shape[1] == 6:
            nature = natures.symmatrix
        else:
            raise shp_err
    else:
        raise shp_err

    n_entities = arr.shape[0]
    field = Field(nentities=n_entities, nature=nature, server=server)
    field.data = arr
    field.scoping.ids = np.arange(1, n_entities + 1)
    return field


def create_matrix_field(num_entities, num_lines, num_col, location=locations.nodal, server=None):
    """Create a matrix :class:`ansys.dpf.core.Field`.

    This field contains entities that have a matrix format. This is a "reserve" mechanism,
    not a resize one. This means that you need to append data to grow the size of your field.

    Parameters
    ----------
    num_entities : int
        Number of entities to reserve.
    num_lines : int
        Number of matrix line.
    num_col : int
        Number of matrix columns.
    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field of the requested format.

    Examples
    --------
    Create a field containing 3 matrix entities of a col*lines = 2*5 size with
    a nodal location (default).

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_matrix_field(3, 5, 2)

    """
    return _create_field(
        server=server,
        nature=natures.matrix,
        nentities=num_entities,
        location=location,
        ncomp_m=num_col,
        ncomp_n=num_lines,
    )


def create_3d_vector_field(num_entities, location=locations.nodal, server=None):
    """Create a specific :class:`ansys.dpf.core.Field` with entities that have 3D vector format.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    num_entities : int
        Number of entities to reserve

    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field of the requested format.

    Examples
    --------
    Create a field containing 4 3D vector entities with a nodal location (default).

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_3d_vector_field(4)

    """
    return _create_field(server, natures.vector, num_entities, location)


def create_tensor_field(num_entities, location=locations.nodal, server=None):
    """Create a specific :class:`ansys.dpf.core.Field` with entities that have a 3*3 format.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    num_entities : int
        Number of entities to reserve.
    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field in the requested format.

    Examples
    --------
    Create a field containing 4 tensor entities with a nodal location (default).

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_tensor_field(4)

    """
    return _create_field(server, natures.symmatrix, num_entities, location)


def create_scalar_field(num_entities, location=locations.nodal, server=None):
    """Create a specific `:class:`ansys.dpf.core.Field` with entities that are scalar.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    num_entities : int
        Number of entities to reserve
    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field in the requested format.

    Examples
    --------
    Create a field containing 4 scalars with a nodal location (default).

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_scalar_field(4)

    """
    return _create_field(server, natures.scalar, num_entities, location)


def create_vector_field(num_entities, num_comp, location=locations.nodal, server=None):
    """Create a specific `:class:`ansys.dpf.core.Field` with entities that have a vector format.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    num_entities : int
        Number of entities to reserve.
    num_comp : int
        Number of vector components.
    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field in the requested format.

    Examples
    --------
    Create a field containing 3 vector entities of 5 components each with a
    nodal location (default).

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_vector_field(3, 5)

    """
    return _create_field(server, natures.vector, num_entities, location, ncomp_n=num_comp)


def create_overall_field(
    value, nature, num_entities, num_comp, location=locations.overall, server=None
):
    """Create a specific `:class:`ansys.dpf.core.Field` with entities that have an overall location.

    Regarding the nature of the entity contained in the field, we set the same value
    for all elements.

    Parameters
    ----------
    value : float
        Value of the entity
    nature : str
        Nature of the field entity data. For example:

        - :class:`ansys.dpf.core.natures.matrix`
        - :class:`ansys.dpf.core.natures.scalar`
    num_entities : int
        Number of entities to reserve.
    num_comp : int
        Number of vector components.
    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    field : Field
        DPF field in the requested format.

    Examples
    --------
    Create a field containing 10 scalar entities of 1 component each with an
    overall location (default). Same value (1.0) is set for all element of the field.

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_overall_field(1.0, natures.scalar, 10, 1)

    """
    overall_field = _create_field(server, nature, num_entities, location, ncomp_n=num_comp)
    for i in range(num_entities):
        overall_field.append(value, i)
    return overall_field


def _create_field(server, nature, nentities, location=locations.nodal, ncomp_n=0, ncomp_m=0):
    """Create a specific :class:`ansys.dpf.core.Field`.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    nature : str
        Nature of the field entity data. For example:

        - :class:`ansys.dpf.core.natures.matrix`
        - :class:`ansys.dpf.core.natures.scalar`

    nentities : int
        Number of entities to reserve.

    location : str, optional
        Location of the field. Options are in :class:`locations <ansys.dpf.core.common.locations>`.
        The default is ``dpf.locations.nodal``.

    ncomp_n : int
        Number of lines.
    ncomp_m : int
        Number of columns.

    Returns
    -------
    field : Field
        DPF field in the requested format.
    """
    if server is None:
        server = server_module.get_or_create_server(server)
    api = server.get_api_for_type(capi=field_capi.FieldCAPI, grpcapi=field_grpcapi.FieldGRPCAPI)
    api.init_field_environment(server)
    internal_obj = Field._field_create_internal_obj(
        api=api,
        client=server.client,
        nature=nature,
        nentities=nentities,
        location=location,
        ncomp_n=ncomp_n,
        ncomp_m=ncomp_m,
    )
    field = Field(field=internal_obj, server=server)
    return field
