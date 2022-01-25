#!/usr/bin/env python3

import glob
import os
from subprocess import call
import shutil
import time
import pathlib

# this script places the py file to create backup images in every banner folder, then it runs every py file to create the backup img

# banner_dir needs a trailing slash path of where your banners are. Needs to be a directory and the only directory in the same level as your run_all_pys file. The pathlib path resolve finds the path to where you are running this py file. The os walk finds the directory in this path, and the slashes are to make sure its written as a trailing slash so it can execute.
root_dir = str(pathlib.Path().resolve())

banner_dir = root_dir + '/' + next(os.walk('.'))[1][0] + '/'

# filenamehtml for loop places the main.py file in every folder there is an html (so every banner directory will now have the main.py file in it, the main.py file deletes itself after the script runs so you should never see it but if the backup img appears it works :) )
for filenamehtml in glob.iglob(banner_dir + '**/**.html', recursive=True):
    source = root_dir + "/main.py"
    destination = filenamehtml.replace("index.html", "main.py")
    shutil.copy( source , destination )

# filenamepy runs every py file in current directory. these py files are the scripts that create the backup img.
for filenamepy in glob.iglob(banner_dir + '**/**.py', recursive=True):
    isCopyMain = filenamepy == root_dir + "/main.py"
    isRunPy = filenamepy == root_dir + "/run_all_pys.py"
    if not isCopyMain or not isRunPy:
        def execfile(filepath, globals=None, locals=None):
            if globals is None:
                globals = {}
            globals.update({
                "__file__": filepath,
                "__name__": "__main__",
            })
            with open(filepath, 'rb') as file:
                exec(compile(file.read(), filepath, 'exec'), globals, locals)

        # execute the file
        execfile(filenamepy)

