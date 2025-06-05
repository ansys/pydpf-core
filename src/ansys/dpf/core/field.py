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

"""Field."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ansys import dpf
from ansys.dpf.core import dimensionality, errors, meshed_region, scoping, time_freq_support
from ansys.dpf.core.common import (
    _get_size_of_list,
    locations,
    natures,
    shell_layers as eshell_layers,
    types,
)
from ansys.dpf.core.field_base import _FieldBase, _LocalFieldBase
from ansys.dpf.core.field_definition import FieldDefinition
from ansys.dpf.gate import (
    dpf_array,
    dpf_vector,
    field_abstract_api,
    field_capi,
    field_grpcapi,
)
from ansys.dpf.gate.errors import DPFServerException

if TYPE_CHECKING:  # pragma: nocover
    from ansys.dpf.core.dpf_operator import Operator
    from ansys.dpf.core.meshed_region import MeshedRegion
    from ansys.dpf.core.results import Result


class Field(_FieldBase):
    """Represents the main simulation data container.

    This can be evaluated data from the :class:`Operator <ansys.dpf.core.Operator>` class
    or created by a factory and directly by an instance of this class.

    A field's data is always associated to its scoping (entities
    associated to each value) and support (subset of the model where the
    data is), making the field a self-describing piece of data.

    The field's scoping defines the order of the data, for example: the first ID in the
    ``scoping`` identifies to which entity the first ``entity data`` belongs.

    The minimum requirement for a well defined field is for it to have a dimensionality
    (scalar, three components vector, six components symmetrical matrix, and so on), a location
    ("Nodal", "Elemental", "ElementalNodal", "TimeFreq"), a data vector, and a scoping with IDs.
    You can also set the number of shell layers. If the field has one elementary data by entity
    (elementary data size equals the number of components for "Nodal" or "Elemental" field for example),
    then the data vector can be set directly. If a more complex field is required
    ("ElementalNodal" field for example), the data can be set entity by entity.

    For more information, see `Fields container and fields
    <https://dpf.docs.pyansys.com/version/stable/user_guide/fields_container.html>`_.


    Parameters
    ----------
    nentities : int, optional
        Number of entities reserved. The default is ``0``.
    nature : :class:`ansys.dpf.core.common.natures`, optional
        Nature of the field.
    location : str, optional
        Location of the field.  Options are in :class:`locations <ansys.dpf.core.common.locations>`

        - ``dpf.locations.nodal``
        - ``dpf.locations.elemental``
        - ``dpf.locations.elemental_nodal``
        - ...

    field : Field, ansys.grpc.dpf.field_pb2.Field, ctypes.c_void_p, optional
        Field message generated from a gRPC stub, or returned by DPF's C clients.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    Create a field from scratch.

    >>> from ansys.dpf.core import locations
    >>> from ansys.dpf import core as dpf
    >>> field_with_classic_api = dpf.Field()
    >>> field_with_classic_api.location = locations.nodal

    Create a symmetrical matrix elemental field from scratch.

    >>> from ansys.dpf import core as dpf
    >>> num_entities = 2
    >>> my_field = dpf.Field(num_entities, dpf.natures.symmatrix, locations.elemental)
    >>> my_scoping = dpf.Scoping(location=locations.elemental, ids=[1, 2])
    >>> my_field.scoping = my_scoping

    Add all the data at once.

    >>> from ansys.dpf import core as dpf
    >>> my_data = [1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0]
    >>> my_field.data = my_data

    Add data entity by entity.

    >>> from ansys.dpf import core as dpf
    >>> my_elem_data = [1.0,1.0,1.0,0.0,0.0,0.0]
    >>> my_field.append(my_elem_data, scopingid=1)
    >>> my_field.append(my_elem_data, scopingid=2)

    Create a nodal scalar field using the fields factory.

    >>> from ansys.dpf.core import fields_factory
    >>> from ansys.dpf import core as dpf
    >>> my_scalar_field = fields_factory.create_scalar_field(num_entities=2, location=locations.nodal)
    >>> my_scalar_field.data = [1.0, 3.0]

    Extract a displacement field from a transient result file.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> fields_container = disp.outputs.fields_container()
    >>> field = fields_container[0]
    >>> len(field)
    11460
    >>> field.component_count
    3
    >>> field.elementary_data_count
    3820

    Create a displacement field.

    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
    >>> my_field.data = np.zeros(30)
    >>> my_field.scoping.ids = range(1,11)

    Set data.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> disp = model.results.displacement()
    >>> fields_container = disp.outputs.fields_container()
    >>> field = fields_container[0]
    >>> field.data[2]
    DPFArray([-0.00672665, -0.03213735,  0.00016716]...

    Accessing data with a custom order.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> ids_order = [2,3]
    >>> stress = model.results.stress(mesh_scoping=dpf.Scoping(
    ...     ids=ids_order, location=dpf.locations.nodal))
    >>> fields_container = stress.outputs.fields_container()
    >>> field = fields_container[0]
    >>> field.scoping.ids
    DPFArray([3, 2]...
    >>> field.data
    DPFArray([[  3755059.33333333,  -2398534.3515625 , -27519072.33333333,
                 2194748.65625   ,   8306637.58333333,   2018637.03125   ],
              [  2796852.09375   ,   -992492.62304688,  22519752.625     ,
                -1049027.46875   ,  10846776.1875    ,   4119072.3125    ]]...
    >>> field.get_entity_data_by_id(2)
    DPFArray([[ 2796852.09375   ,  -992492.62304688, 22519752.625     ,
               -1049027.46875   , 10846776.1875    ,  4119072.3125    ]]...
    >>> field.get_entity_data_by_id(3)
    DPFArray([[  3755059.33333333,  -2398534.3515625 , -27519072.33333333,
                 2194748.65625   ,   8306637.58333333,   2018637.03125   ]]...

    """

    def __init__(
        self,
        nentities=0,
        nature=natures.vector,
        location=locations.nodal,
        field=None,
        server=None,
    ):
        """Initialize the field either with an optional field message or by connecting to a stub."""
        super().__init__(
            nentities=nentities,
            nature=nature,
            location=location,
            field=field,
            server=server,
        )
        self._field_definition = self._load_field_definition()

    @property
    def _api(self) -> field_abstract_api.FieldAbstractAPI:
        if not self._api_instance:
            self._api_instance = self._server.get_api_for_type(
                capi=field_capi.FieldCAPI, grpcapi=field_grpcapi.FieldGRPCAPI
            )
        return self._api_instance

    def _init_api_env(self):
        self._api.init_field_environment(self)

    @staticmethod
    def _field_create_internal_obj(
        api: field_abstract_api.FieldAbstractAPI,
        client,
        nature,
        nentities,
        location=locations.nodal,
        ncomp_n=0,
        ncomp_m=0,
        with_type=None,
    ):
        dim = dimensionality.Dimensionality([ncomp_n, ncomp_m], nature)

        if dim.is_1d_dim():
            if client is not None:
                return api.field_new_with1_ddimensionnality_on_client(
                    client, dim.nature.value, dim.dim[0], nentities, location
                )
            else:
                return api.field_new_with1_ddimensionnality(
                    dim.nature.value, dim.dim[0], nentities, location
                )
        elif dim.is_2d_dim():
            if client is not None:
                return api.field_new_with2_ddimensionnality_on_client(
                    client,
                    dim.nature.value,
                    dim.dim[0],
                    dim.dim[1],
                    nentities,
                    location,
                )
            else:
                return api.field_new_with2_ddimensionnality(
                    dim.nature.value, dim.dim[0], dim.dim[1], nentities, location
                )
        else:
            raise AttributeError("Unable to parse field's attributes to create an instance.")

    def as_local_field(self):
        """Create a deep copy of the field that can be accessed and modified locally.

        This method allows you to access and modify the local copy of the field
        without sending a request to the server. It should be used in a ``with``
        statement so that the local field is released and the data is sent to
        the server in one action. If it is not used in a ``with`` statement,
        :func:`<release_data> Field.release_data()` should be used to update the field.

        Warning
        -------
        If this `as_local_field` method is not used as a context manager in a
        ``with`` statement or if the method `release_data()` is not called,
        the data will not be updated.

        Returns
        -------
        local_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> num_entities = 3
        >>> field_to_local = dpf.fields_factory.create_3d_vector_field(num_entities, location=dpf.locations.elemental_nodal)
        >>> with field_to_local.as_local_field() as f:
        ...     for i in range(1,num_entities+1):
        ...         f.append([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]],i)
        ...         f.get_entity_data(i-1),[[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]
        (DPFArray([[0.1, 0.2, 0.3],
                  [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        (DPFArray([[0.2, 0.4, 0.6],
                  [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
        (DPFArray([[0.3, 0.6, 0.9],
                  [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])

        """  # noqa: E501
        # Do not copy data if using InProcess server
        if self._server.client is not None:
            return _LocalField(self)
        else:
            return self

    @property
    def location(self):
        """Field location.

        Returns
        -------
        str
            Location string, Options are in :class:`locations <ansys.dpf.core.common.locations>`.

        Examples
        --------
        Location for a stress field evaluated at nodes.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.download_transient_result())
        >>> s_op = model.results.stress()
        >>> s_fc = s_op.outputs.fields_container()
        >>> field = s_fc[0]
        >>> field.location
        'ElementalNodal'

        """
        if self.field_definition:
            return self.field_definition.location

    @location.setter
    def location(self, value):
        """Change the field location.

        Parameters
        ----------
        location : str or locations
            Location string, Options are in :class:`locations <ansys.dpf.core.common.locations>`.

        Examples
        --------
        Location for a field evaluated at nodes.

        >>> from ansys.dpf import core as dpf
        >>> import numpy as np
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.data = np.zeros(30)
        >>> my_field.scoping.ids = range(1,11)
        >>> my_field.location
        'Nodal'
        >>> my_field.location = dpf.locations.elemental_nodal
        >>> my_field.location
        'ElementalNodal'

        """
        fielddef = self.field_definition
        fielddef.location = value
        self.field_definition = fielddef

    @property
    def component_count(self):
        """Number of components."""
        return self._api.csfield_get_number_of_components(self)

    @property
    def elementary_data_count(self):
        """Number of elementary data."""
        return self._api.csfield_get_number_elementary_data(self)

    @property
    def size(self):
        """Size of data."""
        return self._api.csfield_get_data_size(self)

    def _set_scoping(self, scoping):
        self._api.csfield_set_cscoping(self, scoping)

    def _get_scoping(self):
        obj = self._api.csfield_get_cscoping(self)
        if obj is not None:
            return scoping.Scoping(scoping=obj, server=self._server)

    @property
    def shell_layers(self):
        """Order of the shell layers.

        Returns
        -------
        :class:`ansys.dpf.core.common.shell_layers`

        """
        if self.field_definition:
            return self.field_definition.shell_layers

    @shell_layers.setter
    def shell_layers(self, value):
        fielddef = self.field_definition
        fielddef.shell_layers = value
        self.field_definition = fielddef

    def get_entity_data(self, index: int) -> dpf_array.DPFArray:
        """Retrieve entity data by index."""
        try:
            vec = dpf_vector.DPFVectorDouble(owner=self)
            self._api.csfield_get_entity_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, index
            )
            data = dpf_array.DPFArray(vec)

        except NotImplementedError:
            data = self._api.csfield_get_entity_data(self, index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def get_entity_data_by_id(self, id: int) -> dpf_array.DPFArray:
        """Retrieve entity data by id."""
        try:
            vec = dpf_vector.DPFVectorDouble(owner=self)
            self._api.csfield_get_entity_data_by_id_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size, id
            )
            data = dpf_array.DPFArray(vec)

        except NotImplementedError:
            index = self.scoping.index(id)
            if index < 0:
                raise ValueError(f"The ID {id} must be greater than 0.")
            data = self.get_entity_data(index)
        n_comp = self.component_count
        if n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def append(self, data, scopingid):
        """Append data to the Field."""
        if isinstance(data, list):
            if isinstance(data[0], list):
                data = np.array(data)
        self._api.csfield_push_back(self, scopingid, _get_size_of_list(data), data)

    def _get_data_pointer(self):
        try:
            vec = dpf_vector.DPFVectorInt(owner=self)
            self._api.csfield_get_data_pointer_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            return dpf_array.DPFArray(vec)

        except NotImplementedError:
            return self._api.csfield_get_data_pointer(self, True)

    def _set_data_pointer(self, data):
        return self._api.csfield_set_data_pointer(self, _get_size_of_list(data), data)

    def _get_data(self, np_array=True):
        try:
            vec = dpf_vector.DPFVectorDouble(owner=self)
            self._api.csfield_get_data_for_dpf_vector(
                self, vec, vec.internal_data, vec.internal_size
            )
            data = dpf_array.DPFArray(vec) if np_array else dpf_array.DPFArray(vec).tolist()
        except NotImplementedError:
            data = self._api.csfield_get_data(self, np_array)
        n_comp = self.component_count
        if np_array and n_comp != 1 and data.size != 0:
            data.shape = (data.size // n_comp, n_comp)
        return data

    def _set_data(self, data):
        if isinstance(data, list):
            if all(isinstance(d, list) for d in data):
                # Transform list of list to numpy_array
                data = np.array(data)
        if isinstance(data, (np.ndarray, np.generic)):
            if (
                0 != self.size
                and self.component_count > 1
                and data.size // self.component_count != data.size / self.component_count
            ):
                raise ValueError(
                    f"An array of shape {self.shape} is expected and "
                    f"shape {data.shape} was input"
                )
            if data.dtype != np.float64:
                copy = np.empty_like(data, shape=data.shape, dtype=np.float64)
                copy[:] = data
                data = copy
        size = _get_size_of_list(data)
        return self._api.csfield_set_data(self, size, data)

    def to_nodal(self):
        """Convert the field to one with a ``Nodal`` location.

        This method is valid only when the field's current location is
        ``ElementalNodal`` or ``Elemental``.

        Returns
        -------
        nodal_field : Field
            with ``location=='Nodal'``.
        """
        if self.location == "Nodal":
            raise errors.LocationError('Location is already "Nodal"')

        op = dpf.core.Operator("to_nodal", server=self._server)
        op.inputs.connect(self)
        return op.outputs.field()

    def plot(
        self,
        shell_layers: eshell_layers = None,
        deform_by: Union[Field, Result, Operator] = None,
        scale_factor: float = 1.0,
        meshed_region: MeshedRegion = None,
        **kwargs,
    ):
        """Plot the field or fields container on the mesh support if it exists.

        Warning
        -------
        This method is primarily added out of convenience as plotting
        directly from the field can be slower than extracting the
        meshed region and plotting the field on top of that.  It is
        more efficient to plot with:

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> mesh = model.metadata.meshed_region
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> mesh.plot(field)

        Parameters
        ----------
        shell_layers:
            Enum used to set the shell layers if the model to plot
            contains shell elements. Defaults to the top layer.
        deform_by:
            Used to deform the plotted mesh. Must output a 3D vector field.
        scale_factor:
            Scaling factor to apply when warping the mesh.
        meshed_region:
            Mesh to plot the field on.
        **kwargs:
            Additional keyword arguments for the plotter. For additional keyword
            arguments, see ``help(pyvista.plot)``.
        """
        from ansys.dpf.core.plotter import Plotter

        if meshed_region is None:
            meshed_region = self.meshed_region
        pl = Plotter(meshed_region, **kwargs)
        return pl.plot_contour(
            self,
            shell_layers,
            deform_by=deform_by,
            scale_factor=scale_factor,
            show_axes=kwargs.pop("show_axes", True),
            **kwargs,
        )

    def resize(self, nentities, datasize):
        """Allocate memory.

        Parameters
        ----------
        nentities : int
            Number of IDs in the scoping.
        datasize : int
            Size of the data vector.

        """
        return self._api.csfield_resize(self, datasize, nentities)

    def _load_field_definition(self):
        """Attempt to load the field definition for this field."""
        try:
            out = self._api.csfield_get_shared_field_definition(self)
            return FieldDefinition(out, self._server)
        except:
            return

    @property
    def unit(self):
        """Units for the field.

        Returns
        -------
        str
           Units for the field.

        Examples
        --------
        Units for a displacement field.

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'

        """
        if self.field_definition:
            return self.field_definition.unit

    @unit.setter
    def unit(self, value):
        """Change the unit for the field.

        Parameters
        ----------
        value : str
            Units for the field.

        Examples
        --------
        Units for a displacement field.

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.unit = "m"
        >>> my_field.unit
        'm'

        """
        fielddef = self.field_definition
        fielddef.unit = value
        self.field_definition = fielddef

    @property
    def dimensionality(self):
        """Dimensionality represents the shape of the elementary data contained in the field.

        Returns
        -------
        dimensionality : :class:`ansys.dpf.core.dimensionality.Dimensionality`
            Nature and size of the elementary data.
        """
        if self.field_definition:
            return self.field_definition.dimensionality

    @dimensionality.setter
    def dimensionality(self, value):
        fielddef = self.field_definition
        fielddef.dimensionality = value
        self.field_definition = fielddef

    @property
    def name(self):
        """Name of the field."""
        from ansys.dpf.gate import integral_types

        size = integral_types.MutableInt32()
        name = integral_types.MutableString(256)
        self._field_definition._api.csfield_definition_fill_name(
            self._field_definition, name=name, size=size
        )
        return str(name)

    @name.setter
    def name(self, value):
        """Change the name of the field.

        Parameters
        ----------
        value : str
            Name of the field.

        Examples
        --------
        Units for a displacement field.

        >>> from ansys.dpf import core as dpf
        >>> my_field = dpf.Field(10, dpf.natures.vector,dpf.locations.nodal)
        >>> my_field.name = "my-field"
        >>> my_field.name
        'my-field'

        """
        self._field_definition._api.csfield_definition_set_name(self._field_definition, name=value)

    def _set_field_definition(self, field_definition):
        """Set the field definition.

        Parameters
        ----------
        field_definition : :class"`ansys.dpf.core.field_definition.FieldDefinition`

        """
        self._api.csfield_set_field_definition(self, field_definition)

    @property
    def field_definition(self):
        """Field information, including its location, unit, dimensionality, and shell layers.

        Returns
        -------
        :class:`ansys.dpf.core.field_definition.FieldDefinition`

        """
        return self._field_definition

    @field_definition.setter
    def field_definition(self, value):
        return self._set_field_definition(value)

    def _get_meshed_region(self) -> MeshedRegion:
        """Retrieve the meshed region.

        Returns
        -------
        :class:`ansys.dpf.core.meshed_region.MeshedRegion`

        """
        try:
            support = self._api.csfield_get_support_as_meshed_region(self)
        except DPFServerException as e:
            if "the field doesn't have this support type" in str(e):
                support = None
            else:
                raise e
        return meshed_region.MeshedRegion(
            mesh=support,
            server=self._server,
        )

    def _get_time_freq_support(self):
        """Retrieve the time frequency support.

        Returns
        -------
        :class:`ansys.dpf.core.time_freq_support.TimeFreqSupport`

        """
        return time_freq_support.TimeFreqSupport(
            time_freq_support=self._api.csfield_get_support_as_time_freq_support(self),
            server=self._server,
        )

    def _set_support(self, support, support_type: str):
        self._api.csfield_set_meshed_region_as_support(self, support)

    @property
    def time_freq_support(self):
        """Time frequency support of the field.

        Returns
        -------
        :class:`ansys.dpf.core.time_freq_support.TimeFreqSupport`

        """
        return self._get_time_freq_support()

    @time_freq_support.setter
    def time_freq_support(self, value):
        self._api.csfield_set_support(self, value)

    @property
    def meshed_region(self) -> MeshedRegion:
        """Meshed region of the field.

        Return
        ------
        :class:`ansys.dpf.core.meshed_region.MeshedRegion`

        """
        return self._get_meshed_region()

    @meshed_region.setter
    def meshed_region(self, value: MeshedRegion):
        self._set_support(support=value, support_type="MESHED_REGION")

    def __add__(self, field_b):
        """Add two fields.

        Returns
        -------
        :class:`ansys.dpf.core.operators.math.add.add`

        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "add"):
            op = operators.math.add(server=self._server)
        else:
            op = dpf_operator.Operator("add", server=self._server)
        op.connect(0, self)
        op.connect(1, field_b)
        return op

    def __pow__(self, value):
        """Compute element-wise field[i]^2."""
        if value != 2:
            raise ValueError('Only the value "2" is supported.')
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "sqr"):
            op = operators.math.sqr(self, server=self._server)
        else:
            op = dpf_operator.Operator("sqr", server=self._server)
            op.connect(0, self)
        return op

    def __mul__(self, value):
        """Multiplies two fields.

        Returns
        -------
        :class:`ansys.dpf.core.operators.math.generalized_inner_product.generalized_inner_product`

        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "generalized_inner_product"):
            op = operators.math.generalized_inner_product(server=self._server)
        else:
            op = dpf_operator.Operator("generalized_inner_product", server=self._server)
        op.connect(0, self)
        op.connect(1, value)
        return op

    def __sub__(self, fields_b):
        """Subtract two fields.

        Returns
        -------
        :class:`ansys.dpf.core.operators.math.minus.minus`

        """
        from ansys.dpf.core import dpf_operator, operators

        if hasattr(operators, "math") and hasattr(operators.math, "minus"):
            op = operators.math.minus(server=self._server)
        else:
            op = dpf_operator.Operator("minus", server=self._server)
        op.connect(0, self)
        op.connect(1, fields_b)
        return op

    def _min_max(self):
        from ansys.dpf.core import dpf_operator

        op = dpf_operator.Operator("min_max", server=self._server)
        op.connect(0, self)
        return op

    def min(self):
        """Retrieve the component-wise minimum over this field.

        Returns
        -------
        min : Field
            Component-wise minimum field.
        """
        return self._min_max().get_output(0, types.field)

    def max(self):
        """Retrieve the component-wise maximum over this field.

        Returns
        -------
        max : Field
            Component-wise maximum field.
        """
        return self._min_max().get_output(1, types.field)

    def deep_copy(self, server=None):
        """Create a deep copy of the field's data on a given server.

        This method can be useful for passing data from one server instance to another.

        Parameters
        ----------
        server : :class:`ansys.dpf.core.server`, optional
            Server with the channel connected to the remote or local instance. The
            default is ``None``, in which case an attempt is made to use the global
            server.

        Returns
        -------
        field_copy : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        >>> disp = model.results.displacement()
        >>> fields_container = disp.outputs.fields_container()
        >>> field = fields_container[0]
        >>> other_server = dpf.start_local_server(as_global=False)
        >>> deep_copy = field.deep_copy(server=other_server)

        """
        f = Field(
            nentities=len(self.scoping),
            location=self.location,
            nature=self.field_definition.dimensionality.nature,
            server=server,
        )
        f.scoping = self.scoping.deep_copy(server)
        f.data = self.data
        f.unit = self.unit
        f.location = self.location
        f.field_definition = self.field_definition.deep_copy(server)
        try:
            f._data_pointer = self._data_pointer
        except:
            pass
        try:
            f.meshed_region = self.meshed_region.deep_copy(server=server)
        except:
            pass
        try:
            f.time_freq_support = self.time_freq_support.deep_copy(server=server)
        except:
            pass

        return f


class _LocalField(_LocalFieldBase, Field):
    """Caches the internal data of a field so that it can be modified locally.

    A single update request is to the server when the local field is deleted.

    Parameters
    ----------
    field : Field
        Field to copy

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> import numpy as np
    >>> num_entities = 3
    >>> field_to_local = dpf.fields_factory.create_3d_vector_field(num_entities, location=dpf.locations.elemental_nodal)
    >>> with field_to_local.as_local_field() as f:
    ...     for i in range(1,num_entities+1):
    ...         f.append(np.array([[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]),i)
    ...         f.get_entity_data(i-1),[[0.1*i,0.2*i, 0.3*i],[0.1*i,0.2*i, 0.3*i]]
    (DPFArray([[0.1, 0.2, 0.3],
              [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    (DPFArray([[0.2, 0.4, 0.6],
              [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
    (DPFArray([[0.3, 0.6, 0.9],
              [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])

    """  # noqa: E501

    def __init__(self, field):
        self._is_property_field = False
        Field.__init__(self, field=field)
        _LocalFieldBase.__init__(self, field)
