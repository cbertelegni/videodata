# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect, render_to_response, render
from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.models import User
import csv
import datetime
import urllib2
import urllib # para leer el archivo
import re
import sys
from pyquery import PyQuery as pq
from lxml import etree
from videodata_app.models import *
import json
from django.core.context_processors import csrf

def home(request):
	videos = Video.objects.all()
	return render_to_response('videodata_app/index.html', {'videos': videos})


def tagging(request, video_id, version = None):
	# print unicode(csrf(request)['csrf_token'])
	# url = "http://www.youtube.com/get_video_info?video_id=Ghz5dQaMKTA"
	# response = urllib2.urlopen(url)
	# html = response.read()
	# print html
	
	video, created = Video.objects.get_or_create(video_id=video_id)
	video_version = video.versions.first()
	if video_version:
		tags = video_version.tags.all()
	else:
		video_version = VideoVersion(video = video)
		video_version.save()
		tags = None
	# if video_version:
	# 	tags = video_version.tags.objects.all()
	# else:
	# 	tags =None
	return render_to_response('videodata_app/tagging.html',
								{"video": video,
								"video_version": video_version,
								"tags": tags,
								"editar": True,
								'csrf_token': unicode(csrf(request)['csrf_token'])})


def save_tag(request, video_id):
	
	video = Video.objects.filter(video_id = video_id, ).first()
	name, created_name = Name.objects.get_or_create(name = request.POST['name'])
	tag, created = Tag.objects.get_or_create(
		video_version_id = video.id,
		name_id = name.id,
		short_desc = request.POST['short_desc'],
		description = request.POST['description'],
		start_time = request.POST['start_time'],
		end_time= request.POST['end_time'],
		)
	print tag
	if(created):
		pass
	else:
		pass


	# print tag_id
	response_data = {}

	response_data['video_id'] = video_id
	# response_data['tag_id'] = tag_id
	response_data['tag'] = request.POST
	response_data['tag_id'] = tag.id

	# Tag.objects.get_or_create()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def viewer_video(request, video_id):
	video = get_object_or_404(Video, video_id=video_id)
	tags = Tag.objects.filter(video_id= video.id)
	return render_to_response('videodata_app/viewer_video.html',
								{"video": video,
								"tags" : tags,
								'csrf_token': unicode(csrf(request)['csrf_token'])})



def scrap_subtitles_es():
	# for @malev, Thanks! :)
	""" esto no esta implementado..."""

	def srt_time_to_seconds(time):
	    split_time=time.split(',')
	    major, minor = (split_time[0].split(':'), split_time[1])
	    return int(major[0])*1440 + int(major[1])*60 + int(major[2]) + float(minor)/1000

	def srt_to_dict(srtText):
	    subs=[]
	    for s in re.sub('\r\n', '\n', srtText).split('\n\n'):
	        st = s.split('\n')
	        if len(st)>=3:
	            split = st[1].split(' --> ')
	            subs.append({'start': srt_time_to_seconds(split[0].strip()),
	                         'end': srt_time_to_seconds(split[1].strip()),
	                         'text': '<br />'.join(j for j in st[2:len(st)])
	                        })
	    return subs

	def get_sub(html):
	    bs = html('b')
	    for b in bs:
	        if re.search('spanish', pq(b).text(), re.I):
	            url = pq(bs.prev('a.l')).attr('href')
	            try:
	                response = urllib2.urlopen(url)
	                return response.read()
	            except URLError: 
	                pass 


	print "main.py [url del video de youtube]"

	url = "http://keepsubs.com?url=" + sys.argv[1]
	html = pq(url= url)

	subs = get_sub(html)


	output = ""
	for element in srt_to_dict(subs):
	    output = output + element["text"] + "\n"

	print output