# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20151119_0855'),
        ('publish', '0015_articlemembershipweb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlemembershipweb',
            options={'ordering': ('order',), 'verbose_name': 'timeline', 'verbose_name_plural': 'timeline'},
        ),
        migrations.AddField(
            model_name='article',
            name='override_image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='sp\xe9cifier image aper\xe7u', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
