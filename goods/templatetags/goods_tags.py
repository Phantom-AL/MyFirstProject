from django.utils.http import urlencode

from goods.models import Categories
from django import template

register = template.Library()


@register.simple_tag()
def tab_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
