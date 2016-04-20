# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0013_auto_20160420_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='courriel'),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, verbose_name='r\xe9f\xe9rence facture', blank=True),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='letterbox',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='bo\xeete postale', blank=True),
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='zip_code',
            field=models.PositiveSmallIntegerField(verbose_name='code postal'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='courriel'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, verbose_name='r\xe9f\xe9rence facture', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='letterbox',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='bo\xeete postale', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='zip_code',
            field=models.PositiveSmallIntegerField(verbose_name='code postal'),
        ),
    ]
