# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0033_auto_20171018_1423"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="registered_from",
            field=models.CharField(
                choices=[
                    ("Email", "Email"),
                    ("Social", "Social"),
                    ("Resume", "Resume"),
                    ("Bounces", "Bounces"),
                ],
                default="",
                max_length=10,
            ),
        ),
    ]
