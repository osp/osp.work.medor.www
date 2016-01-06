# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import publish.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0016_auto_20151119_0855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name': 'Num\xe9ro'},
        ),
        migrations.AlterModelOptions(
            name='license',
            options={'verbose_name': 'Licence'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(max_length=1024, verbose_name="type d'article", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.CharField(max_length=1024, verbose_name='auteurs', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(default=publish.models.body_default, verbose_name='article', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='license',
            field=models.ForeignKey(verbose_name='licence', blank=True, to='publish.License', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date de modification'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='peer_reviewers',
            field=models.CharField(max_length=1024, verbose_name='parrains ou marraines', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='rubric_subtitle',
            field=models.CharField(max_length=1024, verbose_name='sous-titre de la rubrique', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='rubric_title',
            field=models.CharField(max_length=1024, verbose_name='titre de la rubrique', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='statut', choices=[(0, 'proposition'), (1, "demande d'\xe9valutation par les pairs"), (2, 'demande de relecture'), (3, 'pr\xeat')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=1024, verbose_name='sous-titre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='titre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlemembership',
            name='page_number',
            field=models.PositiveIntegerField(default=1, verbose_name='nombre de pages'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='publish_date',
            field=models.DateTimeField(help_text='la date de sortie du num\xe9ro', null=True, verbose_name='Date de publication', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(help_text='le texte utilis\xe9 pour construire les URLs', max_length=1024, verbose_name='Slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='Titre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='name',
            field=models.CharField(help_text='par exemple Creative Commons Attribution-ShareAlike 4.0 International', max_length=1024, verbose_name='Nom', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='short_name',
            field=models.CharField(help_text='par exemple CC BY-SA 4.0', max_length=20, verbose_name='Nom abbr\xe9g\xe9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='url',
            field=models.URLField(help_text="l'adresse \xe0 laquelle le texte de la licence est consultable", verbose_name='URL', blank=True),
            preserve_default=True,
        ),
    ]
