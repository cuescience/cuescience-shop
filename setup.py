#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name='cuescience-shop',
        version='0.2.2',
        description='cuescience shop',
        maintainer='cuescience',
        maintainer_email='kontakt@cuescience.de',
        license="MIT",
        url='',
        packages=['shop', 'shop.views'],
        install_requires=[
	    "Django",
	]
     )
