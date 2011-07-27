#!/usr/bin/env python

from distutils.core import setup

setup(
name = 'dblog',
version = '1.0',
package_dir = {'dblog': ''},
package_data = {'': ['templates/*/*', 'fixtures/*', 'locale/*/*']},
packages = ['dblog'],
)