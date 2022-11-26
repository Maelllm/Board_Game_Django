from django.shortcuts import render
from django.views.generic import ListView

from .models import Game, Publisher, Series


class GetAllGamesView(ListView):
    model = Game
    template_name = "all_games.html"
    context_object_name = "games"


class GetAllPublishersView(ListView):
    model = Publisher
    template_name = "all_publishers.html"
    context_object_name = "publishers"


class GetPublisherSeriesView(ListView):
    model = Publisher
    template_name = "pub_series.html"
    context_object_name = "publishers_series"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = Publisher.objects.get(pk=pk).series.all()
        return queryset


class GetSeriesGamesView(ListView):
    model = Series
    template_name = "series_games.html"
    context_object_name = "series_games"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = Series.objects.get(pk=pk).game.all()
        return queryset
