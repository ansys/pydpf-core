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

"""
AvailableResult.

Module contains the class representing the results that an operator can request.
"""

from enum import Enum, unique
from typing import List
from warnings import warn

from ansys.dpf.core.common import _make_as_function_name, _remove_spaces, natures


@unique
class Homogeneity(Enum):
    """Enum class listing all possible homogeneity names of results."""

    acceleration = 0
    angle = 1
    angular_velocity = 2
    surface = 3
    capacitance = 4
    electric_charge = 5
    electric_charge_density = 6
    conductivity = 7
    current = 8
    current_density = 9
    density = 10
    displacement = 11
    electric_conductivity = 12
    electric_field = 13
    electric_flux_density = 14
    electric_resistivity = 15
    energy = 16
    film_coefficient = 17
    force = 18
    force_intensity = 19
    frequency = 20
    heat_flux = 21
    heat_generation = 22
    heat_rate = 23
    inductance = 24
    inverse_stress = 25
    length = 26
    magnetic_field_intensity = 27
    magnetic_flux = 28
    magnetic_flux_density = 29
    mass = 30
    moment = 31
    moment_inertia = 32
    permeability = 33
    permittivity = 34
    poisson = 35
    power = 36
    pressure = 37
    relative_permeability = 38
    relative_permittivity = 39
    section_modulus = 40
    specific_heat = 41
    specific_weight = 42
    shear_strain = 43
    stiffness = 44
    strain = 45
    stress = 46
    strength = 47
    thermal_expansion = 48
    temperature = 49
    time = 50
    velocity = 51
    voltage = 52
    volume = 53
    moment_inertia_mass = 55
    angular_acceleration = 63
    temperature_difference = 78
    stress_intensity_factor = 92
    thermal_gradient = 95
    resistance = 1000
    dimensionless = 117
    dynamic_viscosity = 118
    dissipation_rate = 119
    momentum = 120
    volume_flow_rate = 121
    mass_flow_rate = 122
    specific_energy = 123
    specific_entropy = 124
    force_density = 125
    magnetic_potential = 126


class AvailableResult:
    """Represents a result that can be requested via an operator.

    Parameters
    ----------
    availableresult : available_result_pb2.AvailableResult message.

    Examples
    --------
    Explore an available result from the model.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> transient = examples.download_transient_result()
    >>> model = dpf.Model(transient)
    >>> result_info = model.metadata.result_info
    >>> res = result_info.available_results[0]
    >>> res.name
    'displacement'
    >>> res.homogeneity
    'length'
    >>> res.dimensionality
    'vector'

    Create the operator of the given available result.

    >>> disp = model.results.displacement()

    """

    def __init__(self, availableresult):
        """Initialize the AvailableResult with an availableResult message."""
        self._name = availableresult.name
        self._physics_name = availableresult.physicsname
        self._dimensionality = availableresult.dimensionality
        self._homogeneity = availableresult.homogeneity
        self._unit = availableresult.unit
        self._n_comp = availableresult.ncomp
        self._properties = {
            "scripting_name": availableresult.properties["scripting_name"],
            "location": availableresult.properties["loc_name"],
        }
        self._sub_res = availableresult.sub_res
        self._qualifiers = availableresult.qualifiers
        self._qualifier_labels = availableresult.qualifier_labels

    def __str__(self):
        """Construct an informal string representation of available result.

        Returns
        -------
        str
            Informal string representation of available result.
        """
        txt = (
            "DPF Result\n----------\n"
            + self.name
            + "\n"
            + 'Operator name: "%s"\n' % self.operator_name
            + "Number of components: %d\n" % self.n_components
            + "Dimensionality: %s\n" % self.dimensionality
            + "Homogeneity: %s\n" % self.homogeneity
        )
        if self.unit:
            txt += "Units: %s\n" % self.unit
        if self.native_location:
            txt += "Location: %s\n" % self.native_location
        if self.qualifiers:
            txt += "Available qualifier labels:\n"
            for label in self.qualifier_labels:
                txt += f"  - {label}: {', '.join(map(str, self.qualifier_labels[label]))}\n"
            txt += "Available qualifier combinations:\n"
            for qualifier in self.qualifiers:
                txt += f"  {qualifier.__dict__()}\n"
        return txt

    def __repr__(self):
        """Construct a formal string representation of available result.

        Returns
        -------
        str
            Formal string representation of available result.
        """
        return f"AvailableResult<name={self.name}>"

    @property
    def name(self):
        """Result operator."""
        if self._properties and "scripting_name" in self._properties.keys():
            name = self._properties["scripting_name"]
        elif self.operator_name in _result_properties:
            name = _result_properties[self.operator_name]["scripting_name"]
        else:
            name = _remove_spaces(self._physics_name)
        return _make_as_function_name(name)

    @property
    def n_components(self):
        """Number of components of the result."""
        return self._n_comp

    @property
    def dimensionality(self):
        """Dimensionality nature of the result, such as a vector, scalar, or tensor."""
        return natures(self._dimensionality).name

    @property
    def homogeneity(self):
        """Homogeneity of the result."""
        try:
            # homogeneity = self._homogeneity
            # if homogeneity == 117:
            #     return Homogeneity(Homogeneity.DIMENSIONLESS).name
            return Homogeneity(self._homogeneity).name
        except ValueError as exception:
            warn(str(exception))
            return ""

    @property
    def unit(self):
        """Unit of the result."""
        return self._unit

    @property
    def operator_name(self):
        """Name of the corresponding operator."""
        return self._name

    @property
    def sub_results(self):
        """List of the subresult."""
        rep_sub_res = self._sub_res
        list_of_rep = []
        for sub_res_name in rep_sub_res.keys():
            sub_res = rep_sub_res[sub_res_name]
            try:
                int(sub_res_name)
                rep_sub = {
                    "name": "principal" + sub_res_name,
                    "operator name": sub_res[0],
                    "description": sub_res[1],
                }
            except:
                rep_sub = {
                    "name": sub_res_name,
                    "operator name": sub_res[0],
                    "description": sub_res[1],
                }
            list_of_rep.append(rep_sub)
        return list_of_rep

    @property
    def native_location(self):
        """Native location of the result."""
        if hasattr(self, "_properties") and "location" in self._properties.keys():
            return self._properties["location"]
        if self.operator_name in _result_properties:
            return _result_properties[self.operator_name]["location"]

    @property
    def native_scoping_location(self):
        """Native scoping location of the result."""
        loc = self.native_location
        if loc == "ElementalNodal":
            return "Elemental"
        else:
            return loc

    @property
    def physical_name(self) -> str:
        """Name of the result with spaces."""
        return self._physics_name

    @property
    def qualifiers(self) -> list:
        """
        Returns the list of qualifiers (equivalent to label spaces) available for a given Result.

        These qualifiers can then be used to request the result
        on specified locations/properties.
        """
        return self._qualifiers

    @property
    def qualifier_labels(self) -> dict:
        """Returns a dictionary of available labels for each available qualifier."""
        return self._qualifier_labels

    @property
    def qualifier_combinations(self) -> List[dict]:
        """Returns the list of valid qualifier combinations for this result.

        Each combination is a dictionary which can be used for a result request.
        """
        return [q.__dict__() for q in self.qualifiers]


_result_properties = {
    "S": {"location": "ElementalNodal", "scripting_name": "stress"},
    "ENF": {"location": "ElementalNodal", "scripting_name": "element_nodal_forces"},
    "EPEL": {"location": "ElementalNodal", "scripting_name": "elastic_strain"},
    "EPPL": {"location": "ElementalNodal", "scripting_name": "plastic_strain"},
    "EPCR": {"location": "ElementalNodal", "scripting_name": "creep_strain"},
    "BFE": {"location": "ElementalNodal", "scripting_name": "structural_temperature"},
    "ETH": {"location": "ElementalNodal", "scripting_name": "thermal_strain"},
    "ETH_SWL": {"location": "ElementalNodal", "scripting_name": "swelling_strains"},
    "ENG_VOL": {"location": "Elemental", "scripting_name": "elemental_volume"},
    "ENG_SE": {"location": "Elemental", "scripting_name": "stiffness_matrix_energy"},
    "ENG_AHO": {
        "location": "Elemental",
        "scripting_name": "artificial_hourglass_energy",
    },
    "ENG_KE": {"location": "Elemental", "scripting_name": "kinetic_energy"},
    "ENG_CO": {"location": "Elemental", "scripting_name": "co_energy"},
    "ENG_INC": {"location": "Elemental", "scripting_name": "incremental_energy"},
    "ENG_TH": {"location": "Elemental", "scripting_name": "thermal_dissipation_energy"},
    "U": {"location": "Nodal", "scripting_name": "displacement"},
    "V": {"location": "Nodal", "scripting_name": "velocity"},
    "A": {"location": "Nodal", "scripting_name": "acceleration"},
    "RF": {"location": "Nodal", "scripting_name": "reaction_force"},
    "F": {"location": "Nodal", "scripting_name": "nodal_force"},
    "M": {"location": "Nodal", "scripting_name": "nodal_moment"},
    "TEMP": {"location": "Nodal", "scripting_name": "temperature"},
    "EF": {"location": "ElementalNodal", "scripting_name": "electric_field"},
    "VOLT": {"location": "Nodal", "scripting_name": "electric_potential"},
    "TF": {"location": "ElementalNodal", "scripting_name": "heat_flux"},
    "UTOT": {"location": "Nodal", "scripting_name": "raw_displacement"},
    "RFTOT": {"location": "Nodal", "scripting_name": "raw_reaction_force"},
    "ECT_STAT": {"location": "ElementalNodal", "scripting_name": "contact_status"},
    "ECT_PRES": {"location": "ElementalNodal", "scripting_name": "contact_pressure"},
    "ECT_PENE": {"location": "ElementalNodal", "scripting_name": "contact_penetration"},
    "ECT_SLIDE": {"location": "ElementalNodal", "scripting_name": "contact_sliding_distance"},
    "ECT_GAP": {"location": "ElementalNodal", "scripting_name": "contact_gap_distance"},
    "ECT_SFRIC": {"location": "ElementalNodal", "scripting_name": "contact_friction_stress"},
    "ECT_STOT": {"location": "ElementalNodal", "scripting_name": "contact_total_stress"},
    "ECT_FRES": {
        "location": "ElementalNodal",
        "scripting_name": "contact_fluid_penetration_pressure",
    },
    "ECT_FLUX": {"location": "ElementalNodal", "scripting_name": "contact_surface_heat_flux"},
    "B_N": {"location": "ElementalNodal", "scripting_name": "beam_axial_force"},
    "B_M1": {"location": "ElementalNodal", "scripting_name": "beam_s_bending_moment"},
    "B_M2": {"location": "ElementalNodal", "scripting_name": "beam_t_bending_moment"},
    "B_MT": {"location": "ElementalNodal", "scripting_name": "beam_torsional_moment"},
    "B_SN": {"location": "ElementalNodal", "scripting_name": "beam_axial_stress"},
    "B_EL": {"location": "ElementalNodal", "scripting_name": "beam_axial_total_strain"},
    "B_T1": {"location": "ElementalNodal", "scripting_name": "beam_s_shear_force"},
    "B_T2": {"location": "ElementalNodal", "scripting_name": "beam_t_shear_force"},
}


def available_result_from_name(name) -> AvailableResult:
    """Create an instance of AvailableResult from a specified results name.

    Parameters
    ----------
    name : str
        Valid property name.

    Returns
    -------
    AvailableResult
        Instance created from specified result name.
    """
    for key, item in _result_properties.items():
        if item["scripting_name"] == name:
            from types import SimpleNamespace

            availableresult = SimpleNamespace(
                name=key,
                physicsname=name,
                ncomp=None,
                dimensionality=None,
                homogeneity=None,
                unit=None,
                sub_res={},
                properties={"loc_name": item["location"], "scripting_name": name},
                qualifiers=[],
                qualifier_labels={},
            )

            return AvailableResult(availableresult)
