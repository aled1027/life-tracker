from django.conf.urls import *
from activity.views import *

urlpatterns = patterns("",
		url(r'^$', activityListView, {}, "home"),
		url(r'^list/$', activityListView, {}, "activity_list"),

		url(r'^new-activity/(?P<pk>\d+)/$', activityFormView, {}, "activity_form"),
		url(r'^new-activity/$', activityFormView, {}, "activity_form"),
		url(r'^(?P<a_id>\d+)/$', activityDetailView, {}, "activity_detail"),
		url(r'^(?P<a_id>\d+)/new-rating/$', rateActivityFormView, {}, "rateActivity_form"),
		url(r'^(?P<a_id>\d+)/rate-activity-detail/(?P<r_id>\d+)/$', rateActivityDetailView, {}, "rateActivity_detail"),
		url(r'^(?P<a_id>\d+)/instance/$', activityInstanceFormView, {}, "activityInstance_form"),
		url(r'^(?P<a_id>\d+)/instance/(?P<aI_id>\d+)/$', activityInstanceDetailView, {}, "activityInstance_detail"),
		url(r'^(?P<a_id>\d+)/instance/(?P<aI_id>\d+)/rate/(?P<r_id>\d+)/instance/(?P<rI_id>\d+)/form/$', rateActivityInstanceFormView, {}, "rateActivityInstance_form"),
)
