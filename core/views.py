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
from autocenter import models
from threadedcomments.models import ThreadedComment

@csrf_exempt
@render_to("index.html")
def index(request):
    title = u"АвтоСерпухов"
    autocenters = models.AutoCenter.objects.prefetch_related().all()
    autocentertypes = models.AutoCenterType.objects.all()
    autocenter_cls = models.AutoCenter
    repairs = models.AutoCenter.objects.repairs()
    comments = ThreadedComment.objects.all()[:3]
    local_vars = locals()
    local_vars.pop('request')
    print request
    return local_vars

@ajax_request
def search_by_name(request):
#    print request
    names = [name.encode("utf8") for name in models.AutoCenter.objects.values_list("name", flat=True)]
    return {"lol": names}
    return {"lol":['big', 'mom']}

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