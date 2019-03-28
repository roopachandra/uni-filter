# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from front.models import Institution

# Register your models here.
class InstitutionAdmin(admin.ModelAdmin):
	list_display = ('university_name', 'country', 'tuition', 'num_students')
	ordering=('university_name',)

admin.site.register(Institution, InstitutionAdmin)