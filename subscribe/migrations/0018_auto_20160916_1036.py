# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0017_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='organization',
            field=models.CharField(max_length=255, verbose_name='organisation', blank=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='box',
            field=models.CharField(max_length=64, verbose_name='bo\xeete', blank=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='postcode',
            field=models.CharField(max_length=64, verbose_name='code postal', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='est publi\xe9?'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(verbose_name='prix', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(verbose_name='type de transaction', choices=[(1, 'Abonnement'), (2, '\xc0 la pi\xe8ce')]),
        ),
        migrations.AlterField(
            model_name='itemmembership',
            name='item',
            field=models.ForeignKey(verbose_name='item', to='subscribe.Item'),
        ),
        migrations.AlterField(
            model_name='itemmembership',
            name='order',
            field=models.ForeignKey(verbose_name='commande', to='subscribe.Order'),
        ),
        migrations.AlterField(
            model_name='itemmembership',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='quantit\xe9'),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(null=True, verbose_name='total', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='confirmation_date',
            field=models.DateTimeField(null=True, verbose_name='date de validation du payement', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="date d'encodage"),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='pr\xe9nom', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_gift',
            field=models.BooleanField(default=False, verbose_name='ceci est un cadeau'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='subscribe.Item', verbose_name='items', through='subscribe.ItemMembership'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='nom', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='promo_code',
            field=models.CharField(max_length=255, verbose_name='code promo', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_details',
            field=models.ForeignKey(verbose_name='Adresse de livraison', to='subscribe.ShippingDetails'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='statut du payement', choices=[(0, 'encod\xe9'), (1, 'pay\xe9'), (2, 'annul\xe9')]),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='city',
            field=models.CharField(max_length=255, verbose_name='ville'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='pr\xe9nom', blank=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='nom', blank=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='letterbox',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='bo\xeete', blank=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='number',
            field=models.CharField(max_length=64, verbose_name='num\xe9ro'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='street',
            field=models.CharField(max_length=255, verbose_name='rue'),
        ),
    ]
