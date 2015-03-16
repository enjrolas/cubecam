import subprocess
import os
from time import time
timestamp=int(time())
binary="%s%d.bin" % ("/home/glass/cubecam/media/",timestamp)

p = subprocess.Popen(['spark', 'compile', "%stempfile.ino" % "/home/glass/cubecam/media/", '--saveTo', binary], stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
out, err = p.communicate()
response='{"out":"%s", "err":"%s"}' % (out, err)
print response
