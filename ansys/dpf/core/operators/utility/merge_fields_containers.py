"""
merge_fields_containers
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class merge_fields_containers(Operator):
    """Take a set of fields containers and assemble them in a unique one

      available inputs:
        - sum_merge (bool) (optional)
        - merged_fields_support (AbstractFieldSupport) (optional)
        - merged_fields_containers_support (AbstractFieldSupport) (optional)
        - fields_containers1 (FieldsContainer)
        - fields_containers2 (FieldsContainer)

      available outputs:
        - merged_fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_fields_containers()

      >>> # Make input connections
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)
      >>> my_merged_fields_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_support.connect(my_merged_fields_support)
      >>> my_merged_fields_containers_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_containers_support.connect(my_merged_fields_containers_support)
      >>> my_fields_containers1 = dpf.FieldsContainer()
      >>> op.inputs.fields_containers1.connect(my_fields_containers1)
      >>> my_fields_containers2 = dpf.FieldsContainer()
      >>> op.inputs.fields_containers2.connect(my_fields_containers2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_fields_containers(sum_merge=my_sum_merge,merged_fields_support=my_merged_fields_support,merged_fields_containers_support=my_merged_fields_containers_support,fields_containers1=my_fields_containers1,fields_containers2=my_fields_containers2)

      >>> # Get output data
      >>> result_merged_fields_container = op.outputs.merged_fields_container()"""
    def __init__(self, sum_merge=None, merged_fields_support=None, merged_fields_containers_support=None, fields_containers1=None, fields_containers2=None, config=None, server=None):
        super().__init__(name="merge::fields_container", config = config, server = server)
        self._inputs = InputsMergeFieldsContainers(self)
        self._outputs = OutputsMergeFieldsContainers(self)
        if sum_merge !=None:
            self.inputs.sum_merge.connect(sum_merge)
        if merged_fields_support !=None:
            self.inputs.merged_fields_support.connect(merged_fields_support)
        if merged_fields_containers_support !=None:
            self.inputs.merged_fields_containers_support.connect(merged_fields_containers_support)
        if fields_containers1 !=None:
            self.inputs.fields_containers1.connect(fields_containers1)
        if fields_containers2 !=None:
            self.inputs.fields_containers2.connect(fields_containers2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of fields containers and assemble them in a unique one""",
                             map_input_pin_spec={
                                 -3 : PinSpecification(name = "sum_merge", type_names=["bool"], optional=True, document="""Default is false. If true redundant quantities are summed instead of being ignored."""), 
                                 -2 : PinSpecification(name = "merged_fields_support", type_names=["abstract_field_support"], optional=True, document="""Already merged field support."""), 
                                 -1 : PinSpecification(name = "merged_fields_containers_support", type_names=["abstract_field_support"], optional=True, document="""Already merged fields containers support."""), 
                                 0 : PinSpecification(name = "fields_containers", type_names=["fields_container"], optional=False, document="""A vector of fields containers to merge or fields containers from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "fields_containers", type_names=["fields_container"], optional=False, document="""A vector of fields containers to merge or fields containers from pin 0 to ...""")},
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
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)
      >>> my_merged_fields_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_support.connect(my_merged_fields_support)
      >>> my_merged_fields_containers_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_fields_containers_support.connect(my_merged_fields_containers_support)
      >>> my_fields_containers1 = dpf.FieldsContainer()
      >>> op.inputs.fields_containers1.connect(my_fields_containers1)
      >>> my_fields_containers2 = dpf.FieldsContainer()
      >>> op.inputs.fields_containers2.connect(my_fields_containers2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields_containers._spec().inputs, op)
        self._sum_merge = Input(merge_fields_containers._spec().input_pin(-3), -3, op, -1) 
        self._inputs.append(self._sum_merge)
        self._merged_fields_support = Input(merge_fields_containers._spec().input_pin(-2), -2, op, -1) 
        self._inputs.append(self._merged_fields_support)
        self._merged_fields_containers_support = Input(merge_fields_containers._spec().input_pin(-1), -1, op, -1) 
        self._inputs.append(self._merged_fields_containers_support)
        self._fields_containers1 = Input(merge_fields_containers._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._fields_containers1)
        self._fields_containers2 = Input(merge_fields_containers._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._fields_containers2)

    @property
    def sum_merge(self):
        """Allows to connect sum_merge input to the operator

        - pindoc: Default is false. If true redundant quantities are summed instead of being ignored.

        Parameters
        ----------
        my_sum_merge : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.sum_merge.connect(my_sum_merge)
        >>> #or
        >>> op.inputs.sum_merge(my_sum_merge)

        """
        return self._sum_merge

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
    def fields_containers1(self):
        """Allows to connect fields_containers1 input to the operator

        - pindoc: A vector of fields containers to merge or fields containers from pin 0 to ...

        Parameters
        ----------
        my_fields_containers1 : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.fields_containers1.connect(my_fields_containers1)
        >>> #or
        >>> op.inputs.fields_containers1(my_fields_containers1)

        """
        return self._fields_containers1

    @property
    def fields_containers2(self):
        """Allows to connect fields_containers2 input to the operator

        - pindoc: A vector of fields containers to merge or fields containers from pin 0 to ...

        Parameters
        ----------
        my_fields_containers2 : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_containers()
        >>> op.inputs.fields_containers2.connect(my_fields_containers2)
        >>> #or
        >>> op.inputs.fields_containers2(my_fields_containers2)

        """
        return self._fields_containers2

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

