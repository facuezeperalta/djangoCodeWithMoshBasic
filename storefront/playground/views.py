from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request --> response.
#request handler.
#action
#here in djando is call views. Its not what the user sees, here en djando is call template.

def say_hello(request):
    #pull data of a database.
    #send emails, etc.
    return HttpResponse('Hello world')
