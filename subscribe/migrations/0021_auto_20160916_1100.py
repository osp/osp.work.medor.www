# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0020_auto_20160916_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='courriel'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='pr\xe9nom'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='courriel'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='pr\xe9nom'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='postcode',
            field=models.CharField(max_length=64, verbose_name='code postal'),
        ),
    ]
