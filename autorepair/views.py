# -*- encoding: utf-8 -*-
# Create your views here.
#from django.views import
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.template import RequestContext
from django.core import serializers
from annoying.decorators import render_to,ajax_request



from autorepair.models import AutoRepair,CarFamily,Defect,DefectReason

@render_to("autorepair.html")
@csrf_protect
def autorepair(request,id):
    #TODO Попробовать сделать с использованием generic views
    try:
        autorepair = AutoRepair.objects.get(pk=id)
    except AutoRepair.DoesNotExist:
        raise Http404("Noe page")
    carFamilies = CarFamily.objects.all()

    return {
        "autorepair" : autorepair,
        'carFamilies':carFamilies
    }

@render_to("list.html")
def list(request):
    autorepairs = AutoRepair.objects.all()

    return {
        "autorepairs":autorepairs
    }

@render_to("list.html")
def list(request):
    autorepairs = AutoRepair.objects.all()

    return {
        "autorepairs":autorepairs
    }


@render_to("defects/index.html")
@csrf_protect
def defects(request):
    defects = Defect.objects.all()
    return { "defects":defects }

@csrf_protect
def defect_causes(request):
    if request.method == "POST":
        if request.POST.has_key(u"defect"):
            try:
                defect = Defect.objects.get(pk=request.POST[u"defect"])
            except Defect.DoesNotExist:
                raise Http404(u"Поломка не найдена")
            reasons = DefectReason.objects.filter(defect=defect)
            #print reasons
            return render_to_response("defects/causes/index.html",{
                "reasons":reasons,
                "defect":defect,
                },context_instance=RequestContext(request))
    return render_to_response("defects/causes/index.html",{},context_instance=RequestContext(request))


@ajax_request
def defects_causes_popup(request):
    id = request.GET["id"]
    try:
        defect = Defect.objects.get(pk=id)
        reasons = defect.defectreason_set.all()
        reasons = [reason.text for reason in reasons]
        return {"reasons":reasons}
    except Defect.DoesNotExist:
        return {}
    return {}