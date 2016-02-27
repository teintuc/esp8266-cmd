#!/usr/bin/python

from distutils.core import setup

setup(name='esp8266-cmd',
      version='1.0',
      description='Run esp8266 At command via serial',
      author='Charles Teinturier',
      author_email='teintu.c@gmail.com',
      scripts=['esp-cmd'],
      packages=['espcmd'],
      install_requires=[
        'pyserial',
        ]
     )
