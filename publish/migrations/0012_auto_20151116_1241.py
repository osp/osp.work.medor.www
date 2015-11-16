# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0011_auto_20151116_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='in_toc',
            field=models.BooleanField(default=True, verbose_name='montr\xe9 dans le table de mati\xe8re'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='published_online',
            field=models.BooleanField(default=False, verbose_name='publi\xe9 en ligne'),
            preserve_default=True,
        ),
    ]
