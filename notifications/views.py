from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
  return HttpResponse('hello from notifications')

def send(request):
  print request.method
  print request.POST
  return HttpResponse('hello from send')