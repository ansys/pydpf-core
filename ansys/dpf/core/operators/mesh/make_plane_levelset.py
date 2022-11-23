"""
make_plane_levelset
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from "mesh" category
"""

class make_plane_levelset(Operator):
    """Compute the levelset for a plane using coordinates.

      available inputs:
        - coordinates (MeshedRegion, Field)
        - normal (Field)
        - origin (Field)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.make_plane_levelset()

      >>> # Make input connections
      >>> my_coordinates = dpf.MeshedRegion()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_normal = dpf.Field()
      >>> op.inputs.normal.connect(my_normal)
      >>> my_origin = dpf.Field()
      >>> op.inputs.origin.connect(my_origin)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.make_plane_levelset(coordinates=my_coordinates,normal=my_normal,origin=my_origin)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, coordinates=None, normal=None, origin=None, config=None, server=None):
        super().__init__(name="levelset::make_plane", config = config, server = server)
        self._inputs = InputsMakePlaneLevelset(self)
        self._outputs = OutputsMakePlaneLevelset(self)
        if coordinates !=None:
            self.inputs.coordinates.connect(coordinates)
        if normal !=None:
            self.inputs.normal.connect(normal)
        if origin !=None:
            self.inputs.origin.connect(origin)

    @staticmethod
    def _spec():
        spec = Specification(description="""Compute the levelset for a plane using coordinates.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "coordinates", type_names=["abstract_meshed_region","field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "normal", type_names=["field"], optional=False, document="""An overall 3d vector that gives normal direction of the plane."""), 
                                 2 : PinSpecification(name = "origin", type_names=["field"], optional=False, document="""An overall 3d vector that gives a point of the plane.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "levelset::make_plane")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakePlaneLevelset 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMakePlaneLevelset 
        """
        return super().outputs


#internal name: levelset::make_plane
#scripting name: make_plane_levelset
class InputsMakePlaneLevelset(_Inputs):
    """Intermediate class used to connect user inputs to make_plane_levelset operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.make_plane_levelset()
      >>> my_coordinates = dpf.MeshedRegion()
      >>> op.inputs.coordinates.connect(my_coordinates)
      >>> my_normal = dpf.Field()
      >>> op.inputs.normal.connect(my_normal)
      >>> my_origin = dpf.Field()
      >>> op.inputs.origin.connect(my_origin)
    """
    def __init__(self, op: Operator):
        super().__init__(make_plane_levelset._spec().inputs, op)
        self._coordinates = Input(make_plane_levelset._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._coordinates)
        self._normal = Input(make_plane_levelset._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._normal)
        self._origin = Input(make_plane_levelset._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._origin)

    @property
    def coordinates(self):
        """Allows to connect coordinates input to the operator

        Parameters
        ----------
        my_coordinates : MeshedRegion, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.make_plane_levelset()
        >>> op.inputs.coordinates.connect(my_coordinates)
        >>> #or
        >>> op.inputs.coordinates(my_coordinates)

        """
        return self._coordinates

    @property
    def normal(self):
        """Allows to connect normal input to the operator

        - pindoc: An overall 3d vector that gives normal direction of the plane.

        Parameters
        ----------
        my_normal : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.make_plane_levelset()
        >>> op.inputs.normal.connect(my_normal)
        >>> #or
        >>> op.inputs.normal(my_normal)

        """
        return self._normal

    @property
    def origin(self):
        """Allows to connect origin input to the operator

        - pindoc: An overall 3d vector that gives a point of the plane.

        Parameters
        ----------
        my_origin : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.make_plane_levelset()
        >>> op.inputs.origin.connect(my_origin)
        >>> #or
        >>> op.inputs.origin(my_origin)

        """
        return self._origin

class OutputsMakePlaneLevelset(_Outputs):
    """Intermediate class used to get outputs from make_plane_levelset operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.make_plane_levelset()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(make_plane_levelset._spec().outputs, op)
        self._field = Output(make_plane_levelset._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.make_plane_levelset()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

