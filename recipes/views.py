from django.http import HttpResponse
from django.urls import path



def home(request):
    return HttpResponse("HOME")


def contato(request):
    return HttpResponse("CONTATO")


def sobre(request):
    return HttpResponse("SOBRE")
