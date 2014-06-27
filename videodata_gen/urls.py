from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videodata_gen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'videodata_app.views.home', name='home'),
    url(r'^viewer/(?P<video_id>[\w-]+)/$', 'videodata_app.views.viewer_video', name='viewer'),
    url(r'^tagging/(?P<video_id>[\w-]+)/$', 'videodata_app.views.tagging', name='tagging'),
    # url(r'^tagging/(?P<video_id>[\w-]+)/(?P<tag_id>[\w-]+)$', 'videodata_app.views.save_tag', name='save_tag'),
    url(r'^tagging/(?P<video_id>[\w-]+)/crear_tag/$', 'videodata_app.views.save_tag', name='crear_tag'),
)
