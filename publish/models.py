# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
from xml.etree import ElementTree

import markdown
import html5lib

from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.webdesign.lorem_ipsum import paragraphs

from ckeditor.fields import RichTextField

SENTENCE_LAST_CHARACTER = re.compile('[.!?]')

class License(models.Model):
    """
    Represents the intellectual property License,
    as attributed to an article or other creative work.
    """
    name = models.CharField(max_length=1024, blank=True)
    short_name = models.CharField(max_length=20, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.short_name or self.name or "Sans titre"


class Issue(models.Model):
    """
    Represents an Issue of the Magazine
    """
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1024, blank=True)
    slug = models.SlugField(max_length=1024, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)

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
        (0, u'proposal'),
        (1, u'request for peer-review'),
        (2, u'request for spell-checking'),
        (3, u'ready')
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    license = models.ForeignKey(License, null=True, blank=True)
    title = models.CharField(max_length=1024, blank=True)
    subtitle = models.CharField(max_length=1024, blank=True)
    rubric_title = models.CharField(max_length=1024, blank=True)
    rubric_subtitle = models.CharField(max_length=1024, blank=True)
    slug = models.SlugField(max_length=1024, blank=True)
    body = RichTextField(blank=True, default=body_default)
    article_type = models.CharField(max_length=1024, blank=True)
    authors = models.CharField(max_length=1024, blank=True)
    peer_reviewers = models.CharField(max_length=1024, blank=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    in_toc = models.BooleanField('montré dans le table de matière', default=True)
    published_online = models.BooleanField('publié en ligne', default=False)
    override_description = models.TextField('exergue spécifique pour le web', blank=True)

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

    # To add still:
    # image filer field
    # date de mise en ligne

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
    page_number = models.PositiveIntegerField(default=1, blank=False, null=False)


    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return self.article.title

    @property
    def folio(self):
        """
        Computes the page number of the first page of the article
        """
        qs = self.issue.articlemembership_set.filter(order__lt=self.order)
        return qs.aggregate(page_count=Sum('page_number'))['page_count'] + 1

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
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    visible = models.BooleanField(default=True)
    web_publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return self.article.title
