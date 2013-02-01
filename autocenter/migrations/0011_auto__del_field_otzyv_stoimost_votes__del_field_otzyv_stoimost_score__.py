# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Otzyv.stoimost_votes'
        db.delete_column('autocenter_otzyv', 'stoimost_votes')

        # Deleting field 'Otzyv.stoimost_score'
        db.delete_column('autocenter_otzyv', 'stoimost_score')

        # Deleting field 'Otzyv.udobstvo_score'
        db.delete_column('autocenter_otzyv', 'udobstvo_score')

        # Deleting field 'Otzyv.kachestvo_score'
        db.delete_column('autocenter_otzyv', 'kachestvo_score')

        # Deleting field 'Otzyv.kachestvo_votes'
        db.delete_column('autocenter_otzyv', 'kachestvo_votes')

        # Deleting field 'Otzyv.udobstvo_votes'
        db.delete_column('autocenter_otzyv', 'udobstvo_votes')

        # Adding field 'Otzyv.kachestvo'
        db.add_column('autocenter_otzyv', 'kachestvo',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Otzyv.udobstvo'
        db.add_column('autocenter_otzyv', 'udobstvo',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=3),
                      keep_default=False)

        # Adding field 'Otzyv.stoimost'
        db.add_column('autocenter_otzyv', 'stoimost',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Otzyv.stoimost_votes'
        db.add_column('autocenter_otzyv', 'stoimost_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Otzyv.stoimost_score'
        db.add_column('autocenter_otzyv', 'stoimost_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Otzyv.udobstvo_score'
        db.add_column('autocenter_otzyv', 'udobstvo_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Otzyv.kachestvo_score'
        db.add_column('autocenter_otzyv', 'kachestvo_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Otzyv.kachestvo_votes'
        db.add_column('autocenter_otzyv', 'kachestvo_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Otzyv.udobstvo_votes'
        db.add_column('autocenter_otzyv', 'udobstvo_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Deleting field 'Otzyv.kachestvo'
        db.delete_column('autocenter_otzyv', 'kachestvo')

        # Deleting field 'Otzyv.udobstvo'
        db.delete_column('autocenter_otzyv', 'udobstvo')

        # Deleting field 'Otzyv.stoimost'
        db.delete_column('autocenter_otzyv', 'stoimost')


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
        },
        'autocenter.otzyv': {
            'Meta': {'object_name': 'Otzyv'},
            'autocenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autocenter.AutoCenter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kachestvo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'stoimost': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'udobstvo': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['autocenter']