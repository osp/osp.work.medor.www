from django.db import models
from django.db.models import Sum


class Issue(models.Model):
    """Represents an Article"""
    title = models.CharField(max_length=1024, blank=True)

    def __unicode__(self):
        return self.title or "Sans titre"


class Article(models.Model):
    """Represents an Article"""
    title = models.CharField(max_length=1024, blank=True)
    slug = models.SlugField(max_length=1024, blank=True)
    body = models.TextField(blank=True)
    article_type = models.CharField(max_length=1024, blank=True)


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

