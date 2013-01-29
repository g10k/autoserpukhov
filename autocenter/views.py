# -*- encoding: utf-8 -*-
from django.http import Http404
from django.contrib.comments.signals import comment_will_be_posted,comment_was_posted
from django.shortcuts import redirect

from loginza.decorators import login_required
from loginza import signals

from threadedcomments.forms import ThreadedCommentForm


def comment_handler(sender,**kwargs):

    print "This is comment_will_be_posted_handler says:",sender, kwargs
    request= kwargs['request']
    #commentForm = kwargs['comment']

    autocenter=AutoCenter.objects.get(pk=request.POST['object_pk'])
    autocenter.udobstvo.add(
        score=request.POST['udobstvo'],
        user=request.user,
        ip_address=request.META['REMOTE_ADDR']
    )
    autocenter.kachestvo.add(
        score=request.POST['kachestvo'],
        user=request.user,
        ip_address=request.META['REMOTE_ADDR']
    )
    autocenter.stoimost.add(
        score=request.POST['stoimost'],
        user=request.user,
        ip_address=request.META['REMOTE_ADDR']
    )
    print "successfull", autocenter
    return True

comment_will_be_posted.connect(comment_handler)
#comment_was_posted.connect(comment_handler)



from annoying.decorators import render_to

from autocenter.models import AutoCenter

@render_to("places/index.html")
def places(request):
    autocenters = AutoCenter.objects.all()
    return {"autocenters":autocenters}


#@login_required
@render_to("places/place.html")
def place(request,pk):
    try:
        autocenter = AutoCenter.objects.get(pk=pk)
    except AutoCenter.DoesNotExist:
        raise Http404(u"Нет такой страницы")
    if request.method == "POST":
        print request.form



    return {"autocenter":autocenter,}