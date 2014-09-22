# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    """ Describes a cooperator or a subscriber"""
    COUNTRY_CHOICES = (
        ('BE', u'Belgique'),
        ('FR', u'France'),
        ('LU', u'Luxembourg')
    )
    NATIONALITY_CHOICES = (
        ('BE', u'Belge'),
        ('FR', u'Française'),
        ('LU', u'Luxembourgeoise')
    )

    TITLE_CHOICES = (
        (0, u'Madame'),
        (1, u'Monsieur')
    )

    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom de famille', max_length=30)
    email = models.EmailField('courriel')
    birth_date = models.DateTimeField('date de naissance', null=True, blank=True)
    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    nationality = models.CharField('nationalité', max_length=2, choices=NATIONALITY_CHOICES, default="BE", blank=True)
    id_number = models.CharField("N° d'identification au registre national", max_length=30, blank=True)
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=10) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', max_length=30, null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal', max_length=5)
    country = models.CharField('pays', max_length=2, choices=COUNTRY_CHOICES, default="BE")
    phone_number = models.CharField('téléphone', blank=True, max_length=30)


    def __unicode__(self):
        return self.first_name


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, u'en cours'),
        (1, u'confirmé')
    )

    person = models.ForeignKey(Person)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    communication = models.PositiveIntegerField('communication', max_length=12)

    class Meta:
        abstract = True


class Subscription(TransactionBase):
    """ Describes a cooperation"""

    #def __unicode__(self):
        #return self.person

    def communication(self):
        invoice_nbr = 2014101234
        nbr = "{:010d}{:02d}".format(invoice_nbr, invoice_nbr % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:6], nbr[6:])


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    SHARE_CHOICES = (
        (1, u'1 (€ 20)'),
        (2, u'2 (€ 40)'),
        (3, u'3 (€ 60)'),
        (4, u'4 (€ 80)'),
        (5, u'5 (€ 100)'),
        (6, u'6 (€ 120)')
    )

    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")

    def __unicode__(self):
        return u"%s" % self.share_number

    def communication(self):
        invoice_nbr = 1234567890
        nbr = "{:010d}{:02d}".format(invoice_nbr, invoice_nbr % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:6], nbr[6:])
