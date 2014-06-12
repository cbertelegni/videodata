# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'videodata_app_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length='128')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length='128', null=True, blank=True)),
        ))
        db.send_create_signal(u'videodata_app', ['Video'])

        # Adding model 'Tag'
        db.create_table(u'videodata_app_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length='140')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.CharField')(max_length='140')),
            ('end_time', self.gf('django.db.models.fields.CharField')(max_length='140', null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videodata_app.Video'])),
        ))
        db.send_create_signal(u'videodata_app', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'videodata_app_video')

        # Deleting model 'Tag'
        db.delete_table(u'videodata_app_tag')


    models = {
        u'videodata_app.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.CharField', [], {'max_length': "'140'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': "'140'"}),
            'start_time': ('django.db.models.fields.CharField', [], {'max_length': "'140'"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videodata_app.Video']"})
        },
        u'videodata_app.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'128'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'128'"})
        }
    }

    complete_apps = ['videodata_app']