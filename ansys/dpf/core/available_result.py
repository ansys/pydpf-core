from warnings import warn
from ansys.grpc.dpf import available_result_pb2, base_pb2
from ansys.dpf.core.common import remove_spaces

class AvailableResult:
    """A class used to represent an Available result which can be
    requested via an operator

    Parameters
    ----------
    availableresult : AvailableResult message
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
        return remove_spaces(self._message.physicsname)

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
