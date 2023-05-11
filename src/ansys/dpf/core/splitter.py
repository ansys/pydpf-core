from ansys.dpf import core

from typing import Dict, Any, Tuple

class Splitter:
    def __init__(self, start_op: core.Operator, end_op: core.Operator, scoping_pin=None):
        """"""
        # input operator should accept a scoping
        # last operator should support incremental evaluation
        #     but it should be permissive too (bad doc/spec whatever)
        self._start_op = start_op
        self._end_op = self._map_to_incremental(end_op)

        self._scoping_pin = self._find_scoping_pin(scoping_pin)

    def estimate_size(self,max_bytes: int, _dict_inputs: Dict[str, Any]) -> int:
        """"""
        # evaluate for the first element to try to guess memory consumption
        # best to use with a lot of elements

    
    def split(self, chunk_size: int, scoping: core.Scoping, end_input_pin: int = 0) -> Tuple[core.Operator,core.Operator]:
        # enables incremental evaluation:
        # using for_each, chunk_in_for_each_range and incremental version of the last op
        # by returning two operators with remapped inputs and outputs to other operators

        _server = self._start_op._server

        for_each = core.Operator("for_each", server=_server)
        split_in_range = core.Operator("chunk_in_for_each_range", server=_server)
        forward = core.Operator("forward", server=_server)

        split_in_range.connect_operator_as_input(1, self._start_op)
        split_in_range.connect(2, self._scoping_pin)
        split_in_range.connect(3, scoping)
        split_in_range.connect(4, chunk_size)


        for_each.connect(0, split_in_range, 0)
        for_each.connect(2, end_input_pin)

        # connect inputs
        fe_pin_idx = 3 # see doc of for_each
        for pin_idx, spec in self._end_op.outputs._dict_outputs.items():
            # connect end_op to for_each
            for_each.connect(fe_pin_idx, self._end_op, pin_idx)
            # remap
            forward.connect(pin_idx, for_each, fe_pin_idx)
            fe_pin_idx += 1
        
        return forward
    
    def _map_to_incremental(self, end_op: core.Operator):
        inc_operators = [
            "accumulate_level_over_label_fc",
            "accumulate_min_over_label_fc",
            "accumulate over label",
            "average over label",
            "min_max_inc",
            "min_max_fc_inc",
            "max_over_time_by_entity",
            "min_max_over_time_by_entity",
            "min_max_by_time",
            "min_over_time_by_entity",
            "time_of_max_by_entity",
            "time_of_min_by_entity"
        ]

        map_to_inc = {
            'min_max': 'min_max_inc',
            'min_max_fc': 'min_max_fc_inc'
        }

        if end_op.name not in inc_operators:
            print(f"WARNING: Operator named {end_op.name} may not support incremental evaluation")
            if end_op.name in map_to_inc.keys():
                print(f"An operator named {map_to_inc[end_op.name]} supports incremental evaluation")

        return end_op

    def _find_scoping_pin(self, pin_idx):
        dict_inputs = self._start_op.inputs._dict_inputs
        # validate given pin_idx
        if pin_idx != None and pin_idx in dict_inputs:
            pin_spec = dict_inputs[pin_idx]
            if 'scoping' in pin_spec.type_names:
                return pin_idx

        # look for scoping pin
        for pin_idx, spec in dict_inputs.items():
            if 'scoping' in spec.type_names:
                return pin_idx
        
        raise Exception(f"Scoping pin could not be found in start_op with name '{self._start_op.name}'")