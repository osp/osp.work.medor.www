# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-27 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0027_auto_20161017_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingdetails',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Coordonn\xe9es de livraison', 'verbose_name_plural': 'Coordonn\xe9es de livraison'},
        ),
    ]
