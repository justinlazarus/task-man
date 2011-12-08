from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),

    url(r'^newsfeed/$', 'projects.views.get_newsfeed'),
    url(r'^projects/$', 'projects.views.get_projects'),
)


