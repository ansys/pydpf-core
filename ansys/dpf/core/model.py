"""
.. _ref_model:

Model
=====
Module contains the Model class to manage file result models.


"""

from ansys import dpf
from ansys.dpf.core import Operator
from ansys.dpf.core.common import types
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.results import Results, CommonResults
from ansys.dpf.core.server_types import LOG
from ansys.dpf.core import misc
from ansys.dpf.core.errors import protect_source_op_not_found
from ansys.dpf.core._model_helpers import DataSourcesOrStreamsConnector
from grpc._channel import _InactiveRpcError
from ansys.dpf.core.check_version import version_requires


class Model:
    """Connects to a gRPC DPF server and allows access to a result using the DPF framework.

    Parameters
    ----------
    data_sources : str, dpf.core.DataSources, os.PathLike
        Accepts either a :class:`dpf.core.DataSources` instance or the path of the
        result file to open as an os.PathLike object or a str. The default is ``None``.
    server : server.DPFServer, optional
        Server with the channel connected to the remote or local instance. The
        default is ``None``, in which case an attempt is made to use the global
        server.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)

    """

    def __init__(self, data_sources=None, server=None):
        """Initialize connection with DPF server."""

        if server is None:
            server = dpf.core._global_server()

        self._data_sources = data_sources
        self._server = server
        self._metadata = None
        self._results = None
        self._mesh_by_default = True

    @property
    def metadata(self):
        """Model metadata.

        Includes:

        - ``data_sources``
        - ``meshed_region``
        - ``time_freq_support``
        - ``result_info``
        - ``mesh_provider``

        Returns
        -------
        metadata : Metadata

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)

        Get the meshed region of the model and extract the element
        numbers.

        >>> meshed_region = model.metadata.meshed_region
        >>> meshed_region.elements.scoping.ids[2]
        759

        Get the data sources of the model.

        >>> ds = model.metadata.data_sources

        Print the number of result sets.

        >>> tf = model.metadata.time_freq_support
        >>> tf.n_sets
        35

        Get the unit system used in the analysis.

        >>> rinfo = model.metadata.result_info
        >>> rinfo.unit_system
        'MKS: m, kg, N, s, V, A, degC'

        """
        if not self._metadata:
            self._metadata = Metadata(self._data_sources, self._server)
        return self._metadata

    @property
    def results(self):
        """Available results of the model.

        Organizes the results from DPF into accessible methods. All the available
        results are dynamically created depending on the model's class:`ansys.dpf.core.result_info`.

        Returns
        -------
        results: Results, CommonResults
            Available results of the model if possible, else
            returns common results.

        Attributes
        ----------
        all types of results : Result
            Result provider helper wrapping all types of provider available for a
            given result file.

            Examples
            --------
            >>> from ansys.dpf import core as dpf
            >>> from ansys.dpf.core import examples
            >>> model = dpf.Model(examples.electric_therm)
            >>> v = model.results.electric_potential
            >>> dissip = model.results.thermal_dissipation_energy

        Examples
        --------
        Extract the result object from a model.

        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.simple_bar)
        >>> results = model.results # printable object

        Access the displacement at all times.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> displacements = model.results.displacement.on_all_time_freqs.eval()

        """
        if not self._results:
            args = [self.metadata._build_connector(), self.metadata.result_info,
                    self.mesh_by_default, self._server]
            if misc.DYNAMIC_RESULTS:
                try:
                    self._results = Results(*args)
                    if len(self._results) == 0:
                        self._results = CommonResults(*args)
                except Exception as e:
                    self._results = CommonResults(*args)
                    LOG.debug(str(e))
            else:
                self._results = CommonResults(*args)
        return self._results

    def operator(self, name):
        """Operator associated with the data sources of this model.

        Parameters
        ----------
        name : str
            Operator name, which must be valid.

        Examples
        --------
        Create a displacement operator.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp = model.operator('U')

        Create a sum operator.

        >>> sum = model.operator('accumulate')

        """
        op = Operator(name=name, server=self._server)
        self.metadata._build_connector().__connect_op__(op, self.mesh_by_default)
        return op

    def __str__(self):
        txt = "DPF Model\n"
        txt += "-" * 30 + "\n"
        txt += str(self.results)
        txt += "-" * 30 + "\n"
        txt += str(self.metadata.meshed_region)
        txt += "\n" + "-" * 30 + "\n"
        txt += str(self.metadata.time_freq_support)
        return txt

    def plot(self, color="w", show_edges=True, **kwargs):
        """Plot the mesh of the model.

        Parameters
        ----------
        color : str
            color of the mesh faces in PyVista format. The default is white with ``"w"``.
        show_edges : bool
            Whether to show the mesh edges. The default is ``True``.
        **kwargs : optional
            Additional keyword arguments for the plotter. For additional keyword
            arguments, see ``help(pyvista.plot)``.

        Examples
        --------
        Plot the model using the default options.

        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> model.plot()

        """
        from ansys.dpf.core.plotter import DpfPlotter
        kwargs["color"] = color
        kwargs["show_edges"] = show_edges
        pl = DpfPlotter(**kwargs)
        pl.add_mesh(self.metadata.meshed_region, show_axes=kwargs.pop("show_axes", True), **kwargs)
        return pl.show_figure(**kwargs)

    @property
    def mesh_by_default(self):
        """If true, the mesh is connected by default to operators
        supporting the mesh input
        """
        return self._mesh_by_default

    @mesh_by_default.setter
    def mesh_by_default(self, value):
        self._mesh_by_default = value


class Metadata:
    """Contains the metadata of a data source.

    Parameters
    ----------
    data_sources : DataSources

    server : server.DPFServer
        Server with the channel connected to the remote or local instance.

    """

    def __init__(self, data_sources, server):
        self._server = server
        self._set_data_sources(data_sources)
        self._meshed_region = None
        self._meshes_container = None
        self._result_info = None
        self._stream_provider = None
        self._time_freq_support = None
        self._mesh_selection_manager = None
        self._mesh_provider_cached_instance = None
        self._cache_streams_provider()

    def _cache_result_info(self):
        """Store result information."""
        if not self._result_info:
            self._result_info = self._load_result_info()

    def _cache_streams_provider(self):
        """Create a stream provider and cache it."""
        from ansys.dpf.core import operators

        if hasattr(operators, "metadata") and hasattr(
                operators.metadata, "stream_provider"
        ):
            self._stream_provider = operators.metadata.streams_provider(
                data_sources=self._data_sources, server=self._server
            )
        else:
            self._stream_provider = Operator("stream_provider", server=self._server)
            self._stream_provider.inputs.connect(self._data_sources)
        try:
            self._stream_provider.run()
        except:
            self._stream_provider = None

    @property
    @protect_source_op_not_found
    def time_freq_support(self):
        """Time frequency support.

        Returns
        -------
        ansys.dpf.core.time_freq_support.TimeFreqSupport
            Time frequency support.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)

        Get the number of sets from the result file.

        >>> tf = model.metadata.time_freq_support
        >>> tf.n_sets
        35

        Get the time values for the active result.

        >>> tf.time_frequencies.data
        DPFArray([0.        , 0.019975  , 0.039975  , 0.059975  , 0.079975  ,
               0.099975  , 0.119975  , 0.139975  , 0.159975  , 0.179975  ,
               0.199975  , 0.218975  , 0.238975  , 0.258975  , 0.278975  ,
               0.298975  , 0.318975  , 0.338975  , 0.358975  , 0.378975  ,
               0.398975  , 0.417975  , 0.437975  , 0.457975  , 0.477975  ,
               0.497975  , 0.517975  , 0.53754972, 0.55725277, 0.57711786,
               0.59702054, 0.61694639, 0.63683347, 0.65673452, 0.67662783]...

        """
        if self._time_freq_support is None:
            timeProvider = Operator("TimeFreqSupportProvider", server=self._server)
            if self._stream_provider:
                timeProvider.inputs.connect(self._stream_provider.outputs)
            else:
                timeProvider.inputs.connect(self.data_sources)
            self._time_freq_support = timeProvider.get_output(
                0, types.time_freq_support
            )
        return self._time_freq_support

    @property
    def data_sources(self):
        """Data sources instance.

        This data source can be connected to other operators.

        Returns
        -------
        data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)

        Connect the model data sources to the 'U' operator.

        >>> ds = model.metadata.data_sources
        >>> op = dpf.operators.result.displacement()
        >>> op.inputs.data_sources.connect(ds)

        """
        return self._data_sources

    @property
    def streams_provider(self):
        """Streams provider operator connected to the data sources.

        This streams provider can be connected to other operators.

        Returns
        -------
        streams_provider : :class:`ansys.dpf.core.operators.metadata.streams_provider`

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)

        Connect the model data sources to the ``U`` operator.

        >>> streams = model.metadata.streams_provider
        >>> op = dpf.operators.result.displacement()
        >>> op.inputs.streams_container.connect(streams)

        """
        return self._stream_provider

    def _set_data_sources(self, var_inp):
        from pathlib import Path
        if isinstance(var_inp, dpf.core.DataSources):
            self._data_sources = var_inp
        elif isinstance(var_inp, (str, Path)):
            self._data_sources = DataSources(var_inp, server=self._server)
        else:
            self._data_sources = DataSources(server=self._server)
        self._cache_streams_provider()

    def _load_result_info(self):
        """Returns a result info object"""
        op = Operator("ResultInfoProvider", server=self._server)
        op.inputs.connect(self._stream_provider.outputs)
        try:
            result_info = op.get_output(0, types.result_info)
        except _InactiveRpcError as e:
            # give the user a more helpful error
            if "results file is not defined in the Data sources" in e.details():
                raise RuntimeError("Unable to open result file") from None
            else:
                raise e
        except:
            return None
        return result_info

    @property
    @protect_source_op_not_found
    def meshed_region(self):
        """Meshed region instance.

        Returns
        -------
        mesh : :class:`ansys.dpf.core.meshed_region.MeshedRegion`
            Mesh
        """
        # NOTE: this uses the cached mesh and we might consider
        # changing this
        if self._meshed_region is None:
            self._meshed_region = self.mesh_provider.get_output(0, types.meshed_region)
            self._meshed_region._set_stream_provider(self._stream_provider)

        return self._meshed_region

    @property
    def mesh_provider(self):
        """Mesh provider operator.

        This operator reads a mesh from the result file. The underlying
        operator symbol is the class:`ansys.dpf.core.operators.mesh.mesh_provider`
        operator.

        Returns
        -------
        mesh_provider : :class:`ansys.dpf.core.operators.mesh.mesh_provider`
            Mesh provider operator.

        """
        try:
            if self._mesh_selection_manager is None:
                self._mesh_selection_manager = Operator(
                    "MeshSelectionManagerProvider",
                    server=self._server
                )
                self._mesh_selection_manager.inputs.connect(self._stream_provider.outputs)
                self._mesh_selection_manager.run()
        except:
            pass
        mesh_provider = Operator("MeshProvider", server=self._server)
        if self._stream_provider:
            mesh_provider.inputs.connect(self._stream_provider.outputs)
        else:
            mesh_provider.inputs.connect(self.data_sources)
        return mesh_provider

    @property
    def _mesh_provider_cached(self):
        if self._mesh_provider_cached_instance is None:
            self._mesh_provider_cached_instance = self.mesh_provider
        return self._mesh_provider_cached_instance

    @property
    @protect_source_op_not_found
    def result_info(self):
        """Result Info instance.

        Returns
        -------
        result_info : :class:`ansys.dpf.core.result_info.ResultInfo`
        """
        self._cache_result_info()

        return self._result_info

    @property
    @version_requires("4.0")
    def meshes_container(self):
        """Meshes container instance.

        Returns
        -------
        meshes : ansys.dpf.core.MeshesContainer
            Meshes
        """
        if self._meshes_container is None:
            self._meshes_container = self.meshes_provider.get_output(0, types.meshes_container)

        return self._meshes_container

    @property
    @version_requires("4.0")
    def meshes_provider(self):
        """Meshes provider operator

        This operator reads a meshes container (with potentially time or space varying meshes)
        from the result files.

        Returns
        -------
        meshes_provider : ansys.dpf.core.Operator
            Meshes provider operator.

        Notes
        -----
        Underlying operator symbol is
        "meshes_provider" operator
        """
        meshes_provider = Operator("meshes_provider", server=self._server)
        if self._stream_provider:
            meshes_provider.inputs.connect(self._stream_provider.outputs)
        else:
            meshes_provider.inputs.connect(self.data_sources)
        return meshes_provider

    @property
    def available_named_selections(self):
        """List of available named selections.

        Returns
        -------
        named_selections : list str
        """
        return self.meshed_region.available_named_selections

    def named_selection(self, named_selection):
        """Scoping containing the list of nodes or elements in the named selection.

        Parameters
        ----------
        named_selection : str
            name of the named selection

        Returns
        -------
        named_selection : :class:`ansys.dpf.core.scoping.Scoping`
        """
        return self.meshed_region.named_selection(named_selection)

    def _build_connector(self):
        return DataSourcesOrStreamsConnector(self)
