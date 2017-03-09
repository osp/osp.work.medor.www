# -*- coding: utf-8 -*-

from django.contrib import admin
from models import RetailOutlet


class RetailOutletAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'zip_code', 'city', 'is_published')
    list_editable = ('is_published',)
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        queryset.update(is_published=True)

    publish.short_description = "Publier la selection"

    def unpublish(self, request, queryset):
        queryset.update(is_published=False)

    unpublish.short_description = "Dépublier la selection"


admin.site.register(RetailOutlet, RetailOutletAdmin)
