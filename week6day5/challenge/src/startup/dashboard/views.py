from django.shortcuts import render


def home(request):
    return render(request, "dashboard/home.html")


def reports(request):
    return render(request, "dashboard/reports.html")