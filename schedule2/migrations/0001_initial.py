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
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'schedule2', ['Employee'])

        # Adding model 'Availability'
        db.create_table(u'schedule2_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule2.Employee'])),
            ('time_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_end', self.gf('django.db.models.fields.DateTimeField')()),
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
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule2.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_end': ('django.db.models.fields.DateTimeField', [], {}),
            'time_start': ('django.db.models.fields.DateTimeField', [], {})
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