#!/usr/bin/env python3

import glob
import os
from subprocess import call

# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = input("\n"+"Enter root directory path, it needs a trailing slash (i.e. /root/dir/): "+"\n")
for filename in glob.iglob(root_dir + '**/**.py', recursive=True):
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
    execfile(filename)

