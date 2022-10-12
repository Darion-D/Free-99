from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
import requests


    
def home(request):
    games=requests.get('https://www.freetogame.com/api/games').json()
    return render(request, 'home.html', {'games': games})

    