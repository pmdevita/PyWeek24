import sys
from cx_Freeze import setup, Executable

exe_name = "TheyreBehindEverything"
optimization = 0
resources = ["resources/"]
packages = ["pyglet"]

build_exe_options = {"optimize": optimization, "include_files": resources, "packages": packages}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "They're behind everything!",
        version = "0.1",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, targetName=exe_name+".exe")])