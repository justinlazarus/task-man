from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import *

@login_required
def index(request):
    return render(request, 'projects/index.html')
