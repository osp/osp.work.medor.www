# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('subscribe', '0016_auto_20160915_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
    ]
