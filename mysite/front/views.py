# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from front.models import Institution
from .forms import *

def index(requests):
    if requests.method == 'POST':
        form = choiceform(requests.POST)
        if form.is_valid():
            location = form.cleaned_data['loc']
            degree = form.cleaned_data['deg']
            subject = form.cleaned_data['sub']
            return HttpResponseRedirect('/'+ location + '/' + degree + '/' + subject +'/results')
    else:
        form = choiceform()

    return render(requests, 'front/home.html', {'form' : form})

def detail(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    return render(request, 'detail/detail.html', {'institution': institution})

def results(request,location,degree,subject):
    filtered_institutions = Institution.objects.all()
    context = {'filtered_institutions': filtered_institutions}
    return render(request, 'list/list.html', context)
