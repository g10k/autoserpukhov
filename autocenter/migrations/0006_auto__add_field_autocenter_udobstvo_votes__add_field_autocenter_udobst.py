# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AutoCenter.udobstvo_votes'
        db.add_column('autocenter_autocenter', 'udobstvo_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.udobstvo_score'
        db.add_column('autocenter_autocenter', 'udobstvo_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AutoCenter.udobstvo_votes'
        db.delete_column('autocenter_autocenter', 'udobstvo_votes')

        # Deleting field 'AutoCenter.udobstvo_score'
        db.delete_column('autocenter_autocenter', 'udobstvo_score')


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