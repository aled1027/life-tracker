from django.db.models import *
from django.contrib import admin
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime

class Activity(Model):
	user = ForeignKey(User, related_name="activities")
	name = CharField(max_length=200)
	tags = TaggableManager()
	class meta:
		unique_together = (("user", "name"))
	def __unicode__(self):
		return self.name

class ActivityInstance(Model):
	startTime = DateTimeField(blank=True, default=datetime.now())
	endTime = DateTimeField(blank=True, default=datetime.now())
	isTimeAccurate = BooleanField(default=False)
	length_days = IntegerField(default=0, blank=True)
	length_hours = IntegerField(default=0, blank=True)
	length_minutes = IntegerField(default=0, blank=True)
	length_seconds = IntegerField(default=0, blank=True)
	isLengthAccurate = BooleanField(default=False)
	log = TextField(blank=True)
	activity = ForeignKey(Activity, related_name="activityInstances", blank=True)
	hasError = BooleanField(default=False)

	def __unicode__(self):
		return u"%s: %s" % (self.activity, self.startTime)

class RateActivity(Model):
	activity = ForeignKey(Activity, related_name="rateActivities", blank=True)
	name = CharField(max_length=1000)

	def __unicode__(self):
		return self.name

# maybe def getMostRecentRating(self):

class RateActivityInstance(Model):
	rating = IntegerField(null=True, blank=True)
	rateActivity = ForeignKey(RateActivity, related_name="rateActivityInstances")
	activityInstance = ForeignKey(ActivityInstance, related_name="rateActivityInstances", blank=True)

	def __unicode__(self):
		return u"%s: %s" % (self.rateActivity, self.rating)

	def save(self, *args, **kwargs):
		if not self.rating:
			self.rating = None
		print self.rating
		super(RateActivityInstance, self).save(*args, **kwargs)

