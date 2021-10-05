"""
members_in_compression_not_certified
====================================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "result" category
"""

class members_in_compression_not_certified(Operator):
    """This operator is a non-certified example of buckling resistance verification for the compression members for Class I, 2 and 3 cross-sections. It is only provided as an example if you want to develop your own compute norm operator. The results computed by this beta operator have not been certified by ANSYS. ANSYS declines all responsibility for the use of this operator.

      available inputs:
        - time_scoping (Scoping, list, int) (optional)
        - field_yield_strength (DataSources, Field)
        - field_end_condition (DataSources, Field)
        - streams (StreamsContainer) (optional)
        - data_sources (DataSources) (optional)
        - manufacture (bool)
        - partial_factor (float)
        - mesh (MeshedRegion)
        - axial_force (FieldsContainer)
        - fabrication_type (bool)

      available outputs:
        - buckling_resistance_compression_yy (FieldsContainer)
        - buckling_resistance_compression_zz (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.members_in_compression_not_certified()

      >>> # Make input connections
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field_yield_strength = dpf.DataSources()
      >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
      >>> my_field_end_condition = dpf.DataSources()
      >>> op.inputs.field_end_condition.connect(my_field_end_condition)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_manufacture = bool()
      >>> op.inputs.manufacture.connect(my_manufacture)
      >>> my_partial_factor = float()
      >>> op.inputs.partial_factor.connect(my_partial_factor)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_axial_force = dpf.FieldsContainer()
      >>> op.inputs.axial_force.connect(my_axial_force)
      >>> my_fabrication_type = bool()
      >>> op.inputs.fabrication_type.connect(my_fabrication_type)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.members_in_compression_not_certified(time_scoping=my_time_scoping,field_yield_strength=my_field_yield_strength,field_end_condition=my_field_end_condition,streams=my_streams,data_sources=my_data_sources,manufacture=my_manufacture,partial_factor=my_partial_factor,mesh=my_mesh,axial_force=my_axial_force,fabrication_type=my_fabrication_type)

      >>> # Get output data
      >>> result_buckling_resistance_compression_yy = op.outputs.buckling_resistance_compression_yy()
      >>> result_buckling_resistance_compression_zz = op.outputs.buckling_resistance_compression_zz()"""
    def __init__(self, time_scoping=None, field_yield_strength=None, field_end_condition=None, streams=None, data_sources=None, manufacture=None, partial_factor=None, mesh=None, axial_force=None, fabrication_type=None, config=None, server=None):
        super().__init__(name="members_in_compression_not_certified", config = config, server = server)
        self._inputs = InputsMembersInCompressionNotCertified(self)
        self._outputs = OutputsMembersInCompressionNotCertified(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if field_yield_strength !=None:
            self.inputs.field_yield_strength.connect(field_yield_strength)
        if field_end_condition !=None:
            self.inputs.field_end_condition.connect(field_end_condition)
        if streams !=None:
            self.inputs.streams.connect(streams)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if manufacture !=None:
            self.inputs.manufacture.connect(manufacture)
        if partial_factor !=None:
            self.inputs.partial_factor.connect(partial_factor)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if axial_force !=None:
            self.inputs.axial_force.connect(axial_force)
        if fabrication_type !=None:
            self.inputs.fabrication_type.connect(fabrication_type)

    @staticmethod
    def _spec():
        spec = Specification(description="""This operator is a non-certified example of buckling resistance verification for the compression members for Class I, 2 and 3 cross-sections. It is only provided as an example if you want to develop your own compute norm operator. The results computed by this beta operator have not been certified by ANSYS. ANSYS declines all responsibility for the use of this operator.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping","vector<int32>","int32"], optional=True, document="""time/freq set ids (use ints or scoping) """), 
                                 1 : PinSpecification(name = "field_yield_strength", type_names=["data_sources","field"], optional=False, document="""This pin contains file csv or field of beam's Yield Strength."""), 
                                 2 : PinSpecification(name = "field_end_condition", type_names=["data_sources","field"], optional=False, document="""This pin contains file csv or field of beam's end condition defined by the user. If no input at this pin found, it would take end condition's value of all beams as 1."""), 
                                 3 : PinSpecification(name = "streams", type_names=["streams_container"], optional=True, document=""" result file container allowed to be kept open to cache data."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=True, document="""result file path container, used if no streams are set."""), 
                                 5 : PinSpecification(name = "manufacture", type_names=["bool"], optional=False, document="""Manufacturing processus:hot finished if TRUE or cold formed if FALSE. Default value : hot finished."""), 
                                 6 : PinSpecification(name = "partial_factor", type_names=["double"], optional=False, document="""partial safety factor for resistance of members to instability assessed by member checks. Default value: 1."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document=""" Mesh containing beam's properties defined by user"""), 
                                 8 : PinSpecification(name = "axial_force", type_names=["fields_container"], optional=False, document="""Fields Container of axial force defined by user"""), 
                                 12 : PinSpecification(name = "fabrication_type", type_names=["bool"], optional=False, document="""If there is beam I in the structure, please define its fabrication type. True: Rolled section, False: Welded section""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "buckling_resistance_compression_yy", type_names=["fields_container"], optional=False, document="""Fields Container of buckling resistance factor on axis y-y in case of compression. These factors should be less than 1 and positive."""), 
                                 1 : PinSpecification(name = "buckling_resistance_compression_zz", type_names=["fields_container"], optional=False, document="""Fields Container of buckling resistance factor on axis z-z in case of compression. These factors should be less than 1 and positive.""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "members_in_compression_not_certified")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMembersInCompressionNotCertified 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMembersInCompressionNotCertified 
        """
        return super().outputs


#internal name: members_in_compression_not_certified
#scripting name: members_in_compression_not_certified
class InputsMembersInCompressionNotCertified(_Inputs):
    """Intermediate class used to connect user inputs to members_in_compression_not_certified operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.members_in_compression_not_certified()
      >>> my_time_scoping = dpf.Scoping()
      >>> op.inputs.time_scoping.connect(my_time_scoping)
      >>> my_field_yield_strength = dpf.DataSources()
      >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
      >>> my_field_end_condition = dpf.DataSources()
      >>> op.inputs.field_end_condition.connect(my_field_end_condition)
      >>> my_streams = dpf.StreamsContainer()
      >>> op.inputs.streams.connect(my_streams)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_manufacture = bool()
      >>> op.inputs.manufacture.connect(my_manufacture)
      >>> my_partial_factor = float()
      >>> op.inputs.partial_factor.connect(my_partial_factor)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_axial_force = dpf.FieldsContainer()
      >>> op.inputs.axial_force.connect(my_axial_force)
      >>> my_fabrication_type = bool()
      >>> op.inputs.fabrication_type.connect(my_fabrication_type)
    """
    def __init__(self, op: Operator):
        super().__init__(members_in_compression_not_certified._spec().inputs, op)
        self._time_scoping = Input(members_in_compression_not_certified._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._time_scoping)
        self._field_yield_strength = Input(members_in_compression_not_certified._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._field_yield_strength)
        self._field_end_condition = Input(members_in_compression_not_certified._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._field_end_condition)
        self._streams = Input(members_in_compression_not_certified._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams)
        self._data_sources = Input(members_in_compression_not_certified._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._manufacture = Input(members_in_compression_not_certified._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._manufacture)
        self._partial_factor = Input(members_in_compression_not_certified._spec().input_pin(6), 6, op, -1) 
        self._inputs.append(self._partial_factor)
        self._mesh = Input(members_in_compression_not_certified._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)
        self._axial_force = Input(members_in_compression_not_certified._spec().input_pin(8), 8, op, -1) 
        self._inputs.append(self._axial_force)
        self._fabrication_type = Input(members_in_compression_not_certified._spec().input_pin(12), 12, op, -1) 
        self._inputs.append(self._fabrication_type)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator

        - pindoc: time/freq set ids (use ints or scoping) 

        Parameters
        ----------
        my_time_scoping : Scoping, list, int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> #or
        >>> op.inputs.time_scoping(my_time_scoping)

        """
        return self._time_scoping

    @property
    def field_yield_strength(self):
        """Allows to connect field_yield_strength input to the operator

        - pindoc: This pin contains file csv or field of beam's Yield Strength.

        Parameters
        ----------
        my_field_yield_strength : DataSources, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.field_yield_strength.connect(my_field_yield_strength)
        >>> #or
        >>> op.inputs.field_yield_strength(my_field_yield_strength)

        """
        return self._field_yield_strength

    @property
    def field_end_condition(self):
        """Allows to connect field_end_condition input to the operator

        - pindoc: This pin contains file csv or field of beam's end condition defined by the user. If no input at this pin found, it would take end condition's value of all beams as 1.

        Parameters
        ----------
        my_field_end_condition : DataSources, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.field_end_condition.connect(my_field_end_condition)
        >>> #or
        >>> op.inputs.field_end_condition(my_field_end_condition)

        """
        return self._field_end_condition

    @property
    def streams(self):
        """Allows to connect streams input to the operator

        - pindoc:  result file container allowed to be kept open to cache data.

        Parameters
        ----------
        my_streams : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.streams.connect(my_streams)
        >>> #or
        >>> op.inputs.streams(my_streams)

        """
        return self._streams

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: result file path container, used if no streams are set.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def manufacture(self):
        """Allows to connect manufacture input to the operator

        - pindoc: Manufacturing processus:hot finished if TRUE or cold formed if FALSE. Default value : hot finished.

        Parameters
        ----------
        my_manufacture : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.manufacture.connect(my_manufacture)
        >>> #or
        >>> op.inputs.manufacture(my_manufacture)

        """
        return self._manufacture

    @property
    def partial_factor(self):
        """Allows to connect partial_factor input to the operator

        - pindoc: partial safety factor for resistance of members to instability assessed by member checks. Default value: 1.

        Parameters
        ----------
        my_partial_factor : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.partial_factor.connect(my_partial_factor)
        >>> #or
        >>> op.inputs.partial_factor(my_partial_factor)

        """
        return self._partial_factor

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc:  Mesh containing beam's properties defined by user

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def axial_force(self):
        """Allows to connect axial_force input to the operator

        - pindoc: Fields Container of axial force defined by user

        Parameters
        ----------
        my_axial_force : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.axial_force.connect(my_axial_force)
        >>> #or
        >>> op.inputs.axial_force(my_axial_force)

        """
        return self._axial_force

    @property
    def fabrication_type(self):
        """Allows to connect fabrication_type input to the operator

        - pindoc: If there is beam I in the structure, please define its fabrication type. True: Rolled section, False: Welded section

        Parameters
        ----------
        my_fabrication_type : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> op.inputs.fabrication_type.connect(my_fabrication_type)
        >>> #or
        >>> op.inputs.fabrication_type(my_fabrication_type)

        """
        return self._fabrication_type

class OutputsMembersInCompressionNotCertified(_Outputs):
    """Intermediate class used to get outputs from members_in_compression_not_certified operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.members_in_compression_not_certified()
      >>> # Connect inputs : op.inputs. ...
      >>> result_buckling_resistance_compression_yy = op.outputs.buckling_resistance_compression_yy()
      >>> result_buckling_resistance_compression_zz = op.outputs.buckling_resistance_compression_zz()
    """
    def __init__(self, op: Operator):
        super().__init__(members_in_compression_not_certified._spec().outputs, op)
        self._buckling_resistance_compression_yy = Output(members_in_compression_not_certified._spec().output_pin(0), 0, op) 
        self._outputs.append(self._buckling_resistance_compression_yy)
        self._buckling_resistance_compression_zz = Output(members_in_compression_not_certified._spec().output_pin(1), 1, op) 
        self._outputs.append(self._buckling_resistance_compression_zz)

    @property
    def buckling_resistance_compression_yy(self):
        """Allows to get buckling_resistance_compression_yy output of the operator


        - pindoc: Fields Container of buckling resistance factor on axis y-y in case of compression. These factors should be less than 1 and positive.

        Returns
        ----------
        my_buckling_resistance_compression_yy : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> # Connect inputs : op.inputs. ...
        >>> result_buckling_resistance_compression_yy = op.outputs.buckling_resistance_compression_yy() 
        """
        return self._buckling_resistance_compression_yy

    @property
    def buckling_resistance_compression_zz(self):
        """Allows to get buckling_resistance_compression_zz output of the operator


        - pindoc: Fields Container of buckling resistance factor on axis z-z in case of compression. These factors should be less than 1 and positive.

        Returns
        ----------
        my_buckling_resistance_compression_zz : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.members_in_compression_not_certified()
        >>> # Connect inputs : op.inputs. ...
        >>> result_buckling_resistance_compression_zz = op.outputs.buckling_resistance_compression_zz() 
        """
        return self._buckling_resistance_compression_zz

