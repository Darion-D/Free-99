from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('games/', views.GamesList.as_view(), name='games_list'),
    path('games/new', views.GameCreate.as_view(), name='game_create'),
]