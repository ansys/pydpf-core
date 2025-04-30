# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""UnitSystem."""

from ansys.dpf import core as dpf
from ansys.dpf.core import errors as dpf_errors, server as server_module


class UnitSystem:
    """Defines an internally coherent way of measuring units.

    Notes
    -----
    Class available with server's version starting at 6.1 (Ansys 2023R2).
    """

    def __init__(self, name, ID=None, unit_names=None):
        """
        Create a new UnitSystem from its name and its Ansys ID.

        Parameters
        ----------
        name: string
            name of the Unit System (compulsory)
        ID: int
            internal Ansys ID that identifies the Unit System (optional)
        unit_names: string
            semicolon-separated string with the base units (Length, Mass, Time, Temperature,
            Electric Charge and Angle) (optional).

        ID and unit_names are mutually exclusionary, but one of them should
        be provided (either one or the other, but not both)

        Examples
        --------
        Create an Ansys default UnitSystem (solver_mks)

        >>> from ansys.dpf import core as dpf
        >>> my_unit_system = dpf.UnitSystem("solver_mks", ID=11)

        Create a customized version of the mks Unit System that measures
        Temperature in Fahrenheit

        >>> from ansys.dpf import core as dpf
        >>> my_unit_system = dpf.UnitSystem("my_mks", unit_names="m;kg;s;degF;C;rad")
        """
        server = server_module.get_or_create_server(None)
        if server and not server.meet_version("6.1"):  # pragma: no cover
            raise dpf_errors.DpfVersionNotSupported("6.1")
        if not isinstance(name, str):
            raise dpf_errors.InvalidTypeError("str", "name")

        if ID is not None and unit_names is None:
            if not isinstance(ID, int):
                raise dpf_errors.InvalidTypeError("int", "ID")
            self._name = name
            self._ID = ID
            self._unit_names = ""
        elif ID is None and unit_names is not None:
            if not isinstance(unit_names, str):
                raise dpf_errors.InvalidTypeError("str", "unit_names")
            unit_system_check = dpf.Operator("check_unit_system")
            unit_system_check.connect(0, unit_names)
            unit_system_isok = unit_system_check.get_output(0, bool)
            if unit_system_isok:
                self._name = name
                self._ID = -2
                self._unit_names = unit_names
            else:
                raise Exception(unit_system_check.outputs.get_output(1, str))

        else:
            raise Exception(
                "ID and unit_names are mutually exclusionary, but one of them should be provided."
            )

    @property
    def ID(self) -> int:
        """Return ID of the unit system."""
        return self._ID

    @property
    def name(self) -> str:
        """Return the name of the unit system."""
        return self._name

    @property
    def unit_names(self) -> str:
        """Return unit names making up the unit system."""
        if self._unit_names == "":  # Ansys UnitSystem
            unit_system_strings = dpf.Operator("unit_system_strings")
            unit_system_strings.connect(0, self._ID)
            return unit_system_strings.get_output(0, str)
        else:  # Custom UnitSystem
            return self._unit_names


class unit_systems:
    """Contains common Ansys predefined UnitSystems.

    Notes
    -----
    Class available with server's version starting at 6.1 (Ansys 2023R2).

    Attributes
    ----------
    solver_mks : Metric (m, kg, N, s, J, Pa, degC, C, rad)

    solver_cgs : Metric (cm, g, dyne, s, erg, dyne*cm^-2, degC, C, rad)

    solver_nmm : Metric (mm, ton, N, s, mJ, MPa, degC, mC, rad)

    solver_umks : Metric (um, kg, uN, s, pJ, MPa, degC, pC, rad)

    solver_knms : Metric (mm, kg, kN, ms, J, GPa, degC, mC, rad)

    solver_bft : U.S. Customary (ft, slug, lbf, s, ft*lbf, lbf*ft^-2, degF, C, rad)

    solver_bin : U.S. Customary (in, slinch, lbf, s, in*lbf, lbf*in^-2, degF, C, rad)

    undefined : All units are dimensionless

    """

    try:
        solver_mks = UnitSystem("solver_mks", ID=11)
        solver_cgs = UnitSystem("solver_cgs", ID=5)
        solver_nmm = UnitSystem("solver_nmm", ID=6)
        solver_umks = UnitSystem("solver_umks", ID=10)
        solver_knms = UnitSystem("solver_knms", ID=16)
        solver_bft = UnitSystem("solver_bft", ID=7)
        solver_bin = UnitSystem("solver_bin", ID=8)
        undefined = UnitSystem("undefined", ID=-1)
    except dpf_errors.DpfVersionNotSupported as e:  # pragma: no cover
        pass
