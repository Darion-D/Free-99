from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Game, FavoritesList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gameslist"] = FavoritesList.objects.all()
        return context

class About(TemplateView):
    template_name = 'about.html'


class GamesList(TemplateView):
    template_name = 'games_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('title')
        if name !=None:
            context['games'] = Game.objects.filter(title__icontains=name)
            context['header'] = f'Serching for {name}'
        else:
            context['games'] = Game.objects.all()
            context['header'] = f'Trending Games'
        return context

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'thumbnail', 'description', 'game_url', 'genre', 'platform', 'publisher', 'developer', 'release_date']
    template_name = 'game_create.html'
    def get_success_url(self):
        return reverse('game_detail', kwargs={'pk': self.object.pk})

class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favlist"] = FavoritesList.objects.all()
        return context

class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'thumbnail', 'description', 'game_url', 'genre', 'platform', 'publisher', 'developer', 'release_date']
    template_name = 'game_update.html'
    def get_success_url(self):
        return reverse('game_detail', kwargs={'pk': self.object.pk})

class GameDelete(DeleteView):
    model=Game
    template_name = 'game_delete_confirmation.html'
    success_url = '/games/'

class FavListGameAssoc(View):

    def get(self, request, pk, game_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            FavoritesList.objects.get(pk=pk).games.remove(game_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            FavoritesList.objects.get(pk=pk).games.add(game_pk)
        return redirect('home')
