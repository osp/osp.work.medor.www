# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class RetailOutlet(models.Model):
    """
    Represents a place where to buy Médor
    """
    is_published = models.BooleanField(_('is published?'), default=True)
    name = models.CharField(_('name'), max_length=1024)
    address = models.CharField(_('address'), max_length=1024, blank=True)
    zip_code = models.PositiveSmallIntegerField(_('zip code'), blank=True, null=True)
    city = models.CharField(_('city'), max_length=1024, blank=True)
    country = models.CharField(_('country'), max_length=1024, blank=True)
    latitude = models.FloatField(_('latitude'), blank=True, null=True)
    longitude = models.FloatField(_('longitude'),  blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("retail outlet")
        verbose_name_plural = _("retail outlets")

    def __unicode__(self):
        return self.name
