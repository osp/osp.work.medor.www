# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0005_auto_20150910_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 12, 53, 9, 400593, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 12, 53, 13, 875291, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
