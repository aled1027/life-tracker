from django.conf.urls import patterns, include, url
from django.contrib import admin
from LifeTracker.views import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),
		url(r'^activity/', include('activity.urls')),
		url(r'^$', 'LifeTracker.views.home', name="home"),
		url(r'^accounts/$', 'LifeTracker.views.accounts_home', name="accounts"),
		url(r'^accounts/login/$', 'LifeTracker.views.login', name="login"),
		url(r'^accounts/auth/$', 'LifeTracker.views.auth_view', name="auth"),
		url(r'^accounts/logout/$', 'LifeTracker.views.logout', name="logout"),
		url(r'^accounts/invalid/$', 'LifeTracker.views.invalid_login'),
		url(r'^accounts/register/$', 'LifeTracker.views.register_user', name='register_user'),
		url(r'^accounts/register_success/$', 'LifeTracker.views.register_success', name="register_success"),
		url(r'^accounts/register_error/$', 'LifeTracker.views.register_error', name="register_error"),

		url(r'^about/$', 'LifeTracker.views.about', name="about"),
		url(r'^help/$', 'LifeTracker.views.help', name="help"),
		url(r'^getting-started/$', 'LifeTracker.views.gettingStarted', name="getting_started"),
)
