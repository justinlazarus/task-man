from django.shortcuts import render
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from projects.models import *

@login_required
def index(request):
    return render(request, 'projects/index.html')

@login_required
def get_projects(request):
    return render(request, 'projects/projects.html')

@login_required
def get_milestones(request):
    return render(request, 'projects/milestones.html')

@login_required
def get_tasks(request):
    tasks = Task.objects.all().order_by(
        'responsible', 'planned_completion_date'
    )
    return render(request, 'projects/tasks.html', {'tasks': tasks})

@login_required
def get_feeds(request):
    if request.is_ajax():
        if request.method == 'POST':
            POST = request.POST
            if POST.get('order'):
                order = POST.get('order')
        else:
            order = 'duedate'

    feeds = FeedEntry.objects.all().order_by('-user')

    return render(request, 'projects/feeds.html', {'feeds': feeds, 'order': order})
