# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Area.subarea'
        db.alter_column(u'schedule2_area', 'subarea', self.gf('django.db.models.fields.CharField')(max_length=3))

    def backwards(self, orm):

        # Changing field 'Area.subarea'
        db.alter_column(u'schedule2_area', 'subarea', self.gf('django.db.models.fields.CharField')(max_length=12))

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
            'time_end': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'time_start': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'schedule2.employee': {
            'Meta': {'object_name': 'Employee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'semester': ('django.db.models.fields.CharField', [], {'default': "('FA', 'Fall 2014')", 'max_length': '2'})
        }
    }

    complete_apps = ['schedule2']