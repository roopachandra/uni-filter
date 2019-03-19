# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from front.models import Institution

def index(requests):
    return render(requests, 'front/home.html')
    
def detail(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    return render(request, 'detail/detail.html', {'institution': institution})

def results(request):
    filtered_institutions = Institution.objects.all()
    context = {'filtered_institutions': filtered_institutions}
    return render(request, 'list/list.html', context)