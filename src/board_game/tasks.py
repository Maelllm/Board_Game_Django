import random

from celery import shared_task
from django.contrib.auth import get_user_model
from faker import Faker

from board_game.models import (AgeCategory, Game, Order, OrderItem,
                               PLayerCountCategory, Series, TimeCategory)


@shared_task
def generate_game(amount):
    fake = Faker("en_US")
    for i in range(amount):
        Game.objects.create(
            name=Faker().unique.company(),
            price=random.randint(10, 5000),
            language="English",
            description=fake.catch_phrase(),
            series=Series.objects.get(pk=random.randint(2, 5)),
            age_category=AgeCategory.objects.get(pk=random.randint(1, 5)),
            player_count=PLayerCountCategory.objects.get(pk=random.randint(1, 5)),
            time_spend=TimeCategory.objects.get(pk=random.randint(1, 4)),
        )


@shared_task
def generate_order(amount):
    fake = Faker("en_US")
    for i in range(amount):
        Order.objects.create(
            customer=get_user_model().objects.get(pk=1), order_date=fake.date(), complete=random.choice([True, False])
        )


@shared_task
def generate_order_item(amount):
    fake = Faker("en_US")
    for i in range(amount):
        OrderItem.objects.create(
            order=Order.objects.get(pk=random.randint(1, len(Order.objects.all()))),
            quantity=random.randint(1, 50),
            created_date=fake.date(),
            game=Game.objects.get(pk=(random.randint(1, 15))),
        )
