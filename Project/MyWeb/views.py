# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import News
from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'author': 'Sakshi',
        'title': 'News 1',
        'content': 'First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Vishal',
        'title': 'News 2',
        'content': 'Second content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'MyWeb/home.html',context)


def about(request):
	return HttpResponse('<h1>About</h1>')
