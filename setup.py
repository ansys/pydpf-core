"""Installation file for python dpf module
"""
import os
from io import open as io_open

from setuptools import setup

install_requires = ['pyvista>=0.24.0',
                    'scooby',
                    'matplotlib==3.2',
                    'psutil',
                    'pillow>=7.0.0',
                    'pexpect',
                    'ansys.grpc.dpf']


# Get version from version info
filepath = os.path.dirname(__file__)
__version__ = None
version_file = os.path.join(filepath, 'ansys', 'dpf', 'core', '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())  # execute file from raw string


readme_file = os.path.join(filepath, 'README.md')

setup(
    name='ansys-dpf-core',
    packages=['ansys.dpf.core', 'ansys.dpf.core.examples', 'ansys.dpf.core.operators'],
    version=__version__,
    description='DPF Python gRPC client',
    # long_description=io_open(readme_file, encoding="utf-8").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_data={'ansys.dpf.core.examples': ['ASimpleBar.rst',
                                              'static.rst',
                                              'complex.rst',
                                              'model_with_ns.rst',
                                              'file_cyclic.rst',
                                              'msup_transient_plate1.rst',
                                              'rth/rth_electric.rth',
                                              'rth/rth_steady.rth',
                                              'rth/rth_transient.rth',
    ]},

    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=install_requires,
)
