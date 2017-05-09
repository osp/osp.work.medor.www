# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from models import RetailOutlet


class RetailOutletAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('__unicode__', 'name', 'zip_code', 'city', 'is_published')
    list_editable = ('is_published',)
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        queryset.update(is_published=True)

    publish.short_description = _("publish selected retail outlets")

    def unpublish(self, request, queryset):
        queryset.update(is_published=False)

    unpublish.short_description = _("unpublish selected retail outlets")


admin.site.register(RetailOutlet, RetailOutletAdmin)
