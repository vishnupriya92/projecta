from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome to india")

def home(request):
    return HttpResponse("welcome to E-city")


def page1(request):
    return HttpResponse("welcome to bangl")

def page2(request):
    return HttpResponse("welcome to karnataka")




    