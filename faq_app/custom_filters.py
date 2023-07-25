from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def trim_excerpt(value, length=100):
    excerpt = strip_tags(value)[:length]
    if len(value) > length:
        excerpt += "..."
    return excerpt
