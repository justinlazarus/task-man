from django.shortcuts import render
from projects.models import *

def get_newsfeed(request):
    feeds = FeedEntry.objects.all().order_by('-user')

    return render(request, 'projects/newsfeed.html', {'feeds': feeds})
