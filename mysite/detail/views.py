# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(requests):
    return render(requests, 'detail/detail.html')
