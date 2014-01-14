from django.db import models
from django.forms import ModelForm
from activity.models import *

class ActivityForm(ModelForm):
	n = "Create a new activity"
	class Meta:
		model = Activity
		exclude = ['user']

class RateActivityForm(ModelForm):
	n = "Create a new rating subject"
	class Meta:
		model = RateActivity
		exclude = ['activity']

class ActivityInstanceForm(ModelForm):
	n = "Record an instance of the activity"
	note = "Use the following format for dates/times: '10/25/2006 14:30' \n You may leave the total times as 0. The program can calcuate them for you. Otherwise, leave the times blank and enter in the total time."
	class Meta:
		model = ActivityInstance
		exclude = ['activity']

class RateActivityInstanceForm(ModelForm):
	n = "Record a rating"
	note = "here's the note"
	class Meta:
		model = RateActivityInstance
		exclude = ['rateActivity']
