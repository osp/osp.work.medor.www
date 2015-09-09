from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import ArticleMembership, Article, Issue


class ArticleMembershipInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ArticleMembership
    orderable_field = 'order'
    extra = 0


class IssueAdmin(admin.ModelAdmin):
    inlines = [ArticleMembershipInline,]


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Issue, IssueAdmin)
admin.site.register(Article, ArticleAdmin)
