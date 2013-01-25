# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TypeAutoCenter'
        db.create_table('autocenter_typeautocenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='50')),
        ))
        db.send_create_signal('autocenter', ['TypeAutoCenter'])

        # Adding model 'AutoCenter'
        db.create_table('autocenter_autocenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('autocenter', ['AutoCenter'])

        # Adding M2M table for field maintenance on 'AutoCenter'
        db.create_table('autocenter_autocenter_maintenance', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('autocenter', models.ForeignKey(orm['autocenter.autocenter'], null=False)),
            ('typeautocenter', models.ForeignKey(orm['autocenter.typeautocenter'], null=False))
        ))
        db.create_unique('autocenter_autocenter_maintenance', ['autocenter_id', 'typeautocenter_id'])


    def backwards(self, orm):
        # Deleting model 'TypeAutoCenter'
        db.delete_table('autocenter_typeautocenter')

        # Deleting model 'AutoCenter'
        db.delete_table('autocenter_autocenter')

        # Removing M2M table for field maintenance on 'AutoCenter'
        db.delete_table('autocenter_autocenter_maintenance')


    models = {
        'autocenter.autocenter': {
            'Meta': {'object_name': 'AutoCenter'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintenance': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['autocenter.TypeAutoCenter']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'autocenter.typeautocenter': {
            'Meta': {'object_name': 'TypeAutoCenter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        }
    }

    complete_apps = ['autocenter']