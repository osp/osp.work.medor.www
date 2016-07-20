# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0023_auto_20160714_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemembership',
            name='slug',
            field=models.SlugField(max_length=1024, blank=True),
        ),
    ]
