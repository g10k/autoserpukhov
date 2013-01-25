# -*- encoding: utf-8 -*-
__author__ = 'Сергей'

from autocenter.models import AutoCenter,AutoCenterImage
from django.contrib import admin

class AutoCenterImageAdmin(admin.TabularInline):
    model = AutoCenterImage
    extra = 3

class AutoCenterAdmin(admin.ModelAdmin):
    inlines = [AutoCenterImageAdmin]


#admin.site.register(AutoCenterImage,AutoCenterImageAdmin)
admin.site.register(AutoCenter,AutoCenterAdmin)




