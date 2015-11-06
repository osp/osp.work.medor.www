from django.core.urlresolvers import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin
from .models import ArticleMembership, Article, Issue, License


class ArticleMembershipInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ArticleMembership
    orderable_field = 'order'
    extra = 0
    readonly_fields = ('links',)

    def links(self, instance):
        """
        Provide links to the relevant CSS, raw HTML, HTML2print template
        in the admin display of an ArticleMemberShip
        """
        # is the instance a proxy? it only works when I call it first this way:
        instance.__unicode__()
        pk = instance.id
        css_link = reverse('article-membership-detail-css', args=[pk])
        html_link = reverse('article-membership-detail-html', args=[pk])
        tpl_link = reverse('article-membership-detail-tpl', args=[pk])
        return mark_safe(
            '<a href="%s">CSS</a>, <a href="%s">raw HTML</a>, <a href="%s">template</a>' %
            (css_link, html_link, tpl_link)
        )

    links.short_description = "Links"
    links.allow_tags = True


class LicenseAdmin(admin.ModelAdmin):
    pass


class IssueAdmin(admin.ModelAdmin):
    inlines = [ArticleMembershipInline,]


class InIssueListFilter(admin.SimpleListFilter):
    title = 'issue'
    parameter_name = 'issue'

    def lookups(self, request, model_admin):
        qs = Article.objects.filter(articlemembership__isnull=False)
        return set(qs.values_list('articlemembership__issue__id', 'articlemembership__issue__title'))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(articlemembership__issue__id=self.value())


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('__unicode__', 'status', 'authors', 'peer_reviewers')
    list_filter = ('status', InIssueListFilter)


admin.site.register(Issue, IssueAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(License, LicenseAdmin)
