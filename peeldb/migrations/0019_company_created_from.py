# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeldb', '0018_user_alternate_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_from',
            field=models.CharField(default='', max_length=200),
        ),
    ]
