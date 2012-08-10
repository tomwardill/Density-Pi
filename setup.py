"""Installer for serverdensity.cloud
"""

import os
cwd = os.path.dirname(__file__)
__version__ = open(os.path.join(cwd, 'src', 'densitypi',
                    'version.txt'), 'r').read().strip()

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='densitypi',
    description='Server Density for Raspberry Pi',
    version=__version__,
    author='Chris Hannam',
    author_email='bassdread@gmail.com',
    url='https://github.com/bassdread/Density-Pi',
    packages=find_packages('src', exclude=['ez_setup']),
    install_requires=open(os.path.join(cwd, 'requirements.txt')).readlines(),
    package_dir={
        '': 'src',
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    }
)
