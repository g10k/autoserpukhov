# -*- encoding: utf-8 -*-
__author__ = 'Сергей'
import json

from django import template

from loginza import models

register = template.Library()


#тег принимает auth.models.User и возвращает в контекст словарь data

@register.assignment_tag
def identity_data(user):
    try:
        map = models.UserMap.objects.get(user=user)
        return json.loads(map.identity.data)
    except models.UserMap.DoesNotExist:
        return {}


from math import ceil
@register.inclusion_tag("templatetags/stars.html")
def stars(num,totaly=5):
    """Высвечивает num заполненых звезд"""
    n = int(ceil(num))
    stars_list = (1,)*n + (0,)*(5-n)
    print stars_list

    return {"stars_list":stars_list}

