from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are the projects')

def project(request, pk):
    return HttpResponse('Single projects' + " " + str(pk))