from django.shortcuts import render
from django.http import HttpResponse
from app_contacto.models import Topic, Webpage, AccessRecord


# Create your views here.
def contacto(request):
    return render(request,"contacto.html",{})


def index(request):

    return render(request, "index.html", {})
