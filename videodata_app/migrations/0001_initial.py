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
            ('font', self.gf('django.db.models.fields.CharField')(default='youtube', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'videodata_app', ['Video'])

        # Adding model 'VideoVersion'
        db.create_table(u'videodata_app_videoversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='versions', to=orm['videodata_app.Video'])),
        ))
        db.send_create_signal(u'videodata_app', ['VideoVersion'])

        # Adding model 'Name'
        db.create_table(u'videodata_app_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length='128')),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'videodata_app', ['Name'])

        # Adding model 'Tag'
        db.create_table(u'videodata_app_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_version', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['videodata_app.VideoVersion'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='tags', to=orm['videodata_app.Name'])),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length='140')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.CharField')(max_length='140')),
            ('end_time', self.gf('django.db.models.fields.CharField')(max_length='140', null=True, blank=True)),
        ))
        db.send_create_signal(u'videodata_app', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'videodata_app_video')

        # Deleting model 'VideoVersion'
        db.delete_table(u'videodata_app_videoversion')

        # Deleting model 'Name'
        db.delete_table(u'videodata_app_name')

        # Deleting model 'Tag'
        db.delete_table(u'videodata_app_tag')


    models = {
        u'videodata_app.name': {
            'Meta': {'object_name': 'Name'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': "'128'"})
        },
        u'videodata_app.tag': {
            'Meta': {'ordering': "('name', 'short_desc')", 'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.CharField', [], {'max_length': "'140'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tags'", 'to': u"orm['videodata_app.Name']"}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': "'140'"}),
            'start_time': ('django.db.models.fields.CharField', [], {'max_length': "'140'"}),
            'video_version': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': u"orm['videodata_app.VideoVersion']"})
        },
        u'videodata_app.video': {
            'Meta': {'ordering': "('video_id',)", 'object_name': 'Video'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'128'", 'null': 'True', 'blank': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'youtube'", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'128'"})
        },
        u'videodata_app.videoversion': {
            'Meta': {'object_name': 'VideoVersion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'versions'", 'to': u"orm['videodata_app.Video']"})
        }
    }

    complete_apps = ['videodata_app']