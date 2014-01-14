from django.conf.urls import patterns, include, url
from django.contrib import admin
from LifeTracker.views import *
admin.autodiscover()

urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),
		url(r'^activity/', include('activity.urls')),
		url(r'^accounts/login/$', 'LifeTracker.views.login'),
		url(r'^accounts/auth/$', 'LifeTracker.views.auth_view'),
		url(r'^accounts/logout/$', 'LifeTracker.views.logout'),
		url(r'^accounts/loggedin/$', 'LifeTracker.views.loggedin'),
		url(r'^accounts/invalid/$', 'LifeTracker.views.invalid_login'),
		url(r'^accounts/register/$', 'LifeTracker.views.register_user'),
		url(r'^accounts/register_success/$', 'LifeTracker.views.register_success'),
)
