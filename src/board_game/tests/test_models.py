from django.core.exceptions import ValidationError
from django.test import TestCase

from board_game.models import *  # NOQA
from core.utils import sample_game, sample_order, sample_order_item


class TestBoardGameModel(TestCase):
    def setUp(self):
        self.game = sample_game(name="first", price=10)
        self.order = sample_order()
        self.orderitem = sample_order_item(game=self.game, order=self.order, quantity=5)

    def tearDown(self):
        self.game.orderitem.all().delete()
        self.game.delete()
        self.order.delete()

    def test_game_validation(self):
        with self.assertRaises(ValidationError):
            self.game = sample_game(name="t" * 500, price=20)
        with self.assertRaises(ValidationError):
            self.game = sample_game(name="test", price=3.544)

    def test_order_summary(self):
        self.game_1 = sample_game(name="test", price=5)
        self.orderitem_1 = sample_order_item(game=self.game_1, order=self.order, quantity=4)

        self.assertEqual(self.order.total_order_quantity, 9)
        self.assertEqual(self.order.total_order_summary, 70)

        self.game_1.price = 10
        self.orderitem_1.quantity = 50
        self.orderitem_1.save()
        self.game_1.save()

        self.assertEqual(self.order.total_order_quantity, 55)
        self.assertEqual(self.order.total_order_summary, 550)

    def test_orderitem_total(self):
        self.orderitem_2 = sample_order_item(game=self.game, order=self.order, quantity=100)
        self.assertEqual(self.orderitem_2.total_price, 1000)
        self.orderitem_2.quantity = 1
        self.assertEqual(self.orderitem_2.total_price, 10)
        self.orderitem_2.quantity = 0
        self.assertEqual(self.orderitem_2.total_price, 0)

    def test_negative(self):
        with self.assertRaises(ValidationError):
            self.orderitem = sample_order_item(game=self.game, order=self.order, quantity=-5)
        with self.assertRaises(ValidationError):
            self.game = sample_game(name="first", price=-10)
        with self.assertRaises(ValidationError):
            self.game.price = -5
            self.game.save()
