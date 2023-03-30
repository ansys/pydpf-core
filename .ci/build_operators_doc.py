import ansys.dpf.core as dpf
from ansys.dpf.core.server_context import (
    SERVER_CONTEXT,
)

print(f"Server version: {dpf.global_server().version}")
# Generate entry documentation
print("Generating operator documentation")
print(f"Current context: {SERVER_CONTEXT}")
dpf.operators.utility.html_doc(r"../docs/source/_static/dpf_operators.html").eval()
print("Done.\n")
