# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0010_auto_20151008_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='publish_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='slug',
            field=models.SlugField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
    ]
