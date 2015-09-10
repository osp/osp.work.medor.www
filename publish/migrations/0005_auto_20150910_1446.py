# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='peer_reviewers',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
    ]
