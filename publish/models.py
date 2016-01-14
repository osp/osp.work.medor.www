# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from urlparse import urlparse
from os.path import basename
from xml.etree import ElementTree

import markdown
import html5lib

from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.webdesign.lorem_ipsum import paragraphs

from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from filer.models.imagemodels import Image

SENTENCE_LAST_CHARACTER = re.compile('[.!?]')


class Rubric(models.Model):
    """
    Represents a type of article and the optional rubric title andsubtitle that
    goes along.
    """
    title = models.CharField('titre de la rubrique', max_length=1024, blank=True)
    subtitle = models.CharField('sous-titre de la rubrique', max_length=1024, blank=True)
    type = models.CharField("type d'article", max_length=1024, blank=True)

    class Meta:
        verbose_name = "Rubrique"

    def __unicode__(self):
        return self.title or self.type or "Sans titre"


class License(models.Model):
    """
    Represents the intellectual property License,
    as attributed to an article or other creative work.
    """
    name = models.CharField("Nom", max_length=1024, blank=True, help_text="par exemple Creative Commons Attribution-ShareAlike 4.0 International")
    short_name = models.CharField("Nom abbrégé", max_length=20, blank=True, help_text="par exemple CC BY-SA 4.0")
    url = models.URLField("URL", blank=True, help_text="l'adresse à laquelle le texte de la licence est consultable")

    class Meta:
        verbose_name = "Licence"

    def __unicode__(self):
        return self.short_name or self.name or "Sans titre"


class Issue(models.Model):
    """
    Represents an Issue of the Magazine
    """
    creation_date = models.DateTimeField("Date de création", auto_now_add=True)
    title = models.CharField("Titre", max_length=1024, blank=True)
    slug = models.SlugField("Slug", max_length=1024, blank=True, help_text="le texte utilisé pour construire les URLs")
    publish_date = models.DateTimeField("Date de publication", blank=True, null=True, help_text="la date de sortie du numéro")

    class Meta:
        verbose_name = "Numéro"

    def __unicode__(self):
        return self.title or "Sans titre"


def body_default():
    """
    Generates plain text Lorem Ipsum,
    then converts it to HTML via Markdown.
    """
    md = markdown.Markdown(output_format="html5", extensions=['extra'])
    return md.convert(u"\n\n".join(paragraphs(30)))


class Article(models.Model):
    """
    Represents an Article
    """
    STATUS_CHOICES = (
        (0, u'proposition'),
        (1, u'demande d\'évalutation par les pairs'),
        (2, u'demande de relecture'),
        (3, u'prêt')
    )

    creation_date = models.DateTimeField('date de création', auto_now_add=True)
    modified_date = models.DateTimeField('date de modification', auto_now=True)
    license = models.ForeignKey(License, null=True, blank=True, verbose_name="licence")
    title = models.CharField('titre', max_length=1024, blank=True)
    subtitle = models.CharField('sous-titre', max_length=1024, blank=True)
    rubric = models.ForeignKey(Rubric, blank=True, null=True, verbose_name="rubrique")
    slug = models.SlugField(max_length=1024, blank=True)
    body = RichTextField('article', blank=True, default=body_default)
    authors = models.CharField("auteurs", max_length=1024, blank=True)
    peer_reviewers = models.CharField("parrains ou marraines", max_length=1024, blank=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    in_toc = models.BooleanField('montré dans le table de matière', default=True)
    published_online = models.BooleanField('publié en ligne', default=False)
    override_description = models.TextField('exergue spécifique pour le web', blank=True)
    override_image = FilerImageField(verbose_name='spécifier image aperçu', blank=True, null=True,
             on_delete=models.SET_NULL)


    def get_excerpt(self):
        """
        Look in the body text to find the ‘chapeau’, the lead text,
        that can be used as a description.
        """
        dom = html5lib.parseFragment(self.body, treebuilder="etree", namespaceHTMLElements=False)
        for el in dom:
            if el.tag == "p" and el.attrib.get("class") == "chapeau":
                head = el.text or ""
                # el.text does not return the entire text if you have <p>Text with <em>child</em> tags</p>
                # cf http://stackoverflow.com/a/380717
                return "".join([head] + [ElementTree.tostring(e) for e in el.getchildren()])
        return u""

    @property
    def description(self):
        """
        The text that should be used as a description in the meta-data.

        The automatically deduced description can be overridden.
        """
        return self.override_description or self.get_excerpt()

    def get_image(self):
        """
        Look in the body text for the first image

        Try to find the associated filer object so we can make thumbnails
        """
        dom = html5lib.parseFragment(self.body, treebuilder="etree", namespaceHTMLElements=False)
        images = dom.findall('.//img')
        if images:
            img = images[0].get('src')            # u'https://medor.coop/media/filer_public/cb/1b/cb1b0760-5931-4766-b062-6ea821ba33c6/gent-cropped.png'
            img_path = urlparse(img).path         # u'/media/filer_public/cb/1b/cb1b0760-5931-4766-b062-6ea821ba33c6/gent-cropped.png'
            img_filename = basename(img_path)     # u'gent-cropped.png'
            for image in Image.objects.filter(original_filename__iexact=img_filename):
                if image.url == img_path:
                    return image
        return None

    @property
    def image(self):
        """
        Image associated with post (FilerImageField).
        """
        if self.override_image:
            return self.override_image
        return self.get_image()

    def __unicode__(self):
        return self.title or "Sans titre"

    #def save(self, *args, **kwargs):
        #if self.body:
            #self.body = self._fix_french(self.body)
        #super(Article, self).save(*args, **kwargs)

    def _fix_french(self, html):
        """
        To update:
        take from the numero 1 repo, but check for things that only work for print.
        safe to specific cached field.
        """
        import html5lib
        from html5lib_typogrify.french.filters import ellipsis, spaces, dashes, widows_orphans

        dom = html5lib.parseFragment(html, treebuilder="dom")
        walker = html5lib.getTreeWalker("dom")

        stream = walker(dom)
        stream = dashes.Filter(stream)
        stream = ellipsis.Filter(stream)
        stream = spaces.Filter(stream)
        stream = widows_orphans.Filter(stream)

        serializer = html5lib.serializer.HTMLSerializer(quote_attr_values=True,
                alphabetical_attributes=True,
                omit_optional_tags=False)
        output = serializer.serialize(stream)

        return serializer.render(stream)



class ArticleMembership(models.Model):
    """
    Registers articles in issues membership
    """
    article = models.ForeignKey(Article)
    issue = models.ForeignKey(Issue)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    page_number = models.PositiveIntegerField("nombre de pages", default=1, blank=False, null=False)


    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return self.article.title

    @property
    def single_page(self):
        return self.page_number == 1

    @property
    def folio(self):
        """
        Computes the page number of the first page of the article
        """
        if self.order == 1:
            return 1
        qs = self.issue.articlemembership_set.filter(order__lt=self.order)
        return qs.aggregate(page_count=Sum('page_number'))['page_count'] + 1

    @property
    def first_page(self):
        """
        With a less cryptic name
        """
        return self.folio

    @property
    def last_page(self):
        return self.folio + self.page_number

    @property
    def is_even(self):
        """
        If true, article starts on a left-hand page (even page number)
        """
        return self.folio % 2 == 0


class ArticleMembershipWeb(models.Model):
    """
    Registers articles as part of the web timeline
    """
    article = models.ForeignKey(Article)
    order = models.PositiveIntegerField("ordre", default=0, blank=False, null=False)
    visible = models.BooleanField("publié en ligne", default=True)
    web_publish_date = models.DateTimeField("date de publication sur le web", default=timezone.now)

    class Meta:
        ordering = ("order",)
        verbose_name = verbose_name_plural = "timeline"

    def __unicode__(self):
        return self.article.title
