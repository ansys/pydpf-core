"""
expansion_psd
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "math" category
"""

class expansion_psd(Operator):
    """
Computes the response power spectral density (RPSD) or 1-sigma response from a PSD analysis by combining mode shapes (or harmonic results), covariance matrices, and optionally static shapes.

**Response type**
- If pin 5 is false (default) and constant covariance matrices are provided: 1-sigma response is computed from mode shapes (label "time") and covariance matrix $Q$  (only labels "Mode_i" and "Mode_j"):
$\displaystyle \sigma_k = \sqrt{\sum_{i=1}^N{\sum_{j=1}^N{\phi_{ik} \phi_{jk} Q_{ij}}}}$
- If pin 5 is false (default) and frequency-dependent covariance matrices are provided: RPSD response is computed from mode shapes (label "time") and modal PSD matrix $R(\omega)$ (labels "Mode_i", "Mode_j" and "time"):
$\displaystyle S_k(\omega) = \sum_{i=1}^N{\sum_{j=1}^N{\phi_{ik} \phi_{jk} R_{ij}(\omega)}}$
- If pin 5 is true: RPSD response is computed from harmonic results amplitude (label "input_dof_index" and "time") and input PSD matrix $\bar{S}(\omega)$ (labels "input_dof_index_i", "input_dof_index_j" and "time"):
$\displaystyle S_k(\omega) = \sum_{i=1}^N{\sum_{j=1}^N{u_{ik}(\omega) u_{jk}(\omega) \bar{S}_{ij}(\omega)}}$

**Absolute/relative response computation**:
- If static shapes (pin 1) are provided and non-empty: computes absolute response ($\sigma^2 = \sigma_{\text{rel}}^2 + \sigma_{\text{stat}}^2 + 2 \sigma_{\text{rel,stat}}^2$).
- If static shapes are empty or not provided: computes relative response from mode-mode covariance terms only ($\sigma^2 = \sigma_{\text{rel}}^2$).
- If input mode shapes or harmonic results are empty: output contains an empty field with the same label structure and support as the covariance matrix input.


      available inputs:
        - mode_shapes (FieldsContainer)
        - static_shapes (FieldsContainer) (optional)
        - rel_rel_covar_matrix (FieldsContainer)
        - stat_stat_covar_matrix (FieldsContainer) (optional)
        - rel_stat_covar_matrix (FieldsContainer) (optional)
        - is_rpsd_from_harm (bool) (optional)

      available outputs:
        - psd (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.expansion_psd()

      >>> # Make input connections
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)
      >>> my_static_shapes = dpf.FieldsContainer()
      >>> op.inputs.static_shapes.connect(my_static_shapes)
      >>> my_rel_rel_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.rel_rel_covar_matrix.connect(my_rel_rel_covar_matrix)
      >>> my_stat_stat_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.stat_stat_covar_matrix.connect(my_stat_stat_covar_matrix)
      >>> my_rel_stat_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.rel_stat_covar_matrix.connect(my_rel_stat_covar_matrix)
      >>> my_is_rpsd_from_harm = bool()
      >>> op.inputs.is_rpsd_from_harm.connect(my_is_rpsd_from_harm)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.expansion_psd(mode_shapes=my_mode_shapes,static_shapes=my_static_shapes,rel_rel_covar_matrix=my_rel_rel_covar_matrix,stat_stat_covar_matrix=my_stat_stat_covar_matrix,rel_stat_covar_matrix=my_rel_stat_covar_matrix,is_rpsd_from_harm=my_is_rpsd_from_harm)

      >>> # Get output data
      >>> result_psd = op.outputs.psd()"""
    def __init__(self, mode_shapes=None, static_shapes=None, rel_rel_covar_matrix=None, stat_stat_covar_matrix=None, rel_stat_covar_matrix=None, is_rpsd_from_harm=None, config=None, server=None):
        super().__init__(name="expansion::psd", config = config, server = server)
        self._inputs = InputsExpansionPsd(self)
        self._outputs = OutputsExpansionPsd(self)
        if mode_shapes !=None:
            self.inputs.mode_shapes.connect(mode_shapes)
        if static_shapes !=None:
            self.inputs.static_shapes.connect(static_shapes)
        if rel_rel_covar_matrix !=None:
            self.inputs.rel_rel_covar_matrix.connect(rel_rel_covar_matrix)
        if stat_stat_covar_matrix !=None:
            self.inputs.stat_stat_covar_matrix.connect(stat_stat_covar_matrix)
        if rel_stat_covar_matrix !=None:
            self.inputs.rel_stat_covar_matrix.connect(rel_stat_covar_matrix)
        if is_rpsd_from_harm !=None:
            self.inputs.is_rpsd_from_harm.connect(is_rpsd_from_harm)

    @staticmethod
    def _spec():
        spec = Specification(description="""
Computes the response power spectral density (RPSD) or 1-sigma response from a PSD analysis by combining mode shapes (or harmonic results), covariance matrices, and optionally static shapes.

**Response type**
- If pin 5 is false (default) and constant covariance matrices are provided: 1-sigma response is computed from mode shapes (label "time") and covariance matrix $Q$  (only labels "Mode_i" and "Mode_j"):
$\displaystyle \sigma_k = \sqrt{\sum_{i=1}^N{\sum_{j=1}^N{\phi_{ik} \phi_{jk} Q_{ij}}}}$
- If pin 5 is false (default) and frequency-dependent covariance matrices are provided: RPSD response is computed from mode shapes (label "time") and modal PSD matrix $R(\omega)$ (labels "Mode_i", "Mode_j" and "time"):
$\displaystyle S_k(\omega) = \sum_{i=1}^N{\sum_{j=1}^N{\phi_{ik} \phi_{jk} R_{ij}(\omega)}}$
- If pin 5 is true: RPSD response is computed from harmonic results amplitude (label "input_dof_index" and "time") and input PSD matrix $\bar{S}(\omega)$ (labels "input_dof_index_i", "input_dof_index_j" and "time"):
$\displaystyle S_k(\omega) = \sum_{i=1}^N{\sum_{j=1}^N{u_{ik}(\omega) u_{jk}(\omega) \bar{S}_{ij}(\omega)}}$

**Absolute/relative response computation**:
- If static shapes (pin 1) are provided and non-empty: computes absolute response ($\sigma^2 = \sigma_{\text{rel}}^2 + \sigma_{\text{stat}}^2 + 2 \sigma_{\text{rel,stat}}^2$).
- If static shapes are empty or not provided: computes relative response from mode-mode covariance terms only ($\sigma^2 = \sigma_{\text{rel}}^2$).
- If input mode shapes or harmonic results are empty: output contains an empty field with the same label structure and support as the covariance matrix input.
""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mode_shapes", type_names=["fields_container"], optional=False, document="""Fields container containing the expansion vectors (mode shapes or harmonic results). Label conventions are defined by pin 5."""), 
                                 1 : PinSpecification(name = "static_shapes", type_names=["fields_container"], optional=True, document="""Fields container containing the static shapes (base excitations) from spectral analysis file. If not empty, pins 3 and 4 are required."""), 
                                 2 : PinSpecification(name = "rel_rel_covar_matrix", type_names=["fields_container"], optional=False, document="""Fields container containing the dynamic covariance or PSD matrix (relative-relative term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5."""), 
                                 3 : PinSpecification(name = "stat_stat_covar_matrix", type_names=["fields_container"], optional=True, document="""Fields container containing the static covariance or PSD matrix (static-static term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5."""), 
                                 4 : PinSpecification(name = "rel_stat_covar_matrix", type_names=["fields_container"], optional=True, document="""Fields container containing the dynamic-static covariance or PSD matrix (relative-static term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5."""), 
                                 5 : PinSpecification(name = "is_rpsd_from_harm", type_names=["bool"], optional=True, document="""
Boolean value selecting the PSD expansion source:
- false (default): expansion from mode shapes.
- true: expansion from harmonic results.

This flag also defines covariance matrix label conventions for pins 2, 3, and 4:
- If false: expected labels are "Mode_i" and "Mode_j"; label "time" is additionally expected for frequency-dependent PSD data.
- If true: expected labels are "input_dof_index_i", "input_dof_index_j", and "time".

Similarly, mode shapes label convention for pin 0 is:
- If false: expected label is "time".
- If true: expected labels are "input_dof_index" and "time".""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "psd", type_names=["fields_container"], optional=False, document="""Response PSD (if frequency-dependent matrices) or 1-sigma response per output label space. Can contain an empty field when mode shapes are empty.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "expansion::psd")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator.

        Returns
        --------
        inputs : InputsExpansionPsd 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it.

        Returns
        --------
        outputs : OutputsExpansionPsd 
        """
        return super().outputs


#internal name: expansion::psd
#scripting name: expansion_psd
class InputsExpansionPsd(_Inputs):
    """Intermediate class used to connect user inputs to expansion_psd operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.expansion_psd()
      >>> my_mode_shapes = dpf.FieldsContainer()
      >>> op.inputs.mode_shapes.connect(my_mode_shapes)
      >>> my_static_shapes = dpf.FieldsContainer()
      >>> op.inputs.static_shapes.connect(my_static_shapes)
      >>> my_rel_rel_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.rel_rel_covar_matrix.connect(my_rel_rel_covar_matrix)
      >>> my_stat_stat_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.stat_stat_covar_matrix.connect(my_stat_stat_covar_matrix)
      >>> my_rel_stat_covar_matrix = dpf.FieldsContainer()
      >>> op.inputs.rel_stat_covar_matrix.connect(my_rel_stat_covar_matrix)
      >>> my_is_rpsd_from_harm = bool()
      >>> op.inputs.is_rpsd_from_harm.connect(my_is_rpsd_from_harm)
    """
    def __init__(self, op: Operator):
        super().__init__(expansion_psd._spec().inputs, op)
        self._mode_shapes = Input(expansion_psd._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mode_shapes)
        self._static_shapes = Input(expansion_psd._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._static_shapes)
        self._rel_rel_covar_matrix = Input(expansion_psd._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._rel_rel_covar_matrix)
        self._stat_stat_covar_matrix = Input(expansion_psd._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._stat_stat_covar_matrix)
        self._rel_stat_covar_matrix = Input(expansion_psd._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._rel_stat_covar_matrix)
        self._is_rpsd_from_harm = Input(expansion_psd._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._is_rpsd_from_harm)

    @property
    def mode_shapes(self):
        """Allows to connect mode_shapes input to the operator

        - pindoc: Fields container containing the expansion vectors (mode shapes or harmonic results). Label conventions are defined by pin 5.

        Parameters
        ----------
        my_mode_shapes : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.mode_shapes.connect(my_mode_shapes)
        >>> #or
        >>> op.inputs.mode_shapes(my_mode_shapes)

        """
        return self._mode_shapes

    @property
    def static_shapes(self):
        """Allows to connect static_shapes input to the operator

        - pindoc: Fields container containing the static shapes (base excitations) from spectral analysis file. If not empty, pins 3 and 4 are required.

        Parameters
        ----------
        my_static_shapes : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.static_shapes.connect(my_static_shapes)
        >>> #or
        >>> op.inputs.static_shapes(my_static_shapes)

        """
        return self._static_shapes

    @property
    def rel_rel_covar_matrix(self):
        """Allows to connect rel_rel_covar_matrix input to the operator

        - pindoc: Fields container containing the dynamic covariance or PSD matrix (relative-relative term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5.

        Parameters
        ----------
        my_rel_rel_covar_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.rel_rel_covar_matrix.connect(my_rel_rel_covar_matrix)
        >>> #or
        >>> op.inputs.rel_rel_covar_matrix(my_rel_rel_covar_matrix)

        """
        return self._rel_rel_covar_matrix

    @property
    def stat_stat_covar_matrix(self):
        """Allows to connect stat_stat_covar_matrix input to the operator

        - pindoc: Fields container containing the static covariance or PSD matrix (static-static term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5.

        Parameters
        ----------
        my_stat_stat_covar_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.stat_stat_covar_matrix.connect(my_stat_stat_covar_matrix)
        >>> #or
        >>> op.inputs.stat_stat_covar_matrix(my_stat_stat_covar_matrix)

        """
        return self._stat_stat_covar_matrix

    @property
    def rel_stat_covar_matrix(self):
        """Allows to connect rel_stat_covar_matrix input to the operator

        - pindoc: Fields container containing the dynamic-static covariance or PSD matrix (relative-static term). Covariance and PSD matrices can both represent displacement, velocity, or acceleration. Label conventions are defined by pin 5.

        Parameters
        ----------
        my_rel_stat_covar_matrix : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.rel_stat_covar_matrix.connect(my_rel_stat_covar_matrix)
        >>> #or
        >>> op.inputs.rel_stat_covar_matrix(my_rel_stat_covar_matrix)

        """
        return self._rel_stat_covar_matrix

    @property
    def is_rpsd_from_harm(self):
        """Allows to connect is_rpsd_from_harm input to the operator

        - pindoc: 
Boolean value selecting the PSD expansion source:
- false (default): expansion from mode shapes.
- true: expansion from harmonic results.

This flag also defines covariance matrix label conventions for pins 2, 3, and 4:
- If false: expected labels are "Mode_i" and "Mode_j"; label "time" is additionally expected for frequency-dependent PSD data.
- If true: expected labels are "input_dof_index_i", "input_dof_index_j", and "time".

Similarly, mode shapes label convention for pin 0 is:
- If false: expected label is "time".
- If true: expected labels are "input_dof_index" and "time".

        Parameters
        ----------
        my_is_rpsd_from_harm : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> op.inputs.is_rpsd_from_harm.connect(my_is_rpsd_from_harm)
        >>> #or
        >>> op.inputs.is_rpsd_from_harm(my_is_rpsd_from_harm)

        """
        return self._is_rpsd_from_harm

class OutputsExpansionPsd(_Outputs):
    """Intermediate class used to get outputs from expansion_psd operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.expansion_psd()
      >>> # Connect inputs : op.inputs. ...
      >>> result_psd = op.outputs.psd()
    """
    def __init__(self, op: Operator):
        super().__init__(expansion_psd._spec().outputs, op)
        self._psd = Output(expansion_psd._spec().output_pin(0), 0, op) 
        self._outputs.append(self._psd)

    @property
    def psd(self):
        """Allows to get psd output of the operator


        - pindoc: Response PSD (if frequency-dependent matrices) or 1-sigma response per output label space. Can contain an empty field when mode shapes are empty.

        Returns
        ----------
        my_psd : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.expansion_psd()
        >>> # Connect inputs : op.inputs. ...
        >>> result_psd = op.outputs.psd() 
        """
        return self._psd

