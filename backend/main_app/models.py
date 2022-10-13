from operator import mod
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=5000)
    description = models.TextField(max_length=5000)
    game_url = models.CharField(max_length=5000)
    genre = models.CharField(max_length=5000)
    platform = models.CharField(max_length=5000)
    publisher = models.CharField(max_length=5000)
    developer = models.CharField(max_length=500)
    release_date = models.CharField(max_length=5000)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class FavoritesList(models.Model):
    title = models.CharField(max_length=150)
    games = models.ManyToManyField(Game)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title