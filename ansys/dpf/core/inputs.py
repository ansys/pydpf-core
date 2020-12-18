from ansys.dpf.core.mapping_types import map_types_to_cpp, map_types_to_python


class Input:
    def __init__(self,spec, pin, operator, count_ellipsis=-1):
        self._spec = spec
        self._operator=operator
        self._pin = pin
        self._count_ellipsis = count_ellipsis
        self._python_expected_types  = []
        for cpp_type in self._spec.type_names:
            self._python_expected_types.append(map_types_to_python[cpp_type])
        if len(self._spec.type_names) == 0:
            self._python_expected_types.append("Any")
        docstr = self.__str__()
        self.name = self._spec.name
        if self._count_ellipsis !=-1:
            self.name+=str(self._count_ellipsis +1)
        self._update_doc_str(docstr,self.name)

    def connect(self,inpt):
        """Allows you to connect any input (an entity or an operator
        output) to a specified input pin of this operator.

        Parameters
        ----------
        inpt : str, int, double, Field, FieldsContainer, Scoping, DataSources,

        MeshedRegion, Output, Outputs
            input of the operator
        """
        input_type_name =type(inpt).__name__
        if (input_type_name in self._python_expected_types or ["Outputs", "Output","Any"])==False :
            for types in self._python_expected_types:
               print(types, end = ' ')
            print("types are expected for", self._spec.name, "pin")
            return
        
        corresponding_pins=[]
        
        self._operator._find_outputs_corresponding_pins(self._python_expected_types,inpt, self._pin, corresponding_pins)
        if len(corresponding_pins)>1:
            print("pin connection is ambiguous, specify the pin with:\n")
            for pin in corresponding_pins:
                print("   - operator.inputs."+self._spec.name+"(out_op."+inpt._dict_outputs[pin[1]].name+")")
            return
        if len(corresponding_pins)==0:
            print("the input operator should have one of this output expected types:" )
            for python_type in self._python_expected_types:
               print("   -",python_type)
            print("for", self._spec.name, "pin")
            return
      
        if input_type_name!="Outputs" and input_type_name!="Output":
            self._operator.connect( self._pin, inpt)
            self._operator.inputs._connected_inputs[self._pin]=inpt
        elif input_type_name == "Output":
             self._operator.connect( self._pin, inpt._operator,inpt._pin)
             self._operator.inputs._connected_inputs[self._pin]={inpt._pin : inpt}
        else:
            self._operator.connect( self._pin, inpt._operator,corresponding_pins[0][1])
            self._operator.inputs._connected_inputs[self._pin]={corresponding_pins[0][1] : inpt._operator}
        
        self.__inc_if_ellipsis()
        
    def __call__(self,inpt):
        self.connect(inpt)
        
    def _update_doc_str(self, docstr, class_name):
        """Dynamically updates the docstring of this instance by
        creating a new class on the fly.
        """
        child_class = type(class_name, (self.__class__,), {'__doc__': docstr})
        self.__class__ = child_class
        
    def __str__(self): 
        docstr ='\033[1m'+ self._spec.name+'\033[0m' 
        if self._spec.optional :
            docstr+=" (optional)"
        docstr+=", expects types:"+'\n'
        for types in  self._python_expected_types:
            docstr+="   -"+types +'\n'
        if self._spec.document :
            docstr+="help: "+self._spec.document +'\n'
        if self._count_ellipsis>=0:
            docstr+="is ellipsis \n"
        return docstr

    def __inc_if_ellipsis(self):
        if self._count_ellipsis >=0:
            self._count_ellipsis+=1
            if isinstance(self._operator.inputs, Inputs):
                self._operator.inputs.__add_input__(self._pin+ self._count_ellipsis, self._spec,self._count_ellipsis)
        
class Inputs:
    def __init__(self, dict_inputs, operator):
        self._dict_inputs = dict_inputs
        self._operator = operator
        self._inputs = []
        self._connected_inputs = {}
        self._python_expected_types_by_pin={}
        
        # dynamically populate input attributes
        for pin, spec in self._dict_inputs.items():
            if spec.ellipsis :
                self.__add_input__(pin, spec,0)
            else:
                 self.__add_input__(pin, spec)
            

    def __add_input__(self,pin,spec, count_ellipsis=-1):
        if spec is not None:
            class_input = Input(spec, pin, self._operator,count_ellipsis)
            class_input.__doc__ = spec.name
            setattr(self, class_input.name, class_input)
            self._inputs.append(class_input)
    
            python_types=[]
            for cpp_type in spec.type_names:
                 python_types.append(map_types_to_python[cpp_type])
            if len(spec.type_names) == 0:
                python_types.append("Any")
            self._python_expected_types_by_pin[pin]=python_types
        
    def __str__(self):
        docstr = 'Available inputs:\n'
        for input in self._inputs :
            tot_string =input.__str__()
            input_string = tot_string.split('\n')
            input_string1 = input_string[0]
            line = ["   ","o ",input_string1]
            docstr+='{:<5}{:<4}{:<20}'.format(*line)
            docstr+='\n'
            for inputstr in input_string :
                if inputstr != input_string1:
                    line = ["   ","  ",inputstr]
                    docstr+='{:<5}{:<4}{:<20}'.format(*line)
                    docstr+='\n'
        return docstr

    def connect(self, inpt):
        """Allows you to connect any input (an entity or an operator
        output) to any input pin of this operator.

        The matching input type corresponding to the output is looked for.

        Parameters
        ----------
        inpt : str, int, double, Field, FieldsContainer, Scoping, DataSources,
        MeshedRegion, Output, Outputs
            input of the operator
        """
        corresponding_pins = []
        input_type_name =type(inpt).__name__
        for pin in self._python_expected_types_by_pin:
            self._operator._find_outputs_corresponding_pins(self._python_expected_types_by_pin[pin], inpt, pin, corresponding_pins)

        if len(corresponding_pins) > 1:
            print("pin connection is ambiguous, specify the pin with:\n")
            for pin in corresponding_pins:
                if isinstance(pin, tuple):
                    pin = pin[0]
                print("   - operator.inputs."+self._dict_inputs[pin].name+"(input)")
            return
        if len(corresponding_pins)==0:
            print("the input should have one of the expected types:" )
            for pin, spec in self._dict_inputs.items():
                for cpp_type in spec.type_names:
                   print("   -"+map_types_to_python[cpp_type])
            return

        if input_type_name != "Outputs" and input_type_name != "Output":
            self._operator.connect(corresponding_pins[0], inpt)
            self._connected_inputs[corresponding_pins[0]]=inpt
        elif input_type_name == "Output":
            self._operator.connect(corresponding_pins[0], inpt._operator, inpt._pin)
            self._connected_inputs[corresponding_pins[0]]={inpt._pin : inpt._operator}
        else:
            self._operator.connect(corresponding_pins[0][0], inpt._operator, corresponding_pins[0][1])
            self._connected_inputs[corresponding_pins[0][0]]={corresponding_pins[0][1] : inpt._operator}
            
    def __call__(self,inpt):
        self.connect(inpt)
