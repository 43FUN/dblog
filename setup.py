#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='dblog',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    package_dir={'dblog': 'dblog'},
    package_data={'dblog': [
        'templatetags/*',
        'urls/*',
        'templates/*/*/*',
        'fixtures/*',
        'locale/*/*',
        'migrations/*']},
    install_requires=[
        'django',
        'django-pure-pagination'
    ],
)
