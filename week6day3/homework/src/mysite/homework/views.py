from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def create_view(request):
    return HttpResponse("CREATE VIEW")


def details_view(request, id):
    return HttpResponse(f"DETAILS VIEW - Product ID: {id}")