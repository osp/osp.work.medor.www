# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'statut', choices=[(0, 'proposal'), (1, 'request for peer-review'), (2, 'request for speelchecking'), (3, 'ready')]),
            preserve_default=True,
        ),
    ]
