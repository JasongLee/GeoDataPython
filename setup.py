#!/usr/bin/env python
"""
setup.py
This is the setup file for the GeoData python package.
To install as a package in development type
python setup.py develop
To uninstall type
python setup.py develop --uninstall

@author: John Swoboda
"""
from setuptools import setup
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass

setup(description='GeoData class and needed functions.',
      author='John Swoboda',
      version=0.2,
      install_requires=['pathlib2'],
      extras_require={'mayavi':'mayavi'},
      packages=['GeoData'],
      name='GeoData',
)

