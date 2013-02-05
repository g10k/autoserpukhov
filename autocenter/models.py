# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from djangoratings.fields import RatingField
# Create your models here.

class AutoCenterType(models.Model):

    TYPE_CHOICES = (
        (u"Автосервис",u"Автосервис"),
        (u"Стоянка",u"Стоянка"),
        (u"Мойка",u"Мойка"),
        (u"Шиномонтаж",u"Шиномонтаж"),
        (u"АЗС",u"АЗС"),
        (u"Тюнинг",u"Тюнинг"),
        (u"Автострахование",u"Автострахование"),
        (u"Автомагазин",u"Автомагазин"),
        )
    type = models.CharField(u"Услуги",choices=TYPE_CHOICES,max_length="50")

    def __unicode__(self):
        return unicode(self.type)

    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"
        ordering = ['type']

class AutoCenterImage(models.Model):
    image =  models.ImageField(u"Фото",upload_to="autocenters")
    autocenter = models.ForeignKey('AutoCenter')

    def __unicode__(self):
        return unicode(self.image)

    class Meta:
        verbose_name = u"Фото автоцентра"
        verbose_name_plural = u"Фото автоцентров"
        ordering = ['autocenter']


class AutoCenterManager(models.Manager):
    def azs(self):
        qs = AutoCenter.objects.filter(maintenance__in=["5"])
        return qs
    def repairs(self):
        qs = AutoCenter.objects.filter(maintenance=1)
        return qs


class AutoCenter(models.Model):
    maintenance = models.ManyToManyField(AutoCenterType,verbose_name=u"Услуги")
    name = models.CharField(u"Название",max_length=100)
    address = models.CharField(u"Адрес",max_length = 300)
    telephone = models.CharField(u"Телефон",max_length =15,blank=True)
    about = models.TextField(u"Подробнее",blank=True)
    longitude = models.FloatField(u"Долгота")
    latitude = models.FloatField(u"Широта")
    worktime = models.CharField(u"Время работы",max_length=180)
    kachestvo = RatingField(range=5, verbose_name=u"Качество")
    udobstvo = RatingField(range=5, verbose_name=u"Удобство")
    stoimost = RatingField(range=5, verbose_name=u"Стоимость услуг")

    objects = AutoCenterManager()

    def _get_full_name(self):
        return u"%s. %s" % (self.name,self.address)

    def _get_coordinates(self):
        return u"%s, %s" % (self.latitude,self.longitude)

    def get_rating(self):
        return (self.udobstvo.get_rating() + self.kachestvo.get_rating() + self.stoimost.get_rating()) / 3

    coordinates = property(_get_coordinates)

    full_name = property(_get_full_name)

    @models.permalink
    def get_absolute_url(self):
        return ("place",(),{"pk":self.pk} )

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = u"Автоцентр"
        verbose_name_plural = u"Автоцентр"
        ordering = ['name']



class Otzyv(models.Model):
    MARK_CHOICES = (
        (5,5),
        (4,4),
        (3,3),
        (2,2),
        (1,1)
    )
    autocenter = models.ForeignKey(AutoCenter,verbose_name=u"Автосервисы")
    text = models.TextField(u"Ваш отзыв")
    user = models.ForeignKey(User,verbose_name=u"Автолюбитель")
    kachestvo = models.PositiveIntegerField(choices=MARK_CHOICES,verbose_name=u"Качество")
    udobstvo = models.PositiveIntegerField(choices=MARK_CHOICES,verbose_name=u"Удобство")
    stoimost = models.PositiveIntegerField(choices=MARK_CHOICES,verbose_name=u"Стоимость услуг")
    #time

    def __unicode__(self):
        return unicode(self.text)[:50]


    def get_absolute_url(self):

        return reverse("autocenter.views.place",kwargs={"pk":self.autocenter.pk}) + "#o%s" % self.pk

    def save(self,*args,**kwargs):
        print self.autocenter
        self.autocenter.udobstvo.add(score=self.udobstvo,user=self.user,ip_address="127.0.0.1")
        self.autocenter.stoimost.add(score=self.stoimost,user=self.user,ip_address="127.0.0.1")
        self.autocenter.kachestvo.add(score=self.kachestvo,user=self.user,ip_address="127.0.0.1")
        super(Otzyv,self).save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        self.autocenter.udobstvo.delete(user=self.user,id_address='127.0.0.1')
        self.autocenter.kachestvo.delete(user=self.user,id_address='127.0.0.1')
        self.autocenter.stoimost.delete(user=self.user,id_address='127.0.0.1')
        super(Otzyv,self).delete(*args,**kwargs)

    class Meta:
        verbose_name = u"Отзыв"
        verbose_name_plural = u"Отзывы"




admin.site.register(AutoCenterType)
admin.site.register(Otzyv)


