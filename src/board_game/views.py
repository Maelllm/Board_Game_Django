from django.http import HttpResponse
from django.views.generic import ListView

from .models import AgeCategory, Game, Publisher, Series
from .tasks import generate_game, generate_order, generate_order_item


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


class GetAgeCategoryGamesView(ListView):
    model = AgeCategory
    template_name = "age_cat_games.html"
    context_object_name = "ac_games"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = AgeCategory.objects.get(pk=pk).game.all()
        return queryset


class GetAllAgeCategoryView(ListView):
    model = AgeCategory
    template_name = "age_categories.html"
    context_object_name = "age_categories"


def game_gen_view(request):
    generate_game.delay(amount=2)
    return HttpResponse("Task is started")


def order_gen_view(request):
    generate_order.delay(amount=5)
    return HttpResponse("Task is started")


def order_item_gen_view(request):
    generate_order_item.delay(amount=15)
    return HttpResponse("Task is started")
