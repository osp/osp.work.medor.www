# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0026_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('email', models.EmailField(max_length=254, verbose_name='courriel')),
                ('offer', models.ForeignKey(to='subscribe.Offer')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='promo_code',
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='order',
            field=models.ForeignKey(to='subscribe.Order'),
        ),
    ]
