from django.contrib import admin
from videodata_app.models import *


class TagsInline(admin.TabularInline):
	model = Tag
	extra = 0

class VideoAdmin(admin.ModelAdmin):
	# inlines = [TagsInline,]
	# search_fields = ['tags__name', 'tags__short_desc']

admin.site.register(Video,)
admin.site.register(Tag,)


# Register your models here.


