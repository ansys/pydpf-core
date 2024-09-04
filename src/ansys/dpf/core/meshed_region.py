"""
MeshedRegion
============
"""
from __future__ import annotations
import traceback
import warnings
from typing import Union, List, TYPE_CHECKING

import ansys.dpf.core
import ansys.dpf.core.errors

from ansys.dpf.core import scoping, field, fields_container
from ansys.dpf.core.property_field import PropertyField
if TYPE_CHECKING:
    from ansys.dpf.core.results import Result
    from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.check_version import server_meet_version, version_requires
from ansys.dpf.core.common import (
    locations,
    types,
    nodal_properties,
)
from ansys.dpf.core.elements import Elements, element_types
from ansys.dpf.core.nodes import Nodes
from ansys.dpf.core.faces import Faces
from ansys.dpf.core.plotter import DpfPlotter, Plotter
from ansys.dpf.core.cache import class_handling_cache
from ansys.dpf.core import server as server_module
from ansys.dpf.gate import meshed_region_capi, meshed_region_grpcapi


def update_grid(func):
    # Decorate mesh setters to centralize the update logic of pyvista objects.
    def wrapper(*args, **kwargs):
        mesh = args[0]
        if mesh._full_grid is not None:
            # Treat each setter separately to improve performance by updating the minimum required.
            if func.__name__ == "set_coordinates_field":
                # When setting node coordinates
                from ansys.dpf.core.vtk_helper import vtk_update_coordinates

                vtk_update_coordinates(vtk_grid=mesh._full_grid, coordinates_array=args[1].data)

        return func(*args, **kwargs)

    return wrapper


@class_handling_cache
class MeshedRegion:
    """
    Represents a mesh from DPF.

    Parameters
    ----------
    num_nodes : int, optional
        Number of nodes to reserve for mesh creation. The default is ``None``.
    num_elements : int, optional
        Number of elements to reserve for mesh creation. The default is ``None``.
    mesh : ansys.grpc.dpf.meshed_region_pb2.MeshedRegion
        The default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Examples
    --------
    Extract a meshed region from a model.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.find_static_rst())
    >>> meshed_region = model.metadata.meshed_region

    Create a meshed region from scratch (line with 3 beam elements).

    >>> import ansys.dpf.core as dpf
    >>> meshed_region = dpf.MeshedRegion(num_nodes=4,num_elements=3)
    >>> i=0
    >>> for node in meshed_region.nodes.add_nodes(4):
    ...     node.id = i+1
    ...     node.coordinates = [float(i), float(i), 0.0]
    ...     i=i+1
    >>> i=0
    >>> for element in meshed_region.elements.add_elements(3):
    ...     element.id=i+1
    ...     element.connectivity = [i, i+1]
    ...     element.is_beam=True #or is_solid, is_beam, is_point
    ...     i=i+1
    >>> meshed_region.elements.add_beam_element(id=4,connectivity=[3,0])

    """

    def __init__(self, num_nodes=None, num_elements=None, mesh=None, server=None):
        # step 1: get server
        self._server = server_module.get_or_create_server(
            mesh._server if isinstance(mesh, MeshedRegion) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=meshed_region_capi.MeshedRegionCAPI,
            grpcapi=meshed_region_grpcapi.MeshedRegionGRPCAPI,
        )

        # step3: init environment
        self._api.init_meshed_region_environment(self)  # creates stub when gRPC

        # step4: if object exists: take instance, else create it:
        # object_name -> protobuf.message, DPFObject*
        if mesh is not None:
            self._internal_obj = mesh
        else:
            # if no mesh object, create one
            if self._server.has_client():
                self._internal_obj = self._api.meshed_region_new_on_client(self._server.client)
            else:
                self._internal_obj = self._api.meshed_region_new()

        self._full_grid = None
        self._elements = None
        self._nodes = None
        self.as_linear = None

    def _get_scoping(self, loc=locations.nodal):
        """
        Parameters
        ----------
        loc : str or ansys.dpf.core.common.locations, optional
            location of the requested scoping ("Nodal", "Elemental"...)

        Returns
        -------
        scoping : Scoping
            ids of the elements or nodes of the mesh
        """
        if loc is locations.nodal:
            out = self._api.meshed_region_get_shared_nodes_scoping(self)
        elif loc is locations.elemental:
            out = self._api.meshed_region_get_shared_elements_scoping(self)
        else:
            raise TypeError(f"Location {loc} is not recognized.")
        if out is None:
            return
        scop_to_return = scoping.Scoping(scoping=out, server=self._server)
        try:
            check = scop_to_return._api.scoping_fast_access_ptr(scop_to_return)
            if check is None:
                return None
        except NotImplementedError:
            # will throw NotImplementedError for ansys-grpc-dpf
            pass
        except ansys.dpf.core.errors.DPFServerException:
            # and DPFServerException for gRPC CLayer
            pass
        return scop_to_return

    @property
    def elements(self):
        """
        All elemental properties of the mesh, such as connectivity and element types.

        Returns
        -------
        elements : Elements
            Elements belonging to the meshed region.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> elements = meshed_region.elements
        >>> print(elements)
        DPF Elements object with 8 elements

        """
        return Elements(self)

    @property
    def faces(self):
        """
        All face properties of the mesh, such as faces_nodes_connectivity and face types.

        Returns
        -------
        faces : Faces
            Faces belonging to the meshed region.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> faces = meshed_region.faces
        >>> print(faces)
        DPF Faces object with 0 faces

        """
        return Faces(self)

    @property
    def nodes(self):
        """
        All nodal properties of the mesh, such as node coordinates and nodal connectivity.

        Returns
        -------
        nodes : Nodes
            Nodes belonging to the meshed region

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> nodes = meshed_region.nodes
        >>> nodes.n_nodes
        81

        """
        return Nodes(self)

    @property
    def unit(self):
        """
        Unit of the meshed region.

        This unit is the same as the unit of the coordinates of the meshed region.

        Returns
        -------
        unit : str
        """
        return self._get_unit()

    @unit.setter
    def unit(self, value):
        """
        Unit type.

        Parameters
        ----------
        unit : str
        """
        return self._set_unit(value)

    def _get_unit(self):
        """
        Retrieve the unit type.

        Returns
        -------
        unit : str
        """
        return self._api.meshed_region_get_unit(self)

    def _set_unit(self, unit):
        """
        Set the unit of the meshed region.

        Parameters
        ----------
        unit: str
        """
        return self._api.meshed_region_set_unit(self, unit)

    def __del__(self):
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())

    def __str__(self):
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    @property
    def available_property_fields(self):
        """
        Returns a list of available property fields

        Returns
        -------
        available_property_fields : list str
        """
        available_property_fields = []
        n_property_field = self._api.meshed_region_get_num_available_property_field(self)
        for index in range(n_property_field):
            available_property_fields.append(
                self._api.meshed_region_get_property_field_name(self, index)
            )
        return available_property_fields

    def property_field(self, property_name: str) -> Union[field.Field, PropertyField]:
        """
        Property field getter. It can be coordinates (field),
        element types (property field)...

        Returns
        -------
        field_or_property_field:
            Field or PropertyField.
        """
        return self.field_of_properties(property_name)

    @version_requires("3.0")
    def set_property_field(self, property_name: str, value: Union[field.Field, PropertyField]):
        """
        Property field setter. It can be coordinates (field),
        element types (property field)...

        Parameters
        ----------
        property_name:
            property name of the field to set
        value:
        """
        if property_name is nodal_properties.coordinates:
            self.set_coordinates_field(value)
        else:
            self._api.meshed_region_set_property_field(self, property_name, value)

    @update_grid
    @version_requires("3.0")
    def set_coordinates_field(self, coordinates_field: field.Field):
        """
        Coordinates field setter.

        Parameters
        ----------
        coordinates_field:
        """
        self._api.meshed_region_set_coordinates_field(self, coordinates_field)

    @property
    def available_named_selections(self) -> List[str]:
        """
        List of available named selections.

        Returns
        -------
        named_selections:
        """
        return self._get_available_named_selections()

    def _get_available_named_selections(self):
        """
        List of available named selections.

        Returns
        -------
        named_selections : list str
        """
        named_selections = []
        n_selections = self._api.meshed_region_get_num_available_named_selection(self)
        for index in range(n_selections):
            named_selections.append(self._api.meshed_region_get_named_selection_name(self, index))
        return named_selections

    def named_selection(self, named_selection: str) -> scoping.Scoping:
        """
        Scoping containing the list of nodes or elements in the named selection.

        Parameters
        ----------
        named_selection:
            Name of the named selection.

        Returns
        -------
        named_selection:
            Scoping equivalent to the named selection.
        """
        if server_meet_version("2.1", self._server):
            out = self._api.meshed_region_get_named_selection_scoping(self, named_selection)
            return scoping.Scoping(scoping=out, server=self._server)
        else:
            if hasattr(self, "_stream_provider"):
                from ansys.dpf.core.dpf_operator import Operator

                op = Operator("scoping_provider_by_ns", server=self._server)
                op.connect(1, named_selection)
                op.connect(3, self._stream_provider, 0)
                return op.get_output(0, types.scoping)
            else:
                raise Exception(
                    "Getting a named selection from a meshed region is "
                    "only implemented for meshed region created from a "
                    "model for server version 2.0. Please update your server."
                )

    @version_requires("3.0")
    def set_named_selection_scoping(self, named_selection_name: str, scoping: scoping.Scoping):
        """
        Named selection scoping setter.

        Parameters
        ----------
        named_selection_name:
            Name of the named selection.
        scoping:
            Scoping to associate to the named selection.
        """
        return self._api.meshed_region_set_named_selection_scoping(
            self, named_selection_name, scoping
        )

    def _set_stream_provider(self, stream_provider):
        self._stream_provider = stream_provider

    # NOTE: kept only for reference as the mesh operator is being moved out of dpf
    # def write_vtk(self, filename, skin_only=True):
    #     """Return a vtk mesh"""
    #     # filename = os.path.join(tempfile.gettempdir(),
    #                             # '%s.vtk' % next(tempfile._get_candidate_names()))

    #     vtk_exp = self._model.operator("vtk_export")
    #     vtk_exp.connect(0, filename)

    #     mesh = self._model.operator("mapdl::rst::MeshProvider")
    #     mesh.connect(4, self._model.data_sources)

    #     if skin_only:
    #         skin = self._model.operator("meshed_skin_sector")
    #         skin.connect(0, mesh, 0)
    #         vtk_exp.connect(1, skin, 0)
    #     else:
    #         vtk_exp.connect(1, mesh, 0)

    #     vtk_exp.run()
    #     if not os.path.isfile(filename):
    #         raise FileNotFoundError('VTK mesh not written to disk')

    # @property
    # def skin(self):
    #     """Surface of the meshed region."""
    #     mesh = self._model.operator("mapdl::rst::MeshProvider")
    #     mesh.connect(4, self._model.data_sources)

    #     skin = self._model.operator("meshed_skin_sector")
    #     skin.connect(0, mesh, 0)
    #     # skin.connect(4, self)

    #     skin.get_output(0, types.meshed_region)

    #     name = None
    #     if self._name:
    #         name = 'Skin of %s' % self._name
    #     self._internal_obj = skin.get_output(0, types.meshed_region)
    #     return MeshedRegion(self._server.channel, skin, self._model, name)

    def deform_by(self, deform_by, scale_factor=1.0):
        """
        Deforms the mesh according to a 3D vector field and an additional scale factor.

        Parameters
        ----------
        deform_by : Field, FieldsContainer, Result, Operator
            Used to deform the plotted mesh. Must output a unique 3D vector field.
            Defaults to None.
        scale_factor : float, Field, FieldsContainer, optional
            Used to scale the mesh deformation. Defaults to 1.0. Can be a scalar Field
            (or a FieldsContainer with only one Field) to get a spatially non-homogeneous scaling.
        Returns
        -------

        """
        from ansys.dpf.core.operators.math import add, scale, unit_convert

        if hasattr(deform_by, "eval"):
            # If a Result or an Operator, eval and get the field.
            deform_by = deform_by.eval()[0]
        if isinstance(deform_by, ansys.dpf.core.fields_container.FieldsContainer):
            # If a FieldsContainer, take the field.
            deform_by = deform_by[0]
        if deform_by.unit != self.unit:
            unit_convert(deform_by, self.unit)
        scale_op = scale(field=deform_by, ponderation=scale_factor)
        return add(fieldA=self.nodes.coordinates_field, fieldB=scale_op.outputs.field).eval()

    def _as_vtk(self, coordinates=None, as_linear=True, include_ids=False):
        """Convert DPF mesh to a PyVista unstructured grid."""
        try:
            from ansys.dpf.core.vtk_helper import dpf_mesh_to_vtk
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plotting capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )
        grid = dpf_mesh_to_vtk(self, coordinates, as_linear)

        # consider adding this when scoping request is faster
        if include_ids:
            self._nodeids = self.nodes.scoping.ids
            self._elementids = self.elements.scoping.ids
            grid["node_ids"] = self._nodeids
            grid["element_ids"] = self._elementids

        self.as_linear = as_linear  # store as_linear to avoid passing through here again
        return grid

    @property
    def grid(self):
        """
        Unstructured grid in VTK format from PyVista.

        Returns
        -------
        pyvista.UnstructuredGrid
            UnstructuredGrid of the mesh.

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> grid = meshed_region.grid

        Plot this grid directly.

        >>> grid.plot()

        Extract the surface mesh of this grid

        >>> mesh = grid.extract_surface()

        """
        if self._full_grid is None:
            self._full_grid = self._as_vtk(self.nodes.coordinates_field)
        return self._full_grid

    def plot(
        self,
        field_or_fields_container: Union[
            field.Field, PropertyField, fields_container.FieldsContainer, None
        ] = None,
        shell_layers=None,
        deform_by: Union[field.Field, Result, Operator, None] = None,
        scale_factor: float = 1.0,
        **kwargs,
    ):
        """
        Plot the mesh, bare or with data.

        Parameters
        ----------
        field_or_fields_container:
            Field, PropertyField, or FieldsContainer to plot on the mesh.
        shell_layers: core.shell_layers, optional
            Enum used to set the shell layers if the model to plot contains shell elements.
        deform_by: Field, Result, Operator, optional
            Used to deform the plotted mesh. Must output a 3D vector field.
            Defaults to None.
        scale_factor:
            Scaling factor to apply when warping the mesh.
        **kwargs: optional
            Additional keyword arguments for the plotter. For additional keyword
            arguments, see ``help(pyvista.plot)``.

        Examples
        --------
        Plot the displacement field from an example file.

        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> disp = model.results.displacement()
        >>> field = disp.outputs.fields_container()[0]
        >>> model.metadata.meshed_region.plot(field)

        """
        if isinstance(field_or_fields_container, (field.Field, fields_container.FieldsContainer)):
            pl = Plotter(self, **kwargs)
            return pl.plot_contour(
                field_or_fields_container,
                shell_layers,
                show_axes=kwargs.pop("show_axes", True),
                deform_by=deform_by,
                scale_factor=scale_factor,
                **kwargs,
            )

        # otherwise, simply plot the mesh
        pl = DpfPlotter(**kwargs)
        pl.add_mesh(
            self,
            deform_by=deform_by,
            scale_factor=scale_factor,
            show_axes=kwargs.pop("show_axes", True),
            **kwargs,
        )
        if isinstance(field_or_fields_container, PropertyField):
            pl.add_field(field=field_or_fields_container, meshed_region=self, **kwargs)
        kwargs.pop("notebook", None)
        return pl.show_figure(**kwargs)

    def deep_copy(self, server=None):
        """
        Create a deep copy of the meshed region's data on a given server.

        This method is useful for passing data from one server instance to another.

        Parameters
        ----------
        server : ansys.dpf.core.server, optional
            Server with the channel connected to the remote or local instance.
            The default is ``None``, in which case an attempt is made to use the
            global server.

        Returns
        -------
        mesh_copy : MeshedRegion

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> other_server = dpf.start_local_server(as_global=False)
        >>> deep_copy = meshed_region.deep_copy(server=other_server)

        """
        if self._server.config.legacy:
            if self.nodes.scoping is None:  # empty Mesh
                return MeshedRegion()
            node_ids = self.nodes.scoping.ids
            element_ids = self.elements.scoping.ids
            mesh = MeshedRegion(
                num_nodes=len(node_ids), num_elements=len(element_ids), server=server
            )
            with self.nodes.coordinates_field.as_local_field() as coord:
                for i, node in enumerate(mesh.nodes.add_nodes(len(node_ids))):
                    node.id = node_ids[i]
                    node.coordinates = coord.get_entity_data(i)
            with self.elements.connectivities_field.as_local_field() as connect:
                with self.elements.element_types_field.as_local_field() as types:
                    for i, elem in enumerate(mesh.elements.add_elements(len(element_ids))):
                        elem.id = element_ids[i]
                        elem.connectivity = connect.get_entity_data(i)
                        elem.shape = element_types.shape(types.get_entity_data(i)[0])
            mesh.unit = self.unit
            return mesh
        else:
            from ansys.dpf.core.core import _deep_copy

            return _deep_copy(self, server=server)

    def field_of_properties(self, property_name):
        """
        Returns the ``Field`` or ``PropertyField`` associated
        to a given property of the mesh

        Parameters
        ----------
        property_name : str, common.elemental_properties, common.nodal_properties
            Name of the property.

        Returns
        -------
        properties : Field, PropertyField

        Examples
        --------
        >>> import ansys.dpf.core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.find_static_rst())
        >>> meshed_region = model.metadata.meshed_region
        >>> connectivity = meshed_region.field_of_properties(
        ...     dpf.common.elemental_properties.connectivity)
        >>> coordinates = meshed_region.field_of_properties(dpf.common.nodal_properties.coordinates)
        """
        if property_name is nodal_properties.coordinates:
            field_out = self._api.meshed_region_get_coordinates_field(self)
            return field.Field(server=self._server, field=field_out)
        else:
            field_out = self._api.meshed_region_get_property_field(self, property_name)
            if isinstance(field_out, int):
                res = PropertyField(server=self._server, property_field=field_out)
                return res
            else:
                if field_out.datatype == "int":
                    return PropertyField(
                        server=self._server, property_field=field_out
                    )
                else:
                    # Not sure we go through here since the only datatype not int is coordinates,
                    # which is already dealt with previously.
                    return field.Field(server=self._server, field=field_out)
