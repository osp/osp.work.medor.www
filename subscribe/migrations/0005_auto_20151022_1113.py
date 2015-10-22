# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_auto_20150120_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, max_length=10, verbose_name=b'r\xc3\xa9f\xc3\xa9rence facture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, max_length=10, verbose_name=b'r\xc3\xa9f\xc3\xa9rence facture', blank=True),
            preserve_default=True,
        ),
    ]
