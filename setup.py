"""Installation file for python dpf module
"""
import os
from io import open as io_open

from setuptools import setup

install_requires = [
    "importlib-metadata >=4.0",
    "psutil",
    "packaging",
    "setuptools",
    "tqdm",
    "numpy",
    "grpcio",
    "google-api-python-client",
]

# Get version from version info
filepath = os.path.dirname(__file__)
__version__ = None
version_file = os.path.join(filepath, "src", "ansys", "dpf", "core", "_version.py")
with io_open(version_file, mode="r") as fd:
    exec(fd.read())  # execute file from raw string

setup(
    name="ansys-dpf-core",
    package_dir={"": "src"},
    packages=[
        "ansys.dpf.core",
        "ansys.dpf.gate",
        "ansys.dpf.gate.generated",
        "ansys.dpf.gatebin",
        "ansys.grpc.dpf",
    ],
    include_package_data=True,
    version=__version__,
    description="Data Processing Framework - Python Core ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={
        "ansys.dpf.gatebin": [
            "DPFClientAPI.dll",
            "Ans.Dpf.GrpcClient.dll",
            "libDPFClientAPI.so",
            "libAns.Dpf.GrpcClient.so",
        ],
        "ansys.dpf.core.examples": [
            "ASimpleBar.rst",
            "static.rst",
            "complex.rst",
            "model_with_ns.rst",
            "file_cyclic.rst",
            "msup_transient_plate1.rst",
            "rth/rth_electric.rth",
            "rth/rth_steady.rth",
            "rth/rth_transient.rth",
            "sub/cp56.sub",
            "msup/file.mode",
            "msup/file.rst",
            "msup/file.rfrq",
            "distributed/file0.rst",
            "distributed/file1.rst",
            "msup_distributed/file0.rst",
            "msup_distributed/file1.rst",
            "msup_distributed/file0.mode",
            "msup_distributed/file1.mode",
            "msup_distributed/file_load_1.rfrq",
            "msup_distributed/file_load_2.rfrq",
        ]
    },
    author='ANSYS, Inc.',
    author_email='pyansys.core@ansys.com',
    maintainer='ANSYS, Inc.',
    maintainer_email="pyansys.core@ansys.com",
    python_requires=">=3.7,<4.0",
    install_requires=install_requires,
    extras_require={
        "plotting": ["pyvista>=0.32.0", "matplotlib>=3.2"],
    },
    url="https://github.com/pyansys/pydpf-core",
    license='MIT License',
)
