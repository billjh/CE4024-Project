from distutils.core import setup
import sys
import os

import py2exe

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files':1}},
    windows = [{'script': 'Problem1.py'}],
    zipfile = None
)