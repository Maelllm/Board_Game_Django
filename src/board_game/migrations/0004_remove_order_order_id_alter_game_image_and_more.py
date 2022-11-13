# Generated by Django 4.1.3 on 2022-11-09 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("board_game", "0003_remove_series_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_id",
        ),
        migrations.AlterField(
            model_name="game",
            name="image",
            field=models.ImageField(null=True, upload_to="src/media/images"),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="order",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="game",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orderitem",
                to="board_game.game",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orderitem",
                to="board_game.order",
            ),
        ),
    ]