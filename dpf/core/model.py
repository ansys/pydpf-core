"""
Model
=====
Module contains the Model class to manage file result models."""
import functools

from ansys import dpf
from ansys.dpf.core import Operator
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.core import BaseService
from ansys.dpf.core.common import types

from grpc._channel import _InactiveRpcError


class Model:
    """This class connects to a gRPC DPF server and allows you to
    access a result using the DPF framework.
    
    Parameters
    ----------
    data_sources : str, dpf.core.DataSources
        Accepts either a dpf.core.DataSources instance or a filename of the
        result file to open.
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.

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

        self._server = server
        self._metadata = Metadata(data_sources, self._server)
        self._results = Results(self)

    @property
    def metadata(self):
        """Model metadata

        Includes:

        - ``data_sources``
        - ``meshed_region``
        - ``time_freq_support``
        - ``result_info``
        - ``mesh_provider``

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

        Get the data_sources of the model.

        >>> ds = model.metadata.data_sources

        Print the number of result sets.

        >>> tf = model.metadata.time_freq_support
        >>> tf.n_sets
        35

        Get the unit system used in the analysis

        >>> rinfo = model.metadata.result_info
        >>> rinfo.unit_system
        'Metric (m, kg, N, s, V, A)'

        """
        return self._metadata

    @property
    def results(self):
        """Available results of the model

        Returns
        -------
        Results
            Available results of the model

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        
        Get printable available results
        
        >>> results = model.results

        Access an individual result operator.

        >>> temp = model.results.temperature()

        """
        return self._results

    def operator(self, name):
        """Returns an operator associated with the data sources of
        this model.

        Parameters
        ----------
        name : str
            Operator name.  Must be a valid operator name.

        Examples
        --------
        Create a displacement operator
        
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp = model.operator('U')
        
        Create a sum operator

        >>> sum = model.operator('accumulate')
        
        """
        op = Operator(name= name, server = self._server)
        if self.metadata._stream_provider is not None and hasattr(op.inputs, 'streams'):
            op.inputs.streams.connect(self.metadata._stream_provider.outputs)
        elif self.metadata._data_sources is not None and hasattr(op.inputs, 'data_sources'):
            op.inputs.data_sources.connect(self.metadata._data_sources)

        return op

    def __str__(self):
        txt = 'DPF Model\n'
        txt += '-'*30 + '\n'
        txt += str(self.results)
        txt += '-'*30 + '\n'
        txt += str(self.metadata.meshed_region)
        txt += '\n' + '-'*30 + '\n'
        txt += str(self.metadata.time_freq_support)
        return txt

    def plot(self, color='w', show_edges=True, **kwargs):
        """Plot the mesh of the model

        Examples
        --------
        Plot the model with the default options.
        
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> model.plot()
        
        """
        self.metadata.meshed_region.grid.plot(color=color,
                                              show_edges=show_edges, **kwargs)


class Results:
    """Organize the results from DPF into accessible methods.

    Examples
    --------
    Extract the result object from a model.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.simple_bar)
    >>> results = model.results # printable object

    Access the displacement operator

    >>> from ansys.dpf.core import Model
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = Model(transient)
    >>> displacements = model.results.displacement()

    """

    def __init__(self, model):
        self._result_info = model.metadata.result_info
        self._model = model
        self._connect_operators()

    def __operator_with_sub_res(self, time_scoping=None, mesh_scoping=None, name=None, sub_results=None):
        """Dynamically add operators for subresults.

        The new operators sub-results are connected to the parent
        operator's inputs when created, but are then completely
        independent of the parent operator.

        Parameters
        ----------
        name : str
            Operator name.  Must be a valid operator name.

        sub_results : list

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp_oper = model.results.displacement()
        >>> disp_x = model.results.displacement().X() 
        >>> disp_y = model.results.displacement().Y() 
        >>> disp_z = model.results.displacement().Z()
        
        """
        op = self._model.operator(name)
        op._add_sub_res_operators(sub_results)
        if time_scoping !=None:
            op.connect(0, time_scoping)
        if mesh_scoping != None:
            op.connect(1, mesh_scoping)
        return op

    def _connect_operators(self):
        """Dynamically add operators for results.

        The new operators subresults are connected to the model's
        streams.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = Model(transient)
        >>> disp_operator = model.results.displacement()
        >>> stress_operator = model.results.stress()
        >>> disp_x = model.results.displacement().X() 
        >>> disp_y = model.results.displacement().Y() 
        >>> disp_z = model.results.displacement().Z()
        
        """
        if self._result_info is None:
            return

        # dynamically add function based on input type
        self._op_map_rev = {}
        for result_type in self._result_info:
            bound_method = self.__operator_with_sub_res.__get__(self, self.__class__)
            method2 = functools.partial(bound_method,
                                        name=result_type.operator_name,
                                        sub_results=result_type.sub_results)
            try: 
                method2.__doc__ = Operator(result_type.operator_name).__str__()
            except: 
                pass
                # print("Impossible to find this operator in the database: " + result_type.operator_name)
            setattr(self, result_type.name, method2)
            self._op_map_rev[result_type.name] = result_type.name

    def __str__(self):
        return str(self._result_info)


class Metadata:
    """Contains the metadata of a data source."""

    def __init__(self, data_sources, server):
        self._server = server
        self._set_data_sources(data_sources)
        self._meshed_region = None
        self.result_info = None
        self._stream_provider = None
        self._time_freq_support = None
        self._cache_streams_provider()
        self._cache_result_info()

    def _cache_result_info(self):
        """Store result info"""
        self.result_info = self._load_result_info()

    def _cache_streams_provider(self):
        """Create a stream provider and cache it"""
        from ansys.dpf.core import operators
        if hasattr(operators, "metadata") and hasattr(operators.metadata,"stream_provider"):
            self._stream_provider = operators.metadata.streams_provider(data_sources=self._data_sources)
        else:
            self._stream_provider = Operator("stream_provider")
            self._stream_provider.inputs.connect(self._data_sources)

    @property
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
        array([0.        , 0.019975  , 0.039975  , 0.059975  , 0.079975  ,
               0.099975  , 0.119975  , 0.139975  , 0.159975  , 0.179975  ,
               0.199975  , 0.218975  , 0.238975  , 0.258975  , 0.278975  ,
               0.298975  , 0.318975  , 0.338975  , 0.358975  , 0.378975  ,
               0.398975  , 0.417975  , 0.437975  , 0.457975  , 0.477975  ,
               0.497975  , 0.517975  , 0.53754972, 0.55725277, 0.57711786,
               0.59702054, 0.61694639, 0.63683347, 0.65673452, 0.67662783])

        """
        if self._time_freq_support is None:
            timeProvider = Operator("TimeFreqSupportProvider")
            timeProvider.inputs.connect(self._stream_provider.outputs)
            self._time_freq_support = timeProvider.get_output(0, types.time_freq_support)
        return self._time_freq_support

    @property
    def data_sources(self):
        """DataSources instance.

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
        """stream_provider operator connected to the data sources

        This streams_provider can be connected to other operators.

        Returns
        -------
        streams_provider : operators.metadata.stream_provider

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> transient = examples.download_transient_result()
        >>> model = dpf.Model(transient)
        
        Connect the model data sources to the 'U' operator.
        
        >>> streams = model.metadata.streams_provider
        >>> op = dpf.operators.result.displacement()
        >>> op.inputs.streams_container.connect(streams)
        
        """
        return self._stream_provider


    def _set_data_sources(self, var_inp):
        if isinstance(var_inp, dpf.core.DataSources):
            self._data_sources = var_inp
        elif isinstance(var_inp, str):
            self._data_sources = DataSources(var_inp, server=self._server)
        else:
            self._data_sources = DataSources(server=self._server)
        self._cache_streams_provider()

    def _load_result_info(self):
        """Returns a result info object"""
        op = Operator("ResultInfoProvider")
        op.inputs.connect(self._stream_provider.outputs)
        try:
            result_info = op.get_output(0, types.result_info)
        except _InactiveRpcError as e:
            # give the user a more helpful error
            if 'results file is not defined in the Data sources' in e.details():
                raise RuntimeError('Unable to open result file') from None
            else:
                raise e
        return result_info

    @property
    def meshed_region(self):
        """Meshed region instance.

        Returns
        -------
        mesh : ansys.dpf.core.MeshedRegion
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
        """Mesh provider operator

        This operator reads a mesh from the result file.

        Returns
        -------
        mesh_provider : ansys.dpf.core.Operator
            Mesh provider operator.

        Notes
        -----
        Underlying operator symbol is
        MeshProvider operator
        """
        tmp = Operator("MeshSelectionManagerProvider")
        tmp.inputs.connect(self._stream_provider.outputs)
        tmp.run()
        mesh_provider = Operator("MeshProvider")
        mesh_provider.inputs.connect(self._stream_provider.outputs)
        return mesh_provider


    @property
    def available_named_selections(self):
        """Returns a list of available named selections
        
        Returns
        -------
        named_selections : list str
        """
        return self.meshed_region.available_named_selections
    
    def named_selection(self, named_selection):
        """Returns a scoping containing the list of nodes or elements
        in the named selection
        
        Parameters
        ----------
        named_selection : str 
            name of the named selection
            
        Returns
        -------
        named_selection : dpf.core.Scoping
        """
        return self.meshed_region.named_selection(named_selection)
        