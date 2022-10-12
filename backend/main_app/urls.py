from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('games/', views.GamesList.as_view(), name='games_list'),
    path('games/new', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game_detail'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='game_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='game_delete'),
]