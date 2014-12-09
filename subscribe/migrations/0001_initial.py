# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.BooleanField(default=False, verbose_name=b'civilit\xc3\xa9', choices=[(False, 'Madame'), (True, 'Monsieur')])),
                ('first_name', models.CharField(max_length=30, verbose_name=b'pr\xc3\xa9nom')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'nom de famille')),
                ('email', models.EmailField(max_length=75, verbose_name=b'courriel')),
                ('street', models.CharField(max_length=30, verbose_name=b'rue')),
                ('number', models.CharField(max_length=10, verbose_name=b'num\xc3\xa9ro')),
                ('letterbox', models.PositiveSmallIntegerField(max_length=30, null=True, verbose_name=b'bo\xc3\xaete postale', blank=True)),
                ('city', models.CharField(max_length=30, verbose_name=b'ville')),
                ('zip_code', models.PositiveSmallIntegerField(max_length=5, verbose_name=b'code postal')),
                ('country', models.CharField(default=b'BE', max_length=2, verbose_name=b'pays', choices=[(b'BE', 'Belgique')])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name=b'statut', choices=[(0, 'en cours'), (1, 'confirm\xe9'), (2, 'annul\xe9')])),
                ('invoice_reference', models.PositiveIntegerField(unique=True, max_length=10, verbose_name=b'r\xc3\xa9f\xc3\xa9rence facture')),
                ('share_number', models.PositiveSmallIntegerField(default=b'1', verbose_name=b'nombre de parts', choices=[(1, '1 (\u20ac 20)'), (2, '2 (\u20ac 40)'), (3, '3 (\u20ac 60)'), (4, '4 (\u20ac 80)'), (5, '5 (\u20ac 100)'), (6, '6 (\u20ac 120)'), (7, '7 (\u20ac 140)'), (8, '8 (\u20ac 160)'), (9, '9 (\u20ac 180)'), (10, '10 (\u20ac 200)'), (11, '11 (\u20ac 220)'), (12, '12 (\u20ac 240)'), (13, '13 (\u20ac 260)'), (14, '14 (\u20ac 280)'), (15, '15 (\u20ac 300)'), (16, '16 (\u20ac 320)'), (17, '17 (\u20ac 340)'), (18, '18 (\u20ac 360)'), (19, '19 (\u20ac 380)'), (20, '20 (\u20ac 400)'), (50, '50 (\u20ac 1000)')])),
            ],
            options={
                'verbose_name': 'part coop\xe9rative',
                'verbose_name_plural': 'parts coop\xe9rative',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.BooleanField(default=False, verbose_name=b'civilit\xc3\xa9', choices=[(False, 'Madame'), (True, 'Monsieur')])),
                ('first_name', models.CharField(max_length=30, verbose_name=b'pr\xc3\xa9nom')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'nom de famille')),
                ('email', models.EmailField(max_length=75, verbose_name=b'courriel')),
                ('street', models.CharField(max_length=30, verbose_name=b'rue')),
                ('number', models.CharField(max_length=10, verbose_name=b'num\xc3\xa9ro')),
                ('letterbox', models.PositiveSmallIntegerField(max_length=30, null=True, verbose_name=b'bo\xc3\xaete postale', blank=True)),
                ('city', models.CharField(max_length=30, verbose_name=b'ville')),
                ('zip_code', models.PositiveSmallIntegerField(max_length=5, verbose_name=b'code postal')),
                ('country', models.CharField(default=b'BE', max_length=2, verbose_name=b'pays', choices=[(b'BE', 'Belgique')])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name=b'statut', choices=[(0, 'en cours'), (1, 'confirm\xe9'), (2, 'annul\xe9')])),
                ('invoice_reference', models.PositiveIntegerField(unique=True, max_length=10, verbose_name=b'r\xc3\xa9f\xc3\xa9rence facture')),
            ],
            options={
                'verbose_name': 'abonnement',
                'verbose_name_plural': 'abonnements',
            },
            bases=(models.Model,),
        ),
    ]
