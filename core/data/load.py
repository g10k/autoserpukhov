# -*- encoding: utf-8 -*-
__author__ = 'Сергей'
import csv
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import sys
#sys.path.append("D:\\sites\\repairit\\repairit")
#from repairit import settings
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from autorepair.models import AutoRepair,Repair,CarFamily



def loaddd(filename):
    def maker(func):
        def wrap():
            import os

            with open(filename,'rb') as f:
                reader = csv.reader(f,delimiter=";",lineterminator=";")
                for row in reader:
                    func(row)
            return
        return wrap
    return maker


@loaddd(filename="data/carFamily.csv")
def load_carFamilies(row):
    pk,name,inomarka = row
    CarFamily(pk=pk,name=name,inomarka=inomarka).save()


@loaddd(filename="data/autorepairs.csv")
def load_autorepairs(row):
    pk,name,about,rank,inomarki,russkie,address,telephone = [r.decode("utf-8") for r in row ]
    a = AutoRepair(pk=pk,name=name,about=about,rank=rank,inomarki=inomarki,
        russkie=russkie,address=address,telephone=telephone)
    a.save()

@loaddd(filename="data/repair_list.csv")
def load_repairs(row):
    pk,name,otdel,autorepair,about,price,carFamily_pk = [r.decode('utf-8') for r in row]
    Repair(pk=pk,name=name,otdel=otdel,autorepair=AutoRepair.objects.get(pk=autorepair),
        about=about,price=price, carFamily=CarFamily.objects.get(pk=carFamily_pk)).save()


def load_autorepairs():
    import os

    with open("data/autorepairs.csv",'rb') as f:
        #frodialect = csv.Dialect(delimiter)
        reader = csv.reader(f,delimiter=";",lineterminator=";")
        for row in reader:
            pass


def load_repairs():
    import csv
    with open("data/repair_list.csv",'rb') as f:
        reader = csv.reader(f,delimiter=";")
        for row in reader:
            pk,name,otdel,autorepair,about,price,carFamily_pk = [r.decode('utf-8') for r in row]
            Repair(pk=pk,name=name,otdel=otdel,autorepair=AutoRepair.objects.get(pk=autorepair),
                about=about,price=price, carFamily=CarFamily.objects.get(pk=carFamily_pk)).save()

def load_carFamily():
    import csv
    with open("data/carFamily.csv") as f:
        reader = csv.reader(f,delimiter=";")
        for row in reader:
            pk,name,inomarka = row
            CarFamily(pk=pk,name=name,inomarka=inomarka).save()


