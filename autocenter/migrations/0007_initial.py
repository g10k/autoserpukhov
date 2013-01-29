# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AutoCenterType'
        db.create_table('autocenter_autocentertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='50')),
        ))
        db.send_create_signal('autocenter', ['AutoCenterType'])

        # Adding model 'AutoCenterImage'
        db.create_table('autocenter_autocenterimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('autocenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autocenter.AutoCenter'])),
        ))
        db.send_create_signal('autocenter', ['AutoCenterImage'])

        # Adding model 'AutoCenter'
        db.create_table('autocenter_autocenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('worktime', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('udobstvo_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('udobstvo_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('autocenter', ['AutoCenter'])

        # Adding M2M table for field maintenance on 'AutoCenter'
        db.create_table('autocenter_autocenter_maintenance', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('autocenter', models.ForeignKey(orm['autocenter.autocenter'], null=False)),
            ('autocentertype', models.ForeignKey(orm['autocenter.autocentertype'], null=False))
        ))
        db.create_unique('autocenter_autocenter_maintenance', ['autocenter_id', 'autocentertype_id'])


    def backwards(self, orm):
        # Deleting model 'AutoCenterType'
        db.delete_table('autocenter_autocentertype')

        # Deleting model 'AutoCenterImage'
        db.delete_table('autocenter_autocenterimage')

        # Deleting model 'AutoCenter'
        db.delete_table('autocenter_autocenter')

        # Removing M2M table for field maintenance on 'AutoCenter'
        db.delete_table('autocenter_autocenter_maintenance')


    models = {
        'autocenter.autocenter': {
            'Meta': {'ordering': "['name']", 'object_name': 'AutoCenter'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'maintenance': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['autocenter.AutoCenterType']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'udobstvo_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'udobstvo_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'worktime': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        'autocenter.autocenterimage': {
            'Meta': {'ordering': "['autocenter']", 'object_name': 'AutoCenterImage'},
            'autocenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autocenter.AutoCenter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'autocenter.autocentertype': {
            'Meta': {'ordering': "['type']", 'object_name': 'AutoCenterType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        }
    }

    complete_apps = ['autocenter']