"""Installation file for the `ansys.dpf.core` module """
import os
from io import open as io_open

from setuptools import setup

install_requires = ['pyvista>=0.24.0',
                    'matplotlib',
                    'scooby',
                    'pillow>=7.0.0',
                    'pexpect',
                    'ansys-grpc-dpf==0.2.2']


# Get version from version info
filepath = os.path.dirname(__file__)
__version__ = None
version_file = os.path.join(filepath, 'ansys', 'dpf', 'core', '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())  # execute file from raw string


readme_file = os.path.join(filepath, 'README.md')

setup(
    name='ansys-dpf-core',
    packages=['ansys.dpf.core'],
    version=__version__,
    description='DPF Python gRPC client',
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
    ],
    python_requires='>=3.5.*',
    install_requires=install_requires,
)
