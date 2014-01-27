from django.conf.urls import *
from activity.views import *
# change form to create...

urlpatterns = patterns("",
		url(r'^$', activityHomeView, {}, "home"),
		url(r'^list/$', activityListView, {}, "activity_list"),
		url(r'^chart/$', chartsView, {}, "chart"),
		url(r'^(?P<a_id>\d+)/viewdata/$', activityViewDataView, {}, "activity_viewdata"),
		url(r'^new-activity/(?P<pk>\d+)/$', activityFormView, {}, "activity_form"),
		url(r'^new-activity/$', activityFormView, {}, "activity_form"),
		url(r'^(?P<a_id>\d+)/$', activityDetailView, {}, "activity_detail"),
		url(r'^(?P<a_id>\d+)/edit/$', activityEditView, {}, "activity_edit"),
		url(r'^(?P<a_id>\d+)/new-rating/$', rateActivityFormView, {}, "rateActivity_form"),
		url(r'^(?P<a_id>\d+)/rate-activity-detail/(?P<r_id>\d+)/$', rateActivityDetailView, {}, "rateActivity_detail"),
		url(r'^(?P<a_id>\d+)/instance/$', activityInstanceFormView, {}, "activityInstance_form"),#create view
		url(r'^(?P<a_id>\d+)/instance/(?P<aI_id>\d+)/$', activityInstanceDetailView, {}, "activityInstance_detail"),
		url(r'^(?P<a_id>\d+)/instance/(?P<aI_id>\d+)/edit$', activityInstanceEditView, {}, "activityInstance_edit"),
		url(r'^(?P<a_id>\d+)/instance/(?P<aI_id>\d+)/rate/(?P<r_id>\d+)/instance/(?P<rI_id>\d+)/form/$', rateActivityInstanceFormView, {}, "rateActivityInstance_form"),
)
