# -*- encoding: utf-8 -*-
from django.http import Http404
from django.contrib.comments.signals import comment_will_be_posted,comment_was_posted
from django.shortcuts import redirect

from loginza.decorators import login_required
from loginza import signals

from threadedcomments.forms import ThreadedCommentForm

# TODO: Переместить OtzyvForm в AutoCenter
from threadedcomments.forms import OtzyvForm,ThreadedComment
from autocenter.models import Otzyv

def with_comments(func):

    def wrap(*args,**kwargs):
        d = func(*args,**kwargs)
        if isinstance(d, dict):
            d['comments'] = ThreadedComment.objects.all()[:3]
        return d
    return wrap

#def comment_handler(sender,**kwargs):
#    try:
#        print "This is comment_will_be_posted_handler says:",sender, kwargs
#        request= kwargs['request']
#        #commentForm = kwargs['comment']
#
#        autocenter=AutoCenter.objects.get(pk=request.POST['object_pk'])
#        autocenter.udobstvo.add(
#            score=request.POST['udobstvo'],
#            user=request.user,
#            ip_address=request.META['REMOTE_ADDR']
#        )
#        autocenter.kachestvo.add(
#            score=request.POST['kachestvo'],
#            user=request.user,
#            ip_address=request.META['REMOTE_ADDR']
#        )
#        autocenter.stoimost.add(
#            score=request.POST['stoimost'],
#            user=request.user,
#            ip_address=request.META['REMOTE_ADDR']
#        )
#        print "successfull", autocenter
#        return True
#    except :
#        return False

#comment_will_be_posted.connect(comment_handler)
#comment_was_posted.connect(comment_handler)


from annoying.decorators import render_to

from autocenter.models import AutoCenter

@render_to("places/index.html")
@with_comments
def places(request):
    autocenters = AutoCenter.objects.all()
    otzyvi = Otzyv.objects.all()[:5]
    return {"autocenters":autocenters,"otzyvi":otzyvi}


#@login_required
@render_to("places/place.html")
@with_comments
def place(request,pk):
    try:
        autocenter = AutoCenter.objects.get(pk=pk)
    except AutoCenter.DoesNotExist:
        raise Http404(u"Нет такой страницы")

    if request.method == "POST":
        form = OtzyvForm(request.POST)
        print request.POST
        print OtzyvForm
        if form.is_valid():
            print "EST CONTACT"
            form.save()
        else:
            print "EST OSHIBKI",form.errors
            #print form.cleaned_data
            return {"autocenter":autocenter,"otzyvForm":form}

    print request.user

    return {"autocenter":autocenter,"otzyvForm":OtzyvForm(initial={"autocenter":autocenter,"user":request.user})}