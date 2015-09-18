# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import publish.models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0006_auto_20150910_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(default=publish.models.body_default, blank=True),
            preserve_default=True,
        ),
    ]
