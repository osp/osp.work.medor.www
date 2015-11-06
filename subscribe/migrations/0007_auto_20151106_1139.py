# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0006_auto_20151022_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperation',
            name='confirmation_date',
            field=models.DateTimeField(null=True, verbose_name='date de confirmation du paiement', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='confirmation_date',
            field=models.DateTimeField(null=True, verbose_name='date de confirmation du paiement', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='country',
            field=models.CharField(default='BE', max_length=5, verbose_name='pays', choices=[('AL', 'Albanie'), ('PT-20', 'A\xe7ores'), ('DE', 'Allemagne'), ('AD', 'Andorre'), ('AT', 'Autriche'), ('BE', 'Belgique'), ('BY', 'Bi\xe9lorussie'), ('BA', 'Bosnie-Herz\xe9govine'), ('BG', 'Bulgarie'), ('IC', 'Canaries (\xceles)'), ('ES-CE', 'Ceuta'), ('CY', 'Chypre'), ('HR', 'Croatie'), ('DK', 'Danemark'), ('ES', 'Espagne'), ('EE', 'Estonie'), ('FO', 'F\xe9ro\xe9 (\xceles)'), ('FI', 'Finlande'), ('FR', 'France (sauf DOM-TOM)'), ('GE', 'G\xe9orgie'), ('GI', 'Gibraltar'), ('GB', 'Grande-Bretagne'), ('GR', 'Gr\xe8ce'), ('GL', 'Groenland'), ('GG', 'Guernesey'), ('HU', 'Hongrie'), ('IE', 'Irlande'), ('IS', 'Islande'), ('IT', 'Italie'), ('JE', 'Jersey'), ('LV', 'Lettonie'), ('LI', 'Liechtenstein'), ('LT', 'Lituanie'), ('LU', 'Luxembourg (Grand-Duch\xe9 de)'), ('MK', 'Mac\xe9doine'), ('PT-30', 'Mad\xe8re'), ('MT', 'Malte'), ('IM', 'Man (\xcele de)'), ('Me', 'Melilla'), ('MD', 'Moldavie'), ('MC', 'Monaco'), ('ME', 'Mont\xe9n\xe9gro'), ('NO', 'Norv\xe8ge'), ('NL', 'Pays-Bas'), ('PL', 'Pologne'), ('PT', 'Portugal'), ('CZ', 'R\xe9publique tch\xe8que'), ('RO', 'Roumanie'), ('RU', 'Russie'), ('SM', 'Saint-Martin'), ('RS', 'Serbie'), ('SK', 'Slovaquie'), ('SI', 'Slov\xe9nie'), ('SE', 'Su\xe8de'), ('CH', 'Suisse'), ('TR', 'Turquie'), ('UA', 'Ukraine'), ('VA', 'Vatican')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='pr\xe9nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, max_length=10, verbose_name='r\xe9f\xe9rence facture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='letterbox',
            field=models.PositiveSmallIntegerField(max_length=30, null=True, verbose_name='bo\xeete postale', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='number',
            field=models.CharField(max_length=10, verbose_name='num\xe9ro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='title',
            field=models.BooleanField(default=False, verbose_name='civilit\xe9', choices=[(False, 'Madame'), (True, 'Monsieur')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='country',
            field=models.CharField(default='BE', max_length=5, verbose_name='pays', choices=[('AL', 'Albanie'), ('PT-20', 'A\xe7ores'), ('DE', 'Allemagne'), ('AD', 'Andorre'), ('AT', 'Autriche'), ('BE', 'Belgique'), ('BY', 'Bi\xe9lorussie'), ('BA', 'Bosnie-Herz\xe9govine'), ('BG', 'Bulgarie'), ('IC', 'Canaries (\xceles)'), ('ES-CE', 'Ceuta'), ('CY', 'Chypre'), ('HR', 'Croatie'), ('DK', 'Danemark'), ('ES', 'Espagne'), ('EE', 'Estonie'), ('FO', 'F\xe9ro\xe9 (\xceles)'), ('FI', 'Finlande'), ('FR', 'France (sauf DOM-TOM)'), ('GE', 'G\xe9orgie'), ('GI', 'Gibraltar'), ('GB', 'Grande-Bretagne'), ('GR', 'Gr\xe8ce'), ('GL', 'Groenland'), ('GG', 'Guernesey'), ('HU', 'Hongrie'), ('IE', 'Irlande'), ('IS', 'Islande'), ('IT', 'Italie'), ('JE', 'Jersey'), ('LV', 'Lettonie'), ('LI', 'Liechtenstein'), ('LT', 'Lituanie'), ('LU', 'Luxembourg (Grand-Duch\xe9 de)'), ('MK', 'Mac\xe9doine'), ('PT-30', 'Mad\xe8re'), ('MT', 'Malte'), ('IM', 'Man (\xcele de)'), ('Me', 'Melilla'), ('MD', 'Moldavie'), ('MC', 'Monaco'), ('ME', 'Mont\xe9n\xe9gro'), ('NO', 'Norv\xe8ge'), ('NL', 'Pays-Bas'), ('PL', 'Pologne'), ('PT', 'Portugal'), ('CZ', 'R\xe9publique tch\xe8que'), ('RO', 'Roumanie'), ('RU', 'Russie'), ('SM', 'Saint-Martin'), ('RS', 'Serbie'), ('SK', 'Slovaquie'), ('SI', 'Slov\xe9nie'), ('SE', 'Su\xe8de'), ('CH', 'Suisse'), ('TR', 'Turquie'), ('UA', 'Ukraine'), ('VA', 'Vatican')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='pr\xe9nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='invoice_reference',
            field=models.PositiveIntegerField(unique=True, max_length=10, verbose_name='r\xe9f\xe9rence facture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='letterbox',
            field=models.PositiveSmallIntegerField(max_length=30, null=True, verbose_name='bo\xeete postale', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='number',
            field=models.CharField(max_length=10, verbose_name='num\xe9ro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='recipient_first_name',
            field=models.CharField(max_length=30, verbose_name='pr\xe9nom du destinataire', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='recipient_title',
            field=models.BooleanField(default=False, verbose_name='civilit\xe9 du destinataire', choices=[(False, 'Madame'), (True, 'Monsieur')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='title',
            field=models.BooleanField(default=False, verbose_name='civilit\xe9', choices=[(False, 'Madame'), (True, 'Monsieur')]),
            preserve_default=True,
        ),
    ]
