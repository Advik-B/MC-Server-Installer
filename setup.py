import os
import sys
from fnmatch import fnmatch
from cx_Freeze import setup, Executable

pattern = "*.*"

include_files=[]

blacklist_dirs = ['.git', '__pycache__', 'docs', 'assets\\fonts']

blacklist_dirs2 = []

blacklist_dirs3 = []

cwd = os.getcwd()

for pathe in blacklist_dirs:
    blacklist_dirs2.append(os.path.join(cwd, pathe))

for path, subdirs, files in os.walk(cwd):
    for name in files:
        if fnmatch(name, pattern):
            ppath = os.path.join(path, name)
            include_files.append(ppath)

for path in include_files:
    for paths in blacklist_dirs2:
        if paths in path:
            blacklist_dirs3.append(path)

for bf in blacklist_dirs3:
    include_files.remove(bf)
    
print(*include_files, sep='\n')

app_title = "Minecraft Server-Installer"
main_py_file = "main.py"
icon = "icon.ico"
author = "Advik Bommu"
descriptions = "An app the help in minecraft server installation"

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    
    name=app_title,
    version='1.0.0',
    description=descriptions,
    author=author,
    options={'build_exe':{'icon':icon, 'include_files':include_files}},
    executables=[Executable(main_py_file, base=base)]
    
)