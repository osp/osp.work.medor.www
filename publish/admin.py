# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import ArticleMembership, ArticleMembershipWeb, Article, Issue, License, Rubric, Contribution, Contributor, Role

from reversion_compare.admin import CompareVersionAdmin



class ContributorAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_team')
    list_filter = ('is_team',)

class RoleAdmin(admin.ModelAdmin):
    pass


class ContributionInline(GenericTabularInline):
    model = Contribution
    extra = 0


class ArticleMembershipInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ArticleMembership
    orderable_field = 'order'
    extra = 0

    # FIXME: this is a dirty trick to inject a css rule that fix a bug with
    # django admin sortable and admin style
    class Media:
        css = {
            'all': ('admin/custom_admin.css', )
        }


class ArticleMembershipWebAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__unicode__', 'web_publish_date', 'visible')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'subtitle', 'type')


class LicenseAdmin(admin.ModelAdmin):
    pass


class IssueAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'published_online')
    inlines = (ContributionInline, ArticleMembershipInline)


class InIssueListFilter(admin.SimpleListFilter):
    title = 'issue'
    parameter_name = 'issue'

    def lookups(self, request, model_admin):
        qs = Article.objects.filter(articlemembership__isnull=False)
        return set(qs.values_list('articlemembership__issue__id', 'articlemembership__issue__title'))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(articlemembership__issue__id=self.value())


class ArticleAdmin(CompareVersionAdmin):
    inlines = (ContributionInline,)
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('__unicode__', 'rubric', 'status', 'authors', 'peer_reviewers')
    list_filter = ('status', 'published_online', 'rubric', 'contributions__license', 'contributions__role', InIssueListFilter)
    readonly_fields = ('creation_date', 'modified_date', 'description_explanation', 'image_explanation')
    search_fields = ("title",)
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'subtitle',
                'slug',
                'rubric',
                ('status', 'license'),
                ('creation_date', 'modified_date'),
                ('authors', 'peer_reviewers'),
                ('published_online',),
                'lead',
                'body',
            )
        }),
        ("Meta", {
            'classes': ('collapse',),
            'fields': (
                'description_explanation',
                'override_description',
                'image_explanation',
                'override_image'
            )
        }),
    )

    def description_explanation(self, instance):
        """
        """
        description = instance.get_excerpt()
        t = """La description web est utilisé entre autre pour l’affichage Facebook du page article.
Elle est aussi utilisé par Google.<br/><br/>"""
        if description:
            t += """La description suivante à ete récupèré de l’exergue de l’article.
Si vous voulez c’est possible de créer une nouvelle description en utilisant le champs ci-dessous."""
            t += """<br/><br/> <em>%s</em> <br/><br/>""" % description
            t += """Cette description pèse pour l’instant %s caractères. """ % len(description)
            t += """Pour les réseaux sociaux c’est le mieux de rester à moins de 300 caractères."""
        else:
            t += """Le CMS n’a pas pu recuperer une exergue de l’article comme base pour la description.
Pour créer la description, utilisez le champs ci-dessous."""

        return mark_safe(t)

    description_explanation.short_description = "Explication exergue"
    description_explanation.allow_tags = True

    def image_explanation(self, instance):
        """
        """
        image = instance.get_image()
        t = """L’aperçu web est utilisé à la fois pour le site et pour l’affichage Facebook du page article."""
        if image:
            t += """L’image suivante a été sélectionné automatiquement:"""
            t += """<br/><br/> <a href="%s">%s</a> <br/><br/>""" % (image, image)
            t += """Pour en choisir une autre,"""
        else:
            t += """Le CMS n’a pas pu recuperer une image,"""
        t += """selectionnez-une dans le champs ci-dessous."""

        return mark_safe(t)

    image_explanation.short_description = "Explication exergue"
    image_explanation.allow_tags = True


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(ArticleMembershipWeb, ArticleMembershipWebAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(License, LicenseAdmin)
