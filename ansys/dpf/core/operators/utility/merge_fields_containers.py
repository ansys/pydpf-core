"""
merge_fields_containers
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_fields_containers(Operator):
    """Take a set of fields containers and assemble them in a unique one

      available inputs:
        - merged_fields_support (AbstractFieldSupport) (optional)
        - merged_fields_containers_support (AbstractFieldSupport) (optional)
        - fields_containers (FieldsContainer)

      available outputs:
        - merged_fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_fields_containers()

      >>> # Make input connections
      >>> my_merged_fields_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_support.connect(my_merged_fields_support)
      >>> my_merged_fields_containers_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_containers_support.connect(my_merged_fields_containers_support)
      >>> my_fields_containers = dpf.FieldsContainer()
      >>> op.inputs.fields_containers.connect(my_fields_containers)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_fields_containers(merged_fields_support=my_merged_fields_support,merged_fields_containers_support=my_merged_fields_containers_support,fields_containers=my_fields_containers)

      >>> # Get output data
      >>> result_merged_fields_container = op.outputs.merged_fields_container()"""
    def __init__(self, merged_fields_support=None, merged_fields_containers_support=None, fields_containers=None, config=None, server=None):
        super().__init__(name="merge::fields_container", config = config, server = server)
        self._inputs = InputsMergeFieldsContainers(self)
        self._outputs = OutputsMergeFieldsContainers(self)
        if merged_fields_support !=None:
            self.inputs.merged_fields_support.connect(merged_fields_support)
        if merged_fields_containers_support !=None:
            self.inputs.merged_fields_containers_support.connect(merged_fields_containers_support)
        if fields_containers !=None:
            self.inputs.fields_containers.connect(fields_containers)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of fields containers and assemble them in a unique one""",
                             map_input_pin_spec={
                                 -2 : PinSpecification(name = "merged_fields_support", type_names=["abstract_field_support"], optional=True, document="""Already merged field support."""), 
                                 -1 : PinSpecification(name = "merged_fields_containers_support", type_names=["abstract_field_support"], optional=True, document="""Already merged fields containers support."""), 
                                 0 : PinSpecification(name = "fields_containers", type_names=["fields_container"], optional=False, document="""A vector of fields containers to merge or fields containers from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::fields_container")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeFieldsContainers 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeFieldsContainers 
        """
        return super().outputs


#internal name: merge::fields_container
#scripting name: merge_fields_containers
class InputsMergeFieldsContainers(_Inputs):
    """Intermediate class used to connect user inputs to merge_fields_containers operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields_containers()
      >>> my_merged_fields_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_support.connect(my_merged_fields_support)
      >>> my_merged_fields_containers_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_containers_support.connect(my_merged_fields_containers_support)
      >>> my_fields_containers = dpf.FieldsContainer()
      >>> op.inputs.fields_containers.connect(my_fields_containers)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields_containers._spec().inputs, op)
        self._merged_fields_support = Input(merge_fields_containers._spec().input_pin(-2), -2, op, -1) 
        self._inputs.append(self._merged_fields_support)
        self._merged_fields_containers_support = Input(merge_fields_containers._spec().input_pin(-1), -1, op, -1) 
        self._inputs.append(self._merged_fields_containers_support)
        self._fields_containers = Input(merge_fields_containers._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_containers)

    @property
    def merged_fields_support(self):
        """Allows to connect merged_fields_support input to the operator

        - pindoc: Already merged field support.

        Parameters
        ----------
        my_merged_fields_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.merged_fields_support.connect(my_merged_fields_support)
        >>> #or
        >>> op.inputs.merged_fields_support(my_merged_fields_support)

        """
        return self._merged_fields_support

    @property
    def merged_fields_containers_support(self):
        """Allows to connect merged_fields_containers_support input to the operator

        - pindoc: Already merged fields containers support.

        Parameters
        ----------
        my_merged_fields_containers_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.merged_fields_containers_support.connect(my_merged_fields_containers_support)
        >>> #or
        >>> op.inputs.merged_fields_containers_support(my_merged_fields_containers_support)

        """
        return self._merged_fields_containers_support

    @property
    def fields_containers(self):
        """Allows to connect fields_containers input to the operator

        - pindoc: A vector of fields containers to merge or fields containers from pin 0 to ...

        Parameters
        ----------
        my_fields_containers : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.fields_containers.connect(my_fields_containers)
        >>> #or
        >>> op.inputs.fields_containers(my_fields_containers)

        """
        return self._fields_containers

class OutputsMergeFieldsContainers(_Outputs):
    """Intermediate class used to get outputs from merge_fields_containers operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields_containers()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_fields_container = op.outputs.merged_fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields_containers._spec().outputs, op)
        self._merged_fields_container = Output(merge_fields_containers._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_fields_container)

    @property
    def merged_fields_container(self):
        """Allows to get merged_fields_container output of the operator


        Returns
        ----------
        my_merged_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_fields_container = op.outputs.merged_fields_container() 
        """
        return self._merged_fields_container

