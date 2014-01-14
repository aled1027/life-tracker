from django.db.models import *
from django.contrib import admin
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.contrib import admin

class Activity(Model):
	user = ForeignKey(User, related_name="activities")
	name = CharField(max_length=200, unique=True)
	tags = TaggableManager()

	def __unicode__(self):
		return self.name

class ActivityInstance(Model):
	startTime = DateTimeField(blank=True)
	endTime = DateTimeField(blank=True)
	length_days = IntegerField(default=0, blank=True)
	length_hours = IntegerField(default=0, blank=True)
	length_minutes = IntegerField(default=0, blank=True)
	length_seconds = IntegerField(default=0, blank=True)
	log = TextField(blank=True)
	activity = ForeignKey(Activity, related_name="activityInstances", blank=True)

	def __unicode__(self):
		return u"%s: %s" % (self.activity, self.startTime)

	# add method to calculate time if needed

class RateActivity(Model):
	activity = ForeignKey(Activity, related_name="rateActivities", blank=True)
	name = CharField(max_length=1000, unique=True)

	def __unicode__(self):
		return self.name

# maybe def getMostRecentRating(self):

class RateActivityInstance(Model):
	rating = IntegerField(blank=True)
	rateActivity = ForeignKey(RateActivity, related_name="rateActivityInstances")
	activityInstance = OneToOneField(ActivityInstance, related_name="rateActivityInstances", blank=True)

	def __unicode__(self):
		return u"%s: %s" % (self.rateActivity, self.rating)

admin.site.register(Activity)
admin.site.register(ActivityInstance)
admin.site.register(RateActivity)
admin.site.register(RateActivityInstance)

