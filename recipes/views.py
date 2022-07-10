
from django.shortcuts import render
from django.urls import path



def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': "Michel Clemer"
    })


