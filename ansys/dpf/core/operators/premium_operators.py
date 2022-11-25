"""List operators only available as Premium"""
from ansys.dpf import core as dpf
from ansys.dpf.core.dpf_operator import available_operator_names


def list_premium_operators(verbose=False):
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


if __name__ == "__main__":
    print(list_premium_operators(verbose=True))
