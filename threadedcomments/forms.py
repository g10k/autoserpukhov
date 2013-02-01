# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.comments.forms import CommentForm,CommentSecurityForm
from django.conf import settings
from django.utils.hashcompat import sha_constructor
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import RadioFieldRenderer,RadioInput
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from djangoratings.forms import RatingField
from threadedcomments.models import ThreadedComment

from autocenter.models import Otzyv,AutoCenter


#class RatingWidget(Checkbox):
#    def render(self, name, value, attrs=None, choices=()):
#        if value is None: value = ''
#        final_attrs = self.build_attrs(attrs, name=name)
#        output = [u'<select%s>' % flatatt(final_attrs)]
#        options = self.render_options(choices, [value])
#        if options:
#            output.append(options)
#        output.append(u'</select>')
#        return mark_safe(u'\n'.join(output))


#TODO
class SimpleInput(RadioInput):
    #input без label
    def render(self, name=None, value=None, attrs=None, choices=()):
        name = name or self.name
        value = value or self.value
        attrs = attrs or self.attrs
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''
        choice_label = conditional_escape(force_unicode(self.choice_label))
        return mark_safe(u'%s' % (self.tag()))



class SimpleRenderer(RadioFieldRenderer):
    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield SimpleInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return SimpleInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def render(self):
        """Outputs a <ul> for this set of radio fields."""
        return mark_safe(u'\n'.join([force_unicode(w) for w in self]))

class UserField(forms.CharField):
    class widget(forms.widgets.TextInput):
        def render(self, name, value, attrs=None):
            if isinstance(value, int):
                value = unicode(User.objects.get(pk=value))
            return super(UserField.widget, self).render(name, value, attrs)

    def clean(self, value):
        value = super(UserField, self).clean(value)
        if not value:
            return None
        try:
            return User.objects.get(username=value)
        except User.DoesNotExist:
            raise forms.ValidationError(u'invalid user name')




class OtzyvForm(forms.ModelForm):
    class Meta:
        model = Otzyv
    MARK_CHOICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    autocenter = forms.ModelChoiceField(queryset=AutoCenter.objects.all(),widget=forms.HiddenInput)
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput)
    kachestvo = forms.ChoiceField(required=True, label=u"Качество",
        choices=MARK_CHOICES,
        widget=forms.RadioSelect(renderer=SimpleRenderer,
            attrs={
                "name":"star-",
                "class":'star'}
        )
    )
    stoimost = forms.ChoiceField(required=True, label=u"Цены",
        choices=tuple(zip(range(1,6),range(1,6))),
        widget=forms.RadioSelect(renderer=SimpleRenderer,
            attrs={
                "name":"star-",
                "class":'star'}
        )
    )
    udobstvo = forms.ChoiceField(required=True, label=u"Удобство",
        choices=tuple(zip(range(1,6),range(1,6))),
        widget=forms.RadioSelect(renderer=SimpleRenderer,
            attrs={
                "name":"star-",
                "class":'star'}
        )
    )


class ThreadedCommentForm(CommentForm):
    parent = forms.IntegerField(required=False, widget=forms.HiddenInput)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput)
    name = forms.CharField(required=False,widget=forms.HiddenInput)
    email = forms.CharField(required=False,widget=forms.HiddenInput)
    comment = forms.CharField(label=_('Comment'),
        widget=forms.TextInput(attrs={
            "cols":1000,
            #"style":"width:300px; height:100px"
        }))
#    kachestvo = RatingField(required=True, label=u"Качество",
#        choices=tuple(zip(range(1,6),range(1,6))),
#        widget=forms.RadioSelect(renderer=SimpleRenderer,
#            attrs={
#            "name":"star-",
#            "class":'star'}
#        )
#    )
#    stoimost = RatingField(required=True, label=u"Цены",
#        choices=tuple(zip(range(1,6),range(1,6))),
#        widget=forms.RadioSelect(renderer=SimpleRenderer,
#            attrs={
#                "name":"star-",
#                "class":'star'}
#        )
#    )
#    udobstvo = RatingField(required=True, label=u"Удобство",
#        choices=tuple(zip(range(1,6),range(1,6))),
#        widget=forms.RadioSelect(renderer=SimpleRenderer,
#            attrs={
#                "name":"star-",
#                "class":'star'}
#        )
#    )

    url = forms.CharField(required=False, widget=forms.HiddenInput)

#    title = forms.CharField(required=False,widget=forms.HiddenInput)
    def __init__(self,target_object, parent=None, data=None, initial=None):
        self.base_fields.insert(
                self.base_fields.keyOrder.index('comment'), 'title',
                forms.CharField(
                    label=_('title'),
                    required=False,
                    max_length=getattr(settings, 'COMMENTS_TITLE_MAX_LENGTH', 255),
                    widget=forms.HiddenInput
                )
            )
        self.parent = parent
        if initial is None:
            initial = {}
        initial.update({'parent': self.parent})
        super(ThreadedCommentForm, self).__init__(target_object, data=data,
            initial=initial)

    def get_comment_model(self):
        return ThreadedComment

    def get_comment_create_data(self):
        d = super(ThreadedCommentForm, self).get_comment_create_data()
        d['parent_id'] = self.cleaned_data['parent']
        d['title'] = self.cleaned_data['title']
        return d


