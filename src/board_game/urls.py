from django.contrib import admin
from django.urls import path

from core.views import PageNotFoundView

app_name = "board_game"

urlpatterns = [
    path("", PageNotFoundView.as_view(), name="all_games"),
    path("publishers/", PageNotFoundView.as_view(), name="publishers"),
    path("series/", PageNotFoundView.as_view(), name="series"),
    path("plct/", PageNotFoundView.as_view(), name="playercount"),
    path("age/", PageNotFoundView.as_view(), name="age"),
    path("time/", PageNotFoundView.as_view(), name="time"),
]
