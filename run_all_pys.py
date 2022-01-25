#!/usr/bin/env python3

import glob
import os
from subprocess import call
import shutil
import time
import pathlib

# this script places the py file to create backup images in every banner folder, then it runs every py file to create the backup img

# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = str(pathlib.Path().resolve()) + '/' + next(os.walk('.'))[1][0] + '/'

# filenamehtml for loop places the main.py file in every folder there is an html (so every banner directory will now have the main.py file in it, the main.py file deletes itself after the script runs so you should never see it but if the backup img appears it works :) )
for filenamehtml in glob.iglob(root_dir + '**/**.html', recursive=True):
    source = "/Users/apierce/Code/python-google-automation/src/backup_img/backup-img-banner/main.py"
    destination = filenamehtml.replace("index.html", "main.py")
    shutil.copy( source , destination )

time.sleep(3)

# filenamepy runs every py file in current directory. these py files are the scripts that create the backup img.
for filenamepy in glob.iglob(root_dir + '**/**.py', recursive=True):
    isCopyMain = filenamepy == "/Users/apierce/Code/python-google-automation/src/backup_img/backup-img-banner/main.py"
    isRunPy = filenamepy == "/Users/apierce/Code/python-google-automation/src/backup_img/backup-img-banner/run_all_pys.py"
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

