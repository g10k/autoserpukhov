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


