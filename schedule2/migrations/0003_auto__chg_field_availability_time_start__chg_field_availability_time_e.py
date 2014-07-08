# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Availability.time_start'
        db.alter_column(u'schedule2_availability', 'time_start', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Availability.time_end'
        db.alter_column(u'schedule2_availability', 'time_end', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):

        # Changing field 'Availability.time_start'
        db.alter_column(u'schedule2_availability', 'time_start', self.gf('django.db.models.fields.CharField')(max_length=8))

        # Changing field 'Availability.time_end'
        db.alter_column(u'schedule2_availability', 'time_end', self.gf('django.db.models.fields.CharField')(max_length=8))

    models = {
        u'schedule2.area': {
            'Meta': {'object_name': 'Area'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule2.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subarea': ('django.db.models.fields.CharField', [], {'default': "('LIB', 'Liberal Arts Math')", 'max_length': '3'})
        },
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'semester': ('django.db.models.fields.CharField', [], {'default': "('FA', 'Fall 2014')", 'max_length': '2'})
        }
    }

    complete_apps = ['schedule2']