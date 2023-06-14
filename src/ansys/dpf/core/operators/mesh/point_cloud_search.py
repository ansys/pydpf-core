"""
point_cloud_search
==================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mesh" category
"""

class point_cloud_search(Operator):
    """For every node in the search domain, search the nearest node in the reference domain within tolerance. By default, the search is not exclusive (different nodes in the search domain can be assigned to the same node in the reference domain). By default, no tolerance is imposed (the nearest node is matched).

      available inputs:
        - search_domain (Field, MeshedRegion)
        - reference_domain (Field, MeshedRegion)
        - tolerance (float) (optional)
        - exclusive_search (bool) (optional)

      available outputs:
        - search_indices (Scoping)
        - reference_indices (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.point_cloud_search()

      >>> # Make input connections
      >>> my_search_domain = dpf.Field()
      >>> op.inputs.search_domain.connect(my_search_domain)
      >>> my_reference_domain = dpf.Field()
      >>> op.inputs.reference_domain.connect(my_reference_domain)
      >>> my_tolerance = float()
      >>> op.inputs.tolerance.connect(my_tolerance)
      >>> my_exclusive_search = bool()
      >>> op.inputs.exclusive_search.connect(my_exclusive_search)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.point_cloud_search(search_domain=my_search_domain,reference_domain=my_reference_domain,tolerance=my_tolerance,exclusive_search=my_exclusive_search)

      >>> # Get output data
      >>> result_search_indices = op.outputs.search_indices()
      >>> result_reference_indices = op.outputs.reference_indices()"""
    def __init__(self, search_domain=None, reference_domain=None, tolerance=None, exclusive_search=None, config=None, server=None):
        super().__init__(name="point_cloud_search", config = config, server = server)
        self._inputs = InputsPointCloudSearch(self)
        self._outputs = OutputsPointCloudSearch(self)
        if search_domain !=None:
            self.inputs.search_domain.connect(search_domain)
        if reference_domain !=None:
            self.inputs.reference_domain.connect(reference_domain)
        if tolerance !=None:
            self.inputs.tolerance.connect(tolerance)
        if exclusive_search !=None:
            self.inputs.exclusive_search.connect(exclusive_search)

    @staticmethod
    def _spec():
        spec = Specification(description="""For every node in the search domain, search the nearest node in the reference domain within tolerance. By default, the search is not exclusive (different nodes in the search domain can be assigned to the same node in the reference domain). By default, no tolerance is imposed (the nearest node is matched).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "search_domain", type_names=["field","abstract_meshed_region"], optional=False, document="""Search domain"""), 
                                 1 : PinSpecification(name = "reference_domain", type_names=["field","abstract_meshed_region"], optional=False, document="""Reference domain"""), 
                                 2 : PinSpecification(name = "tolerance", type_names=["double"], optional=True, document="""Tolerance. Default: no tolerance (match nearest)"""), 
                                 3 : PinSpecification(name = "exclusive_search", type_names=["bool"], optional=True, document="""Make the search exclusive. Default: False""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "search_indices", type_names=["scoping"], optional=False, document="""Matched node Ids in the search domain"""), 
                                 1 : PinSpecification(name = "reference_indices", type_names=["scoping"], optional=False, document="""Matched node Ids in the reference domain""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "point_cloud_search")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsPointCloudSearch 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsPointCloudSearch 
        """
        return super().outputs


#internal name: point_cloud_search
#scripting name: point_cloud_search
class InputsPointCloudSearch(_Inputs):
    """Intermediate class used to connect user inputs to point_cloud_search operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.point_cloud_search()
      >>> my_search_domain = dpf.Field()
      >>> op.inputs.search_domain.connect(my_search_domain)
      >>> my_reference_domain = dpf.Field()
      >>> op.inputs.reference_domain.connect(my_reference_domain)
      >>> my_tolerance = float()
      >>> op.inputs.tolerance.connect(my_tolerance)
      >>> my_exclusive_search = bool()
      >>> op.inputs.exclusive_search.connect(my_exclusive_search)
    """
    def __init__(self, op: Operator):
        super().__init__(point_cloud_search._spec().inputs, op)
        self._search_domain = Input(point_cloud_search._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._search_domain)
        self._reference_domain = Input(point_cloud_search._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._reference_domain)
        self._tolerance = Input(point_cloud_search._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._tolerance)
        self._exclusive_search = Input(point_cloud_search._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._exclusive_search)

    @property
    def search_domain(self):
        """Allows to connect search_domain input to the operator

        - pindoc: Search domain

        Parameters
        ----------
        my_search_domain : Field, MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> op.inputs.search_domain.connect(my_search_domain)
        >>> #or
        >>> op.inputs.search_domain(my_search_domain)

        """
        return self._search_domain

    @property
    def reference_domain(self):
        """Allows to connect reference_domain input to the operator

        - pindoc: Reference domain

        Parameters
        ----------
        my_reference_domain : Field, MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> op.inputs.reference_domain.connect(my_reference_domain)
        >>> #or
        >>> op.inputs.reference_domain(my_reference_domain)

        """
        return self._reference_domain

    @property
    def tolerance(self):
        """Allows to connect tolerance input to the operator

        - pindoc: Tolerance. Default: no tolerance (match nearest)

        Parameters
        ----------
        my_tolerance : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> op.inputs.tolerance.connect(my_tolerance)
        >>> #or
        >>> op.inputs.tolerance(my_tolerance)

        """
        return self._tolerance

    @property
    def exclusive_search(self):
        """Allows to connect exclusive_search input to the operator

        - pindoc: Make the search exclusive. Default: False

        Parameters
        ----------
        my_exclusive_search : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> op.inputs.exclusive_search.connect(my_exclusive_search)
        >>> #or
        >>> op.inputs.exclusive_search(my_exclusive_search)

        """
        return self._exclusive_search

class OutputsPointCloudSearch(_Outputs):
    """Intermediate class used to get outputs from point_cloud_search operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.point_cloud_search()
      >>> # Connect inputs : op.inputs. ...
      >>> result_search_indices = op.outputs.search_indices()
      >>> result_reference_indices = op.outputs.reference_indices()
    """
    def __init__(self, op: Operator):
        super().__init__(point_cloud_search._spec().outputs, op)
        self._search_indices = Output(point_cloud_search._spec().output_pin(0), 0, op) 
        self._outputs.append(self._search_indices)
        self._reference_indices = Output(point_cloud_search._spec().output_pin(1), 1, op) 
        self._outputs.append(self._reference_indices)

    @property
    def search_indices(self):
        """Allows to get search_indices output of the operator


        - pindoc: Matched node Ids in the search domain

        Returns
        ----------
        my_search_indices : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> # Connect inputs : op.inputs. ...
        >>> result_search_indices = op.outputs.search_indices() 
        """
        return self._search_indices

    @property
    def reference_indices(self):
        """Allows to get reference_indices output of the operator


        - pindoc: Matched node Ids in the reference domain

        Returns
        ----------
        my_reference_indices : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.point_cloud_search()
        >>> # Connect inputs : op.inputs. ...
        >>> result_reference_indices = op.outputs.reference_indices() 
        """
        return self._reference_indices

