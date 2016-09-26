# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0024_auto_20160921_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'Produit', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AlterModelOptions(
            name='itemmembership',
            options={'verbose_name': 'Ligne de commande', 'verbose_name_plural': 'Lignes de commandes'},
        ),
        migrations.AlterModelOptions(
            name='shippingdetails',
            options={'verbose_name': 'Coordonn\xe9es de livraison', 'verbose_name_plural': 'Coordonn\xe9es de livraison'},
        ),
    ]
