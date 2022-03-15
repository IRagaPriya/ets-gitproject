from django.shortcuts import render
from django.http import HttpResponse
#create views here
def home(request):
    return HttpResponse("hello world")