# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0008_auto_20151106_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='number',
            field=models.CharField(max_length=50, verbose_name='num\xe9ro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='number',
            field=models.CharField(max_length=50, verbose_name='num\xe9ro'),
            preserve_default=True,
        ),
    ]
