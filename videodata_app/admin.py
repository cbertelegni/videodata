from django.contrib import admin
from videodata_app.models import Video, Tag


class TagsInline(admin.TabularInline):
	model = Tag
	extra = 0

class VideoAdmin(admin.ModelAdmin):
	inlines = [TagsInline,]
	search_fields = ['tags__name',]

admin.site.register(Video, VideoAdmin,)
admin.site.register(Tag,)


# Register your models here.


