"""
data_tree_to_json
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "serialization" category
"""

class data_tree_to_json(Operator):
    """Writes a json file or string from a DataTree

      available inputs:
        - data_tree (DataTree)
        - path (str) (optional)

      available outputs:
        - data_sources (DataSources ,str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.data_tree_to_json()

      >>> # Make input connections
      >>> my_data_tree = dpf.DataTree()
      >>> op.inputs.data_tree.connect(my_data_tree)
      >>> my_path = str()
      >>> op.inputs.path.connect(my_path)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.data_tree_to_json(data_tree=my_data_tree,path=my_path)

      >>> # Get output data
      >>> result_data_sources = op.outputs.data_sources()"""
    def __init__(self, data_tree=None, path=None, config=None, server=None):
        super().__init__(name="data_tree_to_json", config = config, server = server)
        self._inputs = InputsDataTreeToJson(self)
        self._outputs = OutputsDataTreeToJson(self)
        if data_tree !=None:
            self.inputs.data_tree.connect(data_tree)
        if path !=None:
            self.inputs.path.connect(path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Writes a json file or string from a DataTree""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "data_tree", type_names=["abstract_data_tree"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "path", type_names=["string"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources","string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "data_tree_to_json")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsDataTreeToJson 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsDataTreeToJson 
        """
        return super().outputs


#internal name: data_tree_to_json
#scripting name: data_tree_to_json
class InputsDataTreeToJson(_Inputs):
    """Intermediate class used to connect user inputs to data_tree_to_json operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.data_tree_to_json()
      >>> my_data_tree = dpf.DataTree()
      >>> op.inputs.data_tree.connect(my_data_tree)
      >>> my_path = str()
      >>> op.inputs.path.connect(my_path)
    """
    def __init__(self, op: Operator):
        super().__init__(data_tree_to_json._spec().inputs, op)
        self._data_tree = Input(data_tree_to_json._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._data_tree)
        self._path = Input(data_tree_to_json._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._path)

    @property
    def data_tree(self):
        """Allows to connect data_tree input to the operator

        Parameters
        ----------
        my_data_tree : DataTree, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.data_tree_to_json()
        >>> op.inputs.data_tree.connect(my_data_tree)
        >>> #or
        >>> op.inputs.data_tree(my_data_tree)

        """
        return self._data_tree

    @property
    def path(self):
        """Allows to connect path input to the operator

        Parameters
        ----------
        my_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.data_tree_to_json()
        >>> op.inputs.path.connect(my_path)
        >>> #or
        >>> op.inputs.path(my_path)

        """
        return self._path

class OutputsDataTreeToJson(_Outputs):
    """Intermediate class used to get outputs from data_tree_to_json operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.data_tree_to_json()
      >>> # Connect inputs : op.inputs. ...
      >>> result_data_sources = op.outputs.data_sources()
    """
    def __init__(self, op: Operator):
        super().__init__(data_tree_to_json._spec().outputs, op)
        self.data_sources_as_data_sources = Output( _modify_output_spec_with_one_type(data_tree_to_json._spec().output_pin(0), "data_sources"), 0, op) 
        self._outputs.append(self.data_sources_as_data_sources)
        self.data_sources_as_string = Output( _modify_output_spec_with_one_type(data_tree_to_json._spec().output_pin(0), "string"), 0, op) 
        self._outputs.append(self.data_sources_as_string)

