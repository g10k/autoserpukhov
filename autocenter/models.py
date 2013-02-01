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

    objects = AutoCenterManager()

    def _get_full_name(self):
        return u"%s. %s" % (self.name,self.address)

    def _get_coordinates(self):
        return u"%s, %s" % (self.latitude,self.longitude)

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
    autocenter = models.ForeignKey(AutoCenter,verbose_name=u"Автосервисы")
    text = models.TextField(u"Отзыв")
    user = User(u"Автолюбитель")
    kachestvo = RatingField(range=5,verbose_name=u"Качество")
    udobstvo = RatingField(range=5,verbose_name=u"Удобство")
    stoimost = RatingField(range=5,verbose_name=u"Стоимость услуг")



admin.site.register(AutoCenterType)
#admin.site.register(AutoCenter)
#admin.site.register(AutoCenterImage)


