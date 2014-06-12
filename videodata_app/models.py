# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.

class Video(models.Model):
	video_id = models.CharField(max_length='128', null=False, blank=False, unique=True)
	description = models.CharField(max_length='128', null=True, blank=True)

class Tag(models.Model):
	name = models.CharField(max_length='100', null=False, blank=False)
	short_desc = models.CharField(max_length='140', null=False, blank=False)
	description = models.TextField(blank=True)
	start_time = models.CharField(max_length='140', null=False, blank=False)
	end_time = models.CharField(max_length='140', null=True, blank=True)
	video = models.ForeignKey(Video)
