# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Availability.day'
        db.add_column(u'schedule2_availability', 'day',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=1),
                      keep_default=False)


        # Changing field 'Availability.time_start'
        db.alter_column(u'schedule2_availability', 'time_start', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Availability.time_end'
        db.alter_column(u'schedule2_availability', 'time_end', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):
        # Deleting field 'Availability.day'
        db.delete_column(u'schedule2_availability', 'day')


        # Changing field 'Availability.time_start'
        db.alter_column(u'schedule2_availability', 'time_start', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Availability.time_end'
        db.alter_column(u'schedule2_availability', 'time_end', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'schedule2.availability': {
            'Meta': {'object_name': 'Availability'},
            'day': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule2.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_end': ('django.db.models.fields.TimeField', [], {}),
            'time_start': ('django.db.models.fields.TimeField', [], {})
        },
        u'schedule2.employee': {
            'Meta': {'object_name': 'Employee'},
            'emp_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['schedule2']