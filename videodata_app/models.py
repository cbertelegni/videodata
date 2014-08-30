# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.

class Video(models.Model):
	# http://gdata.youtube.com/feeds/api/videos/91pBlB8oH_E
	video_id = models.CharField(max_length='128', null=False, blank=False, unique=True)
	description = models.CharField(max_length='128', null=True, blank=True)
	FONT = (
		('youtube', 'youtube'),
		('vimeo', 'vimeo'),
	)
	font = models.CharField(max_length=100, choices=FONT, blank=True, default="youtube")

	def __unicode__(self):
		return "Video is: %s" % (self.video_id,)
	
	class Meta:
		ordering = ('video_id',)


class VideoVersion(models.Model):
	video = models.ForeignKey(Video, related_name="versions", default=None)
	# ouner = 


class Name(models.Model):
	""" capo name dentro de tag """
	name = models.CharField(max_length='128', unique=True, default=None)
	count= models.IntegerField(default=0)


class Tag(models.Model):
	# name = models.CharField(max_length='100', null=False, blank=False)
	video_version = models.ForeignKey(VideoVersion, related_name="tags")
	name = models.ForeignKey(Name, related_name="tags", default=None)
	short_desc = models.CharField(max_length='140', null=False, blank=False)
	description = models.TextField(blank=True)
	start_time = models.CharField(max_length='140', null=False, blank=False)
	end_time = models.CharField(max_length='140', null=True, blank=True)

	class Meta:
		ordering = ('name', 'short_desc',)

	def __unicode__(self):
		return "%s, %s " % (self.name, self.short_desc,)



# class Hastag(models.Model):
# 	name = models.Model(max_length=50, null=True)
