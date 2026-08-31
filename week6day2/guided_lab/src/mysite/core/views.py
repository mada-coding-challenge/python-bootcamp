from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    return HttpResponse(
    "Welcome to Django!"
    )


def about(request):
    return HttpResponse(
    "about"
    )
    

def contact(request):
    return HttpResponse(
    "contact"
    )
# Create your views here.
