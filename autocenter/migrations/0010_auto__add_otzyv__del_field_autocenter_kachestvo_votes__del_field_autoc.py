# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Otzyv'
        db.create_table('autocenter_otzyv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autocenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autocenter.AutoCenter'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('udobstvo_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('udobstvo_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('stoimost_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('stoimost_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('kachestvo_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('kachestvo_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('autocenter', ['Otzyv'])

        # Deleting field 'AutoCenter.kachestvo_votes'
        db.delete_column('autocenter_autocenter', 'kachestvo_votes')

        # Deleting field 'AutoCenter.udobstvo_votes'
        db.delete_column('autocenter_autocenter', 'udobstvo_votes')

        # Deleting field 'AutoCenter.udobstvo_score'
        db.delete_column('autocenter_autocenter', 'udobstvo_score')

        # Deleting field 'AutoCenter.stoimost_votes'
        db.delete_column('autocenter_autocenter', 'stoimost_votes')

        # Deleting field 'AutoCenter.stoimost_score'
        db.delete_column('autocenter_autocenter', 'stoimost_score')

        # Deleting field 'AutoCenter.kachestvo_score'
        db.delete_column('autocenter_autocenter', 'kachestvo_score')


    def backwards(self, orm):
        # Deleting model 'Otzyv'
        db.delete_table('autocenter_otzyv')

        # Adding field 'AutoCenter.kachestvo_votes'
        db.add_column('autocenter_autocenter', 'kachestvo_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.udobstvo_votes'
        db.add_column('autocenter_autocenter', 'udobstvo_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.udobstvo_score'
        db.add_column('autocenter_autocenter', 'udobstvo_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.stoimost_votes'
        db.add_column('autocenter_autocenter', 'stoimost_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.stoimost_score'
        db.add_column('autocenter_autocenter', 'stoimost_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'AutoCenter.kachestvo_score'
        db.add_column('autocenter_autocenter', 'kachestvo_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


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
            'kachestvo_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'kachestvo_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'stoimost_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'stoimost_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'udobstvo_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'udobstvo_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['autocenter']