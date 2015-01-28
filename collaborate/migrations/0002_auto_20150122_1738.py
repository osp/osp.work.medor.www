# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleproposal',
            name='abstract',
            field=models.CharField(help_text=b'R\xc3\xa9digez comme s\xe2\x80\x99il s\xe2\x80\x99agissait d\xe2\x80\x99un chapeau destin\xc3\xa9 \xc3\xa0 un m\xc3\xa9dia g\xc3\xa9n\xc3\xa9raliste \xe2\x80\x94 750 signes maximum.', max_length=750, verbose_name=b'r\xc3\xa9sum\xc3\xa9 (pr\xc3\xa9visionnel)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='approach',
            field=models.CharField(help_text=b'Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'approche'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='belgian',
            field=models.CharField(help_text=b'En quoi votre sujet est-il sp\xc3\xa9cifiquement belge ? Que nous dit-il de la Belgique et comment, \xc3\xa0 travers lui, la Belgique nous parle-t-elle du monde ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'Belgique'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='difficulties',
            field=models.CharField(help_text=b'Quelles difficult\xc3\xa9s (principales et particuli\xc3\xa8res) pr\xc3\xa9voyez-vous de rencontrer dans la r\xc3\xa9alisation de votre enqu\xc3\xaate ou reportage ? Comment pr\xc3\xa9voyez-vous de pallier ces difficult\xc3\xa9s ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'difficult\xc3\xa9s'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='innovation',
            field=models.CharField(help_text=b'En quoi votre sujet est-il innovant par rapport \xc3\xa0 l\xe2\x80\x99offre m\xc3\xa9diatique francophone de Belgique ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'innovation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='media',
            field=models.CharField(help_text=b'Quelle(s) contribution(s) envisagez-vous? \xc3\x89crits, photographies, dessins, peintures, infographies, vid\xc3\xa9o, son, jeux de r\xc3\xb4les, autres (pr\xc3\xa9cisez) \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'm\xc3\xa9dia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='method',
            field=models.CharField(help_text=b'Comment comptez-vous obtenir vos informations et vous immerger dans votre th\xc3\xa9matique ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'm\xc3\xa9thode'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='miscellaneous',
            field=models.CharField(help_text=b'Avez-vous une remarque ou une demande particuli\xc3\xa8re li\xc3\xa9e \xc3\xa0 votre proposition? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'divers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='partnership',
            field=models.CharField(help_text=b'Quelle synergie serait possible entre votre projet et un autre correspondant de M\xc3\xa9dor : \xc3\xa9crits, photographies, dessins, peintures, infographies, vid\xc3\xa9o, son, jeux de r\xc3\xb4les, autres (pr\xc3\xa9cisez) \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'partenariat'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='section',
            field=models.CharField(help_text=b'Destinez-vous votre sujet \xc3\xa0 une rubrique pr\xc3\xa9cise ? Entretien, portrait, r\xc3\xa9cit, enqu\xc3\xaate, br\xc3\xa8ves \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'rubrique concern\xc3\xa9e (a priori)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='sectioning',
            field=models.CharField(help_text=b'Votre sujet se d\xc3\xa9cline-t-il en plusieurs entr\xc3\xa9es ? Sinon, le pourrait-il ? O\xc3\xb9 va votre pr\xc3\xa9f\xc3\xa9rence et pourquoi ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'd\xc3\xa9coupage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='sources',
            field=models.CharField(help_text=b'Aupr\xc3\xa8s de quelles sources ou quels types de sources (principales) pensez-vous d\xc3\xa9marrer votre recherche ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'sources'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='subject_title',
            field=models.CharField(help_text=b'Titre le plus clair possible. Avec sous-titre \xc3\xa9ventuel.', max_length=300, verbose_name=b'intitul\xc3\xa9 du sujet (provisoire)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='term',
            field=models.CharField(help_text=b'Quand pr\xc3\xa9voyez-vous de remettre votre contribution (d\xc3\xa9finitive) \xc3\xa0 M\xc3\xa9dor ?', max_length=200, verbose_name=b'\xc3\xa9ch\xc3\xa9ance'),
            preserve_default=True,
        ),
    ]
