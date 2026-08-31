from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
    


def faq(request):
    return render(request, "faq.html")
    

def team(request):
    return render(request, "team.html")