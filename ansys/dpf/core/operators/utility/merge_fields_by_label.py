"""
merge_fields_by_label
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "utility" category
"""

class merge_fields_by_label(Operator):
    """Take a fields container and merge its fields that share the same label value.

      available inputs:
        - fields_container (FieldsContainer)
        - label (str)
        - merged_field_support (AbstractFieldSupport) (optional)
        - sum_merge (bool) (optional)

      available outputs:
        - fields_container (FieldsContainer)
        - merged_field_support (AbstractFieldSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_fields_by_label()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)
      >>> my_merged_field_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_field_support.connect(my_merged_field_support)
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_fields_by_label(fields_container=my_fields_container,label=my_label,merged_field_support=my_merged_field_support,sum_merge=my_sum_merge)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()
      >>> result_merged_field_support = op.outputs.merged_field_support()"""
    def __init__(self, fields_container=None, label=None, merged_field_support=None, sum_merge=None, config=None, server=None):
        super().__init__(name="merge::fields_container_label", config = config, server = server)
        self._inputs = InputsMergeFieldsByLabel(self)
        self._outputs = OutputsMergeFieldsByLabel(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if label !=None:
            self.inputs.label.connect(label)
        if merged_field_support !=None:
            self.inputs.merged_field_support.connect(merged_field_support)
        if sum_merge !=None:
            self.inputs.sum_merge.connect(sum_merge)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a fields container and merge its fields that share the same label value.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "label", type_names=["string"], optional=False, document="""Label identifier that should be merged."""), 
                                 2 : PinSpecification(name = "merged_field_support", type_names=["abstract_field_support"], optional=True, document="""The FieldsContainer's support that has already been merged."""), 
                                 3 : PinSpecification(name = "sum_merge", type_names=["bool"], optional=True, document="""Default is false. If true redundant quantities are summed instead of being ignored.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "merged_field_support", type_names=["abstract_field_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::fields_container_label")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeFieldsByLabel 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeFieldsByLabel 
        """
        return super().outputs


#internal name: merge::fields_container_label
#scripting name: merge_fields_by_label
class InputsMergeFieldsByLabel(_Inputs):
    """Intermediate class used to connect user inputs to merge_fields_by_label operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields_by_label()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_label = str()
      >>> op.inputs.label.connect(my_label)
      >>> my_merged_field_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_field_support.connect(my_merged_field_support)
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields_by_label._spec().inputs, op)
        self._fields_container = Input(merge_fields_by_label._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._label = Input(merge_fields_by_label._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._label)
        self._merged_field_support = Input(merge_fields_by_label._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._merged_field_support)
        self._sum_merge = Input(merge_fields_by_label._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._sum_merge)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def label(self):
        """Allows to connect label input to the operator

        - pindoc: Label identifier that should be merged.

        Parameters
        ----------
        my_label : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> op.inputs.label.connect(my_label)
        >>> #or
        >>> op.inputs.label(my_label)

        """
        return self._label

    @property
    def merged_field_support(self):
        """Allows to connect merged_field_support input to the operator

        - pindoc: The FieldsContainer's support that has already been merged.

        Parameters
        ----------
        my_merged_field_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> op.inputs.merged_field_support.connect(my_merged_field_support)
        >>> #or
        >>> op.inputs.merged_field_support(my_merged_field_support)

        """
        return self._merged_field_support

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

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> op.inputs.sum_merge.connect(my_sum_merge)
        >>> #or
        >>> op.inputs.sum_merge(my_sum_merge)

        """
        return self._sum_merge

class OutputsMergeFieldsByLabel(_Outputs):
    """Intermediate class used to get outputs from merge_fields_by_label operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields_by_label()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
      >>> result_merged_field_support = op.outputs.merged_field_support()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields_by_label._spec().outputs, op)
        self._fields_container = Output(merge_fields_by_label._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)
        self._merged_field_support = Output(merge_fields_by_label._spec().output_pin(1), 1, op) 
        self._outputs.append(self._merged_field_support)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

    @property
    def merged_field_support(self):
        """Allows to get merged_field_support output of the operator


        Returns
        ----------
        my_merged_field_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields_by_label()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_field_support = op.outputs.merged_field_support() 
        """
        return self._merged_field_support

