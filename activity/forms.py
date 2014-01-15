from django.db import models
from django.forms import ModelForm
from activity.models import *

class ActivityForm(ModelForm):
	n = "Create a new activity"
	class Meta:
		model = Activity
		exclude = ['user', 'tags']

class RateActivityForm(ModelForm):
	n = "Create a new rating subject"
	class Meta:
		model = RateActivity
		exclude = ['activity']

class ActivityInstanceForm(ModelForm):
	n = "Record an instance of the activity"
	note = "Either edit the start and end time below, or enter the amount of time that you spent on the activity. If you leave the amounts of time as zero, the program will automatically calculate the time spent. Try to stick to one timezone please."

	class Meta:
		model = ActivityInstance
		exclude = ['activity']

class RateActivityInstanceForm(ModelForm):
	n = "Record a rating"
	note = "here's the note"
	class Meta:
		model = RateActivityInstance
		exclude = ['rateActivity', 'activityInstance']
