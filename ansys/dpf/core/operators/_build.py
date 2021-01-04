"""Build static source operators from DPF server

"""
from collections import OrderedDict
from datetime import datetime
import os
from collections import namedtuple
from textwrap import wrap

from ansys.dpf import core as dpf
from ansys.dpf.core.operators._operators_list import oper_dict
from ansys.dpf.core.mapping_types import map_types_to_cpp, map_types_to_python

map_types_to_python = dict(map_types_to_python)
map_types_to_python['b'] = 'bool'

InputSpec = namedtuple('InputSpec', ['document', 'ellipsis', 'name', 'optional',
                                     'type_names'])

OutputSpec = namedtuple('OutputSpec', ['name', 'type_names', 'document'])


def gen_docstring(op):
    """Used to generate class docstrings"""
    txt = f'DPF "{op.name}" Operator\n\n'
    if op._description:
        txt += '\n'.join(wrap(op._description, initial_indent='    ',
                              subsequent_indent='    '))
        txt += '\n\n'
    if op.inputs:
        line = [' ', str(op.inputs)]
        txt += '{:^3} {:^21}'.format(*line)
        txt += '\n'
    if op.outputs:
        line = [' ', str(op.outputs)]
        txt += '{:^3} {:^21}'.format(*line)
    return txt


def build_example(op, cls_name, req_parm, opt_parm):
    lines = []
    lines.append('    Create the operator')
    lines.append('')
    line = f'    >>> op = dpf.operators.{cls_name}('
    indent = ' '*len(line)

    req_keys = list(req_parm.keys())
    opt_keys = list(opt_parm.keys())

    if req_keys:
        parm = req_keys[0]
        line += f'my_{parm},'
        req_keys.remove(parm)
    elif opt_keys:
        parm = opt_keys[0]
        line += f'my_{parm},'
    else:
        line += ')'

    lines.append(line)
    for parm in req_keys[:-1]:
        lines.append(f'{indent}my_{parm},')
    if req_keys:
        if opt_keys:
            lines.append(f'{indent}my_{req_keys[-1]},')
        else:
            lines.append(f'{indent}my_{req_keys[-1]})')

    for parm in opt_keys[:-1]:
        lines.append(f'{indent}my_{parm}, # optional')
    lines.append(f'{indent}my_{opt_keys[-1]})  # optional')
    for item in op.outputs._dict_outputs.values():
        lines.append(f'    >>> my_{item.name} = op.{item.name}')

    lines.append('')
    lines.append('    Alternative: Connect operator using Inputs and Outputs')
    lines.append('')
    lines.append(f'    >>> op = dpf.operators.{cls_name}()')
    for item in op.inputs._dict_inputs.values():
        if hasattr(item, 'optional') and item.optional:
            lines.append(f'    >>> op.inputs.{item.name}.connect(my_{item.name})  # optional')
        else:
            lines.append(f'    >>> op.inputs.{item.name}.connect(my_{item.name})')

    for item in op.outputs._dict_outputs.values():
        lines.append(f'    >>> my_{item.name} = op.outputs.{item.name}()')
    return '\n'.join(lines)


def input_messagemap_to_dict(msg_map):
    """Translate google.protobuf.pyext._message.MessageMapContainer to dict"""
    spec_dict = OrderedDict()
    pins = [pin for pin in msg_map.keys()]
    pins.sort()

    for pin in pins:
        spec = msg_map[pin]
        spec_dict[pin] = InputSpec(spec.document, spec.ellipsis, spec.name,
                                   spec.optional, spec.type_names)
    return spec_dict


def output_messagemap_to_dict(msg_map):
    """Translate google.protobuf.pyext._message.MessageMapContainer to dict"""
    spec_dict = OrderedDict()
    pins = [pin for pin in msg_map.keys()]
    pins.sort()

    for pin in pins:
        spec = msg_map[pin]
        spec_dict[pin] = OutputSpec(spec.name, spec.type_names, spec.document)
    return spec_dict


def build_input_cls(input_spec, indent='    '):
    lines = ['class _Inputs(dpf.inputs.Inputs):']
    lines.append(f'    _spec = {input_spec}')
    lines.append('    def __init__(self, oper):')
    for _, spec in input_spec.items():
        lines.append(f'        self._{spec.name} = None')
    lines.append('        super().__init__(self._spec, oper)')
    lines.append('')
    for _, spec in input_spec.items():
        lines.append('    @property')
        lines.append(f'    def {spec.name}(self):')
        if spec.document:
            lines.append(f'        """{spec.document}"""')
        lines.append(f'        return self._{spec.name}')
        lines.append('')
        lines.append(f'    @{spec.name}.setter')
        lines.append(f'    def {spec.name}(self, {spec.name}):')
        lines.append(f'        self._{spec.name}.connect({spec.name})')
        lines.append('')
    return '\n'.join(f'{indent}{line}' for line in lines)


def build_output_cls(output_spec, indent='    '):
    lines = ['class _Outputs(dpf.outputs.Outputs):']
    lines.append(f'    _spec = {output_spec}')
    lines.append('    def __init__(self, oper):')
    for _, spec in output_spec.items():
        lines.append(f'        self._{spec.name} = None')
    lines.append('        super().__init__(self._spec, oper)')
    lines.append('')
    for _, spec in output_spec.items():
        lines.append('    @property')
        lines.append(f'    def {spec.name}(self):')
        lines.append(f'        """{spec.document}"""')
        lines.append(f'        return self._{spec.name}')
        lines.append('')

    return '\n'.join(f'{indent}{line}' for line in lines)


def build_output_parm(output_spec, indent='    '):
    lines = []
    for _, spec in output_spec.items():
        lines.append('@property')
        lines.append(f'def {spec.name}(self):')
        lines.append(f'    """{spec.document}"""')
        lines.append(f'    return self.outputs._{spec.name}')
        lines.append('')

    return '\n'.join(f'{indent}{line}' for line in lines)


def build_parameters(input_spec):
    required = OrderedDict()
    optional = OrderedDict()
    for spec in input_spec.values():
        types = []
        for cpp_type in spec.type_names:
            if cpp_type in map_types_to_python:
                types.append(map_types_to_python[cpp_type])
            else:
                types.append(cpp_type)

        parm_str = f'    {spec.name} : {" or ".join(types)}'
        if spec.optional:
            parm_str += ', optional'
        parm_str += '\n'

        if spec.document:
            docs = wrap(spec.document.capitalize(), initial_indent='        ',
                        subsequent_indent='        ')
            parm_str += '\n'.join(docs)

        if spec.optional:
            optional[spec.name] = parm_str
        else:
            required[spec.name] = parm_str

    return required, optional


def build_operator(name, cls_name):
    op = dpf.Operator(name)
    docstring = gen_docstring(op)

    input_spec = input_messagemap_to_dict(op.inputs._dict_inputs)
    output_spec = output_messagemap_to_dict(op.outputs._dict_outputs)

    # build parameters
    req_parm, opt_parm = build_parameters(input_spec)
    req_sig = ', '.join(list(req_parm.keys())) + ', '
    opt_sig = ', '.join([f'{parm}=None' for parm in opt_parm.keys()]) + ', '

    example = build_example(op, cls_name, req_parm, opt_parm)
    parameters = '\n\n'.join(req_parm.values()) + '\n\n' + '\n\n'.join(opt_parm.values())

    attributes = build_output_parm(output_spec)

    inp_cls = build_input_cls(input_spec)
    out_cls = build_output_cls(output_spec)

    cls = f'''class {cls_name}(dpf.Operator):
    """{docstring}

    Parameters
    ----------
{parameters}

    Examples
    --------
{example}
    """

{inp_cls}

{out_cls}

    def __init__(self, {req_sig}{opt_sig}channel=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "{op.name}"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

{attributes}
'''

    # cleanup
    cls = cls.replace('[0m', '``').replace('[1m', '``')

    # remove trailing whitespace
    lines = cls.split('\n')
    cls = '\n'.join([line.rstrip() for line in lines])

    return cls


HEADER = f'''"""Autogenerated DPF operator classes.

Created on {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}
"""
from collections import OrderedDict
from collections import namedtuple
from ansys.dpf import core as dpf

InputSpec = namedtuple('InputSpec', ['document', 'ellipsis', 'name', 'optional',
                                     'type_names'])

OutputSpec = namedtuple('OutputSpec', ['name', 'type_names', 'document'])


'''

# op_str = build_operator('U', 'Displacement')
# exec(op_str)
# disp = Displacement()

if __name__ == '__main__':
    this_path = os.path.dirname(os.path.abspath(__file__))

    # reorganize according to categories
    categories = {}
    for oper_name, oper_data in oper_dict.items():
        category = oper_data['category']
        if category not in categories:
            categories[category] = {}
        categories[category][oper_name] = oper_data

    for category, operators in categories.items():
        oper_file = os.path.join(this_path, category + '.py')
        with open(oper_file, 'w') as f:
            f.write(HEADER)
            for name, data in operators.items():
                split_name = data['short_name'].split('_')
                pyclsname = ''.join([part.capitalize() for part in split_name])
                try:
                    op_str = build_operator(name, pyclsname)
                    f.write(op_str + '\n\n')
                except:
                    print(f'Unable to generate {name}')
