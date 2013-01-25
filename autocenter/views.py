# -*- encoding: utf-8 -*-
from django.http import Http404
from django.contrib.comments.signals import comment_will_be_posted


def comment_handler(sender,**kwargs):
    print sender, kwargs
    return True
comment_will_be_posted.connect(comment_handler)



from annoying.decorators import render_to

from autocenter.models import AutoCenter

@render_to("places/index.html")
def places(request):
    autocenters = AutoCenter.objects.all()
    return {"autocenters":autocenters}


@render_to("places/place.html")
def place(request,pk):
    try:
        autocenter = AutoCenter.objects.get(pk=pk)
    except AutoCenter.DoesNotExist:
        raise Http404(u"Нет такой страницы")


    return {"autocenter":autocenter}