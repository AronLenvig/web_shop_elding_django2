# myapp/templatetags/breadcrumb_tags.py
from django import template

register = template.Library()

@register.inclusion_tag('products/breadcrumps.html')
def breadcrumb_tag(breadcrumbs):
    return {'breadcrumbs': breadcrumbs}
