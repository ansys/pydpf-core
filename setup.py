"""Installation file for python dpf module
"""
# To keep according to https://setuptools.pypa.io/en/stable/userguide/pyproject_config.html
# to allow -e with pip<21.1
from setuptools import setup, find_namespace_packages


setup(
    package_dir={"": "src"},
    include_package_data=True,
    packages=find_namespace_packages(where="src"),
    # package_data={
    #     "ansys.dpf.gatebin": ["*.so", "*.dll"],
    #     "ansys.dpf.core.examples": ["*.rst"],
    # },
)
# "ansys.dpf.core.examples" = [
#     "ASimpleBar.rst",
#     "static.rst",
#     "complex.rst",
#     "model_with_ns.rst",
#     "file_cyclic.rst",
#     "msup_transient_plate1.rst",
#     "rth/rth_electric.rth",
#     "rth/rth_steady.rth",
#     "rth/rth_transient.rth",
#     "sub/cp56.sub",
#     "msup/file.mode",
#     "msup/file.rst",
#     "msup/file.rfrq",
#     "distributed/file0.rst",
#     "distributed/file1.rst",
#     "msup_distributed/file0.rst",
#     "msup_distributed/file1.rst",
#     "msup_distributed/file0.mode",
#     "msup_distributed/file1.mode",
#     "msup_distributed/file_load_1.rfrq",
#     "msup_distributed/file_load_2.rfrq",
# ]
