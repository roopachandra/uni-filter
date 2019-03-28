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
            students = form.cleaned_data['stud']
            tuition = form.cleaned_data['tuit']
            return HttpResponseRedirect('/'+ location + '/' + students + '/' + tuition +'/results')
    else:
        form = choiceform()

    return render(requests, 'front/home.html', {'form' : form})

def detail(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    return render(request, 'detail/detail.html', {'institution': institution})

def results(request,location,students,tuition):
    filtered_institutions = Institution.objects.all().order_by('university_name')
    if location != 'NA':
        filtered_institutions = filtered_institutions.filter(country = location)
    if (students != 'any'):
        if (students == 'small'):
            filtered_institutions = filtered_institutions.filter(num_students__lte = 5000)
        elif (students == 'med'):
            filtered_institutions = filtered_institutions.filter(num_students__lte = 15000, num_students__gte = 5000)
        elif (students == 'large'):
            filtered_institutions = filtered_institutions.filter(num_students__gte = 5000)
    if (tuition != 'all'):
        if (tuition == 'less'):
            filtered_institutions = filtered_institutions.filter(tuition__lte = 15000)
        elif (tuition == 'midless'):
            filtered_institutions = filtered_institutions.filter(tuition__lte = 30000, tuition__gte = 15000)
        elif (tuition == 'midmore'):
            filtered_institutions = filtered_institutions.filter(tuition__lte = 45000, tuition__gte = 30000)
        elif (tuition == 'more'):
            filtered_institutions = filtered_institutions.filter(tuition__gte = 45000)
    context = {'filtered_institutions': filtered_institutions}
    return render(request, 'list/list.html', context)
