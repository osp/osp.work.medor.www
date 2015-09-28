# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0007_auto_20150918_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
    ]
