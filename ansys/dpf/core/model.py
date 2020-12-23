"""Module contains the Model class to manage file result models."""
import functools

from ansys import dpf
from ansys.dpf.core import Operator
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.core import BaseService
from ansys.dpf.core.common import types

from grpc._channel import _InactiveRpcError

# BASE_RST_OP_DOC = """

# Parameters
# ----------
# time_scoping : int or list, optional
#     Index of the results requested.  One based indexing.  Defaults to
#     last result.

# mesh_entities_scoping : mesh_entities_scoping
#     Mesh entities scoping, unordered_map id to index (optional) (index
#     is optional, to be set if a user wants the results at a given
#     order)

# fields_container : fields_container, optional
#     Fields container to update/create and set as output.

# streams : result file container, optional
#     Results file container

# solution_cs : bool, optional
#     If False get the results in the solution CS.

# Returns
# -------
# oper : ansys.Operator
#     Operator containing a field container matching the number of
#     result sets.
# """


class Model():
    """This class connects to a gRPC DPF server and allows you to
    access a result using the DPF framework.

    Parameters
    ----------
    data_sources : str, dpf.core.DataSources
        Accepts either a dpf.core.DataSources instance or a filename of the
        result file to open.

    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to
        the global channel.

    Attributes
    ----------
    metadata : ansys.dpf.core.model.Metadata
        Entity containing model's metadata: data_sources,
        meshed_region, time_freq_support, result_info

    results : ansys.dpf.core.model.Results
        Entity containing all the available results for this model
        (operators already connected to the model's streams)

    Examples
    --------
    >>> from ansys.dpf import core
    >>> model = core.Model('file.rst')

    Start a local DPF server and load a result file

    >>> from ansys.dpf import core
    >>> core.start_local_server()
    >>> model = core.Model('file.rst')
    """

    def __init__(self, data_sources=None, channel=None):
        """ Initialize connection with mapdl """

        if channel is None:
            channel = dpf.core._global_channel()

        self._channel = channel
        # base service required to load operators
        self._base = BaseService(self._channel)
        self.metadata = Metadata(data_sources, channel)
        self.results = Results(self)

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

        >>> disp = model.operator('U')

        Create a sum operator

        >>> disp = model.operator('accumulate')
        """
        op= Operator(name, self._channel)
        if self.metadata._stream_provider!=None and hasattr(op.inputs, 'streams') :
            op.inputs.streams.connect(self.metadata._stream_provider.outputs)
        elif self.metadata._data_sources!=None and hasattr(op.inputs, 'data_sources') :
            op.inputs.data_sources.connect(self.metadata._data_sources)
            
        return op

    def __str__(self):
        txt = 'DPF Model\n'
        txt += '-'*30 + '\n'
        txt += self.metadata.result_info.__str__()
        txt += '-'*30 + '\n'
        txt += self.metadata.meshed_region.__str__()
        txt += '-'*30 + '\n'
        txt += self.metadata.time_freq_support.__str__()
        return txt

    def plot(self, color='w', show_edges=True, **kwargs):
        self.metadata.meshed_region.grid.plot(color=color, show_edges=show_edges, **kwargs)

    # @property
    # def physics_type(self):
    #     """The physics type of the model"""
    #     self.result_info.physics_type

class Results:

    def __init__(self, model):
        self._result_info = model.metadata.result_info
        self._model = model
        self._connect_operators()

    def __operator_with_sub_res(self, name, sub_results):
        """Returns an operator and binds it with other operators for its subresults
        Dynamically add operators instanciation for subresults 
        (the new operators subresults are connected to the parent operator's inputs when created,
        but are, then, completly independent of the parent operator's)
        
        Parameters
        ----------
        name : str
            Operator name.  Must be a valid operator name.
            
        sub_results : list
        
        Examples
        --------
        disp_oper = model.displacement()
        generates: model.displacement().X() model.displacement().Y() model.displacement().Z()
        
        
        """
        op= self._model.operator(name)
        op._add_sub_res_operators(sub_results)
        return op
    
    def _connect_operators(self):
        """Dynamically add operators instanciation for results 
        (the new operators subresults are connected to the model's streams)
        
        Examples
        --------
        generated: model.displacement(), model.stress()...
        """
        if self._result_info is None:
            return

        # dynamically add function based on input type
        self._op_map_rev = {}
        for result_type in self._result_info:
            bound_method = self.__operator_with_sub_res.__get__(self, self.__class__)
            method2=functools.partial(bound_method,name=result_type.operator_name, sub_results=result_type.sub_results)
            setattr(self, result_type.name, method2)

            self._op_map_rev[result_type.name] = result_type.name

class Metadata:
    def __init__(self, data_sources, channel):
        self._channel = channel
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
        self._stream_provider = Operator("stream_provider")
        self._stream_provider.inputs.connect(self._data_sources)

    @property
    def time_freq_support(self):
        """TimeFreqSupportProvider"""
        if self._time_freq_support is None:
            timeProvider = Operator("TimeFreqSupportProvider")
            timeProvider.inputs.connect(self._stream_provider.outputs)
            self._time_freq_support = timeProvider.get_output(0, types.time_freq_support)
        return self._time_freq_support
    
    @property
    def data_sources(self):
        """DataSources instance.
        this object is read only
        
        Returns
        -------
        ds : ansys.dpf.core.DataSources
        """
        return self._data_sources

    def _set_data_sources(self, var_inp):
        if isinstance(var_inp, dpf.core.DataSources):
            self._data_sources = var_inp
        elif isinstance(var_inp, str):
            self._data_sources = DataSources(var_inp, channel=self._channel)
        else:
            self._data_sources = DataSources(channel=self._channel)
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
            self._meshed_region = self.__mesh_provider.get_output(0, types.meshed_region)
            # default (pin 10) for element is to check and cure degenerated elements

        return self._meshed_region

    @property
    def __mesh_provider(self):
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
        mesh_provider = Operator("MeshProvider")
        mesh_provider.inputs.connect(self._stream_provider.outputs)
        return mesh_provider
