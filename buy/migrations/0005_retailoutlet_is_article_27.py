# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-03 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_auto_20171013_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailoutlet',
            name='is_article_27',
            field=models.BooleanField(default=False, verbose_name='is article 27?'),
        ),
    ]
