import subprocess
from time import time
import os
import getpass
import pexpect

user=getpass.getuser()
timestamp=int(time())
binary="/home/glass/cubecam/media/%d.bin" % timestamp
#    os.system('/home/glass/cubecam/editor/compile.py')
p=subprocess.Popen(['python', '/home/glass/cubecam/editor/compile.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
response='{"out":"%s", "err":"%s", "user":"%s"}' % (out, err, user)
print response
