"""
.. _ref_unit_system:

UnitSystem
===============
"""
from ansys import dpf
from ansys.dpf import core as dpf
from ansys.dpf.core import errors as dpf_errors

class UnitSystem:
    """Defines an internally coherent way of measuring units.
    """
    def __init__(self, name, id=None, unit_names=None):
        """
        Creates a new UnitSystem from its name and its Ansys Id

        Parameters
        ----------
        name: string
            name of the Unit System (compulsory)
        id: int
            internal Ansys Id that identifies the Unit System (optional)
        unit_names: string
            semicolon-separated string with the base units (Length, Mass, Time, Temperature, Electric Charge and Angle)
            (optional).

        id and unit_names are mutually exclusionary, but one of them should
        be provided (either one or the other, but not both)

        Examples
        --------
        Create an Ansys default UnitSystem (solver_mks)

        >>> from ansys.dpf import core as dpf
        >>> my_unit_system = dpf.UnitSystem("solver_mks", id=11)

        Create a customized version of the mks Unit System that measures
        Temperature in Fahrenheit

        >>> from ansys.dpf import core as dpf
        >>> my_unit_system = dpf.UnitSystem("my_mks", unit_names="m;kg;s;degF;C;rad")
        """
        if not isinstance(name, str):
            raise dpf_errors.InvalidTypeError("str", "name")

        if id is not None and unit_names is None:
            if not isinstance(id, int):
                raise dpf_errors.InvalidTypeError("int", "id")
            self._name = name
            self._id = id
            self._unit_names = ""
        elif id is None and unit_names is not None:
            if not isinstance(unit_names, str):
                raise dpf_errors.InvalidTypeError("str", "unit_names")
            unit_system_check = dpf.Operator("check_unit_system")
            unit_system_check.connect(0, unit_names)
            unit_system_isok = unit_system_check.get_output(0, bool)
            if unit_system_isok:
                self._name = name
                self._id = -2
                self._unit_names = unit_names
            else:
                raise Exception(unit_system_check.outputs.get_output(1, str))
            
        else:
            raise Exception("id and unit_names are mutually exclusionary, but one of them should be provided.")

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def unit_names(self) -> str:
        if self._unit_names == "": #Ansys UnitSystem
            unit_system_strings = dpf.Operator("unit_system_strings")
            unit_system_strings.connect(0, self._id)
            return unit_system_strings.get_output(0, str)
        else: #Custom UnitSystem
            return self._unit_names


class unit_systems:
    """Contains common Ansys predefined UnitSystems.

    Attributes
    -----------
    solver_mks : Metric (m, kg, N, s, J, Pa, degC, C, rad)

    ansys_cgs : Metric (cm, g, dyne, s, erg, dyne*cm^-2, degC, C, rad)

    solver_nmm : Metric (mm, ton, N, s, mJ, MPa, degC, mC, rad)

    solver_umks : Metric (um, kg, uN, s, pJ, MPa, degC, pC, rad)

    solver_knms : Metric (mm, kg, kN, ms, J, GPa, degC, mC, rad)

    solver_bft : U.S. Customary (ft, slug, lbf, s, ft*lbf, lbf*ft^-2, degF, C, rad)

    solver_bin : U.S. Customary (in, slinch, lbf, s, in*lbf, lbf*in^-2, degF, C, rad)

    undefined : All units are dimensionless

    """
    solver_mks = UnitSystem("solver_mks", id=11)
    solver_cgs = UnitSystem("solver_cgs", id=5)
    solver_nmm = UnitSystem("solver_nmm", id=6)
    solver_umks = UnitSystem("solver_umks", id=10)
    solver_knms = UnitSystem("solver_knms", id=16)
    solver_bft = UnitSystem("solver_bft", id=7)
    solver_bin = UnitSystem("solver_bin", id=8)
    undefined = UnitSystem("undefined", id=-1)
