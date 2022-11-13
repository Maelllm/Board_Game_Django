from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1.0)])
    language = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=2000, null=True)
    image = models.ImageField(null=True, upload_to="src/media/images", blank=True)
    series = models.ForeignKey(to="board_game.Series", related_name="game", on_delete=models.CASCADE)
    age_category = models.ForeignKey(to="board_game.AgeCategory", related_name="game", on_delete=models.CASCADE)
    player_count = models.ForeignKey(
        to="board_game.PLayerCountCategory", related_name="game", on_delete=models.CASCADE
    )
    time_spend = models.ForeignKey(to="board_game.TimeCategory", related_name="game", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Publisher(models.Model):
    publisher = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.publisher


class Series(models.Model):
    series = models.CharField(max_length=100)
    publisher = models.ForeignKey(to="board_game.Publisher", related_name="series", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "series"

    def __str__(self):
        return self.series


class AgeCategory(models.Model):
    age_category = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "age categories"

    def __str__(self):
        return self.age_category


class PLayerCountCategory(models.Model):
    player_count = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "player counting"

    def __str__(self):
        return self.player_count


class TimeCategory(models.Model):
    time_spend = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "time categories"

    def __str__(self):
        return self.time_spend


class Order(models.Model):
    customer = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, blank=True, null=True, related_name="order"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    @property
    def total_order_summary(self):
        orderitems = self.orderitem.all()
        total = sum([i.total_price for i in orderitems])
        return total

    @property
    def total_order_quantity(self):
        orderitems = self.orderitem.all()
        total = sum([i.quantity for i in orderitems])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(
        "board_game.Order", on_delete=models.SET_NULL, blank=True, null=True, related_name="orderitem"
    )
    quantity = models.SmallIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(
        "board_game.Game", on_delete=models.PROTECT, blank=True, null=True, related_name="orderitem"
    )

    @property
    def total_price(self):
        total = self.game.price * self.quantity
        return total

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
