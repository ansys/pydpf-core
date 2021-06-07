"""
AvailableResult
===============
"""

from warnings import warn
from ansys.grpc.dpf import available_result_pb2, base_pb2
from ansys.dpf.core.common import _remove_spaces

class AvailableResult:
    """A class used to represent an Available result which can be
    requested via an operator

    Parameters
    ----------
    availableresult : available_result_pb2.AvailableResult message
    
    Examples
    --------
    Explore an available result from the model
    
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
    
    Create the operator of the given available result    
    >>> disp = model.results.displacement()

    """

    def __init__(self, availableresult):
        """Initialize the AvailableResult with an availableResult message"""
        self._message = availableresult

    def __str__(self):
        txt = self.name+'\n' +\
              'Operator name: "%s"\n' % self.operator_name +\
              'Number of components: %d\n' % self.n_components +\
              'Dimensionality: %s\n' % self.dimensionality +\
              'Homogeneity: %s\n' % self.homogeneity
        if self.unit:
            txt += 'Units: %s\n' % self.unit
        return txt

    @property
    def name(self):
        """Result operator"""
        if self.operator_name in _result_properties:
            return _result_properties[self.operator_name]["scripting_name"]
        else:
            return _remove_spaces(self._message.physicsname)

    @property
    def n_components(self):
        """Number of components of the results"""
        return self._message.ncomp

    @property
    def dimensionality(self):
        """Dimensionality nature of the result (vector, scalar, tensor...)"""
        return base_pb2.Nature.Name(self._message.dimensionality).lower()

    @property
    def homogeneity(self):
        """Homogeneity of the result"""
        try:
            homogeneity = self._message.homogeneity
            if (homogeneity==117):
                return available_result_pb2.Homogeneity.Name(available_result_pb2.Homogeneity.DIMENSIONLESS).lower()
            return available_result_pb2.Homogeneity.Name(homogeneity).lower()
        except ValueError as exception:
            warn(str(exception))
            return ''

    @property
    def unit(self):
        """Unit of the result"""
        return self._message.unit.lower()

    @property
    def operator_name(self):
        """Name of the corresponding operator"
        """
        return self._message.name
    
    @property
    def sub_results(self):
        """List of sub result"
        """
        rep_sub_res =self._message.sub_res
        list = []
        for sub_res in rep_sub_res:
            try :
                int(sub_res.name)
                dict ={"name":"principal"+sub_res.name, "operator name":sub_res.op_name, "description":sub_res.description }
            except :
                dict ={"name":sub_res.name, "operator name":sub_res.op_name, "description":sub_res.description }
            list.append(dict)
        return list
    
    
    @property
    def native_location(self):
        if self.operator_name in _result_properties:
            return _result_properties[self.operator_name]["location"]
        
    @property
    def native_scoping_location(self):
        loc = self.native_location
        if loc == "ElementalNodal":
            return "Elemental"
        else:
            return loc
    
_result_properties ={ "S":{"location":"ElementalNodal", "scripting_name":"stress"},
            "ENF":{"location":"ElementalNodal", "scripting_name":"element_nodal_forces"},
            "EPEL":{"location":"ElementalNodal", "scripting_name":"elastic_strain"},
            "EPPL":{"location":"ElementalNodal", "scripting_name":"plastic_strain"},
            "ECR":{"location":"ElementalNodal", "scripting_name":"creep_strain"},
            "BFE":{"location":"ElementalNodal", "scripting_name":"structural_temperature"},
            "ETH":{"location":"ElementalNodal", "scripting_name":"thermal_strain"},
            "ETH_SWL":{"location":"ElementalNodal", "scripting_name":"swelling_strains"},
            "ENG_VOL":{"location":"Elemental", "scripting_name":"elemental_volume"},
            "ENG_SE":{"location":"Elemental", "scripting_name":"stiffness_matrix_energy"},
            "ENG_AHO":{"location":"Elemental", "scripting_name":"artificial_hourglass_energy"},
            "ENG_KE":{"location":"Elemental", "scripting_name":"kinetic_energy"},
            "ENG_CO":{"location":"Elemental", "scripting_name":"co_energy"},
            "ENG_INC":{"location":"Elemental", "scripting_name":"incremental_energy"},
            "ENG_TH":{"location":"Elemental", "scripting_name":"thermal_dissipation_energy"},
            "U":{"location":"Nodal", "scripting_name":"displacement"},
            "V":{"location":"Nodal", "scripting_name":"velocity"},
            "A":{"location":"Nodal", "scripting_name":"acceleration"},
            "RF":{"location":"Nodal", "scripting_name":"reaction_force"},
            "F":{"location":"Nodal", "scripting_name":"nodal_force"},
            "M":{"location":"Nodal", "scripting_name":"nodal_moment"},
            "TEMP":{"location":"Nodal", "scripting_name":"temperature"},
            "EF":{"location":"ElementalNodal", "scripting_name":"electric_field"},
            "VOLT":{"location":"Nodal", "scripting_name":"electric_potential"},
            "TF":{"location":"ElementalNodal", "scripting_name":"heat_flux"},
            "UTOT":{"location":"Nodal", "scripting_name":"raw_displacement"},
            "RFTOT":{"location":"Nodal", "scripting_name":"raw_reaction_force"}
            }
