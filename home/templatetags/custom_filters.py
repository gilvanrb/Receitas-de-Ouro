# home/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    if "youtube.com/watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    elif "youtu.be/" in url:
        video_id = url.split('/')[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    return url