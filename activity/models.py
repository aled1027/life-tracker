from django.db.models import *
from django.contrib import admin
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime

class ActivityManager(Manager):
	def all(self, user=None):
		#maybe add condidition for superuser
		if user:
			return super(ActivityManager, self).get_query_set().filter(user=user)
		else:
			return super(ActivityManager, self).get_query_set().all()

class Activity(Model):
	user = ForeignKey(User, related_name="activities")
	name = CharField(max_length=200)
	tags = TaggableManager()
	objects = ActivityManager()
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
	duration = IntegerField(default=0, blank=True, help_text="Must be an integer value")
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
		return u"%s: %s" % (self.rateActivity, str(self.rating))

	def save(self, *args, **kwargs):
		print "in save"
		if not self.rating:
			self.rating = None
		super(RateActivityInstance, self).save(*args, **kwargs)
		print "in rai save"


