# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('publish', '0028_contributor_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='is_team',
            field=models.BooleanField(default='False'),
        ),
    ]
