import ansys.dpf.core as dpf
from ansys.dpf.core.server_context import (
    SERVER_CONTEXT,
    AvailableServerContexts,
    set_default_server_context,
)

print(f"Server version: {dpf.global_server().version}")
# Generate entry documentation
print("Generating entry operator documentation")
print(f"Current context: {SERVER_CONTEXT}")
dpf.operators.utility.html_doc(r"../docs/source/_static/dpf_entry.html").eval()
print("Done.\n")

# Generate premium documentation
print("Generating premium operator documentation")
set_default_server_context(AvailableServerContexts.premium)
print(f"Current context: {SERVER_CONTEXT}")
dpf.operators.utility.html_doc(r"../docs/source/_static/dpf_premium.html").eval()
print("Done.\n")
