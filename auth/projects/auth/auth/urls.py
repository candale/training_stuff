from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^login/', include('login.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
