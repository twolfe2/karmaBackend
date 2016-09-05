from django.shortcuts import render

from django.http import HttpResponse

from pyfcm import FCMNotification

import os

fcm_key = str(os.environ.get('FCM_KEY'))
push_service = FCMNotification(api_key=fcm_key)
# Create your views here.

def index(request):
  return HttpResponse('hello from notifications')

def send(request):
  print request.method
  if request.type == 'POST':
    print request.POST
    registration_id = request.POST['registration_id']
    message_title = 'Application Accepted'
    message_body = 'Hi, your application has been recieved'
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print result
    return HttpResponse('notification sent to'+registration_id)
  return HttpResponse('Hello World')