from django.contrib.auth import get_user_model
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from board_game.models import (AgeCategory, Game, Order, OrderItem,
                               PLayerCountCategory, Publisher, Series,
                               TimeCategory)


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "is_staff")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class SeriesSerializer(ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"


class AgeCategorySerializer(ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = "__all__"


class PLayerCountCategorySerializer(ModelSerializer):
    class Meta:
        model = PLayerCountCategory
        fields = "__all__"


class TimeCategorySerializer(ModelSerializer):
    class Meta:
        model = TimeCategory
        fields = "__all__"


class GameListSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameSerializer(ModelSerializer):
    time_spend = StringRelatedField()
    age_category = StringRelatedField()
    player_count = StringRelatedField()
    series = StringRelatedField()

    class Meta:
        model = Game
        fields = ("name", "price", "language", "description", "time_spend", "age_category", "player_count", "series")
