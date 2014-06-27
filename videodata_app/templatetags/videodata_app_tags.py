from django.core.context_processors import csrf
from django import template
from django.template.loader import get_template
register = template.Library()


@register.simple_tag(takes_context=True)
def render_video(context, video, tags, editar = None):
    t = get_template("videodata_app/tags/render_video.html")
    context["video"] = video
    context["tags"] = tags
    context["editar"] = editar
    return t.render(context)