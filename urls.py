from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),

    url(r'^projects/$', 'projects.views.index'),
    url(r'^projects/feeds/$', 'projects.views.get_feeds'),
    url(r'^projects/projects/$', 'projects.views.get_projects'),
    url(r'^projects/tasks/$', 'projects.views.get_tasks'),
    url(r'^projects/task/(?P<task_id>\d+)/$', 'projects.views.get_task'),
)


