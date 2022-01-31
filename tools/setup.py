#!/usr/bin/env python
# run "pip install -e ." to install scripts to python path in current environment

from setuptools import setup, find_packages

setup(name='ev-imo-tools',
      version='1.0',
      description='EV-IMO command line tools',
      author='Levi Burner',
      author_email='lburner@umd.edu',
      url='https://github.com/better-flow/evimo/tools',
      packages=find_packages(include=['tools', '*.py']),
      install_requires=[
            'numpy','argparse', 'tqdm', 'easygui', 'scipy'
      ],
      entry_points = {
            'console_scripts': ['evimo_flow=tools.ev_imo_flow:main', 'bag_to_txt=tools.bag_to_txt:main'],
      }
)
