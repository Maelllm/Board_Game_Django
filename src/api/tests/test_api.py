import os
from collections import OrderedDict
from unittest import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from board_game.models import (AgeCategory, Game, Order, OrderItem,
                               PLayerCountCategory, Publisher, Series,
                               TimeCategory)
from core.utils import sample_game, sample_order, sample_order_item


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = sample_game(name="apigame", price=100)
        self.order = sample_order()
        self.orderitem = sample_order_item(game=self.game, order=self.order, quantity=10)
        self.user = get_user_model().objects.create(email="apitest@test.com")
        self.user.set_password("test")
        self.user.save()

    def tearDown(self):
        self.game.orderitem.all().delete()
        self.game.delete()
        Game.objects.all().delete()
        self.order.delete()
        get_user_model().objects.all().delete()

    def test_game_list_authorized(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(reverse("api:game_detail", kwargs={"pk": self.game.pk}))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            {
                "name": "apigame",
                "price": "100.00",
                "time_spend": "",
                "age_category": "",
                "player_count": "",
                "series": "",
                "language": "English",
                "description": "test",
            },
        )

    def test_game_list_not_authorized(self):
        result = self.client.get(reverse("api:game_detail", kwargs={"pk": self.game.pk}))

        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_game_list_multiply(self):
        self.client.force_authenticate(user=self.user)
        self.game_2 = sample_game(name="apigame_2", price=50)
        self.game_3 = sample_game(name="apigame_3", price=5)

        result = self.client.get(reverse("api:game_all"))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            [
                OrderedDict(
                    [
                        ("name", "apigame"),
                        ("price", "100.00"),
                        ("language", "English"),
                        ("description", "test"),
                        ("time_spend", ""),
                        ("age_category", ""),
                        ("player_count", ""),
                        ("series", ""),
                    ]
                ),
                OrderedDict(
                    [
                        ("name", "apigame_2"),
                        ("price", "50.00"),
                        ("language", "English"),
                        ("description", "test"),
                        ("time_spend", ""),
                        ("age_category", ""),
                        ("player_count", ""),
                        ("series", ""),
                    ]
                ),
                OrderedDict(
                    [
                        ("name", "apigame_3"),
                        ("price", "5.00"),
                        ("language", "English"),
                        ("description", "test"),
                        ("time_spend", ""),
                        ("age_category", ""),
                        ("player_count", ""),
                        ("series", ""),
                    ]
                ),
            ],
        )

    def test_game_update_authorized(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.patch(path=reverse("api:game_detail", kwargs={"pk": self.game.pk}), data={"price": 50})

        self.assertEqual(
            result.data,
            {
                "name": "apigame",
                "price": "50.00",
                "time_spend": "",
                "age_category": "",
                "player_count": "",
                "series": "",
                "language": "English",
                "description": "test",
            },
        )

    def test_game_create_not_authorized(self):
        if os.environ.get("GITHUB_WORKFLOW"):
            pub = Publisher.objects.create(publisher="1")
            Series.objects.create(publisher=pub, series="1")
            AgeCategory.objects.create(age_category="1")
            TimeCategory.objects.create(time_spend="1")
            PLayerCountCategory.objects.create(player_count="1")

            result = self.client.post(
                path=reverse("api:game_create"),
                data={
                    "name": "apigame_created",
                    "price": 100,
                    "series": 10,
                    "age_category": 10,
                    "player_count": 10,
                    "time_spend": 10,
                    "language": "English",
                    "description": "some",
                },
            )
            self.assertEqual(
                result.data,
                {
                    "id": 7,
                    "name": "apigame_created",
                    "price": "100.00",
                    "time_spend": 10,
                    "age_category": 10,
                    "player_count": 10,
                    "series": 10,
                    "language": "English",
                    "description": "some",
                    "image": "http://testserver/media/images/default.webp",
                },
            )
        else:
            result = self.client.post(
                path=reverse("api:game_create"),
                data={
                    "name": "apigame_created",
                    "price": 100,
                    "series": 1,
                    "age_category": 1,
                    "player_count": 1,
                    "time_spend": 1,
                    "language": "English",
                    "description": "some",
                },
            )
            self.assertEqual(
                result.data,
                {
                    "id": 2,
                    "name": "apigame_created",
                    "price": "100.00",
                    "time_spend": 1,
                    "age_category": 1,
                    "player_count": 1,
                    "series": 1,
                    "language": "English",
                    "description": "some",
                    "image": "http://testserver/media/images/default.webp",
                },
            )
