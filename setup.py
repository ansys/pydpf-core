"""Installation file for python dpf module
"""
# To keep according to https://setuptools.pypa.io/en/stable/userguide/pyproject_config.html
# to allow -e with pip<21.1
from setuptools import setup, find_namespace_packages

# gatebin_binaries = ["*.so"]


# def set_gatebin(plat):
#     if plat == "toto":
#         global gatebin_binaries
#         gatebin_binaries = []
#
#
#
# try:
#     from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
#
#
#     class bdist_wheel(_bdist_wheel):
#         def get_tag(self):
#             python, abi, plat = _bdist_wheel.get_tag(self)
#             # set_gatebin(plat)
#             return python, abi, plat
# except ImportError:
#     bdist_wheel = None


setup(
    # package_dir={"": "src"},
    # include_package_data=True,
    # packages=find_namespace_packages(where="src"),
    # package_data={
    #     # "ansys.dpf.gatebin": gatebin_binaries,
    #     "ansys.dpf.core.examples": ["**/*"],
    # },
    # exclude_package_data={
    #     "ansys.dpf.gatebin": ["**/*.so"],
    #     "ansys.dpf.core.examples": ["**/*.lck"]
    # }
)

