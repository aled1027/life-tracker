# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RateActivityInstance.activityInstance'
        db.alter_column(u'activity_rateactivityinstance', 'activityInstance_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['activity.ActivityInstance']))
        # Adding unique constraint on 'RateActivityInstance', fields ['activityInstance']
        db.create_unique(u'activity_rateactivityinstance', ['activityInstance_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'RateActivityInstance', fields ['activityInstance']
        db.delete_unique(u'activity_rateactivityinstance', ['activityInstance_id'])


        # Changing field 'RateActivityInstance.activityInstance'
        db.alter_column(u'activity_rateactivityinstance', 'activityInstance_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activity.ActivityInstance']))

    models = {
        u'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'to': u"orm['auth.User']"})
        },
        u'activity.activityinstance': {
            'Meta': {'object_name': 'ActivityInstance'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activityInstances'", 'blank': 'True', 'to': u"orm['activity.Activity']"}),
            'endTime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_hours': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_minutes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'length_seconds': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'activity.rateactivity': {
            'Meta': {'object_name': 'RateActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'rateActivities'", 'null': 'True', 'to': u"orm['activity.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'})
        },
        u'activity.rateactivityinstance': {
            'Meta': {'object_name': 'RateActivityInstance'},
            'activityInstance': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rateActivityInstances'", 'unique': 'True', 'to': u"orm['activity.ActivityInstance']"}),
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