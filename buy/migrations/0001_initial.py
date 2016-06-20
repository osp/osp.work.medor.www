# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RetailOutlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name=b'nom')),
                ('address', models.CharField(max_length=1024, verbose_name=b'adresse', blank=True)),
                ('zip_code', models.PositiveSmallIntegerField(null=True, verbose_name=b'code postal', blank=True)),
                ('city', models.CharField(max_length=1024, verbose_name=b'ville', blank=True)),
                ('country', models.CharField(max_length=1024, verbose_name=b'pays', blank=True)),
                ('latitude', models.FloatField(null=True, verbose_name=b'lattitude', blank=True)),
                ('longitude', models.FloatField(null=True, verbose_name=b'longitude', blank=True)),
            ],
            options={
                'verbose_name': 'Point de vente',
            },
        ),
    ]
