from django.db import models
from django.db.models import Sum
from ckeditor.fields import RichTextField

import markdown
from django.contrib.webdesign.lorem_ipsum import paragraphs


class Issue(models.Model):
    """Represents an Article"""
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1024, blank=True)

    def __unicode__(self):
        return self.title or "Sans titre"


def body_default():
    md = markdown.Markdown(output_format="html5", extensions=['extra'])
    return md.convert(u"\n\n".join(paragraphs(30)))


class Article(models.Model):
    """Represents an Article"""
    STATUS_CHOICES = (
        (0, u'proposal'),
        (1, u'request for peer-review'),
        (2, u'request for speelchecking'),
        (3, u'ready')
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1024, blank=True)
    subtitle = models.CharField(max_length=1024, blank=True)
    slug = models.SlugField(max_length=1024, blank=True)
    body = RichTextField(blank=True, default=body_default)
    article_type = models.CharField(max_length=1024, blank=True)
    authors = models.CharField(max_length=1024, blank=True)
    peer_reviewers = models.CharField(max_length=1024, blank=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)

    def __unicode__(self):
        return self.title or "Sans titre"

    #character count
    #nombre de mots
    #Chaine de decision: proposition/demande de relecture/demande de correction orthographique/habille web
    #Theme (surtout pour le site web
    #Numero dans lequel paraitre
    #Type d'habillage
    #Micro bibliographie
    #Web + -> Lien
    # Champ Notes de bas de page
    # Extrait (uniquement pour le web mot d'intro avant de cliquer sur le texte)

    # Commentaires editoriaux: uniquement pour les exergues et les legendes.

    #def save(self, *args, **kwargs):
        #if self.body:
            #self.body = self._fix_french(self.body)
        #super(Article, self).save(*args, **kwargs)

    def _fix_french(self, html):
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
    """Registers articles in issues membership"""
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
        """Computes the first page number"""
        qs = self.issue.articlemembership_set.filter(order__lt=self.order)
        return qs.aggregate(page_count=Sum('page_number'))['page_count'] + 1

    @property
    def is_even(self):
        """Computes the first page number"""
        return self.folio % 2 == 0

