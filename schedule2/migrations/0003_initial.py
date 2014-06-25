# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'schedule2_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('area', self.gf('django.db.models.fields.CharField')(default=('M', 'Math'), max_length=1)),
            ('subarea', self.gf('django.db.models.fields.CharField')(default=('LIB', 'Liberal Arts Math'), max_length=12)),
        ))
        db.send_create_signal(u'schedule2', ['Employee'])

        # Adding model 'Availability'
        db.create_table(u'schedule2_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule2.Employee'])),
            ('day', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('time_start', self.gf('django.db.models.fields.TimeField')()),
            ('time_end', self.gf('django.db.models.fields.TimeField')()),
            ('semester', self.gf('django.db.models.fields.CharField')(default=('FA', 'Fall 2014'), max_length=2)),
        ))
        db.send_create_signal(u'schedule2', ['Availability'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'schedule2_employee')

        # Deleting model 'Availability'
        db.delete_table(u'schedule2_availability')


    models = {
        u'schedule2.availability': {
            'Meta': {'object_name': 'Availability'},
            'day': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule2.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'default': "('FA', 'Fall 2014')", 'max_length': '2'}),
            'time_end': ('django.db.models.fields.TimeField', [], {}),
            'time_start': ('django.db.models.fields.TimeField', [], {})
        },
        u'schedule2.employee': {
            'Meta': {'object_name': 'Employee'},
            'area': ('django.db.models.fields.CharField', [], {'default': "('M', 'Math')", 'max_length': '1'}),
            'emp_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subarea': ('django.db.models.fields.CharField', [], {'default': "('LIB', 'Liberal Arts Math')", 'max_length': '12'})
        }
    }

    complete_apps = ['schedule2']