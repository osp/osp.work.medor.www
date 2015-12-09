# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0009_auto_20151106_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='from_issue',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\xe0 partir du num\xe9ro', blank=True),
            preserve_default=True,
        ),
    ]
