from django.shortcuts import render
from django_app.models import Blockedusers


def showdata(request):
    resultsdisplay = Blockedusers.objects.all()
    return render(request , "index.html" ,{"Blockedusers" : resultsdisplay})
