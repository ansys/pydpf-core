"""
merge_scopings_containers
=========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_scopings_containers(Operator):
    """Take a set of scopings containers and assemble them in a unique one

      available inputs:
        - scopings_containers1 (ScopingsContainer)
        - scopings_containers2 (ScopingsContainer)

      available outputs:
        - merged_scopings_container (ScopingsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_scopings_containers()

      >>> # Make input connections
      >>> my_scopings_containers1 = dpf.ScopingsContainer()
      >>> op.inputs.scopings_containers1.connect(my_scopings_containers1)
      >>> my_scopings_containers2 = dpf.ScopingsContainer()
      >>> op.inputs.scopings_containers2.connect(my_scopings_containers2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_scopings_containers(scopings_containers1=my_scopings_containers1,scopings_containers2=my_scopings_containers2)

      >>> # Get output data
      >>> result_merged_scopings_container = op.outputs.merged_scopings_container()"""
    def __init__(self, scopings_containers1=None, scopings_containers2=None, config=None, server=None):
        super().__init__(name="merge::scopings_container", config = config, server = server)
        self._inputs = InputsMergeScopingsContainers(self)
        self._outputs = OutputsMergeScopingsContainers(self)
        if scopings_containers1 !=None:
            self.inputs.scopings_containers1.connect(scopings_containers1)
        if scopings_containers2 !=None:
            self.inputs.scopings_containers2.connect(scopings_containers2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of scopings containers and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "scopings_containers", type_names=["scopings_container"], optional=False, document="""a vector of scopings containers to merge or scopings containers from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "scopings_containers", type_names=["scopings_container"], optional=False, document="""a vector of scopings containers to merge or scopings containers from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_scopings_container", type_names=["scopings_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::scopings_container")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeScopingsContainers 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeScopingsContainers 
        """
        return super().outputs


#internal name: merge::scopings_container
#scripting name: merge_scopings_containers
class InputsMergeScopingsContainers(_Inputs):
    """Intermediate class used to connect user inputs to merge_scopings_containers operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_scopings_containers()
      >>> my_scopings_containers1 = dpf.ScopingsContainer()
      >>> op.inputs.scopings_containers1.connect(my_scopings_containers1)
      >>> my_scopings_containers2 = dpf.ScopingsContainer()
      >>> op.inputs.scopings_containers2.connect(my_scopings_containers2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_scopings_containers._spec().inputs, op)
        self._scopings_containers1 = Input(merge_scopings_containers._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._scopings_containers1)
        self._scopings_containers2 = Input(merge_scopings_containers._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._scopings_containers2)

    @property
    def scopings_containers1(self):
        """Allows to connect scopings_containers1 input to the operator

        - pindoc: a vector of scopings containers to merge or scopings containers from pin 0 to ...

        Parameters
        ----------
        my_scopings_containers1 : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_scopings_containers()
        >>> op.inputs.scopings_containers1.connect(my_scopings_containers1)
        >>> #or
        >>> op.inputs.scopings_containers1(my_scopings_containers1)

        """
        return self._scopings_containers1

    @property
    def scopings_containers2(self):
        """Allows to connect scopings_containers2 input to the operator

        - pindoc: a vector of scopings containers to merge or scopings containers from pin 0 to ...

        Parameters
        ----------
        my_scopings_containers2 : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_scopings_containers()
        >>> op.inputs.scopings_containers2.connect(my_scopings_containers2)
        >>> #or
        >>> op.inputs.scopings_containers2(my_scopings_containers2)

        """
        return self._scopings_containers2

class OutputsMergeScopingsContainers(_Outputs):
    """Intermediate class used to get outputs from merge_scopings_containers operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_scopings_containers()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_scopings_container = op.outputs.merged_scopings_container()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_scopings_containers._spec().outputs, op)
        self._merged_scopings_container = Output(merge_scopings_containers._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_scopings_container)

    @property
    def merged_scopings_container(self):
        """Allows to get merged_scopings_container output of the operator


        Returns
        ----------
        my_merged_scopings_container : ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_scopings_containers()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_scopings_container = op.outputs.merged_scopings_container() 
        """
        return self._merged_scopings_container

