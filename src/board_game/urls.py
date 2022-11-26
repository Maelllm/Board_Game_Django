from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from board_game.views import (GetAllGamesView, GetAllPublishersView,
                              GetPublisherSeriesView, GetSeriesGamesView)
from core.views import PageNotFoundView

app_name = "board_game"

urlpatterns = [
    path("", GetAllGamesView.as_view(), name="all_games"),
    path("publishers/", GetAllPublishersView.as_view(), name="publishers"),
    path("publishers/<int:pk>", GetPublisherSeriesView.as_view(), name="publishers_series"),
    path("publishers/series/<int:pk>", GetSeriesGamesView.as_view(), name="series_games"),
    path("plct/", PageNotFoundView.as_view(), name="playercount"),
    path("age/", PageNotFoundView.as_view(), name="age"),
    path("time/", PageNotFoundView.as_view(), name="time"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
