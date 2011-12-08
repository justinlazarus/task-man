from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import *

def get_newsfeed(request):
    feeds = FeedEntry.objects.all().order_by('-user')

    return render(request, 'projects/newsfeed.html', {'feeds': feeds})

@login_required
def get_projects(request):
    projects = Project.objects.all().order_by('-stamp')

    return render(request, 'projects/projects.html', {'projects': projects})
