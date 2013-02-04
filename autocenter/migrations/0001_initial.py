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
            ('stoimost_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('stoimost_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('kachestvo_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('kachestvo_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('autocenter', ['AutoCenter'])

        # Adding M2M table for field maintenance on 'AutoCenter'
        db.create_table('autocenter_autocenter_maintenance', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('autocenter', models.ForeignKey(orm['autocenter.autocenter'], null=False)),
            ('autocentertype', models.ForeignKey(orm['autocenter.autocentertype'], null=False))
        ))
        db.create_unique('autocenter_autocenter_maintenance', ['autocenter_id', 'autocentertype_id'])

        # Adding model 'Otzyv'
        db.create_table('autocenter_otzyv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autocenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autocenter.AutoCenter'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('kachestvo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('udobstvo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('stoimost', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('autocenter', ['Otzyv'])


    def backwards(self, orm):
        # Deleting model 'AutoCenterType'
        db.delete_table('autocenter_autocentertype')

        # Deleting model 'AutoCenterImage'
        db.delete_table('autocenter_autocenterimage')

        # Deleting model 'AutoCenter'
        db.delete_table('autocenter_autocenter')

        # Removing M2M table for field maintenance on 'AutoCenter'
        db.delete_table('autocenter_autocenter_maintenance')

        # Deleting model 'Otzyv'
        db.delete_table('autocenter_otzyv')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'autocenter.autocenter': {
            'Meta': {'ordering': "['name']", 'object_name': 'AutoCenter'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kachestvo_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'kachestvo_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'maintenance': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['autocenter.AutoCenterType']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'stoimost_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'stoimost_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
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
        },
        'autocenter.otzyv': {
            'Meta': {'object_name': 'Otzyv'},
            'autocenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autocenter.AutoCenter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kachestvo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'stoimost': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'udobstvo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['autocenter']