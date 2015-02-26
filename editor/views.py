from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from editor.models import User, Sketch
from django.conf import settings

def edit(request):
    return render(request, "editor/edit.html")

@csrf_exempt
def compile(request):
    code=request.POST['code']
    file=open("%stempfile" % settings.MEDIA_ROOT, 'w')
    file.write(code)
    file.close()
    response='{"filename":"%s"}' % file.name
    return HttpResponse(response, content_type="application/json")  

def flash(request):
    return render(request, "editor/edit.html")



