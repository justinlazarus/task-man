from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from projects.models import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),

    # Projects URLS
    url(r'^projects/$', 'projects.views.index'),
    url(r'^projects/feedentry_list/$', ListView.as_view(
        model=FeedEntry, context_object_name="feedentry_list"
    ),),
    (r'^projects/task_list/$', ListView.as_view(
        model=Task, context_object_name="task_list"
    ),),
    (r'^projects/project_list/$', ListView.as_view(
        model=Project, context_object_name="project_list",
        queryset=Project.objects.exclude(completions__isnull=False),
    ),),
    (r'^projects/milestone_list/$', ListView.as_view(
        model=Milestone, context_object_name="milestone_list"
    ),),
    (r'^projects/project_list/$', ListView.as_view(
        model=Project, context_object_name="project_list"
    ),),
    (r'^projects/complete/$', 'projects.views.complete'),
    (r'^projects/delete/$', 'projects.views.delete_project'),
)
