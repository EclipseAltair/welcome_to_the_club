# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def create_checks(request):
    if request.POST:
        return HttpResponse({})


def new_checks(request):
    return HttpResponse({})


def check(request):
    return HttpResponse({})
