# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0002_auto_20150122_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleproposal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 22, 17, 33, 35, 177003, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
