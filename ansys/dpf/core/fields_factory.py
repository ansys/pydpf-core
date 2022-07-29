"""
fields_factory
==============

Contains functions to simplify creating fields.
"""

from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import Field
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import field_capi, field_grpcapi

import numpy as np


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
        "Array must be either contain 1 dimension or "
        "2 dimensions with three components."
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


def create_matrix_field(
    num_entities, num_lines, num_col, location=locations.nodal, server=None
):
    """Create a matrix :class:`ansys.dpf.core.Field`.

    This field contain entities that have a matrix format. This is a "reserve" mechanism,
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
        Location of the field. The default is ``"Nodal"``. For example:

        - :class:`ansys.dpf.core.natures.nodal` (``"Nodal"``)
        - :class:`ansys.dpf.core.natures.elemental` (``"Elemental"``)
        - :class:`ansys.dpf.core.natures.elemental_nodal` (``"ElementalNodal"``)
        - ...

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
        server,
        natures.matrix,
        num_entities,
        location,
        num_col,
        num_lines,
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
        Location of the field. The default is ``"Nodal"``. For example:

        - ansys.dpf.core.natures.nodal (``"Nodal"``)
        - ansys.dpf.core.natures.elemental (``"Elemental"``)
        - ansys.dpf.core.natures.elemental_nodal (``"ElementalNodal"``)
        - ...

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
        Location of the field. The default is ``"Nodal"``. For example:

        - :class:`ansys.dpf.core.natures.nodal` (``"Nodal"``)
        - :class:`ansys.dpf.core.natures.elemental` (``"Elemental"``)
        - :class:`ansys.dpf.core.natures.elemental_nodal` (``"ElementalNodal"``)
        - ...

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
        Location of the field. The default is ``"Nodal"``. For example:

        - ansys.dpf.core.natures.nodal (``"Nodal"``)
        - ansys.dpf.core.natures.elemental (``"Elemental"``)
        - ansys.dpf.core.natures.elemental_nodal (``"ElementalNodal"``)
        - ...

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
        Location of the field. The default is ``"Nodal"``. For example:

        - ansys.dpf.core.natures.nodal (``"Nodal"``)
        - ansys.dpf.core.natures.elemental (``"Elemental"``)
        - ansys.dpf.core.natures.elemental_nodal (``"ElementalNodal"``)
        - ...

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
    return _create_field(
        server, natures.vector, num_entities, location, ncomp_n=num_comp
    )


def _create_field(
    server, nature, nentities, location=locations.nodal, ncomp_n=0, ncomp_m=0
):
    """Create a specific :class:`ansys.dpf.core.Field`.

    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow the size of your field.

    Parameters
    ----------
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.
    snature : str
        Nature of the field entity data. For example:

        - :class:`ansys.dpf.core.natures.matrix`
        - :class:`ansys.dpf.core.natures.scalar`

    num_entities : int
        Number of entities to reserve.

    location : str, optional
        Location of the field. For example:

        - :class:`ansys.dpf.core.natures.nodal` (``"Nodal"``)
        - :class:`ansys.dpf.core.natures.elemental` (``"Elemental"``)
        - :class:`ansys.dpf.core.natures.elemental_nodal` (``"ElementalNodal"``)
        - ...

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
        api=api, client=server.client,  nature=nature, nentities=nentities, location=location,
        ncomp_n=ncomp_n, ncomp_m=ncomp_m
    )
    field = Field(field=internal_obj, server=server)
    return field
