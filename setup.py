"""Installation file for the `ansys-dpf-core` module """
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
    packages=['ansys.dpf.core', 'ansys.dpf.core.examples'],
    version=__version__,
    maintainer='ANSYS',
    maintainer_email='alexander.kaszynski@ansys.com',
    url='https://github.com/pyansys/DPF-Core',
    description='DPF Python gRPC client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
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
    package_data={'ansys.dpf.core.examples': ['ASimpleBar.rst',
                                              'static.rst',
                                              'complex.rst',
                                              'model_with_ns.rst',
                                              'msup_transient_plate1.rst',
                                              'rth/rth_electric.rth',
                                              'rth/rth_steady.rth',
                                              'rth/rth_transient.rth',
    ]},
    python_requires='>=3.5.*',
    install_requires=install_requires,
)
