# -*- coding: utf-8 -*-


from django.db import models


class RetailOutlet(models.Model):
    """
    Represents a place where to buy Médor
    """
    is_published = models.BooleanField(default=True)
    name = models.CharField('nom', max_length=1024)
    address = models.CharField('adresse', max_length=1024, blank=True)
    zip_code = models.PositiveSmallIntegerField('code postal', blank=True, null=True)
    city = models.CharField('ville', max_length=1024, blank=True)
    country = models.CharField('pays', max_length=1024, blank=True)
    latitude = models.FloatField('lattitude', blank=True, null=True)
    longitude = models.FloatField('longitude',  blank=True, null=True)

    class Meta:
        verbose_name = "Point de vente"

    def __unicode__(self):
        return self.name
