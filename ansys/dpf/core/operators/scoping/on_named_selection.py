"""
on_named_selection
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "scoping" category
"""

class on_named_selection(Operator):
    """provides a scoping at a given location based on a given named selection

      available inputs:
        - requested_location (str)
        - named_selection_name (str)
        - int_inclusive (int) (optional)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)

      available outputs:
        - mesh_scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.on_named_selection()

      >>> # Make input connections
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_named_selection_name = str()
      >>> op.inputs.named_selection_name.connect(my_named_selection_name)
      >>> my_int_inclusive = int()
      >>> op.inputs.int_inclusive.connect(my_int_inclusive)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.on_named_selection(requested_location=my_requested_location,named_selection_name=my_named_selection_name,int_inclusive=my_int_inclusive,streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_mesh_scoping = op.outputs.mesh_scoping()"""
    def __init__(self, requested_location=None, named_selection_name=None, int_inclusive=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="scoping_provider_by_ns", config = config, server = server)
        self._inputs = InputsOnNamedSelection(self)
        self._outputs = OutputsOnNamedSelection(self)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if named_selection_name !=None:
            self.inputs.named_selection_name.connect(named_selection_name)
        if int_inclusive !=None:
            self.inputs.int_inclusive.connect(int_inclusive)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""provides a scoping at a given location based on a given named selection""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "requested_location", type_names=["string"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "named_selection_name", type_names=["string"], optional=False, document="""the string is expected to be in upper case"""), 
                                 2 : PinSpecification(name = "int_inclusive", type_names=["int32"], optional=True, document="""If element scoping is requested on a nodal named selection, if Inclusive == 1 then add all the elements adjacent to the nodes.If Inclusive == 0, only the elements which have all their nodes in the named selection are included"""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping_provider_by_ns")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOnNamedSelection 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOnNamedSelection 
        """
        return super().outputs


#internal name: scoping_provider_by_ns
#scripting name: on_named_selection
class InputsOnNamedSelection(_Inputs):
    """Intermediate class used to connect user inputs to on_named_selection operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_named_selection()
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_named_selection_name = str()
      >>> op.inputs.named_selection_name.connect(my_named_selection_name)
      >>> my_int_inclusive = int()
      >>> op.inputs.int_inclusive.connect(my_int_inclusive)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(on_named_selection._spec().inputs, op)
        self._requested_location = Input(on_named_selection._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._requested_location)
        self._named_selection_name = Input(on_named_selection._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._named_selection_name)
        self._int_inclusive = Input(on_named_selection._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._int_inclusive)
        self._streams_container = Input(on_named_selection._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(on_named_selection._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

    @property
    def named_selection_name(self):
        """Allows to connect named_selection_name input to the operator

        - pindoc: the string is expected to be in upper case

        Parameters
        ----------
        my_named_selection_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> op.inputs.named_selection_name.connect(my_named_selection_name)
        >>> #or
        >>> op.inputs.named_selection_name(my_named_selection_name)

        """
        return self._named_selection_name

    @property
    def int_inclusive(self):
        """Allows to connect int_inclusive input to the operator

        - pindoc: If element scoping is requested on a nodal named selection, if Inclusive == 1 then add all the elements adjacent to the nodes.If Inclusive == 0, only the elements which have all their nodes in the named selection are included

        Parameters
        ----------
        my_int_inclusive : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> op.inputs.int_inclusive.connect(my_int_inclusive)
        >>> #or
        >>> op.inputs.int_inclusive(my_int_inclusive)

        """
        return self._int_inclusive

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsOnNamedSelection(_Outputs):
    """Intermediate class used to get outputs from on_named_selection operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_named_selection()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(on_named_selection._spec().outputs, op)
        self._mesh_scoping = Output(on_named_selection._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator


        Returns
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_named_selection()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping() 
        """
        return self._mesh_scoping

