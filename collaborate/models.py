# -*- coding: utf-8 -*-
from django.db import models
import markdown
from markdown.extensions.toc import TocExtension


SECTION_CHOICES = (
    (0, u'Enquête'),
    (1, u'Portrait ou récit'),
    (2, u'Interview'),
    (3, u'Portfolio photo'),
    (4, u'Autre')
)


class ArticleProposal(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=50,
        verbose_name="Nom"
    )
    email = models.EmailField(
        max_length=75,
        verbose_name="Courriel"
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Téléphone"
    )
    twitter_account = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Compte Twitter"
    )
    address = models.TextField(
        verbose_name="Adresse"
    )
    subject_title = models.CharField(
        max_length=300,
        verbose_name="Intitulé du sujet (provisoire)",
        help_text="Titre le plus clair possible. Avec sous-titre éventuel."
    )
    section = models.PositiveSmallIntegerField(
        choices=SECTION_CHOICES,
        default=0,
        verbose_name="Rubrique concernée (a priori)",
        help_text="Destinez-vous votre sujet à une rubrique précise ?"
    )
    abstract = models.CharField(
        max_length=750,
        verbose_name="Résumé",
        help_text="Rédigez comme s’il s’agissait d’un chapeau destiné à un média généraliste."
    )
    is_urgent = models.BooleanField(
        default=False,
        verbose_name="Urgence",
        help_text="Votre sujet nécessite-t-il une publication rapide sur le web ou sur papier (pour préserver l'exclusivité par exemple) ?"
    )
    body = models.TextField(
        verbose_name="Contenu",
        blank=True
    )

    class Meta:
        verbose_name = "Proposition d'article"
        verbose_name_plural = "Propositions d'articles"
        ordering = ['-creation_date']

    def __unicode__(self):
        return self.subject_title

    @models.permalink
    def get_absolute_url(self):
        return ('article-proposal-detail', (), {'pk': self.pk})

    @property
    def body_as_html(self):
        md = markdown.Markdown(output_format="html5", extensions=['extra', TocExtension(baselevel=2)])
        return md.convert(self.body)
