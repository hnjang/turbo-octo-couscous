#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from pprint import pprint
# sys.path.append('c:\\work\\python\\venv\\venv\\lib\\site-packages')
sys.path = ['c:\\work\\python\\venv\\venv\\lib\\site-packages'] + sys.path
pprint(sys.path)
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
'''
if sys.platform == "win32":
    base = "Win32GUI"
'''
setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("simple_pyqt.py", base=base)])
