from django.contrib import admin  # NOQA
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import (GameAllView, GameCreateView, GameDeleteView,
                       GameUpdateView, UserViewSet)

app_name = "api"
routes = DefaultRouter()
routes.register("customers", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quizez API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
    path("", include(routes.urls)),
    path("game/<int:pk>", GameUpdateView.as_view(), name="game_detail"),
    path("game/", GameAllView.as_view(), name="game_all"),
    path("game/delete/<int:pk>", GameDeleteView.as_view()),
    path("game/create", GameCreateView.as_view(), name="game_create"),
]
