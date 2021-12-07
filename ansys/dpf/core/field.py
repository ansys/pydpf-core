"""
.. _ref_field:

Field
=====
"""

from ansys import dpf
from ansys.dpf.core import errors, meshed_region, time_freq_support
from ansys.dpf.core.common import locations, natures, types
from ansys.dpf.core.field_base import _FieldBase, _LocalFieldBase
from ansys.dpf.core.field_definition import FieldDefinition
from ansys.dpf.core.plotter import Plotter
from ansys.grpc.dpf import base_pb2, field_pb2


class Field(_FieldBase):
    """Represents the main simulation data container.

    This can be evaluated data from the :class:`Operator <ansys.dpf.core.Operator>` class
    or created by a factory and directly by an instance of this class.

    A field's data is always associated to its scoping (entities
    associated to each value) and support (subset of the model where the
    data is), making the field a self-describing piece of data.

    Parameters
    ----------
    nentities : int, optional
        Number of entities reserved. The default is ``0``.
    nature : :class:`ansys.dpf.core.common.natures`, optional
        Nature of the field.
    location : str, optional
        Location of the field.  Options are:

        - ``"Nodal"``
        - ``"Elemental"``
        - ``"ElementalNodal"``

    field : ansys.grpc.dpf.field_pb2.Field, optional
        Field message generated from a gRPC stub.
    server : :class:`ansys.dpf.core.server`, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.
    Examples
    --------
    Create a field from scratch.

    >>> from ansys.dpf.core import fields_factory
    >>> from ansys.dpf.core import locations
    >>> from ansys.dpf import core as dpf
    >>> field_with_classic_api = dpf.Field()
    >>> field_with_classic_api.location = locations.nodal
    >>> field_with_factory = fields_factory.create_scalar_field(10)

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
    array([-0.00672665, -0.03213735,  0.00016716])

    """

    def __init__(
        self,
        nentities=0,
        nature=natures.vector,
        location=locations.nodal,
        field=None,
        server=None,
    ):
        """Initialize the field either with an optional field message or
        by connecting to a stub.
        """
        super().__init__(nentities, nature, location, False, field, server)
        self._field_definition = self._load_field_definition()

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
        (array([[0.1, 0.2, 0.3],
               [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
        (array([[0.2, 0.4, 0.6],
               [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
        (array([[0.3, 0.6, 0.9],
               [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])

        """  # noqa: E501
        return _LocalField(self)

    @property
    def location(self):
        """Field location.

        Returns
        -------
        str
            Location string, which is ``"Nodal"``, ``"Elemental"``,
            or ``"ElementalNodal"``.

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
        -------
        location : str or locations
            Location string, which is ``"Nodal"``, ``"Elemental"``,
            or ``"ElementalNodal"``.

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

        op = dpf.core.Operator("to_nodal")
        op.inputs.connect(self)
        return op.outputs.field()

    def plot(self, notebook=None, shell_layers=None):
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
        notebook : bool, optional
            Whether the plotting is in the notebook as
            a static image or is a dynamic plot outside of the
            notebook. The default is ``None``.
        shell_layers : shell_layers, optional
            Enum used to set the shell layers if the model to plot
            contains shell elements. The default is ``None``.
        """
        pl = Plotter(self.meshed_region)
        pl.plot_contour(self, notebook, shell_layers)

    def resize(self, nentities, datasize):
        """Allocate memory.

        Parameters
        ----------
        nentities : int
            Number of IDs in the scoping.
        datasize : int
            Size of the data vector.

        """
        request = field_pb2.UpdateSizeRequest()
        request.field.CopyFrom(self._message)
        request.size.scoping_size = nentities
        request.size.data_size = datasize
        self._stub.UpdateSize(request)

    def _load_field_definition(self):
        """Attempt to load the field definition for this field."""
        try:
            request = field_pb2.GetRequest()
            request.field.CopyFrom(self._message)
            out = self._stub.GetFieldDefinition(request)
            return FieldDefinition(out.field_definition, self._server)
        except:
            return

    @property
    def unit(self):
        """Units for the field.

        Returns
        ----------
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
        """Change the unit for the field

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
        request = field_pb2.GetRequest()
        request.field.CopyFrom(self._message)
        out = self._stub.GetFieldDefinition(request)
        return out.name

    def _set_field_definition(self, field_definition):
        """Set the field definition.

        Parameters
        ----------
        field_definition : :class"`ansys.dpf.core.field_definition.FieldDefinition`

        """
        request = field_pb2.UpdateFieldDefinitionRequest()
        request.field_def.CopyFrom(field_definition._messageDefinition)
        request.field.CopyFrom(self._message)
        self._stub.UpdateFieldDefinition(request)

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

    def _get_meshed_region(self):
        """Retrieve the meshed region.

        Returns
        -------
        :class:`ansys.dpf.core.meshed_region.MeshedRegion`

        """
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("MESHED_REGION")
        try:
            message = self._stub.GetSupport(request)
            return meshed_region.MeshedRegion(mesh=message, server=self._server)
        except:
            raise RuntimeError(
                "The field's support is not a mesh. "
                "Try to retrieve the time frequency support."
            )

    def _get_time_freq_support(self):
        """Retrieve the time frequency support.

        Returns
        -------
        :class:`ansys.dpf.core.time_freq_support.TimeFreqSupport`

        """
        request = field_pb2.SupportRequest()
        request.field.CopyFrom(self._message)
        request.type = base_pb2.Type.Value("TIME_FREQ_SUPPORT")
        try:
            message = self._stub.GetSupport(request)
            return time_freq_support.TimeFreqSupport(
                time_freq_support=message, server=self._server
            )
        except:
            raise RuntimeError(
                "The field's support is not a timefreqsupport.  Try a mesh."
            )

    def _set_support(self, support, support_type: str):
        request = field_pb2.SetSupportRequest()
        request.field.CopyFrom(self._message)
        request.support.type = base_pb2.Type.Value(support_type)
        request.support.id = support._message.id
        self._stub.SetSupport(request)

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
        self._set_support(value, "TIME_FREQ_SUPPORT")

    @property
    def meshed_region(self):
        """Meshed region of the field.

        Return
        ------
        :class:`ansys.dpf.core.meshed_region.MeshedRegion`

        """
        return self._get_meshed_region()

    @meshed_region.setter
    def meshed_region(self, value):
        self._set_support(value, "MESHED_REGION")

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
        if value != 2:
            raise ValueError('Only the value "2" is suppported.')
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

        if hasattr(operators, "math") and hasattr(
            operators.math, "generalized_inner_product"
        ):
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
    (array([[0.1, 0.2, 0.3],
           [0.1, 0.2, 0.3]]), [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    (array([[0.2, 0.4, 0.6],
           [0.2, 0.4, 0.6]]), [[0.2, 0.4, 0.6], [0.2, 0.4, 0.6]])
    (array([[0.3, 0.6, 0.9],
           [0.3, 0.6, 0.9]]), [[0.30000000000000004, 0.6000000000000001, 0.8999999999999999], [0.30000000000000004, 0.6000000000000001, 0.8999999999999999]])

    """  # noqa: E501

    def __init__(self, field):
        super().__init__(field)
