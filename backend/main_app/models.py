from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100, default='Darion')
    thumbnail = models.CharField(max_length=5000, default='Darion')
    description = models.TextField(max_length=5000, default='Darion')
    game_url = models.CharField(max_length=5000, default='Darion')
    genre = models.CharField(max_length=5000, default='Darion')
    platform = models.CharField(max_length=5000, default='Darion')
    publisher = models.CharField(max_length=5000, default='Darion')
    developer = models.CharField(max_length=5000, default='Darion')
    release_date = models.CharField(max_length=5000, default='Darion')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']