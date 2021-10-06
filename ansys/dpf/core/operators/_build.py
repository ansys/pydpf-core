"""Build static source operators from DPF server

"""
from collections import OrderedDict
from datetime import datetime
import os
from collections import namedtuple
from textwrap import wrap
import black

from ansys.dpf import core as dpf
from ansys.dpf.core.operators._operators_list import operators
from ansys.dpf.core.mapping_types import map_types_to_python

map_types_to_python = dict(map_types_to_python)
map_types_to_python["b"] = "bool"

InputSpec = namedtuple(
    "InputSpec", ["document", "ellipsis", "name", "optional", "type_names"]
)

OutputSpec = namedtuple("OutputSpec", ["name", "type_names", "document"])


def gen_docstring(op):
    """Used to generate class docstrings"""
    txt = f'DPF "{op.name}" Operator\n\n'
    if op._description:
        txt += "\n".join(
            wrap(op._description, initial_indent="    ", subsequent_indent="    ")
        )
        txt += "\n\n"
    if op.inputs:
        line = [" ", str(op.inputs)]
        txt += "{:^3} {:^21}".format(*line)
        txt += "\n"
    if op.outputs:
        line = [" ", str(op.outputs)]
        txt += "{:^3} {:^21}".format(*line)
    return txt


def build_example(op, cls_name, req_param, opt_param, build_class_methods=False):
    lines = []

    if build_class_methods:
        lines.append("    Create the operator")
        lines.append("")
        line = f"    >>> op = dpf.operators.{cls_name}("
        indent = " " * len(line)

        req_keys = list(req_param.keys())
        opt_keys = list(opt_param.keys())

        if req_keys:
            param = req_keys[0]
            line += f"my_{param},"
            req_keys.remove(param)
        elif opt_keys:
            param = opt_keys[0]
            line += f"my_{param},"
        else:
            line += ")"

        lines.append(line)
        for param in req_keys[:-1]:
            lines.append(f"{indent}my_{param},")
        if req_keys:
            if opt_keys:
                lines.append(f"{indent}my_{req_keys[-1]},")
            else:
                lines.append(f"{indent}my_{req_keys[-1]})")

        for param in opt_keys[:-1]:
            lines.append(f"{indent}my_{param}, # optional")
        lines.append(f"{indent}my_{opt_keys[-1]})  # optional")
        for item in op.outputs._dict_outputs.values():
            lines.append(f"    >>> my_{item.name} = op.{item.name}")

        lines.append("")
        lines.append("    Alternative: Connect operator using Inputs and Outputs")
        lines.append("")

    lines.append(f"    >>> op = dpf.operators.{cls_name}()")
    for item in op.inputs._dict_inputs.values():
        if hasattr(item, "optional") and item.optional:
            lines.append(
                f"    >>> op.inputs.{item.name}.connect(my_{item.name})  # optional"
            )
        else:
            lines.append(f"    >>> op.inputs.{item.name}.connect(my_{item.name})")

    if op.outputs:
        for item in op.outputs._dict_outputs.values():
            lines.append(f"    >>> my_{item.name} = op.outputs.{item.name}()")
    joined = "\n".join(lines)
    return joined.replace('"', "'")


def input_messagemap_to_dict(msg_map):
    """Translate google.protobuf.pyext._message.MessageMapContainer to dict"""
    spec_dict = OrderedDict()
    pins = [pin for pin in msg_map.keys()]
    pins.sort()

    for pin in pins:
        spec = msg_map[pin]
        # Ignore flake8 check for line length on doc
        doc = spec.document.replace('"', "'")
        formatted_doc = f'"{doc}" # noqa: E501'
        spec_dict[pin] = InputSpec(
            formatted_doc,
            spec.ellipsis,
            spec.name,
            spec.optional,
            spec.type_names,
        )
    return spec_dict


def output_messagemap_to_dict(msg_map):
    """Translate google.protobuf.pyext._message.MessageMapContainer to dict"""
    spec_dict = OrderedDict()
    pins = [pin for pin in msg_map.keys()]
    pins.sort()

    for pin in pins:
        spec = msg_map[pin]
        # Ignore flake8 check for line length on doc
        formatted_doc = f'"{spec.document}" # noqa: E501'
        spec_dict[pin] = OutputSpec(spec.name, spec.type_names, formatted_doc)
    return spec_dict


def build_input_cls(input_spec, indent="    "):
    lines = ["class _Inputs(dpf.inputs.Inputs):"]
    lines.append("")
    lines.append(f"    _spec = {input_spec}")
    lines.append("")
    lines.append("    def __init__(self, oper):")
    for _, spec in input_spec.items():
        lines.append(f"        self._{spec.name} = None")
    lines.append("        super().__init__(self._spec, oper)")
    for _, spec in input_spec.items():
        lines.append("")
        lines.append("    @property")
        lines.append(f"    def {spec.name}(self):")
        if spec.document:
            doc = wrap(
                f'"""{spec.document}"""',
                initial_indent="        ",
                subsequent_indent="        ",
                width=65
            )
            lines.extend(doc)
        lines.append(f"        return self._{spec.name}")
        lines.append("")
        lines.append(f"    @{spec.name}.setter")
        lines.append(f"    def {spec.name}(self, {spec.name}):")
        lines.append(f"        self._{spec.name}.connect({spec.name})")
    return "\n".join(f"{indent}{line}" for line in lines)


def build_output_cls(output_spec, indent="    "):
    lines = [""]
    lines.append("class _Outputs(dpf.outputs.Outputs):")
    lines.append("")
    lines.append(f"    _spec = {output_spec}")
    lines.append("")
    lines.append("    def __init__(self, oper):")
    for _, spec in output_spec.items():
        lines.append(f"        self._{spec.name} = None")
    lines.append("        super().__init__(self._spec, oper)")
    for _, spec in output_spec.items():
        lines.append("")
        lines.append("    @property")
        lines.append(f"    def {spec.name}(self):")
        lines.append(f'        """{spec.document}"""')
        lines.append(f"        return self._{spec.name}")
    lines.append("")
    return "\n".join(f"{indent}{line}" for line in lines)


def build_output_param(output_spec, indent="    "):
    lines = []
    for _, spec in output_spec.items():
        lines.append("")
        lines.append("@property")
        lines.append(f"def {spec.name}(self):")
        lines.append(f'    """{spec.document}"""')
        lines.append(f"    return self.outputs._{spec.name}")

    return "\n".join(f"{indent}{line}" for line in lines)


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

        param_str = f'    {spec.name} : {" or ".join(types)}'
        if spec.optional:
            param_str += ", optional"
        param_str += "\n"

        if spec.document:
            docs = wrap(
                spec.document.capitalize(),
                initial_indent="        ",
                subsequent_indent="        ",
            )
            param_str += "\n".join(docs)

        if spec.optional:
            optional[spec.name] = param_str
        else:
            required[spec.name] = param_str

    return required, optional


def build_operator(name, cls_name, build_class_methods=False):
    op = dpf.Operator(name)
    docstring = gen_docstring(op)

    input_spec = input_messagemap_to_dict(op.inputs._dict_inputs)

    # build parameters string for function signature
    req_param, opt_param = build_parameters(input_spec)
    param = ["self"]
    if req_param:
        param.extend(list(req_param.keys()))
    if opt_param:
        param.extend([f"{param}=None" for param in opt_param.keys()])
    parameters_str = ", ".join(param)

    example = build_example(op, cls_name, req_param, opt_param, build_class_methods)
    parameters_docstring = (
        "\n\n".join(req_param.values()) + "\n\n" + "\n\n".join(opt_param.values())
    )

    out_cls = ""
    attributes = ""
    if op.outputs:
        output_spec = output_messagemap_to_dict(op.outputs._dict_outputs)
        attributes = build_output_param(output_spec)
        out_cls = build_output_cls(output_spec)

    inp_cls = build_input_cls(input_spec)

    cls = f'''class {cls_name}(dpf.Operator):
    """{docstring}

    Parameters
    ----------
{parameters_docstring}

    Examples
    --------
{example}
    """

{inp_cls}
{out_cls}
    def __init__({parameters_str}):
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
    cls = cls.replace("[0m", "``").replace("[1m", "``")

    # remove trailing whitespace
    lines = cls.split("\n")
    cls = "\n".join([line.rstrip() for line in lines])

    cls = black.format_str(cls, mode=black.FileMode())

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

if __name__ == "__main__":
    this_path = os.path.dirname(os.path.abspath(__file__))

    # Create file per operator and organize into directories
    # per category
    succeeded = 0
    for operator_name, operator_data in operators.items():
        # Make directory for new category
        category = operator_data["category"]
        category_path = os.path.join(this_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        # Clean up short name
        short_name = operator_data["short_name"]
        if short_name == "":
            short_name = operator_name
        if "::" in short_name:
            short_name = short_name.split("::")[-1]
        if "." in short_name:
            short_name = short_name.split(".")[-1]

        # Get python class name fron short name
        split_name = short_name.split("_")
        class_name = "".join([part.capitalize() for part in split_name])

        # Write to operator file
        operator_file = os.path.join(category_path, short_name + ".py")
        with open(operator_file, "w") as f:
            f.write(HEADER)
            try:
                operator_str = build_operator(operator_name, class_name)
                exec(operator_str)
                f.write(operator_str)
                succeeded += 1
            except SyntaxError:
                print(f"Unable to generate {operator_name}, {short_name}, {class_name}")

    print(f"Generated {succeeded} out of {len(operators)}")
    dpf.SERVER.shutdown()
