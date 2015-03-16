#!/usr/bin/python
from __future__ import print_function
import os
import subprocess
import sys

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

os.setreuid(1000,1000)
p = subprocess.Popen(['spark', 'compile', "/home/glass/cubecam/media/tempfile.ino", '--saveTo', "/home/glass/cubecam/media/binary.bin"], stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
out, err = p.communicate()
print(out)
warning(err)

