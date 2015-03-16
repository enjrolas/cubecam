from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import logging
log = logging.getLogger(__name__)

def browser(request):
    return render(request, "javascript/cube.html")
