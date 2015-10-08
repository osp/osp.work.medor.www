from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import ArticleMembership, Article, Issue, License


class ArticleMembershipInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ArticleMembership
    orderable_field = 'order'
    extra = 0


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
