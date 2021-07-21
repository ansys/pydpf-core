"""
merge_fields
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_fields(Operator):
    """Take a set of fields and assemble them in a unique one

      available inputs:
        - sum_merge (bool) (optional)
        - merged_support (AbstractFieldSupport) (optional)
        - fields1 (Field)
        - fields2 (Field)

      available outputs:
        - merged_field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_fields()

      >>> # Make input connections
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)
      >>> my_merged_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_support.connect(my_merged_support)
      >>> my_fields1 = dpf.Field()
      >>> op.inputs.fields1.connect(my_fields1)
      >>> my_fields2 = dpf.Field()
      >>> op.inputs.fields2.connect(my_fields2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_fields(sum_merge=my_sum_merge,merged_support=my_merged_support,fields1=my_fields1,fields2=my_fields2)

      >>> # Get output data
      >>> result_merged_field = op.outputs.merged_field()"""
    def __init__(self, sum_merge=None, merged_support=None, fields1=None, fields2=None, config=None, server=None):
        super().__init__(name="merge::field", config = config, server = server)
        self._inputs = InputsMergeFields(self)
        self._outputs = OutputsMergeFields(self)
        if sum_merge !=None:
            self.inputs.sum_merge.connect(sum_merge)
        if merged_support !=None:
            self.inputs.merged_support.connect(merged_support)
        if fields1 !=None:
            self.inputs.fields1.connect(fields1)
        if fields2 !=None:
            self.inputs.fields2.connect(fields2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of fields and assemble them in a unique one""",
                             map_input_pin_spec={
                                 -2 : PinSpecification(name = "sum_merge", type_names=["bool"], optional=True, document="""Default is false. If true redundant quantities are summed instead of being ignored."""), 
                                 -1 : PinSpecification(name = "merged_support", type_names=["abstract_field_support"], optional=True, document="""Already merged field support."""), 
                                 0 : PinSpecification(name = "fields", type_names=["field"], optional=False, document="""A vector of fields to merge or fields from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "fields", type_names=["field"], optional=False, document="""A vector of fields to merge or fields from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::field")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeFields 
        """
        return super().outputs


#internal name: merge::field
#scripting name: merge_fields
class InputsMergeFields(_Inputs):
    """Intermediate class used to connect user inputs to merge_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields()
      >>> my_sum_merge = bool()
      >>> op.inputs.sum_merge.connect(my_sum_merge)
      >>> my_merged_support = dpf.AbstractFieldSupport()
      >>> op.inputs.merged_support.connect(my_merged_support)
      >>> my_fields1 = dpf.Field()
      >>> op.inputs.fields1.connect(my_fields1)
      >>> my_fields2 = dpf.Field()
      >>> op.inputs.fields2.connect(my_fields2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields._spec().inputs, op)
        self._sum_merge = Input(merge_fields._spec().input_pin(-2), -2, op, -1) 
        self._inputs.append(self._sum_merge)
        self._merged_support = Input(merge_fields._spec().input_pin(-1), -1, op, -1) 
        self._inputs.append(self._merged_support)
        self._fields1 = Input(merge_fields._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._fields1)
        self._fields2 = Input(merge_fields._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._fields2)

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

        >>> op = dpf.operators.utility.merge_fields()
        >>> op.inputs.sum_merge.connect(my_sum_merge)
        >>> #or
        >>> op.inputs.sum_merge(my_sum_merge)

        """
        return self._sum_merge

    @property
    def merged_support(self):
        """Allows to connect merged_support input to the operator

        - pindoc: Already merged field support.

        Parameters
        ----------
        my_merged_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields()
        >>> op.inputs.merged_support.connect(my_merged_support)
        >>> #or
        >>> op.inputs.merged_support(my_merged_support)

        """
        return self._merged_support

    @property
    def fields1(self):
        """Allows to connect fields1 input to the operator

        - pindoc: A vector of fields to merge or fields from pin 0 to ...

        Parameters
        ----------
        my_fields1 : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields()
        >>> op.inputs.fields1.connect(my_fields1)
        >>> #or
        >>> op.inputs.fields1(my_fields1)

        """
        return self._fields1

    @property
    def fields2(self):
        """Allows to connect fields2 input to the operator

        - pindoc: A vector of fields to merge or fields from pin 0 to ...

        Parameters
        ----------
        my_fields2 : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields()
        >>> op.inputs.fields2.connect(my_fields2)
        >>> #or
        >>> op.inputs.fields2(my_fields2)

        """
        return self._fields2

class OutputsMergeFields(_Outputs):
    """Intermediate class used to get outputs from merge_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_field = op.outputs.merged_field()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_fields._spec().outputs, op)
        self._merged_field = Output(merge_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_field)

    @property
    def merged_field(self):
        """Allows to get merged_field output of the operator


        Returns
        ----------
        my_merged_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_field = op.outputs.merged_field() 
        """
        return self._merged_field

