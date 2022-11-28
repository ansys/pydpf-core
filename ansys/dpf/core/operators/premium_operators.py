"""List operators only available as Premium"""
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


def get_premium_description(verbose: bool = False) -> str:
    dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
    premium_only_operators = list_premium_operators()
    premium_only_descriptions = {}
    result = ""
    if verbose:
        print(result)
    for operator_name in premium_only_operators:
        op = dpf.Operator(operator_name)
        premium_only_descriptions[operator_name] = op.specification.description
        lines = f"{operator_name}:\n{op.specification.description}\n"
        result += lines
        if verbose:
            print(lines)
    return result


if __name__ == "__main__":
    get_premium_description(verbose=True)
