# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0013_auto_20151116_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='override_description',
            field=models.TextField(default='', verbose_name='exergue sp\xe9cifique pour le web', blank=True),
            preserve_default=False,
        ),
    ]
