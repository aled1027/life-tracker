from django.db import models
from django.forms import ModelForm
from django import forms
from activity.models import *
from datetime import datetime, timedelta

def convert_timedelta(duration):
		days, seconds = duration.days, duration.seconds
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = (seconds % 60)
		return days, hours, minutes, seconds

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
		exclude = ['activity', 'hasError']

 	def save(self, commit=True):
		instance = super(ActivityInstanceForm, self).save(commit=False)
		if not instance.isLengthAccurate:
			l = instance.endTime - instance.startTime
			days, hours, minutes, seconds = convert_timedelta(l)
			instance.duration = 5
			instance.length_days = days
			instance.length_hours = hours
			instance.length_minutes = minutes
			instance.length_seconds = seconds
			instance.isLengthAccurate = True
		if instance.hasError and (endTime - startTime)  < 0:
			instance.hasError = True
			return instance
		else:
			instance.hasError = False
		if commit:
			instance.save()
		return instance


class RateActivityInstanceForm(ModelForm):
	n = "Record a rating"
	class Meta:
		model = RateActivityInstance
		exclude = ['rateActivity', 'activityInstance']

# delete this - not needed
class ChartForm(forms.Form):
	xaxis = forms.ChoiceField(required=False)
	#yaxis = forms.ChoiceField(required=False)

	def __init__(self, *args, **kwargs):
		super(ChartForm, self).__init__(*args, **kwargs)
		if "new" in args[0]:
			self.fields['xaxis'].choices = (('hi', 'hi'),('bye', 'bye'))

# rename this
class MyForm(forms.Form):
	def __init__(self, choices, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		if choices:
			print choices
			self.fields['xaxis'] = forms.ChoiceField(choices=choices[0])
			self.fields['yaxis'] = forms.ChoiceField(choices=choices[1])

