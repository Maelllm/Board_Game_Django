from datetime import datetime  # NOQA

from board_game.models import *  # NOQA


def sample_game(name, price, **params):
    publisher = Publisher.objects.create()
    defaults = {
        "language": "English",
        "description": "test",
        "series": Series.objects.create(publisher=publisher),
        "age_category": AgeCategory.objects.create(),
        "player_count": PLayerCountCategory.objects.create(),
        "time_spend": TimeCategory.objects.create(),
    }
    defaults.update(params)
    return Game.objects.create(name=name, price=price, **defaults)


def sample_order(**params):
    defaults = {
        "customer": get_user_model().objects.create(),
        "order_date": datetime.now(),
        "complete": False,
    }
    defaults.update(params)
    return Order.objects.create(**defaults)


def sample_order_item(game, order, quantity, **params):
    defaults = {
        "created_date": datetime.now(),
    }
    defaults.update(params)
    return OrderItem.objects.create(game=game, order=order, quantity=quantity, **defaults)
