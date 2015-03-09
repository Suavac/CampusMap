from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('map.views',
    url(r'^$', 'home'),
    url(r'^home/$', 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', 'course'),
    url(r'^module/', 'module'),
    url(r'^room/', 'room'),
    url(r'^building/', 'building'),
    url(r'^lecturer/', 'lecturer'),
    url(r'^timetable/$', 'timetable'),
    url(r'^edit-timetable/$', 'editTimetable'),
    url(r'^department/$', 'department'),
    url(r'^edit-map/$', 'editMap'),

    url(r'^json/', 'JSON'),
    url(r'^JSON/', 'JSON'),

)

