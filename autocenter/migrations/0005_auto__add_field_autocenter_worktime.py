# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AutoCenter.worktime'
        db.add_column('autocenter_autocenter', 'worktime',
                      self.gf('django.db.models.fields.CharField')(default='\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba \xd1\x81\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0 \xd0\xbf\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd1\x81 16 \xd0\xb4\xd0\xbe 18', max_length=180),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AutoCenter.worktime'
        db.delete_column('autocenter_autocenter', 'worktime')


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
        }
    }

    complete_apps = ['autocenter']