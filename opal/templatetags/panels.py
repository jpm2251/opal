"""
Templatetags for panels
"""
from django import template
from django.template.loader import get_template

from opal.utils import camelcase_to_underscore

register = template.Library()


@register.inclusion_tag('_helpers/record_panel.html')
def record_panel(model, editable=1, title=None, name=None, detail_template=None, angular_filter=None, noentries=None, only_display_if_exists=False):
    """
    Register a panel for our record.
    Editable is an angular expression
    to be evaluated
    """

    if name is None:
        name = camelcase_to_underscore(model.__class__.__name__)

    if detail_template is None:
        detail_template = model.__class__.get_detail_template()

    if title is None:
        title = getattr(model, '_title', name.replace('_', ' ').title())

    return {
        'name': name,
        'singleton': getattr(model, '_is_singleton', False),
        'title': title,
        'detail_template': detail_template,
        'icon': getattr(model, '_icon', None),
        'editable': editable,
        'angular_filter': angular_filter,
        'noentries': noentries,
        'only_display_if_exists': only_display_if_exists
    }

@register.inclusion_tag('_helpers/record_timeline.html')
def record_timeline(model, whenfield):
    name = camelcase_to_underscore(model.__class__.__name__)

    return {
        'name': name,
        'editable': True,
        'title': getattr(model, '_title', name.replace('_', ' ').title()),
        'detail_template': model.__class__.get_detail_template(),
        'icon': getattr(model, '_icon', None),
        'whenfield': whenfield,
    }

@register.inclusion_tag('_helpers/teams_panel.html')
def teams_panel():
    return {}
