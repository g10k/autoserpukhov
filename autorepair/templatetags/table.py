# -*- encoding: utf-8 -*-
__author__ = 'Сергей'

from django import template
register = template.Library()

from autorepair.models import Repair


@register.inclusion_tag("tags/preiskurant.html")
def preiskurant(autorepair):

    repairs = Repair.objects.filter(autorepair=autorepair)
    return {'repairs':repairs }
