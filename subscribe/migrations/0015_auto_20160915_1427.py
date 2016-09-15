# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0014_auto_20160420_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_published', models.BooleanField(default=False)),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Abonnement'), (2, '\xc0 la pi\xe8ce')])),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ItemMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('is_shipped', models.BooleanField(default=False, verbose_name='envoy\xe9?')),
                ('item', models.ForeignKey(to='subscribe.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First name', blank=True)),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='courriel', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='payment statut', choices=[(0, 'encod\xe9'), (1, 'pay\xe9'), (2, 'annul\xe9')])),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('confirmation_date', models.DateTimeField(null=True, verbose_name='date de validation', blank=True)),
                ('invoice_reference', models.PositiveIntegerField(null=True, verbose_name='r\xe9f\xe9rence facture', blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('is_gift', models.BooleanField(default=False)),
                ('promo_code', models.CharField(max_length=255, blank=True)),
                ('comment', models.TextField(verbose_name='commentaire', blank=True)),
                ('items', models.ManyToManyField(to='subscribe.Item', through='subscribe.ItemMembership')),
            ],
            options={
                'verbose_name': 'commande',
                'verbose_name_plural': 'commandes',
            },
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First name', blank=True)),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='courriel', blank=True)),
                ('street', models.CharField(max_length=30, verbose_name='rue')),
                ('number', models.CharField(max_length=50, verbose_name='num\xe9ro')),
                ('letterbox', models.PositiveSmallIntegerField(null=True, verbose_name='bo\xeete postale', blank=True)),
                ('zip_code', models.PositiveSmallIntegerField(verbose_name='code postal')),
                ('city', models.CharField(max_length=30, verbose_name='ville')),
                ('country', models.CharField(default='BE', max_length=5, verbose_name='pays', choices=[('AL', 'Albanie'), ('PT-20', 'A\xe7ores'), ('DE', 'Allemagne'), ('AD', 'Andorre'), ('AT', 'Autriche'), ('BE', 'Belgique'), ('BY', 'Bi\xe9lorussie'), ('BA', 'Bosnie-Herz\xe9govine'), ('BG', 'Bulgarie'), ('IC', 'Canaries (\xceles)'), ('ES-CE', 'Ceuta'), ('CY', 'Chypre'), ('HR', 'Croatie'), ('DK', 'Danemark'), ('ES', 'Espagne'), ('EE', 'Estonie'), ('FO', 'F\xe9ro\xe9 (\xceles)'), ('FI', 'Finlande'), ('FR', 'France (sauf DOM-TOM)'), ('GE', 'G\xe9orgie'), ('GI', 'Gibraltar'), ('GB', 'Grande-Bretagne'), ('GR', 'Gr\xe8ce'), ('GL', 'Groenland'), ('GG', 'Guernesey'), ('HU', 'Hongrie'), ('IE', 'Irlande'), ('IS', 'Islande'), ('IT', 'Italie'), ('JE', 'Jersey'), ('LV', 'Lettonie'), ('LI', 'Liechtenstein'), ('LT', 'Lituanie'), ('LU', 'Luxembourg (Grand-Duch\xe9 de)'), ('MK', 'Mac\xe9doine'), ('PT-30', 'Mad\xe8re'), ('MT', 'Malte'), ('IM', 'Man (\xcele de)'), ('Me', 'Melilla'), ('MD', 'Moldavie'), ('MC', 'Monaco'), ('ME', 'Mont\xe9n\xe9gro'), ('NO', 'Norv\xe8ge'), ('NL', 'Pays-Bas'), ('PL', 'Pologne'), ('PT', 'Portugal'), ('CZ', 'R\xe9publique tch\xe8que'), ('RO', 'Roumanie'), ('RU', 'Russie'), ('SM', 'Saint-Martin'), ('RS', 'Serbie'), ('SK', 'Slovaquie'), ('SI', 'Slov\xe9nie'), ('SE', 'Su\xe8de'), ('CH', 'Suisse'), ('TR', 'Turquie'), ('UA', 'Ukraine'), ('VA', 'Vatican')])),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_details',
            field=models.ForeignKey(to='subscribe.ShippingDetails'),
        ),
        migrations.AddField(
            model_name='itemmembership',
            name='order',
            field=models.ForeignKey(to='subscribe.Order'),
        ),
    ]
