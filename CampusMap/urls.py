from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('map.views',
    url(r'^home/$', 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', 'course'),
    url(r'^module/', 'module'),
    url(r'^room/', 'room'),
    url(r'^building/', 'building'),
    url(r'^lecturer/', 'lecturer'),
    url(r'^timetable/', 'timetable'),


)

