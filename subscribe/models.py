# -*- coding: utf-8 -*-
from django.db import models


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, u'en cours'),
        (1, u'confirmé')
    )

    COUNTRY_CHOICES = (
        ('BE', u'Belgique'),
        ('FR', u'France'),
        ('LU', u'Luxembourg')
    )

    TITLE_CHOICES = (
        (False, u'Madame'),
        (True, u'Monsieur')
    )

    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom de famille', max_length=30)
    email = models.EmailField('courriel')
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=10) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', max_length=30, null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal', max_length=5)
    country = models.CharField('pays', max_length=2, choices=COUNTRY_CHOICES, default="BE")
    phone_number = models.CharField('téléphone (facultatif)', blank=True, max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0, blank=True)
    communication = models.PositiveIntegerField('communication', max_length=12, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.status = 0
        #invoice_nbr = 1234567890
        #nbr = "{:010d}{:02d}".format(invoice_nbr, invoice_nbr % 97)
        self.communication = 1234567890
        super(TransactionBase, self).save(*args, **kwargs)

    def structured_communication(self):
        nbr = str(self.communication)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:6], nbr[6:])


class Subscription(TransactionBase):
    """ Describes a cooperation"""
    pass


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    NATIONALITY_CHOICES = (
        ('BE', u'Belge'),
        ('FR', u'Française'),
        ('LU', u'Luxembourgeoise')
    )

    SHARE_CHOICES = (
        (1, u'1 (€ 20)'),
        (2, u'2 (€ 40)'),
        (3, u'3 (€ 60)'),
        (4, u'4 (€ 80)'),
        (5, u'5 (€ 100)'),
        (6, u'6 (€ 120)')
    )

    birth_date = models.DateTimeField('date de naissance')
    nationality = models.CharField('nationalité', max_length=2, choices=NATIONALITY_CHOICES, default="BE")
    id_number = models.CharField("N° d'identification au registre national", max_length=30)
    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")
