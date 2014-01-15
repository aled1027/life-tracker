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
	note = "I recommend sticking to one timezone."
	class Meta:
		model = ActivityInstance
	def save(self, commit=True):
		print "in save"
		instance = super(ActivityInstanceForm, self).save(commit=False)
		if not instance.isLengthAccurate:
			l = instance.endTime - instance.startTime
			instance.length_days = l.days
			instance.length_hours = l.hours
			instance.length_minutes = l.minutes
			instance.length_seconds = l.seconds
			instance.isLengthAccurate = True
		if hasError and (endTime - startTime)  < 0:
			instance.hasError = True
			return instance
		else:
			instance.hasError = False
		if commit:
			instance.save()
		return instance

exclude = ['activity', 'hasError']

class RateActivityInstanceForm(ModelForm):
	n = "Record a rating"
	note = "here's the note"
	class Meta:
		model = RateActivityInstance
		exclude = ['rateActivity', 'activityInstance']
