# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlemembership',
            name='page_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
