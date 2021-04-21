from ansys import dpf
import os


class PinSpecification:
    def __init__(self, name = None, type_names = None, optional = None, document = None, ellipsis = None):
        self.name = name
        self.type_names = type_names
        self.document = document
        self.optional = optional
        self.ellipsis = ellipsis
        

class Specification:
    def __init__(self, description = None, map_input_pin_spec = None, map_output_pin_spec = None):
        self.description = description
        self._map_input_pin_spec = map_input_pin_spec
        self._map_output_pin_spec = map_output_pin_spec
     
    @property
    def inputs(self):
        return self._map_input_pin_spec
        
    @property
    def outputs(self):
        return self._map_output_pin_spec
    
    def output_pin(self, pin_num):
        return self._map_output_pin_spec[pin_num]
    
    def input_pin(self, pin_num):
        return self._map_input_pin_spec[pin_num]
    
        