from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from editor.models import User, Sketch
from django.conf import settings
import subprocess
from time import time
import os
import logging
import getpass
import pexpect
log = logging.getLogger(__name__)

def edit(request):
    return render(request, "editor/edit.html")

@csrf_exempt
def compile(request):
    login()
    user=getpass.getuser()
    log.debug("compiling")
    code=request.POST['code']
    file=open("%stempfile.ino" % settings.MEDIA_ROOT, 'w')
    file.write(code)
    file.close()
    timestamp=int(time())
    binary="/home/glass/cubecam/media/%d.bin" % timestamp
#    os.system('/home/glass/cubecam/editor/compile.py')
#    p=subprocess.Popen(['sudo', 'glass', 'python', '/home/glass/cubecam/editor/compile.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    p=subprocess.Popen(['sh /home/glass/cubecam/editor/compile.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    out, err = p.communicate()
#    response='{"out":"%s", "err":"%s", "user":"%s"}' % (out, err, user)

    login()
    p = subprocess.Popen(['spark', 'compile', file.name, '--saveTo', binary], stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    response='{"out":"%s", "err":"%s", "user":"%s"}' % (out, err, user)    

    
    return HttpResponse(response, content_type="application/json")  

def flash(request):
    return render(request, "editor/edit.html")


def login():
    child = pexpect.spawn('spark cloud login')
    print "logging in"
    child.expect('Could I please have an email address?')
    print "sending email address"
    child.sendline('alex@lookingglassfactory.com')
    child.expect('and a password?')
    print "sending password"
    child.sendline('lookatthatglass')
    
