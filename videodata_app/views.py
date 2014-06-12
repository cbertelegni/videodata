# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect, render_to_response, render
from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.context_processors import csrf
# from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
# from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# from utils import get_index_cols_csv # helpers de la app congreso
# from congreso.models import Legislador, Partido, MiembrosPartido, MiembrosAgrupacion, Ley, Sesion, Voto, AliasNombre, AliasPartido
# from congreso.models import Legislador, Partido, Ley, Sesion, Voto, AliasNombre, AliasPartido
import csv
import datetime
# from var_dump import var_dump # Debugs objs
# import the logging library
# import logging
# Get an instance of a logger
# log = logging.getLogger(__name__)
import urllib2
import urllib # para leer el archivo
import re
import sys
from pyquery import PyQuery as pq
from lxml import etree
from videodata_app import models

def home(request):
	return render_to_response('videodata_app/index.html', {})


def taguear_video(request, video_id):
	# url = "http://www.youtube.com/get_video_info?video_id=Ghz5dQaMKTA"
	# response = urllib2.urlopen(url)
	# html = response.read()
	# print html
	return render_to_response('videodata_app/tagging.html', {"video_id": video_id})


def save_tag(request, video_id, tag_id):
	pass


def scrap_subtitles_es(): # for maleb
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