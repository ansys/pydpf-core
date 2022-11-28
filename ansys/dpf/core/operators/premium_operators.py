"""List operators only available as Premium"""
import os

from ansys.dpf import core as dpf
from ansys.dpf.core.dpf_operator import available_operator_names


def list_premium_operators(verbose: bool = False) -> list:
    # Start a DPF server as entry and a DPF server as premium and query available operators
    server_entry = dpf.start_local_server(context=dpf.AvailableServerContexts.entry,
                                          as_global=False)
    available_operators_entry = available_operator_names(server=server_entry)
    if verbose:
        print(f"{len(available_operators_entry)} operators where found for entry.")

    server_premium = dpf.start_local_server(context=dpf.AvailableServerContexts.premium,
                                            as_global=False)
    available_operators_premium = available_operator_names(server=server_premium)
    if verbose:
        print(f"{len(available_operators_premium)} operators where found for premium.")

    # Take the difference between the two lists
    premium_only = [operator for operator in available_operators_premium
                    if operator not in set(available_operators_entry)]

    if verbose:
        print(f"Of {len(available_operators_premium)} operators in the Premium context, "
              f"{len(premium_only)} are premium-only:")
    premium_only.sort(key=str.lower)
    return premium_only


def get_premium_only_descriptions_rst(verbose: bool = False) -> str:
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    premium_only_operators = list_premium_operators()
    premium_only_descriptions = {}
    result = "List of Premium-only operators"
    result += "\n" + "="*len(result) + "\n"
    result += "Generated using ``dpf.core.operators.premium_operators``\n\n"
    if verbose:
        print(result)
    for operator_name in premium_only_operators:
        op = dpf.Operator(operator_name)
        premium_only_descriptions[operator_name] = op.specification.description
        lines = f"* {operator_name}:\n{op.specification.description}\n\n"
        result += lines
        if verbose:
            print(lines)
    return result


def write_premium_only_rst_doc(file_path: os.PathLike = None):
    text = get_premium_only_descriptions_rst()
    if file_path is None:
        file_path = os.path.dirname(os.path.realpath(__file__))
        file_path = file_path.rsplit(sep=os.path.sep, maxsplit=4)[0]
        file_path = os.path.join(file_path, "docs", "source", "_static",
                                 "premium_only_operators.rst")
    with open(file=file_path, mode="w") as f:
        f.write(text)


if __name__ == "__main__":
    write_premium_only_rst_doc()
