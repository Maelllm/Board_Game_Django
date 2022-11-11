from django.contrib import admin  # NOQA
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (GameAllView, GameCreateView, GameDeleteView,
                       GameUpdateView, UserViewSet)

app_name = "api"
routes = DefaultRouter()
routes.register("customers", UserViewSet)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("", include(routes.urls)),
    path("game/<int:pk>", GameUpdateView.as_view()),
    path("game/", GameAllView.as_view()),
    path("game/delete/<int:pk>", GameDeleteView.as_view()),
    path("game/create", GameCreateView.as_view()),
]
