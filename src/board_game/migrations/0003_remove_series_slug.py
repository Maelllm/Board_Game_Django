# Generated by Django 4.1.3 on 2022-11-08 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board_game", "0002_alter_agecategory_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="series",
            name="slug",
        ),
    ]