# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_gift',
            field=models.BooleanField(default=False, verbose_name=b'ceci est un cadeau?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='recipient_email',
            field=models.CharField(default='', max_length=30, verbose_name=b'courriel du destinataire', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='recipient_first_name',
            field=models.CharField(default='', max_length=30, verbose_name=b'pr\xc3\xa9nom du destinataire', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='recipient_last_name',
            field=models.CharField(default='', max_length=30, verbose_name=b'nom de famille du destinataire', blank=True),
            preserve_default=False,
        ),
    ]
