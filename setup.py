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
import os,sys
from setuptools import setup
import subprocess

exepath = os.path.dirname(sys.executable)
try:
    subprocess.call([os.path.join(exepath,'conda'),'install','--yes','--file','requirements.txt'])
except Exception as e:
    print('tried conda in {}, but you will need to install packages in requirements.txt  {}'.format(exepath,e))

with open('README.rst','r') as f:
	long_description = f.read()

setup(description='GeoData class and needed functions.',
      author='John Swoboda',
      version=0.2,
      install_requires=[],
      extras_require={'mayavi2':'mayavi2'},
      packages=['GeoData'],
      name='GeoData',
      long_description=long_description
)

