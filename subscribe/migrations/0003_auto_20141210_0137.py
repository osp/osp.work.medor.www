# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_auto_20141208_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='recipient_title',
            field=models.BooleanField(default=False, verbose_name=b'civilit\xc3\xa9 du destinataire', choices=[(False, 'Madame'), (True, 'Monsieur')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'nom'),
            preserve_default=True,
        ),
    ]
