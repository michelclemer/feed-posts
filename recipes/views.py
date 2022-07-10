from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path



def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse("CONTATO")


def sobre(request):
    return HttpResponse("SOBRE")
