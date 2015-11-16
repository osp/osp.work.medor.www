# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0012_auto_20151116_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 16, 12, 59, 12, 676948, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='statut', choices=[(0, 'proposal'), (1, 'request for peer-review'), (2, 'request for spell-checking'), (3, 'ready')]),
            preserve_default=True,
        ),
    ]
