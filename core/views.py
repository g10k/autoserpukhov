# -*- encoding: utf-8 -*-
__author__ = 'Сергей'
from random import randint
from functools import wraps

from django.shortcuts  import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson


from annoying.decorators import render_to,ajax_request
from autorepair.models import AutoRepair
from autocenter.models import AutoCenter, AutoCenterType






@csrf_exempt
@render_to("index.html")
def index(request):
    repairs = AutoRepair.objects.all()
    title = u"АвтоСерпухов"
    autocenters = AutoCenter.objects.all()
    autocentertypes = AutoCenterType.objects.all()
    autocenter_cls = AutoCenter
    repairs = AutoCenter.objects.repairs()
    local_vars = locals()
    local_vars.pop('request')
    print request
    return local_vars


@render_to("guess_button.html")
def guess_button(request):
    if request.is_ajax():

        try:
            count = int(request.GET["count"])
        except ValueError as e:
            return HttpResponse(simplejson.dumps({"error":request.GET["count"] + u" - не целое число"}),mimetype="application/json")

        request.session['count'] = count
        request.session['guess_int'] = randint(1,count)

        if request.session.has_key('button_created') and request.session.has_key('button_created'):
            print "already created"

        request.session['button_created'] = True

        return HttpResponse(simplejson.dumps({"count":count}),mimetype="application/json")

    return {}