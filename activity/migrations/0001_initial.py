# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'activity_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activities', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'activity', ['Activity'])

        # Adding model 'ActivityInstance'
        db.create_table(u'activity_activityinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 15, 0, 0), blank=True)),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 15, 0, 0), blank=True)),
            ('isTimeAccurate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('length_days', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('length_hours', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('length_minutes', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('length_seconds', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('isLengthAccurate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('log', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activityInstances', blank=True, to=orm['activity.Activity'])),
            ('hasError', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'activity', ['ActivityInstance'])

        # Adding model 'RateActivity'
        db.create_table(u'activity_rateactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rateActivities', blank=True, to=orm['activity.Activity'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'activity', ['RateActivity'])

        # Adding model 'RateActivityInstance'
        db.create_table(u'activity_rateactivityinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('rateActivity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rateActivityInstances', to=orm['activity.RateActivity'])),
            ('activityInstance', self.gf('django.db.models.fields.related.OneToOneField')(related_name='rateActivityInstances', unique=True, blank=True, to=orm['activity.ActivityInstance'])),
        ))
        db.send_create_signal(u'activity', ['RateActivityInstance'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'activity_activity')

        # Deleting model 'ActivityInstance'
        db.delete_table(u'activity_activityinstance')

        # Deleting model 'RateActivity'
        db.delete_table(u'activity_rateactivity')

        # Deleting model 'RateActivityInstance'
        db.delete_table(u'activity_rateactivityinstance')


    models = {
        u'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'to': u"orm['auth.User']"})
        },
        u'activity.activityinstance': {
            'Meta': {'object_name': 'ActivityInstance'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activityInstances'", 'blank': 'True', 'to': u"orm['activity.Activity']"}),
            'endTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 15, 0, 0)', 'blank': 'True'}),
            'hasError': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLengthAccurate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isTimeAccurate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'length_days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_hours': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_minutes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_seconds': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 15, 0, 0)', 'blank': 'True'})
        },
        u'activity.rateactivity': {
            'Meta': {'object_name': 'RateActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rateActivities'", 'blank': 'True', 'to': u"orm['activity.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'activity.rateactivityinstance': {
            'Meta': {'object_name': 'RateActivityInstance'},
            'activityInstance': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rateActivityInstances'", 'unique': 'True', 'blank': 'True', 'to': u"orm['activity.ActivityInstance']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rateActivity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rateActivityInstances'", 'to': u"orm['activity.RateActivity']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['activity']