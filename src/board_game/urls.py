from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from board_game.views import (GetAgeCategoryGamesView, GetAllAgeCategoryView,
                              GetAllGamesView, GetAllPublishersView,
                              GetPublisherSeriesView, GetSeriesGamesView,
                              game_gen_view, order_gen_view,
                              order_item_gen_view)
from core.views import PageNotFoundView

app_name = "board_game"

urlpatterns = [
    path("", GetAllGamesView.as_view(), name="all_games"),
    path("publishers/", GetAllPublishersView.as_view(), name="publishers"),
    path("publishers/<int:pk>", GetPublisherSeriesView.as_view(), name="publishers_series"),
    path("publishers/series/<int:pk>", GetSeriesGamesView.as_view(), name="series_games"),
    path("plct/", PageNotFoundView.as_view(), name="playercount"),
    path("age/", GetAllAgeCategoryView.as_view(), name="age_category"),
    path("age/<int:pk>", GetAgeCategoryGamesView.as_view(), name="age_cat_games"),
    path("time/", PageNotFoundView.as_view(), name="time"),
    path("test/game/", game_gen_view, name="test_game"),
    path("test/order/", order_gen_view, name="test_order"),
    path("test/orderitem/", order_item_gen_view, name="test_order_item"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
