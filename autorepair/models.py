# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils import unittest
from django.test.client import Client
from django import test


# Create your models here.

class CarFamily(models.Model):
    """Семейство автомобилей
    """
    name = models.TextField(verbose_name=u"Семейство автомобилей")
    inomarka = models.BooleanField(verbose_name=u"Иномарка")
    def __unicode__(self):
        return unicode(self.name)

class CarPart(models.Model):
    """Отдел для починки
    """
    name = models.TextField(verbose_name=u"Отдел машины для починки")

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']


class AutoRepair(models.Model):
    """Автомастерские
    """
    name = models.CharField(max_length=30,verbose_name=u"Название мастерской")
    about = models.TextField(verbose_name=u"Описание")
    rank = models.FloatField(verbose_name=u"Оценка",blank=True)
    inomarki = models.BooleanField(verbose_name=u"Ремонт иномарок")
    russkie = models.BooleanField(verbose_name=u"Ремонт русских машин")
    address = models.TextField(verbose_name=u"Адрес расположения")
    telephone = models.TextField(verbose_name=u"Телефон(ы)")

    @models.permalink
    def get_absolute_url(self):
        return ("autorepair",(),{"id":self.pk})

    def __unicode__(self):
        return unicode(self.name)



class Repair(models.Model):
    """Услуга
    """
    OTDEL_CHOICES = (
        ("Подвеска","Подвеска"),
        ("Карданный вал","Карданный вал"),
        ("Подушки двигателя","Подушки двигателя"),
        ("Сцепление","Сцепление"),
        ("Тормоза","Тормоза"),
        ("Двигатель","Двигатель"),
        ("Система выпуска отраб. газов","Система выпуска отраб. газов"),
        ("Сервисные работы","Сервисные работы"),
    )
    name = models.CharField(verbose_name=u"Услуга",max_length=50)
    otdel = models.CharField(verbose_name=u"Отдел для починки",max_length=40,choices=OTDEL_CHOICES)
    autorepair = models.ForeignKey(AutoRepair,verbose_name=u"Мастерская")
    about = models.TextField(verbose_name=u"Описание услуги",blank=True)
    price = models.PositiveIntegerField(verbose_name=u"Цена")
    carFamily = models.ForeignKey(CarFamily,verbose_name=u"Семейство")

    def __unicode__(self):
        return unicode(self.name)

class Defect(models.Model):
    text = models.TextField(verbose_name=u"Неисправность")
    #TODO написать менеджер, возвращающий поломки, для которых известны починки DefectReason

    def __unicode__(self):
        return unicode(self.text)
    class Meta:
        ordering = ['text']

class DefectReason(models.Model):
    defect = models.ForeignKey(Defect,verbose_name=u"Неисправность")
    text = models.TextField(verbose_name=u"Возможная причина")
    carPart = models.ForeignKey(CarPart,verbose_name=u"Неисправная часть")

    def __unicode__(self):
        return unicode(self.text)



class DefectReasonAdmin(admin.ModelAdmin):
    list_filter = ['defect','carPart']

admin.site.register(CarFamily)
admin.site.register(CarPart)
admin.site.register(AutoRepair)
admin.site.register(Repair)
admin.site.register(Defect)
admin.site.register(DefectReason,DefectReasonAdmin)


#class AllTestCase(unittest.TestCase):
class AllTestCase(test.TestCase):
#    def setUp(self):
#        self.termostat = Defect(text="Полетел термостат")

    fixtures = ['dump_2.json']
    def test_defect(self):
        self.assertEqual("1","1")

    def test_path(self):
        c = Client()
        for path in ["/","/repairs","/defects","/defects/causes","/play"]:
            response = c.get("/")
            self.assertEqual(200,response.status_code)


    def test_defects_post(self):
        c = Client()
        #print Defect.objects.all()
        for x in range(10):
            response = c.post("/defects/",{"defect":str(x)})


    def test_causes_count(self):
        c = Client(enforce_csrf_checks=True)
        pks = [obj.pk for obj in Defect.objects.all()]
        print pks
        for pk in pks:

            response = c.post("/defects/causes",data={u"defect" :str(pk)},follow=True)
            #print len(response.content),response.content

            self.assertEqual(200,response.status_code)

            print response.status_code, response.context





