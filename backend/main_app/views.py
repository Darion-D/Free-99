from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Game:
    def __init__(self, title, thumbnail, description):
        self.title = title
        self.thumbnail = thumbnail
        self.description = description

class GamesList(TemplateView):
    template_name = 'games_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = games
        return context

games = [
    Game('Overwatch 2', 'https://www.freetogame.com/g/540/thumbnail.jpg', 'A hero-focused first-person team shooter from Blizzard Entertainment.'),
    Game('Diablo Immortal', 'https://www.freetogame.com/g/521/thumbnail.jpg', 'Built for mobile and also released on PC, Diablo Immortal fills in the gaps between Diablo II and III in an MMOARPG environment.')

]
