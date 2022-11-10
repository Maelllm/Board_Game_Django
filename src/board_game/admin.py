from django.contrib import admin

from board_game.models import *  # NOQA

admin.site.register([Game, Publisher, Series, Order, OrderItem, AgeCategory, TimeCategory, PLayerCountCategory])
