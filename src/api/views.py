from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializer import (CustomerSerializer, GameListSerializer,
                            GameSerializer)
from board_game.models import Game


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class GameCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameAllView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameUpdateView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDeleteView(RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
