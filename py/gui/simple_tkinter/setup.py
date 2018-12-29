#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from pprint import pprint
# sys.path.append('c:\\work\\python\\venv\\venv\\lib\\site-packages')
sys.path = ['c:\\work\\python\\venv\\venv\\lib\\site-packages'] + sys.path
pprint(sys.path)

includes = []
include_files = [r"C:\Python36\DLLs\tcl86t.dll",
                 r"C:\Python36\DLLs\tk86t.dll"]
pprint(("includes: ",includes))
pprint(("include_files: ",include_files))
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "tkinter"],
                     "includes": includes, "include_files": include_files}

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
        executables = [Executable("simple_tkinter.py", base=base)])
