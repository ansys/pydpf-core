"""Installation file for python dpf module
"""
import os
from io import open as io_open

from setuptools import setup

install_requires = ["packaging", "psutil", "tqdm", "numpy", "ansys-dpf-gate>=0.2.*"]

# Get version from version info
filepath = os.path.dirname(__file__)
__version__ = None
version_file = os.path.join(filepath, "ansys", "dpf", "core", "_version.py")
with io_open(version_file, mode="r") as fd:
    exec(fd.read())  # execute file from raw string

readme_file = os.path.join(filepath, "README.md")

setup(
    name="ansys-dpf-core",
    packages=[
        "ansys.dpf.core",
        "ansys.dpf.core.examples",
        "ansys.dpf.core.examples.msup_distributed",
        "ansys.dpf.core.operators",
        "ansys.dpf.core.operators.averaging",
        "ansys.dpf.core.operators.filter",
        "ansys.dpf.core.operators.geo",
        "ansys.dpf.core.operators.invariant",
        "ansys.dpf.core.operators.logic",
        "ansys.dpf.core.operators.mapping",
        "ansys.dpf.core.operators.math",
        "ansys.dpf.core.operators.mesh",
        "ansys.dpf.core.operators.metadata",
        "ansys.dpf.core.operators.min_max",
        "ansys.dpf.core.operators.result",
        "ansys.dpf.core.operators.scoping",
        "ansys.dpf.core.operators.serialization",
        "ansys.dpf.core.operators.utility",
    ],
    version=__version__,
    description="DPF Python client",
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
    author='ANSYS',
    author_email='ramdane.lagha@ansys.com',
    maintainer_email="pyansys.maintainers@ansys.com",
    python_requires=">=3.7.*,<4.0",
    install_requires=install_requires,
    extras_require={
        "plotting": ["pyvista>=0.32.0", "matplotlib>=3.2"],
    },
    url="https://github.com/pyansys/pydpf-core",
    license='MIT License',
)
