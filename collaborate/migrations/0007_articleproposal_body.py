# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0006_auto_20150306_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleproposal',
            name='body',
            field=models.TextField(default='', verbose_name=b'Contenu', blank=True),
            preserve_default=False,
        ),
    ]
